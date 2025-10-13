# Bookstore
Bookstore with a list of all books, publishers and authors. Also you can access them separately using id. You can authorize to be able to order items from your cart.

## Books
| Method | Endpoint | Description | Response status | Request body | Response body |
| ----------- | ----------- | ----------- |---------------------------------------------| ----------- | ----------- |
| GET | /books | Get a list of all books | 200 | - | json {"id": 1, "name": "Dune", "genre": Science-fiction, "author": "Frank Herbert", "price": 15.00, "popularity": 100} |
| GET | /books/{id} | Get one book by id | 200, 404(if not found) | - | json {"id": 1, "name": "Dune", "description": "...", "genre": Science-fiction, "author": "Frank Herbert", "price": 15.00, "popularity": 100}, "year": 2020 |
| POST | /books | Add new book | 201, 400(if bad request) | json {"name": "Dune", "description": "...", "genre": Science-fiction, "author_id": 1, "price": 15.00, "year": 2020} | json {"id": 1, "name": "Dune", "description": "...", "genre": Science-fiction, "author": "Frank Herbert", "price": 15.00, "popularity": 100, "year": 2020} |
| PUT | /books/{id} | Update a book | 200, 404(if not found), 400(if bad request) | json {"price: 10.00"} | json {"id": 1, "name": "Dune", "description": "...", "genre": Science-fiction, "author": "Frank Herbert", "price": 10.00, "popularity": 100}, "year": 2020 |
| DELETE | /books/{id} | Delete one book by id | 204, 404(if not found) | - | - |

## Authors
| Method | Endpoint | Description | Response status | Request body | Response body |
| ----------- | -------- | ----------- |--------------------------| ----------- | ----------- |
| GET | /authors | Get a list of all authors | 200 | - | json {"id": 1, "name": "Frank Herbert", "books": [...]} |
| GET | /authors/{id} | Get an author by id | 200, 404(if not found) | - | json {"id": 1, "name": "Frank Herbert", "description": "...", "books": [...]} |
| POST | /authors | Add a new author | 201, 400(if bad request) | json {"name": "Frank Herbert", "description": "...", "books": [...]} | json {"id": 1, "name": "Frank Herbert", "description": "...", "books": [...]} |
| PUT | /authors/{id} | Update an author | 200, 404(if no found), 400(if bad request) | json {"description": "..."} | json {"id": 1, "name": "Frank Herbert", "description": "...", "books": [...]} |
| DELETE | /authors/{id} | Delete an author | 204, 404(if not found) | - | - |

## Publishers
| Method | Endpoint | Description | Response status | Request body | Response body |
| ----------- | ----------- | ----------- |--------------------------| ----------- | ----------- |
| GET | /publishers | Get all publishers | 200 | - | {"id": 1, "name": "KCD", "books": [...]} |
| GET | /publishers/{id} | Get a publisher by id | 200, 404(if not found) | - | json {"id": 1, "name": "KCD", "books": [...], "description": "..."} |
| POST | /publishers | Add a new publisher | 201, 400(if bad request) | json {"name": "KCD", "books": [...], "description": "..."} | json {"id": 1, "name": "KCD", "books": [...], "description": "..."} |
| PUT | /publishers/{id} | Update a publisher | 200, 404(if not found), 400(if bad request) | json {"description": "..."} | json {"id": 1, "name": "KCD", "books": [...], "description": "..."} |
| DELETE | /publishers/{id} | Delete a publisher | 204, 404(if not found) | - | - |

## Cart
| Method | Endpoint | Description | Response status | Request body | Response body |
| ----------- | ----------- | ----------- | ----------- | ----------- | ----------- |
| GET | /cart | Get all items in the cart | 200 | - | json [{"id": 1, "book_id": 2, "book_name": "Dune", "quantity": 2, "price": 15.00, "total": 30.00}] |
| POST | /cart | Add a new item to the cart | 201, 400(if invalid) | json {"book_id": 2, "quantity": 1} | json {"id": 1, "book_id": 2, "book_name": "Dune", "quantity": 1, "price": 15.00, "total": 15.00} |
| PUT | /cart/{item_id} | Update quantity of an item in the cart | 200, 404(if not found) | json {"quantity": 3} | json {"id": 1, "book_id": 2, "book_name": "Dune", "quantity": 3, "price": 15.00, "total": 45.00} |
| DELETE | /cart/{item_id} | Remove an item from the cart | 204, 404(if not found) | - | - |

## Authorization
| Method | Endpoint | Description | Response status | Request body | Response body |
| ----------- | ----------- | ----------- | ----------- | ----------- | ----------- |
| POST | /auth/login | Login a user | 200, 401(if login failed) | json {"login": "artem", "password": "@rtem123!"} | json {"token": "..."} |
| POST | /auth/register | Register a user | 200 | json {"username": "artem", "email": "artem.sh@gmail.com", "password": "@rtem123!"} | json {"token": "..."} |

## User
| Method | Endpoint | Description | Response status | Request body | Response body |
| ----------- | ----------- | ----------- | ----------- | ----------- | ----------- |
| GET | /user | Get user info | 200 | - | json {"username": "artem", "email": "artem.sh@gmail.com", "orders": [...]} |
| PUT | /user | Update user info | 200 | json {"username": "artem"} | json {"username": "artem", "email": "artem.sh@gmail.com", "orders": [...]} |

## Orders
| Method | Endpoint | Description | Response status | Request body | Response body |
| ----------- | ----------- | ----------- | ----------- | ----------- | ----------- |
| GET | /orders | Get all orders | 200 | - | json [{"id": 1, "items": [{"book_id": 2, "name": "Dune", "quantity": 1, "price": 15.00}], "total": 15.00, "created_at": "2025-09-30"}] |
| GET | /orders/{id} | Get a specific order | 200, 404(if not found) | - | json {"id": 1, "items": [{"book_id": 2, "name": "Dune", "quantity": 1, "price": 15.00}], "total": 15.00, "created_at": "2025-09-30"} |
| POST | /orders | Create an order from cart | 201 | - | json {"id": 1, "items": [{"book_id": 2, "name": "Dune", "quantity": 1, "price": 15.00}], "total": 15.00, "created_at": "2025-09-30"} |
| DELETE | /orders/{id} | Delete an order | 200, 404(if not found) | - | - |

## Database image
<img width="1225" height="857" alt="image" src="https://github.com/user-attachments/assets/4548eeee-3cfb-4c3b-85bc-991e66dabe0b" />