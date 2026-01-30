# Python Backend DevOps Practice

A simple FastAPI backend service for DevOps containerization practice.

## Features

- **Health Check**: `/health` - Service health status
- **Items API**: `/items` - CRUD operations for items
- **Auto Documentation**: `/docs` - Interactive API documentation

## API Endpoints

| Method | Endpoint | Description |
|--------|----------|-------------|
| GET | `/` | Welcome message |
| GET | `/health` | Health check |
| GET | `/items` | Get all items |
| GET | `/items/{id}` | Get specific item |
| POST | `/items` | Create new item |

## Local Development

### Run with Python
```bash
pip install -r requirements.txt
python main.py
```

### Run with Docker
```bash
# Build the image
docker build -t python-backend .

# Run the container
docker run -p 8000:8000 python-backend
```

## Testing the API

Once running, visit:
- **API**: http://localhost:8000
- **Health Check**: http://localhost:8000/health
- **Items**: http://localhost:8000/items
- **Interactive Docs**: http://localhost:8000/docs

## Sample API Calls

```bash
# Health check
curl http://localhost:8000/health

# Get all items
curl http://localhost:8000/items

# Get specific item
curl http://localhost:8000/items/1

# Create new item
curl -X POST "http://localhost:8000/items" \
     -H "Content-Type: application/json" \
     -d '{"name": "Headphones", "description": "Wireless headphones", "price": 99.99}'
```
