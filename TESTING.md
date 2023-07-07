# Travel Tickr API
The testing.md file provides an overview of the testing conducted on Travel Tickr webapp. It covers code validation, accessibility, performance, testing on various devices, browser compatibility, testing user stories, and user feedback and improvements. Each section describes the tools used, the issues found (if any), and the corresponding test results.

## Table of Content
1. [Code Validation](#code-validation)
2. [Automated testing](#automated-testing)
3. [Summary](#summary)

### Code Validation 
[PEP 8](https://pep8ci.herokuapp.com/) is a style guide for writing Python code to ensure consistency and readability. It provides guidelines on how to format code, naming conventions for variables and functions, and other best practices. Following PEP 8 helps to improve code quality, readability, and maintainability.

#### backend
| **Tested** | **Result** | **View Result** | **Pass** |
--- | --- | --- | :---:
|serializers|No errors|[Result](/docs/testing/backend/serializers.png)| :white_check_mark:
|settings|No errors|[Result](/docs/testing/backend/settings.png)| :white_check_mark:
|urls|No errors|[Result](/docs/testing/backend/urls.png)| :white_check_mark:
|views|No errors|[Result](/docs/testing/backend/views.png)| :white_check_mark:

#### Bucketlist
| **Tested** | **Result** | **View Result** | **Pass** |
--- | --- | --- | :---:
|models|No errors|[Result](/docs/testing/bucketlist/models.png)| :white_check_mark:
|serializers|No errors|[Result](/docs/testing/bucketlist/serializers.png)| :white_check_mark:
|urls|No errors|[Result](/docs/testing/bucketlist/urls.png)| :white_check_mark:
|views|No errors|[Result](/docs/testing/bucketlist/views.png)| :white_check_mark:

#### Comments
| **Tested** | **Result** | **View Result** | **Pass** |
--- | --- | --- | :---:
|models|No errors|[Result](/docs/testing/comments/models.png)| :white_check_mark:
|serializers|No errors|[Result](/docs/testing/comments/serializers.png)| :white_check_mark:
|urls|No errors|[Result](/docs/testing/comments/urls.png)| :white_check_mark:
|views|No errors|[Result](/docs/testing/comments/views.png)| :white_check_mark:

#### Followers
| **Tested** | **Result** | **View Result** | **Pass** |
--- | --- | --- | :---:
|models|No errors|[Result](/docs/testing/followers/models.png)| :white_check_mark:
|merializers||[Result](/docs/testing/followers/serializers.png)| :white_check_mark:
|urls|No errors|[Result](/docs/testing/followers/urls.png)| :white_check_mark:
|views|No errors|[Result](/docs/testing/followers/views.png)| :white_check_mark:

#### Likes
| **Tested** | **Result** | **View Result** | **Pass** |
--- | --- | --- | :---:
|models|No errors|[Result](/docs/testing/likes/models.png)| :white_check_mark:
|merializers|No errors|[Result](/docs/testing/likes/serializers.png)| :white_check_mark:
|urls|No errors|[Result](/docs/testing/likes/urls.png)| :white_check_mark:
|views|No errors|[Result](/docs/testing/likes/views.png)| :white_check_mark:

#### Posts
| **Tested** | **Result** | **View Result** | **Pass** |
--- | --- | --- | :---:
|models|No errors|[Result](/docs/testing/posts/models.png)| :white_check_mark:
|serializers|No errors|[Result](/docs/testing/posts/serializers.png)| :white_check_mark:
|tests|No errors|[Result](/docs/testing/posts/tests.png)| :white_check_mark:
|urls|No errors|[Result](/docs/testing/posts/urls.png)| :white_check_mark:
|views|No errors|[Result](/docs/testing/posts/views.png)| :white_check_mark:

#### Travelers
| **Tested** | **Result** | **View Result** | **Pass** |
--- | --- | --- | :---:
|models|No errors|[Result](/docs/testing/travelers/models.png)| :white_check_mark:
|serializers|No errors|[Result](/docs//testing/travelers/serializers.png)| :white_check_mark:
|tests|No errors|[Result](/docs/testing/travelers/tests.png)| :white_check_mark:
|urls|No errors|[Result](/docs/testing/travelers/urls.png)| :white_check_mark:
|views|No errors|[Result](/docs//testing/travelers/views.png)| :white_check_mark:

Note: The specific details and validation results for each file can be viewed by expanding the corresponding sections.

### Automated testing

The application have used some automated testing to ensure the functionality of the Post API endpoints as well as the consistent extension of teh User model with the Traveler model. Her is an overview of the tests:

**Post Listing:** To verify that the API correctly lists the posts available.
**Post Creation:** To check whether an authenticated user can successfully create a post.
**Unauthorized Post Creation:** To ensure that unauthenticated users are not allowed to create posts.
**Post Retrieval:** The test verify that posts can be retrieved using valid identifiers. Additionally, it will check that the system correctly handles retrieval requests for non-existent posts.
**Post Updates:** To confirm that a user can update their own posts, and importantly, they cannot modify other user's posts. 
**User-Traveler Consistency:** We run tests to confirm that each user is always extended with the Traveler model. 

To run the tests, navigate to the main directory of the project and execute the following command in the terminal:

```bash
python manage.py test 
```
Upon successful execution of the tests, you should see output similar to the following:
```bash
Creating test database for alias 'default'...
System check identified no issues (0 silenced).
....OrderedDict([('count', 1), ('next', None), ('previous', None), ('results', [OrderedDict([('id', 1), ('owner', 'testUser'), ('is_owner', False), ('traveler_id', 1), ('traveler_image', 'https://res.cloudinary.com/sandrabergstrom/image/upload/v1/media/../default_profile_uwgpte'), ('created_at', 'now'), ('updated_at', 'now'), ('title', 'test title'), ('content', ''), ('image', 'https://res.cloudinary.com/sandrabergstrom/image/upload/v1/media/../default_post_rgq6aq'), ('likes_count', 0), ('comments_count', 0), ('like_id', None), ('bucketlists_count', 0), ('bucketlist_id', None), ('location', 'Somewhere'), ('country', 'Unknown')])])])
4
....
----------------------------------------------------------------------
Ran 8 tests in 1.077s

OK
Destroying test database for alias 'default'...
```

This signifies that all tests have passed successfully. If any test fails, the output will clearly specify which test failed and the reason to failure. If you see an output similar to the above, it means your setup is working as expected. 

### Manual testing
Throughout the development process, rigorous manual testing was performed to ensure the effective operation of the backend components. Each API endpoint was tested for correct functionality, response, and error handling. Database interactions were also scrutinized to confirm data integrity, accuracy and consistency. This level of detailed manual testing has proven essential in validating the performance of the backend and its seamless integration with the frontend application.

### Summary
The testing process for the Travel Tickr API has been exhaustive and meticulous, reinforcing the robustness and reliability of the platform. Python's best coding practices were upheld by utilizing the PEP 8 tool to check for errors in each application module.

Automated testing has been a critical part of the process, covering key functionalities such as post listing, post creation, post retrieval, post updates, and user-traveler consistency.

All tests for the Travel Tickr API have been passed, demonstrating its readiness for deployment and public use. For a detailed account of the front-end testing, please  [click here](https://github.com/SandraBergstrom/travel-tickr/blob/main/TESTING.md).
