from google.cloud import bigquery

client = bigquery.Client.from_service_account_json("google-cloud-credentials.json")

rows_to_insert = [
    {
        "akeneo_id": "631226420e6b11ed936566820d83b770sap",
        "supplier": "948934",
        "supplier_sku": "541710",
        "ean": "5710441305156",
        "created": "2022-07-28T11:50:19+00:00",
        "updated": "2022-09-21T09:31:11+00:00"
    }
]

errors = client.insert_rows_json("globus-mdm.haris_wdb.products", rows_to_insert)

if errors == []:
    print("Finished")
else:
    print(errors)


