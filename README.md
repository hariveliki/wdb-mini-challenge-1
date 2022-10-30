## Introduction
The idea of this API is to provide a way to store and retrieve product data.

## Why REST API vs GraphQL?
<table><thead><tr><th>GraphQL</th><th>REST</th></tr></thead><tbody><tr><td>A query language for solving common problems when integrating APIs</td><td>An architectural style largely viewed as a conventional standard for designing APIs</td></tr><tr><td>Deployed over HTTP using a single endpoint that provides the full capabilities of the exposed service</td><td>Deployed over a set of URLs where each of them exposes a single resource</td></tr><tr><td>Uses a client-driven architecture</td><td>Uses a server-driven architecture</td></tr><tr><td>Lacks in-built caching mechanism</td><td>Uses caching automatically</td></tr><tr><td>No API versioning required</td><td>Supports multiple API versions</td></tr><tr><td>Response output in JSON</td><td>Response output usually in XML, JSON, and YAML</td></tr><tr><td>Offers type-safety and auto-generated documentation</td><td>Doesn't offer type-safety or auto-generated documentation</td></tr><tr><td>Allows for schema stitching and remote data fetching</td><td>Simplifying work with multiple endpoints requires expensive custom middleware</td></tr></tbody></table>

## HTTP Methods for RESTful Services

### url/api/v1/products
Get all existing products.

### <code>GET:</code>/getlist
Get a specific watchlist.
<table><tr><th>Required Params</th><th>Login Required</th></tr><td>name</td><td>True</td></table>

### <code>POST:</code>/addlist
Add a new watchlist.
<table><tr><th>Required Params</th><th>Login Required</th></tr><td>name</td><td>True</td></table>

### <code>DELETE:</code>/removelist
Remove a watchlist.
<table><tr><th>Required Params</th><th>Login Required</th></tr><td>name</td><td>True</td></table>

### <code>POST:</code>/additem
Add an item to a watchlist.
<table><tr><th>Required Params</th><th>Login Required</th></tr><td>name, item, amount</td><td>True</td></table>

### <code>PUT:</code>/updateitem
Update an item of a watchlist.
<table><tr><th>Required Params</th><th>Login Required</th></tr><td>name, item, amount</td><td>True</td></table>

### <code>DELETE:</code>/removeitem
Remove an item from a watchlist.
<table><tr><th>Required Params</th><th>Login Required</th></tr><td>name, item</td><td>True</td></table>

### <code>POST:</code>/adduser
Add a user.
<table><tr><th>Required Params</th><th>Login Required</th></tr><td>user, password</td><td>False</td></table>

### <code>POST:</code>/login
Login a user.
<table><tr><th>Required Params</th><th>Login Required</th></tr><td>user, password</td><td>False</td></table>

### <code>GET:</code>/logout
Logout a user.
<table><tr><th>Required Params</th><th>Login Required</th></tr><td>None</td><td>True</td></table>

 
## Error Response:


  * **Code:** 400 BAD REQUEST <br />
    **Content Example:** `{ Error : Missing required arguments }`

  OR

  * **Code:** 401 UNAUTHORIZED <br />
    **Content:** `{ Error : "Invalid username or password" }`

  OR
   * **Code:** 404 NOT FOUND <br />
    **Content:** `{ Error : ... }`


## Unit Tests
Windows: <code>python3 pytest</code>

OS/Linux:<code> sh test.sh</code>
