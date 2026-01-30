from fastapi import FastAPI
from typing import List, Dict
import uvicorn

app = FastAPI(title="Simple Python Backend", version="1.0.0")

# In-memory storage for demo purposes
items_db = [
    {"id": 1, "name": "Laptop", "description": "Gaming laptop", "price": 999.99},
    {"id": 2, "name": "Mouse", "description": "Wireless mouse", "price": 29.99},
    {"id": 3, "name": "Keyboard", "description": "Mechanical keyboard", "price": 79.99},
]

@app.get("/health")
async def health_check():
    """Health check endpoint"""
    return {"status": "healthy", "message": "Service is running"}

@app.get("/items")
async def get_items():
    """Get all items"""
    return {"items": items_db, "count": len(items_db)}

@app.get("/items/{item_id}")
async def get_item(item_id: int):
    """Get a specific item by ID"""
    item = next((item for item in items_db if item["id"] == item_id), None)
    if item:
        return {"item": item}
    return {"error": "Item not found"}, 404

@app.post("/items")
async def create_item(item: Dict):
    """Create a new item"""
    new_id = max([item["id"] for item in items_db]) + 1 if items_db else 1
    new_item = {
        "id": new_id,
        "name": item.get("name", ""),
        "description": item.get("description", ""),
        "price": item.get("price", 0.0)
    }
    items_db.append(new_item)
    return {"message": "Item created successfully", "item": new_item}

@app.get("/")
async def root():
    """Welcome message"""
    return {"message": "Welcome to Simple Python Backend API v1.1", "docs": "/docs"}

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)