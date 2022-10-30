## Introduction
The idea of this API is to provide a way to store and retrieve product data.

## Data structure
```json
{
    "records": [
        {
            "id": "value",
            "supplier": "value",
            "supplier_sku": "value",
            "ean": "value"
        }
    ]
}
```


## HTTP Methods for RESTful Services

### GET
url/api/v1/products -> Get all existing products.

### POST
url/api/v1/products -> Store new product. <br />
Allowed data structure in body:
```json
{
    "supplier": "value",
    "supplier_sku": "value",
    "ean": "value"
}
```

### PUT
url/api/v1/products/<product_id> -> Update existing product <br />
Allowed data structure in body:
```json
{
    "supplier": "value",
    "supplier_sku": "value",
    "ean": "value"
}
```

### DELETE
url/api/v1/products/<product_id> -> Delete existing product <br />


 

## REST API vs GraphQL

| REST | GRAPHQL |
|------|---------|
|   Over- and underfetching   |    Specifiying exactly the data it needs     |
|   Caches automatically   |    Lacks built-in caching mechanism     |
|   Deployed over a set of URLs   |    Single endpoint     |
| Multiple API versions | No API versions required|

I chose REST because it is a common standard for APIs.
