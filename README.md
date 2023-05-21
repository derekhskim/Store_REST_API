# My First REST API

This project showcases a simple REST API that enables various store management operations. It enables creation of stores and items, as well as retrieval of information related to stores and the items they stock.

## Features

This REST API provides the following operations:

1. **Create a Store:** You can create a new store by providing its name.
2. **Create an Item:** You can add an item to a specific store by providing the item's name and price.
3. **Retrieve Stores:** Retrieve a list of all the stores along with the items they stock.
4. **Retrieve a Particular Store:** Retrieve the details of a specific store along with the items it stocks, by providing the store's name.
5. **Retrieve Items from a Store:** Retrieve a list of all items from a specific store, by providing the store's name.

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
        "items": []
    }
    ```

**Create an Item**

- **Request:**

    `POST /store/My Store/item`

    ```json
    {
        "name": "Chair", 
        "price": 175.50
    }
    ```

- **Response:**

    ```json
    {
        "name": "Chair", 
        "price": 175.50
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
                "items": [
                    {
                        "name": "Chair",
                        "price": 175.50
                    }
                ]
            }
        ]
    }
    ```

    **Retrieve a Particular Store**

- **Request:**

    `GET /store/My Store`

- **Response:**

    ```json
    {
        "name": "My Store",
        "items": [
            {
                "name": "Chair",
                "price": 175.50
            }
        ]
    }
    ```

**Retrieve Items from a Store**

- **Request:**

    `GET /store/My Store/item`

- **Response:**

    ```json
    [
        {
            "name": "Chair",
            "price": 175.50
        }
    ]
    ```