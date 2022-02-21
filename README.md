# testClicoh

## API with Django Rest Framework.

## Installation

Install all dependencies.

```bash
pip install -r requirements.txt
```

## API Usage

## Generate token
###### POST /api/token/

```
Body: 
    {
        "username": <string>,
        "password": <string>
    }
```

```
Response: 
    {
        "refresh": <refresh>,
        "access": <access>
    }
```

## Authorization header

```
Header: Authorization Bearer
Body: Token <access>
```

## List products
###### GET /api/products/

## Get a product
###### GET /api/products/{id}

## Create new product
###### POST /api/products/

```
Body: 
    {
        "name": <string>,
        "price": <integer>,
        "stock": <integer>
    }
```
## Edit a product
###### PUT /api/products/{id}

```
Body: 
    {
        "id": <integer>,
        "name": <string>,
        "price": <integer>,
        "stock": <integer>
    }
```

## Delete a product
###### DELETE /api/products/{id}

## List orders with details
###### GET /api/orders/

## Get an order with details
###### GET /api/orders/{id}

## Create new order
###### POST /api/orders/

```
Body: 
    {
        "date_time": "2022-02-17 01:23:00",
        "details": [
            {
                "product": <product_id>,
                "cuantity": <cuantity>
            },
            {
                "product": <product_id>,
                "cuantity": <cuantity>
            }
        ]
    }
```
## Edit an order
###### PUT /api/orders/{id}

```
Body: 
    {
        "date_time": "2022-02-17 01:23:00",
        "details": [
            {
                "id": <id>,
                "product": <product_id>,
                "cuantity": <cuantity>
            },
            {
                "id": <id>,
                "product": <product_id>,
                "cuantity": <cuantity>
            }
        ]
    }
```

## Delete an order 
###### DELETE /api/orders/{id}




