import sys, os, requests, json
import unittest
sys.path.append(os.getcwd())
from app import app
from utils import utils

class TestAPI(unittest.TestCase):


    def setUp(self):
        app.config["TESTING"] = True
        self.app = app.test_client()
        print("Testing API")


    def tearDown(self):
        pass
    

    def test_get_success_1(self):
        response = self.app.get("/", follow_redirects=True)
        self.assertEqual(200, response.status_code)


    def test_get_success_2(self):
        response = self.app.get("/api/v1/products")
        self.assertEqual(200, response.status_code)

    
    def test_post_success_1(self):
        record = {
            "supplier": "test",
            "supplier_sku": "test",
            "ean": "test"
        }
        response = self.app.post("/api/v1/products", json=record)
        self.assertEqual(201, response.status_code)
    

    def test_post_failure_1(self):
        record = {
            "supplier" : "",
            "supplier_sku" : "",
            "ean" : "",
            "row_not_allowed" : ""
        }
        actual = self.app.post("/api/v1/products", json=record)
        expectation = "Too many or too few rows"
        self.assertEqual(expectation, actual.data.decode("utf-8"))
        self.assertEqual(400, actual.status_code)


    def test_post_failure_2(self):
        record = {
            "wrong_key" : "",
            "supplier_sku" : "",
            "ean" : ""
        }
        actual = self.app.post("/api/v1/products", json=record)
        expectation = "One of the keys is incorrect"
        self.assertEqual(expectation, actual.data.decode("utf-8"))
        self.assertEqual(400, actual.status_code)


    def test_put_success_1(self):
        record = {
            "supplier" : "put_success",
            "supplier_sku" : "put_success",
            "ean" : "put_success"
        }
        actual = self.app.put("api/v1/products/0", json=record)
        self.assertEqual(200, actual.status_code)
    

    def test_put_failure_1(self):
        record = {
            "supplier" : "put_success",
            "supplier_sku" : "put_success",
            "ean" : "put_success"
        }
        actual = self.app.put("/api/v1/products/-1", json=record)
        expectation = "ID doesnt exist"
        self.assertEqual(expectation, actual.data.decode("utf-8"))
        self.assertEqual(400, actual.status_code)


    def test_put_failure_2(self):
        record = {
            "supplier" : "",
            "supplier_sku" : "",
            "ean" : "",
            "row_not_allowed" : ""
        }
        actual = self.app.put("/api/v1/products/1", json=record)
        expectation = "Too many or too few rows"
        self.assertEqual(expectation, actual.data.decode("utf-8"))
        self.assertEqual(400, actual.status_code)


    def test_put_failure_3(self):
        record = {
            "wrong_key" : "",
            "supplier_sku" : "",
            "ean" : ""
        }
        actual = self.app.put("/api/v1/products/1", json=record)
        expectation = "One of the keys is incorrect"
        self.assertEqual(expectation, actual.data.decode("utf-8"))
        self.assertEqual(400, actual.status_code)
    

    def test_z_delete_success_1(self):
        actual = self.app.delete("/api/v1/products/0")
        self.assertEqual(200, actual.status_code)


if __name__ == "__main__":
    with open("data/data.json") as f:
        data = json.load(f)
    data["records"].append({
        "id": "0",
        "supplier": "put_success",
        "supplier_sku": "put_success",
        "ean": "put_success"
    })
    utils.write_json_to_file("data/data.json", data)
    unittest.main()