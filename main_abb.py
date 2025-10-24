"""
Servidor FastAPI para Árbol Binario de Búsqueda (ABB)
Puerto: 8000
Swagger: http://127.0.0.1:8000/docs
"""
from umanizales_edu.main_abb import app

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="127.0.0.1", port=8000, reload=True)
