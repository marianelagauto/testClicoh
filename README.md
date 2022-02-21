# testClicoh

## API with django rest framework.

### Installation

Use the requirements file to install all dependencies.

```bash
pip install -r requirements.txt
```

### API Usage
#### Authentication
##### Generate a token 
###### POST /api/token/

```
Body: 
    {
        "username": <string>,
        "password": <string>
    }
```

## Header para todos los endpoints
Header: Authorization Bearer
Body: Token <access_token>

#### Listar todos los productos
##### GET /api/products/

#### Obtener un producto
##### GET /api/products/{id}

#### Crear un producto
##### POST /api/products/

```
Body: 
    {
        "name": <string>,
        "price": <integer>,
        "stock": <integer>
    }
```

#### Eliminar un producto
##### DELETE /api/products/{id}




