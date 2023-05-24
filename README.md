# My First REST API

This project showcases a REST API that enables store and item management operations. It enables the creation, retrieval, and deletion of stores and items.

## Features

This REST API provides the following operations:

1. **Create a Store:** You can create a new store by providing its name.
2. **Retrieve All Stores:** Retrieve a list of all the stores along with the items they stock.
3. **Retrieve a Specific Store:** Retrieve the details of a specific store along with the items it stocks, by providing the store's ID.
4. **Delete a Store:** Delete a specific store by providing its ID.
5. **Retrieve All Items:** Retrieve a list of all items.
6. **Retrieve a Specific Item:** Retrieve the details of a specific item by providing its ID.
7. **Delete an Item:** Delete a specific item by providing its ID.
8. **Update an Item:** Update the details of a specific item by providing its ID and the updated details.

## API Endpoints and Usage

**Create a Store**

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
        "name": "My Store", 
        "id": "<generated_store_id>"
    }
    ```

**Retrieve All Stores and Their Items**

- **Request:**

    `GET /store`

- **Response:**

    ```json
    {
        "stores": [
            {
                "name": "My Store",
                "id": "<store_id>",
                "items": []
            }
            // ... additional stores
        ]
    }
    ```

**Retrieve a Specific Store**

- **Request:**

    `GET /store/<store_id>`

- **Response:**

    ```json
    {
        "name": "My Store",
        "id": "<store_id>",
        "items": []
    }
    ```

**Delete a Store**

- **Request:**

    `DELETE /store/<store_id>`

- **Response:**

    ```json
    {
        "message": "Store was successfully deleted."
    }
    ```

**Retrieve All Items**

- **Request:**

    `GET /item`

- **Response:**

    ```json
    {
        "items": [
            // ... list of items
        ]
    }
    ```

**Retrieve a Specific Item**

- **Request:**

    `GET /item/<item_id>`

- **Response:**

    ```json
    {
        "name": "<item_name>", 
        "price": "<item_price>", 
        "id": "<item_id>"
    }
    ```

**Delete an Item**

- **Request:**

    `DELETE /item/<item_id>`

- **Response:**

    ```json
    {
        "message": "Item was successfully deleted."
    }
    ```

**Update an Item**

- **Request:**

    `PUT /item/<item_id>`

    ```json
    {
        "name": "New Name", 
        "price": "<new_price>"
    }
    ```

- **Response:**

    ```json
    {
        "name": "New Name", 
        "price": "<new_price>", 
        "id": "<item_id>"
    }
    ```

## POSTMAN Testing: 
[Postman Workspace Link](https://www.postman.com/technical-cosmologist-79040812/workspace/rest-apis-course-project/overview)
