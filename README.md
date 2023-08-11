# News-Server RESTAPI
Brief introduction to your API, what it does, and its purpose.

## Table of Contents
Authentication
Articles
Categories
## Authentication
Explain how authentication works in your API and provide details about the authentication endpoints.

### POST api/v1/auth/login/
Description: Logs in a user and returns an authentication token.

Request:

```
json
Copy code
{
  "username": "your_username",
  "password": "your_password"
}
```

Response:
```
json
Copy code
{
  "token": "your_authentication_token"
}
```
### GET api/v1/auth/logout/
Description: Logs out the user and deletes the associated token.

### POST api/v1/auth/password/change/
Description: Allows the user to change their password.

Request:

```
json
Copy code
{
  "old_password": "your_old_password",
  "new_password": "your_new_password"
}
...
```
Provide similar explanations for other authentication endpoints.

## Articles
Explain the endpoints related to articles.

### GET api/v1/articles/
Description: Retrieves a list of articles.

Response:

```
json
Copy code
[
  {
    "id": 1,
    "title": "Article Title",
    ...
  },
  ...
]
```
## GET api/v1/articles/admin/
Description: Retrieves a list of articles for admin users.

### POST api/v1/articles/create/
Description: Creates a new article.

Request:
```
json
Copy code
{
  "title": "New Article",
  ...
}
```
Response:
```
json
Copy code
{
  "id": 123,
  "title": "New Article",
  ...
}
...
```
Continue with explanations for other article-related endpoints.

## Categories
Explain the endpoints related to categories.

### GET api/v1/category/
Description: Retrieves a list of categories.

Response:
```
json
Copy code
[
  {
    "id": 1,
    "name": "Category Name",
    ...
  },
  ...
]
```
### POST api/v1/category/create/
Description: Creates a new category.

Request:
```
json
Copy code
{
  "name": "New Category",
  ...
}
```
Response:
```
json
Copy code
{
  "id": 456,
  "name": "New Category",
  ...
}
...
```
Continue with explanations for other category-related endpoints.

## API Documentation
If you'd like to dive into more technical details about the API endpoints, their request and response formats, you can provide a link to more in-depth API documentation. This could be a separate document or a hosted API documentation tool.
