## Introduction and How To

The idea of this API is to provide a way to store and retrieve product data.
Just clone the repository on your local machine and run the programm "app.py".
After running "app.py" a webserver starts running and you can use GET/POST/PATCH/DELETE requests via the webbrowser or with Postman.
The data is stored on your local machine at "data/data.json".
For running the tests go to "test/test_api.py" and run the programm.

## Data structure
Used data structure to store the data:
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

e.g. through webbrowser:<br/>
<img width="637" alt="image" src="https://user-images.githubusercontent.com/98284163/201217188-61a1dad2-f0ef-492e-b88c-80ce7e4bb2f8.png">

e.g. through postman:<br/>
<img width="676" alt="image" src="https://user-images.githubusercontent.com/98284163/201218486-9885ecbd-e6b1-4894-baf1-b0e7d0dc71c8.png">


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

e.g. through Postman:<br/>
<img width="624" alt="image" src="https://user-images.githubusercontent.com/98284163/201218142-e71a6155-1315-4b20-84ff-8be5a1af2275.png">


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
e.g. through Postman:<br/>
<img width="624" alt="image" src="https://user-images.githubusercontent.com/98284163/201217716-21868303-7cc2-46a3-9e9b-b9537feae945.png">


### DELETE
url/api/v1/products/<product_id> -> Delete existing product <br />


### Report
For further details look at docs/report.md
