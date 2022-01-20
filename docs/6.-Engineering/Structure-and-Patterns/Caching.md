[[_TOC_]]

## Basic Cache Usage

Caching is primarily performed using the `ICache` interface. To used cached values in code, first use Dependency Injection to retrieve an `ICache` instance. In many ways, the cache can be thought of just like a `Dictionary<string, anything>` that stores values that take a long time to calculate or retrieve from remote locations. In this analogy, we use a `string` cache key to store and retrieve these results.

Most of the time the best apracoh is to use the `T Get<T>(string cacheKey, Func<T> getter)` method. This call takes two parameters: a string (cache key) which behaves just like the dictionary key, and a getter: a function which calculates the value if it does not exist already in the cache.

```c#
string cacheKey = "global.my.cache.key"; // cache key that probably contains ClientKey or WebsiteKey
var cachedValue = _cache.Get(cacheKey, () =>
{
    // expensive, long running piece of code to calculte value
    return calculateValue;
});
```

This call will first check to see if the cache contains a value with the specified key.

1. If the value can be found, it is returned immediately
1. If it cannot be found within the cache, it will run the getter to calculte the required value and
  1. Store the value in the cache for future quick retrieval
  1. Returns the value to the calling code


The first time a given cached value is requested, it will not yet exist in the cache, and go through route 2. above. On subsequant requests for the same cached value, it now exists and will go through route 1.

### Cache Scope

Quartex has several levels of caching, called "Cache Scopes". Each Scope typically requires more time/resource to store/retrieve than the previous Scope; as such it makes sense to store larger/more expensive to compute values in a higher Scope:

* `Disabled`: the value is never cached, and the `getter()` will always be called
* `Ephemeral`: cached values are stored for the duration of the current HTTP Request, within `HttpContext.Items`. If the same value is requested in another HTTP Request, it will need to be re-calculated
* `InMemory`: values are stored for a configurable length of time in Memory, but only within the same application. If the same value is requested within another application, or in another instance of the same application (e.g. on a different server), it will need to be re-calculated.
* `Distributed`: values are stored for a configurable length of time in Redis.


> _**NOTE:** If you do not configure a new Cache Key (or it is not convered by configuration for an existing prefix), the default behaviour is to use `NotCached` for the cache scope. If it seems like a newly cached value is never appearing in Redis, or your `getter()` is getting called every time; ensure the cache key is covered by a configuration entry. See below for configuration._

### Configuration of Cached Values

Cache Scope is configured along with expiry times in `quartex.cache.json`. Related sets of cache keys are configured by common prefixes. E.g. in the example below, any value stored with a cache key that begins `sw.CSS.SiteStyles` will be cached in Redis, with an expiry time of 3 hours:

```json
"sw.CSS.SiteStyles": {
  "Scope": "Distributed",
  "Hours": 3
}
```

Cache configuration and cache key naming strategies go hand in hand. Typically, we use a convention of the form `{Component}.{Category}.{Value}.{ClientKey}.{WebsiteKey}`.

In the above example, the component is the Static Webservice (abbreviated as  `sw`), the category is `CSS`, and the specific value is `SiteStyles`, finally the Client Key and Website Key are append giving the following:

```cs
string cacheKey = $"sw.CSS.SiteStyles.{_website.ClientKey}.{_website.WebsiteKey}";
```

### Cache Key Naming

When creating a cache key, **always** be careful to ensure that the ky is unique, as otherwise a value cached for one client/site would then get used for all clients or sites. Imagine caching Site Styles for one front-end site, and having them retrieved for a completely unrelated front-end.

A cache key should always include the Client Key and Website Key as appropriate, and should make reference to individual identifiers where appropriate too. The following examples are for the HTML of a static page, and the document details and fields retrieved from Elastic Search. The static page uses it's Path as the unique individual identifier, and the document response uses the document's ID.

```cs
string htmlCacheKey = $"fe.Html.{_website.ClientKey}{_website.WebsiteKey}.Static.{_page.Path}";
string documentResponse = $"dms.InitDataRequest.{websiteKey}.{documentId}";
```

## Cache Invalidation

When caching data, we need to make sure that outdated or stale data does not stay in the cache. There are some exceptions to this rule; for example with the DAM Dashboard we have explicitly decided that having a the UI return potentially out-of-date results quickly is preferable to always serving up fresh data very slowly.

However, in most cases if you are caching data you will need to consider when and how to clear the cached values when they update.

In Quartex the easiest method for invalidating cache data is to use the `IEventBus` to raise a custom event, along with some configuration in `quartex.cache.json` to clear certain cache keys whenever that event is raised.

### Clearing cache entries via the IEventBus

Raising an event works as follows: use the `IEventBus` to call the `Raise` method, and pass in an `Event` object specifying a Name and a dictionary of Arguments:

```cs
_eventBus.Raise(new Event
{
    Name = EventNames.FrontEndStaticPagePublish,
    Arguments = new Dictionary<string, string>
    {
        { "ClientKey", client.ClientKey },
        { "WebsiteKey", websiteKey },
        { "PageId", page.Id.ToString() },
        { "PagePath", page.Path }
    }
});
```

In this example, we are raising an event to broadcast the fact that a Static Page has just been published. Note that we pass in a dictionary of relevant arguments which we can reference later when defining which cache entries to cache. In the above example, `EventNames.FrontEndStaticPagePublish` is a static string that returns `"evt.fe.staticpagepublished"`.

To configure cache invalidation, we use the Event Name as the key, and define an array of cache keys that need to be cleared. The keys to be cleared can then reference the event's arguments by putting the argument's name in braces, e.g. `{ArgumentName}`. It is also possible to use a `*` as a wildcard.

```json
{
  "CacheSettings": {
    "CacheInvalidation": {
        // other items...
        "evt.fe.staticpagepublished": [ "common.WebsiteTenant.{WebsiteKey}", "fe.Html.{ClientKey}.{WebsiteKey}.*" ]
        // other items...
    }
  }
}
```

In this worked example, when a static page is published, we want to clear the followinag things:

* The `WebsiteInfo` object for the current website
* All cache HTML for the website - note that this is using a wildcard


### Creating new Events to clear caches

When you have worked out the best time to clear a set of related cache keys, follow the process below.

* Create a new static string in `Quartex.Common\EventBus\EventNames.cs`
* Raise the event in your code using the `IEventBus` and using the `EventNames` static string you created above
* Add a configuration entry to `Quartex.Configuration\quartex.cache.json`

The `quartex.cache.json` entry needs to use the raw event name (i.e. format like `evt.component.eventname`) instead of the `EventNames.SomeEventName` notation (which is only applicable in C#).

### Clearing Local vs Distributed caches

There are a range of different [cache scopes](?anchor=cache-scope) and clearing each of these is done differently.

* `Disabled` - these items are not cached, so there is nothing to clear
* `Ephemeral` - these items are only stored for the duration of an HTTP request, so don't hang around long enough to need clearing
* `InMemory` - the Event based system means that any other Quartex component that has an In Memory key cached will receive the event and clear its own cached copy
* `Distributed` - these items are stored in Redis, so whichever Quartex component is raising the event will also remove the value from Redis

All of this is handled by the Shared Code Library for you, so raising the relevant Event and adding the relevant configuration is all that needs to be done from a developer perspective.

## Caching Service Requests

> _**NOTE**: the methods described below will only work in whilst using the `IServiceClient` in C#. The methods are not applicable to Type Script microservice calls._

As more of Quartex is being built using a microservice architecture, we are finding that microservice requests can be a very useful point to add caching to the system. Most microservice requests will fall into one of two categories:

* We have GET type requests to retrieve information, or Read operations
* We POST/PUT/DELETE etc type requests that update information, or Write operations

Read operations are the kind of things we might want to cache, and Write operations by definition will update data that may be cached (making the cached information out-of-date) and thus will be operations where we want to invaliate cached data.

### Using the Service Client to cache data

Caching microservice requests and having them invalidate data is achieved by simply making the `IServiceRequest` classes implement some additional interfaces; once these setup steps are complete, everything is handled by the `IServiceClient` and nothing additional needs to be done from a developer perspective.

To illustrate how these can be used together, we will use the example of the Features endpoints on the Clients Microservice. We will show how to cache the results of the `GetFeaturesRequest` (a Read operation), and show how to clear the cache whenever we use `SetFeaturesRequest` (a Write operation) to modify data.

### Caching the results of a Microservice Call

Firstly, implement the `ICacheableRequest` on your request class. This requires us to implement a single method, `GetCacheKey()` which simply enough generates a string that will later be used as the cache key. Bear in mind that [good cache key naming](?anchor=cache-key-naming) is essential. In this case, we have a `ClientKey` property to use to ensure we cache the features for different clients separately.

```cs
 public class GetFeaturesRequest : IServiceRequest<GetFeaturesResponse>, IInternalRequest, ICacheableRequest
 {
    // normal IServiceRequest Properties ...

    public string ClientKey { get; set; }
    public string GetCacheKey()
    {
        return $"client.Features.{ClientKey}";
    }
 }
```

Having created a new cache key, we also need to configure the cache location and expiry in `quartex.cache.json`:

```json
{
    "CacheSettings": { 
        "KeySettings":{
            // Any entries in KeySettings apply to any cached values that start with the following keys.
            // So "client.Features" will apply to "client.Features.{anything...}"
            "client.Features": {
                "Scope": "Distributed",
                "Hours": 2,
                "Priority": 1,
                "RetryLimit": 1
            }
        }
    }
}
```

Once this is setup, any time any component uses the `IServiceClient` to make make a `GetFeaturesRequest`, the `IServiceClient` will first check to see if the result is in the cache; if yes, it doesn't bother making the actual microservice request and simply returns the cached result.

If the results are not in the cache, the `IServiceClient` will make the microservice request as normal, and if it gets a Successful response, the result will be cached for future occasions.

{{% alert theme="info" %}} **NOTE**: only successful results are cached. So if the microservice responds with a 404 Not Found response or a 500 Internal Server Error for example, the result will not be cached. {{%/alert%}}

### Clearing the cache when making a Microservice Call

Cache clearing is done via the mechanism of raising an event, so we will need to create a new Event Name in the `Quartex.Common/EventBus/EventNames.cs` file:

```cs
public static class EventNames
{
    // other existing event names..

    public static string ClientFeaturesEdit => "evt.clients.featureschanged";
}
```


Similarly, in order to make our Write operation clear invalid cache keys, we need to make the request class extend `IEventRaisingRequest` and implement the `Event` property.

```cs
public class SetFeatureRequest : IServiceRequest<SetFeatureResponse>, IInternalRequest, IEventRaisingRequest
{
    // normal IServiceRequest Properties ...

    public string ClientKey { get; set; }

    public Event Event => new Event() { Name = EventNames.ClientFeaturesEdit, Arguments = new Dictionary<string, string> { { "ClientKey", ClientKey  } } };
}
```

Similarly, we will need to configure the [invalidation](?anchor=cache-invalidation) section of `quartex.cache.json`. As before, we need to use the raw event name (instead of referencing it via the `EventNames` static variable).

```json
{
  "CacheSettings": {
      "CacheInvalidation": {
          "evt.clients.featureschanged": [ "client.Features.{ClientKey}", "client.Features.{ClientKey}.*" ]
      }
  }
}
```

Now, whenever any component uses the `IServiceClient` to make a `SetFeatureRequest`, if the response from the microservice comes back as successful, our event will be raised and any related caches cleared.