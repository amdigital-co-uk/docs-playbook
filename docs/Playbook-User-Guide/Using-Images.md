---
title: Using Images
authors: 
- Ed Earle 
reviewed: 
reviewer:
next-review: 2023-04-01
---

## Creating and Managing Images

1. All images should be placed into the same folder as the document they are included in.
1. In some cases one image may need to be used in multiple documents.
    1. Before adding an image, check carefully to see if the image already exists.
    1. Consider referencing the page that already has that image instead of adding the image to both pages.
    1. Do not duplicate or move the image, leave it in the original location and use that path in the document you are working on.
1. Image files should be named named:
    1. Using kebab-case. (Lower case, separated with a hyphen and no spaces)
    1. Descriptively. The use of version numbers, dates and other versioning descriptors (e.g. "final") are generally unnecessary and should be avoided. 
1. If an image is being updated, do not create another image. Instead you should replace the image, keeping the same name.
1. You may create subfolders within the _images_ folder, however:
    - Be considerate of future use of the image and folder you are creating
    - Remember that the same a
1. If you delete an image you must ensure that there are not references to that image in any of the documents.

## Using Images in Docs

1. When referencing an image in a Playbook markdown file you should use the following syntax:

    ``` md
    ![a descriptor here](filename-here.jpg)

    Here is an example of an image: ![example image](example-image.jpg) 
    ```

    Here is an example of an image: ![example image](example-image.jpg)

1. If the image file is in a different folder to the one you are working on, you will need to include its path:

    ``` md
    ![example image](\Section-Name\Subfolder\example-image.jpg) 

    ```
