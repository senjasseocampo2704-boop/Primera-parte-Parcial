from fastapi import FastAPI
from .controller.abb_controller import router as children_router

app = FastAPI(
    title="Children Management API - BST",
    description="API REST para gestionar registros de niños almacenados en un Árbol Binario de Búsqueda (ABB/BST) en memoria",
    version="1.0.0",
    docs_url="/docs",
    redoc_url="/redoc"
)

# Incluir el router de children
app.include_router(children_router)

@app.get("/", tags=["Root"])
def read_root():
    return {
        "message": "Children Management API - Binary Search Tree",
        "version": "1.0.0",
        "docs": "/docs",
        "endpoints": {
            "POST /children": "Insertar un nuevo niño",
            "GET /children/{documento}": "Obtener un niño por documento",
            "GET /children?order=in|pre|post": "Listar todos los niños",
            "PUT /children/{documento}": "Actualizar un niño",
            "DELETE /children/{documento}": "Eliminar un niño"
        }
    }
