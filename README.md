# Plus Resources: Django Project Starter

Starter code for the Plus Django project.

# Sahar Kavousi - She Codes News Project

## About This Project
We used Django to create a website for She Codes New. I create this news website that allows users to read news stories, and authors to create them. 

## How To Run This Code

{{
    Give a quick step-by-step guide on how to download and run your codebase.

    It's ok to assume the reader is another developer here, so don't feel like you have to explain what a virtual environment is, etc.
    
    Give directions like "clone the repo to your local machine", "create a virtualenvironment", "migrate the database", etc.

    When you need to specify terminal commands, you can surround them withbackticks, like so: `python manage.py runserver`. 
    
    This formats them ascode in the markdown document. (The backtick key is to the left of thenumber 1 at the top of your keyboard.)

}}

## Database Schema
![ {{ My ERD }} ]( {{ ./relative_path_to_your_entity_relationship_diagram }} )

## Project Features
- [x] Order stories by date
    
    ![ In Django, we can order stories by date using the order_by method in your query. Here we have a model with a date_published field, that allow us to order the stories by date in descending order,from newest to oldest.]
    (./img/images for news project Django/ order stories by date.png) 

 - [x] Styled "new story" form
    ![ I've applied styling to the "new story" form, allowing users to submit their stories. Users have the option to include an image related to their story, though it's not mandatory. However, specifying the publication date for the image is required. Additionally, users must provide a title for their story.]
    ( ./img/images for news project Django/Styled "new story" form.png )

- [x] Story images
    ![ {{ Description of image }} ]( {{ ./relative_path_to_image_file }} )

- [ ] Log-in/log-out
    ![ {{ Description of image }} ]( {{ ./relative_path_to_image_file }} )

- [ ] "Account view" page
    ![ {{ Description of image }} ]( {{ ./relative_path_to_image_file }} )

- [ ] "Create Account" page
    ![ {{ Description of image }} ]( {{ ./relative_path_to_image_file }} )

- [ ] View stories by author
    ![ {{ Description of image }} ]( {{ ./relative_path_to_image_file }} )

- [ ] "Log-in" button only visible when no user is logged in/"Log-out" buttononly visible when a user *is* logged in
    ![ {{ Description of image }} ]( {{ ./relative_path_to_image_file }} )

- [ ] "Create Story" functionality only available when user is logged in
    ![ {{ Description of image }} ]( {{ ./relative_path_to_image_file }} )


## Additional Features:

- [ ] Add categories to the stories and allow the user to search for stories bycategory.
    ![ {{ Description of image }} ]( {{ ./relative_path_to_image_file }} )

- [ ] Add the ability to update and delete stories (consider permissions - whoshould be allowed to update or and/or delete stories).
    ![ {{ Description of image }} ]( {{ ./relative_path_to_image_file }} )

- [ ] Add the ability to “favourite” stories and see a page with your favouritestories.
    ![ {{ Description of image }} ]( {{ ./relative_path_to_image_file }} )

- [ ] Our form for creating stories requires you to add the publication date,update this to automatically save the publication date as the day thestory was first published (maybe you could then add a field to showwhen the story was updated).
    ![ {{ Description of image }} ]( {{ ./relative_path_to_image_file }} )


- [ ] Gracefully handle the error where someone tries to create a new story whenthey are not logged in.
    ![ {{ Description of image }} ]( {{ ./relative_path_to_image_file }} )

