# Plus Resources: Django Project Starter

Starter code for the Plus Django project.

# Sahar Kavousi - She Codes News Project

## About This Project
We used Django to create a website for She Codes New. I create this news website that allows users to read news stories, and authors to create them. 

## How To Run This Code

1- Open a Terminal or Command Prompt.

2-Navigate to the Directory Where You Want to Clone the Repository:
Use the cd command to navigate to the directory where you want to store the Django app.
`cd path/to/your/directory`

3-Clone the Repository:
Use the git clone command to clone the repository. Replace the URL with the URL of the Django app you want to clone. For example:`git clone https://github.com/username/repo.git`

4-Navigate to the Cloned Directory:
Use the cd command to enter the cloned directory:`cd repo`

5-Install Dependencies:
Django apps often have dependencies listed in a requirements.txt file. Use a virtual environment and the following command to install these dependencies:
`python -m venv venv` 
`source venv/bin/activate` # On Windows, use 'venv\Scripts\activate'
`pip install -r requirements.txt`

6-Apply Migrations:
Django apps often require database migrations. Run the following commands:
`python manage.py makemigrations`
`python manage.py migrate`

7-Create a Superuser:
If the app includes user authentication, you might want to create a superuser account:
`python manage.py createsuperuser`

8-Run the Development Server:
Start the Django development server:
`python manage.py runserver`

9-Access the App:
Open your web browser and go to http://localhost:8000/ or the address indicated in the terminal. If you created a superuser, you can also access the Django admin panel at http://localhost:8000/admin/ and log in with the superuser credentials.


## Database Schema
![ My ERD ](./img/readme/NewsStroy_db_digram.png)

## Project Features
- [x] Order stories by date
    
    ![ In Django, we can order stories by date using the order_by method in your query. Here we have a model with a date_published field, that allow us to order the stories by date in descending order,from newest to oldest.](./img/readme/order-stories-by-date.png) 

 - [x] Styled "new story" form
    ![ I've applied styling to the "new story" form, allowing users to submit their stories. Users have the option to include an image related to their story, though it's not mandatory. However, specifying the publication date for the image is required. Additionally, users must provide a title for their story.]( ./img/readme/new-story-form.png)

- [x] Story images
    ![ Every story has an image for a visually engaging experience. The story images are presented as card components, featuring essential details like the story title, author's name, and publication date below them. ]( ./img/readme/Story-images.png)

- [x] **Log-in/Log-out**

    - **Login:**
      Login serves as the gateway for users to access their accounts. It typically requires users to input their credentials, such as a username or email and a password, to authenticate their identity. After a successful login, users can have access to the "create new story" button and add a new story.
      
      ![Login](./img/readme/Log-in.png)

      ![Login Page](./img/readme/login-page.png)

    - **Logout:**
      On the News page, Profile page, and Home page, users have the option to log out, which disconnects them from their current session. Even after logging out, users can still view the stories available on the page. However, to contribute by creating a new story, users are prompted to create an account and log in.
      
      ![Logout](./img/readme/logout.png)  

- [x] "Account view" page
    ![ On the account view or profile page, users have the ability to upload their profile picture, input their name, and provide a description about themselves. An edit option is available, enabling users to make adjustments to their profile details as desired. ]( ./img/readme/Account-view.png)

- [x] "Create Account" page
    ![ The Create Account page is where users provide basic details like a unique username, secure password, and email. It initiates setting up an account and granting access to some of the features, such as the "create news story" button, upon completion. ]( ./img/readme/creat-account-page.png)

- [x] View stories by author
    ![ This feature allows users to explore a collection of stories specifically organized by their respective authors. Clicking on an author's name within a story card redirects users to that specific author's dedicated story page. ]( ./img/readme/View-stories-by-author.png )

- [x] "Log-in" button only visible when no user is logged in/"Log-out" buttononly visible when a user *is* logged in
    ![ Users will see the "Log-in" button only if they're not logged in. It's there to help them sign in. On the flip side, the "Log-out" button shows up when they're logged in, making it easy to log out. These buttons displayed in NAV bar and will be adjust based on whether they're logged in or not.]( ./img/readme/login-visibility.png )

- [x] "Create Story" functionality only available when user is logged in
    ![ The "Create Story" button on the story news page is visible exclusively to users who are logged in. This button serves as a prompt for authenticated users, allowing them to contribute by crafting and sharing their own stories.]( ./img/readme/Create-Story.png)


## Additional Features:

- [] Add categories to the stories and allow the user to search for stories bycategory.
    ![ {{ Description of image }} ]( {{ ./relative_path_to_image_file }} )

- [x] Add the ability to update and delete stories (consider permissions - whoshould be allowed to update or and/or delete stories).
    ![ I've included an Edit button that allows users to make changes to their stories. This option appears when the user is logged in and the story belongs to that particular author. ](./img/readme/edit-story-button.png)

- [ ] Add the ability to “favourite” stories and see a page with your favouritestories.
    ![ {{ Description of image }} ]( {{ ./relative_path_to_image_file }} )

- [ ] Our form for creating stories requires you to add the publication date,update this to automatically save the publication date as the day thestory was first published (maybe you could then add a field to showwhen the story was updated).
    ![ {{ Description of image }} ]( {{ ./relative_path_to_image_file }} )


- [ ] Gracefully handle the error where someone tries to create a new story whenthey are not logged in.
    ![ {{ Description of image }} ]( {{ ./relative_path_to_image_file }} )


[x] "Add comment" form
    ![ This "Add Comment" form and functionality enable users to contribute their thoughts or feedback to a particular story. It could be found beneath the story, the form includes fields for users to enter their name, username and comment text . Users can submit their comments by clicking a "Add Comment" button.]( ./img/readme/adding_comment.png)
( ./img/readme/comment-sample.png)