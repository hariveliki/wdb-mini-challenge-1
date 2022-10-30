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


 

## Why REST API vs GraphQL?
<table><thead><tr><th>GraphQL</th><th>REST</th></tr></thead><tbody><tr><td>A query language for solving common problems when integrating APIs</td><td>An architectural style largely viewed as a conventional standard for designing APIs</td></tr><tr><td>Deployed over HTTP using a single endpoint that provides the full capabilities of the exposed service</td><td>Deployed over a set of URLs where each of them exposes a single resource</td></tr><tr><td>Uses a client-driven architecture</td><td>Uses a server-driven architecture</td></tr><tr><td>Lacks in-built caching mechanism</td><td>Uses caching automatically</td></tr><tr><td>No API versioning required</td><td>Supports multiple API versions</td></tr><tr><td>Response output in JSON</td><td>Response output usually in XML, JSON, and YAML</td></tr><tr><td>Offers type-safety and auto-generated documentation</td><td>Doesn't offer type-safety or auto-generated documentation</td></tr><tr><td>Allows for schema stitching and remote data fetching</td><td>Simplifying work with multiple endpoints requires expensive custom middleware</td></tr></tbody></table>

| test  | test2  |   |   |   |
|-------|--------|---|---|---|
| value | value2 |   |   |   |
|       |        |   |   |   |
|       |        |   |   |   |
