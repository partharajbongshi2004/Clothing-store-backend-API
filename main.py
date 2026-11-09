from typing import List
from fastapi import FastAPI, HTTPException, status
from pydantic import BaseModel, Field

# Define the FastAPI application instance
app = FastAPI(
    title="Clothing Store Backend API",
    description="An in-memory REST API to manage a clothing store product catalog.",
    version="1.0.0"
)

# Define the Product data structure schema using Pydantic
class Product(BaseModel):
    id: int = Field(..., description="Unique identifier for the product")
    name: str = Field(..., description="Name of the clothing item")
    category: str = Field(..., description="Category of the clothing (e.g., T-Shirt, Jeans)")
    size: str = Field(..., description="Size of the clothing (e.g., S, M, L, XL)")
    color: str = Field(..., description="Color of the item")
    price: float = Field(..., gt=0, description="Price of the item (must be greater than 0)")
    stock: int = Field(..., ge=0, description="Stock available in inventory (must be 0 or more)")

# Seed data to initialize the in-memory product catalog database
products_db: List[Product] = [
    Product(id=1, name="Classic Denim", category="Jeans", size="32", color="Blue", price=59.99, stock=15),
    Product(id=2, name="Graphic Tee", category="T-Shirt", size="L", color="Black", price=24.99, stock=50),
    Product(id=3, name="Cozy Hoodie", category="Hoodie", size="M", color="Gray", price=45.00, stock=20)
]

# 1. Root GET endpoint with a welcome message
@app.get("/", status_code=status.HTTP_200_OK)
def root():
    return {
        "message": "Welcome to the Clothing Store Backend API!",
        "docs_url": "/docs",
        "status": "Running"
    }

# 2. GET endpoint to retrieve all products
@app.get("/products", response_model=List[Product], status_code=status.HTTP_200_OK)
def get_all_products():
    return products_db

# 3. POST endpoint to add a new product
@app.post("/products", response_model=Product, status_code=status.HTTP_201_CREATED)
def create_product(new_product: Product):
    # Check if a product with the given ID already exists
    for product in products_db:
        if product.id == new_product.id:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail=f"Product with ID {new_product.id} already exists."
            )
    
    # Append the verified product to our in-memory list
    products_db.append(new_product)
    return new_product
