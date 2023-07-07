![Logo](/docs/logo.jpg)
# Travel Tickr API Documentation

Welcome to the Travel Tickr API documentation. This readme provides information about the API endpoints and functionalities. For the documentation of the Travel Tickr web app, please visit the following link: [Travel Tickr Repository](https://github.com/SandraBergstrom/travel-tickr-api).

## Table of Content
- [Database](#database)
  * [Bucketlist:](#bucketlist-)
  * [Comment:](#comment-)
  * [Follower:](#follower-)
  * [Like:](#like-)
  * [Post:](#post-)
  * [Traveler:](#traveler-)
- [Bugs](#bugs)
  * [Known bugs](#known-bugs)
  * [Fixed bugs](#fixed-bugs)
- [Testing](#testing)
  * [Languages](#languages)
  * [Frameworks](#frameworks)
  * [Database](#database-1)
  * [Tools](#tools)
  * [Supporting Libraries and Packages](#supporting-libraries-and-packages)
- [Deployment](#deployment)
  * [Django Documentation:](#django-documentation-)

<small><i><a href='http://ecotrust-canada.github.io/markdown-toc/'>Table of contents generated with markdown-toc</a></i></small>

## Database
The Travel Tickr utilizes the following database schema:
<details><summary>See Database Schema</summary>
<img src="/docs/database-diagram.png">
</details> <br>

### Bucketlist: 
This model represents the list of posts that a user wants to keep track of. It is related to the User model (as the owner of the bucketlist) and the Post model. 

### Comment: 
This model represents comments made by users. It is associated with the User model (as the owner of the comment) and the Post model. In addition to the content of the comment, it keeps track of the times when each comment was created and last updated.

### Follower: 
This model maintains the follower-following relationships between users. It is related to the User model twice, once for the owner of the follow (the follower) and once for the followed user. A timestamp of each follow event is also stored.

### Like: 
This model captures the likes given by users either to a post or a comment. It is linked to the User, Post, and Comment models. It also records the time when each like event was created.

### Post: 
This model represents the posts made by users. It is related to the User model as the owner of the post. It keeps track of the times when each post was created and last updated, along with the content of the post including the title, image, and location information.

### Traveler: 
This model extends the User model with additional traveler-specific information such as their name, profile image, and other personal details. It also keeps timestamps of when each traveler profile was created and last updated. The creation of a Traveler object is automatically triggered by the creation of a User object, thanks to the post_save signal connected to the create_traveler function.

Each of these models serves a unique purpose and together they support a range of features in your application, from user registration and social networking to content creation and curation.

## Bugs

### Known bugs

| **Bug** | **Status** |
| ----------- | ----------- |
| [iPhone X log in](https://github.com/SandraBergstrom/travel-tickr-api/issues/3)| There is a known bug identified in the initial codebase that has been acknowledged and will not be addressed prior to the project submission. |

### Fixed bugs 
Here is a summary of the identified bugs along with brief descriptions of their fixes. For more detailed information, please follow the provided link to the corresponding GitHub issue, where you can track the entire process including the bug report, commits, and the steps taken to resolve the issue.

| **Bug** | **Fix** |
| ----------- | ----------- |
|[Submit issue with registration form](https://github.com/SandraBergstrom/travel-tickr-api/issues/1)|Correct CORS settings|
|[Can't follow some travelers](https://github.com/SandraBergstrom/travel-tickr/issues/60#issue-1789572956)|See details and steps in link to issue|
|[Likes_count showing NaN in comments](https://github.com/SandraBergstrom/travel-tickr-api/issues/4#issue-1793434957)|Correct connection in queryset for comments|
|[Filter function is not working](https://github.com/SandraBergstrom/travel-tickr/issues/48#issue-1775479887)|Added filter used in frontend|


[Back up](#table-of-content)

## Testing
All tests for the Travel Tickr API have been passed, demonstrating its readiness for deployment and public use. See [full testing documentation](https://github.com/SandraBergstrom/travel-tickr-api/blob/main/TESTING.md).

### Languages
- Python

### Frameworks
- Django: A high-level Python web framework used for building the Travel Tickr API.

### Database
- ElephantSQL: ElephantSQL is a PostgreSQL database as a service. It is used as the database for the Travel Tickr project, providing a reliable and scalable storage solution for the application's data.

### Tools
- Git: A distributed version control system used for tracking changes in the project's source code.
- GitHub: A web-based hosting service for version control repositories, used for storing and managing the project's source code.
- Gitpod: An online integrated development environment (IDE) used for developing and testing the Travel Tickr project.
- Heroku: A cloud platform that enables deployment and hosting of web applications. Heroku was used for deploying the Travel Tickr project to a live server.
- Adobe Photoshop: A professional image editing software used for advanced image manipulation and design in the Travel Tickr project.
- Lucidchart: Lucidchart is a web-based diagramming tool that offers a wide range of diagramming capabilities, including ER diagrams. It provides an intuitive interface and collaboration features, making it suitable for both individual and team use.

### Supporting Libraries and Packages
- asgiref: A server gateway interface for Django, it acts as a translation layer between the web server and Django.
- cloudinary, django-cloudinary-storage: Used for managing the storage and delivery of images through Cloudinary, a cloud-based service.
- dj-database-url: Utility to help you load your database into your dictionary from the DATABASE_URL environment variable.
- dj-rest-auth, Django-allauth, djangorestframework-simplejwt, PyJWT, oauthlib, requests-oauthlib, python3-openid: These libraries are used for managing user authentication, providing support for JWT tokens, OAuth and OpenID.
- Django, djangorestframework, django-filter: These are core components of the Django web framework, used for building the backend of the Travel Tickr application.
- gunicorn: A Python WSGI HTTP server for UNIX, used in deploying the application.
- Pillow: An imaging library in Python, allowing support for opening, manipulating, and saving many different image file formats.
- psycopg2: PostgreSQL adapter for Python, enabling Python to connect to the PostgreSQL database.
- pytz: A Python library that enables accurate and cross-platform timezone calculations.
- sqlparse: A non-validating SQL parser module for Python, it provides support for parsing, splitting and formatting SQL statements.

## Deployment
Deploying the Django backend of the Travel Tickr application involves below steps:

1. **Create Required Accounts**: If you haven't done so yet, create accounts on Heroku, ElephantSQL, and Cloudinary. These services are necessary for hosting the application, managing the database, and storing images, respectively.
2. **Prepare the Application**: Set DEBUG to False in the settings.py file, which ensures that the application runs in production mode during deployment. Commit all changes and push your code to your GitHub repository.
3. **Create a New Application on Heroku**: From your Heroku dashboard, create a new application and select the appropriate region.
4. **Set Environment Variables**: In your local env.py file, set your environment variables including the ElephantSQL URL, Cloudinary URL, and Django Secret Key. These variables should also be added to your Heroku app settings under the Config Vars section. This ensures that these services can communicate with your Heroku app.
5. **Database Management**: Ensure that all database migrations have been made and the current state of your models is reflected in the database schema. The command python manage.py makemigrations and python manage.py migrate are usually used for this purpose in Django.
6. **Deployment Process**: In your Heroku dashboard, go to your application's deploy page. Connect your GitHub repository to your Heroku application under the "Deployment method" section. Under the "Manual deploy" section, select the branch you want to deploy and click "Deploy Branch".
7. **Verify Deployment**: Once the deployment is successful, Heroku will provide a URL to access the live application. Test the application to ensure all components are functioning properly.

Remember to avoid exposing your environment variables in your public repository. Use the Config Vars section in Heroku to securely set your environment variables.

### Django Documentation:
[django-versatileimagefield - Custom filters](https://django-versatileimagefield.readthedocs.io/en/2.1/writing_custom_sizers_and_filters.html)
[Pillow - Image module ](https://pillow.readthedocs.io/en/stable/reference/Image.html)