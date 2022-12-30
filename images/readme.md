# How to use images in the Playbook

## Creating and managing images

1. All images should be placed into the _images_ folder at the root.
1. Image files should be named named:
    1. Using kebab-case. (Lower case, separated with a hyphen and no spaces)
    1. Descriptively. The use of version numbers, dates and other versioning descriptors (e.g. "final") are generally unnecessary and should be avoided.
1. Before adding an image, check carefully to see if the image already exists.
1. If an image is being updated, do not create another image. Instead you should replace the image, keeping the same name.
1. You may create subfolders within the _images_ folder, however:
    - Be considerate of future use of the image and folder you are creating
    - Remember that the same a
1. If you delete an image you must ensure that there are not references to that image in any of the documents

## Using image in docs

1. When referencing an image in a playbook markdown file you should use the following syntax:

    ``` md
    ![a descriptor here](/images/filename-here.jpg)

    Here is an example of an image: ![example image](/images/example-image.jpg) 
    ```

    Here is an example of an image: ![example image](example-image.jpg)

1. If the file is in a subfolder(s) you will need to include this in the path:

    ``` md
    ![example image](/images/subfolder/subfolder/example-image.jpg) 
    ```
