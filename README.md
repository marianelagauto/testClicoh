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

## Authorization header

```
Header: Authorization Bearer
Body: Token <access_token>
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




