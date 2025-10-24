from fastapi import FastAPI
from .controller.avl_controller import router as children_avl_router

app = FastAPI(
    title="Children Management API - AVL Tree",
    description="""
    REST API for managing children's records stored in an **AVL Tree (Self-balancing)** in memory.
    
    ## AVL Tree Features
    
    - ✅ **Self-balancing**: The tree automatically rebalances after each insertion/deletion
    - ✅ **Rotations**: Implements LL, RR, LR, RL rotations to maintain balance
    - ✅ **Guaranteed Efficiency**: High performance for all operations (search, insert, delete)
    - ✅ **Balance Factor**: Maintains -1 ≤ BF ≤ 1 for each node
    
    ## Advantages over Simple BST
    
    - Superior performance compared to unbalanced BST
    - Predictable and consistent performance
    - Ideal for data that may arrive sorted or semi-sorted
    """,
    version="1.0.0",
    docs_url="/docs",
    redoc_url="/redoc"
)

# Incluir el router de children AVL
app.include_router(children_avl_router)

@app.get("/", tags=["Root"])
def read_root():
    return {
        "message": "Children Management API - AVL Tree (Self-balancing)",
        "version": "1.0.0",
        "tree_type": "AVL (Self-balancing Binary Search Tree)",
        "docs": "/docs",
        "features": {
            "auto_balancing": "Rotaciones automáticas (LL, RR, LR, RL)",
            "guaranteed_performance": "Alto rendimiento en todas las operaciones",
            "balance_factor": "Mantiene -1 ≤ BF ≤ 1 en cada nodo"
        },
        "endpoints": {
            "POST /children": "Insertar un nuevo niño (con auto-balanceo)",
            "GET /children/{documento}": "Obtener un niño por documento",
            "GET /children?order=in|pre|post": "Listar todos los niños",
            "PUT /children/{documento}": "Actualizar un niño",
            "DELETE /children/{documento}": "Eliminar un niño (con auto-balanceo)",
            "GET /children/stats/tree": "Obtener estadísticas del árbol AVL"
        }
    }
