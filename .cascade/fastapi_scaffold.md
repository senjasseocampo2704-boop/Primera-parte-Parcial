---
name: fastapi_scaffold
description: Initial structure setup for a FastAPI project with best practices
version: 1.0.0
---

# FastAPI Project Scaffold Workflow

This workflow creates the initial structure for a FastAPI project following best practices.

## Instructions

Please provide the name for your API following these naming conventions:

### Naming Best Practices:
- Use **lowercase letters only**
- Use **underscores** to separate words (snake_case)
- **No spaces** or special characters
- Should be descriptive and concise
- Examples of valid names:
  - `product_api`
  - `user_service`
  - `inventory_management`
  - `order_system`
  
### Invalid examples:
- `Product-API` (contains uppercase and hyphens)
- `authService` (camelCase)
- `Order Management!` (contains spaces and special characters)

---

## What will be created:

Once you provide a valid API name, the workflow will create:

### 1. Project Structure:
```
{api_name}/
├── controller/
│   └── __init__.py
├── service/
│   └── __init__.py
├── model/
│   └── __init__.py
├── main.py
└── requirements.txt
```

### 2. Directory Descriptions:
- **`controller/`** - API endpoints and request handling layer
- **`service/`** - Business logic and service layer
- **`model/`** - Pydantic models and data schemas

### 3. Requirements File:
The `requirements.txt` will include:
```
fastapi>=0.115.0
uvicorn[standard]>=0.30.0
pydantic>=2.9.0
pydantic-settings>=2.5.0
```

### 4. Empty Structure Files:
- Each directory will have an `__init__.py` file
- A basic `main.py` file will be created
- No code implementation, just the structure

---

## Workflow Steps:

1. **Prompt**: Enter the API name
2. **Validation**: Check if the name follows best practices
3. **Create directories**: `controller/`, `service/`, `model/`
4. **Create files**: `__init__.py` in each directory
5. **Generate**: `requirements.txt` with dependencies
6. **Create**: Empty `main.py` file
7. **Confirm**: Structure created successfully

---

## Next Steps After Running:

1. Navigate to your project directory
2. Create a virtual environment: `python -m venv venv`
3. Activate it: `venv\Scripts\activate` (Windows) or `source venv/bin/activate` (Linux/Mac)
4. Install dependencies: `pip install -r requirements.txt`
5. Start implementing your models, services, and controllers

---

**Ready to start? Please provide your API name.**
