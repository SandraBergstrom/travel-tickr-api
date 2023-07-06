

## Bugs

### Known bugs

| **Bug** | **Status** |
| ----------- | ----------- |
| []()|  |
|||

### Fixed bugs 

| **Bug** | **Fix** |
| ----------- | ----------- |
|[Submit issue with registration form](https://github.com/SandraBergstrom/travel-tickr-api/issues/1)|Correct CORS settings|


[Back up](#table-of-content)

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