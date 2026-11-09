import pandas as pd
import streamlit as str

# Set up page configurations
str.set_page_config(
    page_title="Clothing Store Management Dashboard",
    page_icon="👕",
    layout="wide"
)

# App Title & Description
str.title("👕 Clothing Store Management Dashboard")
str.markdown("Manage your clothing store product catalog and track inventory in real-time.")
str.divider()

# Initialize Streamlit session state for product storage if it doesn't exist
if "products_db" not in str.session_state:
    str.session_state.products_db = [
        {"id": 1, "name": "Classic Denim", "category": "Jeans", "size": "32", "color": "Blue", "price": 59.99, "stock": 15},
        {"id": 2, "name": "Graphic Tee", "category": "T-Shirt", "size": "L", "color": "Black", "price": 24.99, "stock": 50},
        {"id": 3, "name": "Cozy Hoodie", "category": "Hoodie", "size": "M", "color": "Gray", "price": 45.00, "stock": 20},
        {"id": 4, "name": "Premium Cotton Panjabi", "category": "Panjabi", "size": "XL", "color": "White", "price": 35.50, "stock": 10}
    ]

# --- SIDEBAR: Input Form ---
str.sidebar.header("➕ Add New Clothing Item")

with str.sidebar.form(key="add_product_form", clear_on_submit=True):
    # Form input fields
    p_id = str.number_input("Product ID", min_value=1, step=1, value=5)
    p_name = str.text_input("Product Name", placeholder="e.g., Slim Fit Polo")
    p_category = str.selectbox("Category", ["T-Shirt", "Jeans", "Hoodie", "Panjabi"])
    p_size = str.text_input("Size", placeholder="e.g., S, M, L, XL, 32")
    p_color = str.text_input("Color", placeholder="e.g., Red, Black, Olive")
    p_price = str.number_input("Price ($)", min_value=0.01, step=0.01, format="%.2f")
    p_stock = str.number_input("Stock Quantity", min_value=0, step=1)
    
    # Form submission button
    submit_button = str.form_submit_button(label="Add Item")

# Handle form submission and validation
if submit_button:
    if not p_name.strip() or not p_size.strip() or not p_color.strip():
        str.sidebar.error("❌ Please fill out all text fields.")
    else:
        # Check if Product ID already exists
        id_exists = any(item["id"] == p_id for item in str.session_state.products_db)
        
        if id_exists:
            str.sidebar.error(f"❌ Product ID {p_id} already exists. Please use a unique ID.")
        else:
            # Build the new product dictionary
            new_item = {
                "id": p_id,
                "name": p_name.strip(),
                "category": p_category,
                "size": p_size.strip().upper(),
                "color": p_color.strip().title(),
                "price": p_price,
                "stock": p_stock
            }
            # Append to session state list
            str.session_state.products_db.append(new_item)
            str.sidebar.success(f"✅ '{p_name}' successfully added to inventory!")

# --- MAIN DASHBOARD AREA: Inventory Display ---

# Convert the session state list of dicts into a Pandas DataFrame
df = pd.DataFrame(str.session_state.products_db)

# Rename columns for cleaner display presentation
df_display = df.rename(columns={
    "id": "Product ID",
    "name": "Product Name",
    "category": "Category",
    "size": "Size",
    "color": "Color",
    "price": "Price ($)",
    "stock": "Stock Quantity"
})

# Display quick metrics
col1, col2, col3 = str.columns(3)
with col1:
    str.metric(label="Total Unique Items", value=len(df))
with col2:
    str.metric(label="Total Stock Pieces", value=int(df["stock"].sum()))
with col3:
    str.metric(label="Average Item Price", value=f"${df['price'].mean():.2f}")

str.subheader("📦 Current Stock Inventory")

# Render interactive data table
str.dataframe(df_display, use_container_width=True, hide_index=True)

