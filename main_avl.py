"""
Servidor FastAPI para Árbol AVL (Auto-balanceado)
Puerto: 8001
Swagger: http://127.0.0.1:8001/docs
"""
from umanizales_edu.main_avl import app

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="127.0.0.1", port=8001, reload=True)
