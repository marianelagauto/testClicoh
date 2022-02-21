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

## Listar todos los productos
###### GET /api/products/

## Obtener un producto
###### GET /api/products/{id}

## Crear un producto
###### POST /api/products/

```
Body: 
    {
        "name": <string>,
        "price": <integer>,
        "stock": <integer>
    }
```

## Eliminar un producto
###### DELETE /api/products/{id}




