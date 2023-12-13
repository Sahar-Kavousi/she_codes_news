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
    (./img/readme/ order-stories-by-date.png) 

 - [x] Styled "new story" form
    ![ I've applied styling to the "new story" form, allowing users to submit their stories. Users have the option to include an image related to their story, though it's not mandatory. However, specifying the publication date for the image is required. Additionally, users must provide a title for their story.]
    ( ./img/readme/new-story-form.png)

- [x] Story images
    ![ Every story has an image for a visually engaging experience. The story images are presented as card components, featuring essential details like the story title, author's name, and publication date below them. ]
    ( ./img/readme/Story-images.png)

- [x] Log-in/log-out
    ![ Login:
    Login serves as the gateway for users to access their accounts. It typically requires users to input their credentials, such as a username or email and a password, to authenticate their identity.After a successful login users can have access to "creat new story" button and add a new story.

    Logout: On the News page, Profile page anad Home page users have the option to log out, which disconnects them from their current session. Even after logging out, users can still view the stories available on the page. However, to contribute by creating a new story, users are prompted to create an account and log in.]
    
    ( ./img/readme/Log-in.png )
    ( ./img/readme/login-page.png)
    ( ./img/readme/logout.png )

- [x] "Account view" page
    ![ On the account view or profile page, users have the ability to upload their profile picture, input their name, and provide a description about themselves. An edit option is available, enabling users to make adjustments to their profile details as desired. ]
    ( ./img/readme/Account-view.png)

- [x] "Create Account" page
    ![ The Create Account page is where users provide basic details like a unique username, secure password, and email. It initiates setting up an account and granting access to some of the features, such as the "create news story" button, upon completion. ]
    ( ./img/readme/creat-account-page.png)

- [x] View stories by author
    ![ This feature allows users to explore a collection of stories specifically organized by their respective authors. Clicking on an author's name within a story card redirects users to that specific author's dedicated story page. ]
    ( ./img/readme/View-stories-by-author.png )

- [x] "Log-in" button only visible when no user is logged in/"Log-out" buttononly visible when a user *is* logged in
    ![ Users will see the "Log-in" button only if they're not logged in. It's there to help them sign in. On the flip side, the "Log-out" button shows up when they're logged in, making it easy to log out. These buttons dipalyed in NAV bar and will be adjust based on whether they're logged in or not.]
    ( ./img/readme/login-visibility.png )

- [x] "Create Story" functionality only available when user is logged in
    ![ The "Create Story" button on the story news page is visible exclusively to users who are logged in. This button serves as a prompt for authenticated users, allowing them to contribute by crafting and sharing their own stories.]
    ( ./img/readme/Create-Story.png)


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

