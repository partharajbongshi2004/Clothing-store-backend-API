# 👕 Clothing Store Backend API

A lightweight, robust backend API built with **FastAPI** to manage a clothing store's product catalog. This project uses an in-memory list as a temporary data store, making it perfect for rapid prototyping, testing, and understanding FastAPI basics.

## 🚀 Features

- **Root Endpoint**: Welcome message with quick links to documentation.
- **Product Catalog Management**: Retrieve all products seamlessly.
- **Data Validation**: Built-in validation for product entries using Pydantic (ensuring valid prices, stock numbers, and data types).
- **Duplicate Prevention**: Verification check to ensure duplicate product IDs cannot be added.
- **Interactive API Docs**: Auto-generated Swagger UI and Redoc.

---

## 🛠️ Tech Stack

- **Framework**: FastAPI
- **Data Validation**: Pydantic v2
- **ASGI Server**: Uvicorn

---

## 📋 Product Data Structure

Each product in the inventory contains the following fields:

| Field | Type | Description |
| :--- | :--- | :--- |
| `id` | Integer | Unique identifier for the product |
| `name` | String | Name of the clothing item |
| `category`| String | Category (e.g., T-Shirt, Jeans, Hoodie) |
| `size` | String | Size of the clothing (e.g., S, M, L, XL, 32) |
| `color` | String | Color of the item |
| `price` | Float | Price of the item (Must be greater than 0) |
| `stock` | Integer | Inventory count (Must be 0 or greater) |

---

## ⚙️ Getting Started

### 1. Prerequisites
Ensure you have Python 3.8+ installed on your machine.

### 2. Installation
Clone this repository or navigate to your project directory, then install the required dependencies:

```bash
pip install fastapi uvicorn
```

### 3. Running the Application
Start the Uvicorn local development server by running:

```bash
uvicorn main:app --reload
```

The server will start running at **`http://127.0.0.1:8000`**.

---

## 🛣️ API Endpoints

### 1. Root Welcome
- **Endpoint**: `GET /`
- **Description**: Returns a friendly welcome message and basic API info.

### 2. Get All Products
- **Endpoint**: `GET /products`
- **Description**: Fetches the complete list of clothing items in the catalog.

### 3. Add a New Product
- **Endpoint**: `POST /products`
- **Description**: Adds a new product to the in-memory database. 
- **Validation**: Throws a `400 Bad Request` error if the `id` already exists.
- **Example Request Body**:
  ```json
  {
    "id": 4,
    "name": "Summer Shorts",
    "category": "Shorts",
    "size": "M",
    "color": "Khaki",
    "price": 29.99,
    "stock": 35
  }
  ```

---

## 📖 Interactive Documentation

FastAPI automatically generates interactive documentation for this API. Once the server is running, you can access them via:

- **Swagger UI**: [http://127.0.0](http://127.0.0) (Allows you to test endpoints directly from the browser)
- **ReDoc**: [http://127.0.0](http://127.0.0) (Clean, structured technical documentation)
