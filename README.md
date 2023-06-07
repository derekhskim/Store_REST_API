# Store REST API

This project showcases a REST API that enables store and item management operations. It enables the creation, retrieval, and deletion of stores and items.

## Key Features

- User authentication using JWT tokens
- CRUD operations on stores, items, and tags
- Ability to add and remove tags from items
- Asynchronous email notifications upon user registration
- Error handling for JWT token-related issues (expiry, invalidity, etc.)

## Main Modules

### Models

- `ItemModel`: Represents an item with unique name, description, price, and associated store.
- `ItemTags`: Represents a many-to-many relationship between items and tags.
- `StoreModel`: Represents a store with a unique name and associated items and tags.
- `TagModel`: Represents a tag with a unique name and associated items.
- `UserModel`: Represents a user with a unique username and email, and an encrypted password.

### Resources

- `item`: Allows CRUD operations on items. All operations require user authentication.
- `store`: Allows CRUD operations on stores. All operations require user authentication.
- `tag`: Allows adding and removing tags from items. Also allows retrieving all tags associated with a store and deleting a tag if it's not associated with any items.
- `user`: Handles user registration and login.

## Deployment Information
The application has been deployed using the following services:

- **Database**: PostgreSQL hosted on ElephantSQL
- **Backend**: Deployed on render.com
- **Mail Services**: Utilizing Mailgun for email functionality
- **Swagger API**: [Swagger Documentation](https://store-rest-api-f4yf.onrender.com/swagger-ui)

You can test things with the link: https://store-rest-api-f4yf.onrender.com/ or use provided Postman Workspace link below.

## POSTMAN Testing: 
[Postman Workspace Link](https://www.postman.com/technical-cosmologist-79040812/workspace/rest-apis-course-project/overview)

# API Documentation

## Endpoints and Usage

### Create a Store

- **Request:**

    `POST /store`

    ```json
    {
        "name": "My Store"
    }
    ```

- **Response:**

    ```json
    {
        "id": "<generated_store_id>",
        "items": [
            {
                "id": <item_id>,
                "name": "Your Item",
                "price": Item Price
            }
        ], 
        "name": "My Store", 
        "tags": []
    }
    ```

### Retrieve All Stores and Their Items

- **Request:**

    `GET /store`

- **Response:**

    ```json
    {
        "id": "<generated_store_id>",
        "items": [
            {
                "id": <item_id>,
                "name": "Your Item",
                "price": Item Price
            }
        ],
        "name": "My Store", 
        "tags": []
    }
    ```

### Retrieve a Specific Store

- **Request:**

    `GET /store/<store_id>`

- **Response:**

    ```json
    {
        "id": "<generated_store_id>",
        "items": [
            {
                "id": <item_id>,
                "name": "Your Item",
                "price": Item Price
            }
        ], 
        "name": "My Store", 
        "tags": []
    }
    ```

### Update a Store

- **Request:**

    `PUT /store/<store_id>`

    ```json
    {
        "name": "New Store Name"
    }
    ```

- **Response:**

    ```json
    {
        "id": "<generated_store_id>",
        "items": [
            {
                "id": <item_id>,
                "name": "Your Item",
                "price": Item Price
            }
        ], 
        "name": "New Store Name", 
        "tags": []
    }
    ```

### Delete a Store

- **Request:**

    `DELETE /store/<store_id>`

- **Response:**

    ```json
    {
        "message": "Store deleted."
    }
    ```

### Create an Item

- **Request:**

    `POST /item`

    ```json
    {
        "name": "Item Name",
        "price": Item Price,
        "store_id": "<store_id>"
    }
    ```

- **Response:**

    ```json
    {
        "id": <generated_item_id>,
        "name": "Item Name",
        "price": Item Price,
        "store": {
            "id": <store_id>,
            "name": "Store Name"
        },
        "tags": []
    }
    ```

### Retrieve All Items

- **Request:**

    `GET /item`

- **Response:**

    ```json
    {
        "id": <item_id>,
        "name": "Item Name",
        "price": Item Price,
        "store": {
            "id": <store_id>,
            "name": "Store Name"
        },
        "tags": []
    }
    ```

### Retrieve a Specific Item

- **Request:**

    `GET /item/<item_id>`

- **Response:**

    ```json
    {
        "id": <item_id>,
        "name": "Item Name",
        "price": Item Price,
        "store": {
            "id": <store_id>,
            "name": "Store Name"
        },
        "tags": []
    }
    ```

### Update an Item

- **Request:**

    `PUT /item/<item_id>`

    ```json
    {
        "name": "New Name", 
        "price": New Price,
        "store_id": <store_id>
    }
    ```

- **Response:**

    ```json
    {
        "id": <item_id>,
        "name": "New Name",
        "price": New Price,
        "store": {
            "id": <store_id>,
            "name": "Store Name"
        },
        "tags": []
    }
    ```

### Delete an Item

- **Request:**

    `DELETE /item/<item_id>`

- **Response:**

    ```json
    {
        "message": "Item deleted."
    }
    ```
    
### User Registration

- **Request:**

    `POST /register`

    ```json
    {
        "username": "noobietubie",
        "email": "noobie@example.com",
        "password": "password123"
    }
    ```

- **Response:**

    ```json
    {
        "message": "User created successfully."
    }
    ```

### User Login

- **Request:**

    `POST /login`

    ```json
    {
        "username": "noobietubie",
        "password": "password123"
    }
    ```

- **Response:**

    ```json
    {
        "access_token": "<access_token>",
        "refresh_token": "<refresh_token>"
    }
    ```

### Token Refresh

- **Request:**

    `POST /refresh`

- **Response:**

    ```json
    {
        "access_token": "<new_access_token>"
    }
    ```

### User Logout

- **Request:**

    `POST /logout`

- **Response:**

    ```json
    {
        "message": "Successfully logged out."
    }
    ```

### Retrieve a Specific User

- **Request:**

    `GET /user/<user_id>`

- **Response:**

    ```json
    {
        "id": "<user_id>",
        "username": "noobie"
    }
    ```

### Delete a User

- **Request:**

    `DELETE /user/<user_id>`

- **Response:**

    ```json
    {
        "message": "User deleted."
    }
    ```

### Create a Tag in a Store

- **Request:**

    `POST /store/<store_id>/tag`

    ```json
    {
        "name": "Tag Name"
    }
    ```

- **Response:**

    ```json
    {
        "id": <tag_id>,
        "items": [
            {
                "id": <item_id>,
                "name": "Your Item",
                "price": Item Price
            }
        ],
        "name": "Tag name",
        "store": {
            "id": <store_id>,
            "name": "Store Name"
        }
    }
    ```
    
### Retrieve a Specific Tag

- **Request:**

    `GET /tag/<tag_id>`

- **Response:**

    ```json
    {
        "id": <tag_id>,
        "items": [
                {
                    "id": <item_id>,
                    "name": "Your Item",
                    "price": Item Price
                }
            ],
        "name": "Tag name",
        "store": {
            "id": <store_id>,
            "name": "Store Name"
        }
    }
    ```

### Retrieve Tags in a Store

- **Request:**

    `GET /store/<store_id>/tag`

- **Response:**

    ```json
    {
        "id": <tag_id>,
        "items": [
            {
                "id": <item_id>,
                "name": "Your Item",
                "price": Item Price
            }
        ],
        "name": "Tag name",
        "store": {
            "id": <store_id>,
            "name": "Store Name"
        }
    }
    ```

### Link Tags to an Item

- **Request:**

    `POST /item/<item_id>/tag/<tag_id>`

- **Response:**

    ```json
    {
        "id": <tag_id>,
        "items": [
            {
                "id": <item_id>,
                "name": "Your Item",
                "price": Item Price
            }
        ],
        "name": "Tag name",
        "store": {
            "id": <store_id>,
            "name": "Store Name"
        }
    }
    ```

### Remove Tags from an Item

- **Request:**

    `DELETE /item/<item_id>/tag/<tag_id>`

- **Response:**

    ```json
    {
        "item": {
            "id": <item_id>,
            "name": "Your Item",
            "price": Item Price,
            "store": {
                "id": <store_id>,
                "name": "Store Name"
            },
            "tags": []
        },
        "message": "Item removed from tag",
        "tag": {
            "id": <tag_id>,
            "items": [
                {
                    "id": <item_id>,
                    "name": "Your Item",
                    "price": Item Price
                }
            ],
            "name": "Tag name",
            "store": {
                "id": <store_id>,
                "name": "Store Name"
            }
        }
    }
    ```

### Delete a Tag

- **Request:**

    `DELETE /tag/<tag_id>`

- **Response:**

    ```json
    {
        "message": "Tag deleted."
    }
    ```
