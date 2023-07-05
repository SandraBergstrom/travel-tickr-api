# Travel Tickr API
The testing.md file provides an overview of the testing conducted on Travel Tickr webapp. It covers code validation, accessibility, performance, testing on various devices, browser compatibility, testing user stories, and user feedback and improvements. Each section describes the tools used, the issues found (if any), and the corresponding test results.

## Table of Content

1. [Code Validation](#html-validation)
    1. [Python Validation](#python-validation)
2. [Automated testing]()
3. [Summary](#summary)

### Python Validation 
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