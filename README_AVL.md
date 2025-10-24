# Children Management API - AVL Tree (Auto-balanceado)

API REST para gestionar registros de niños almacenados en un **Árbol AVL (Auto-balanceado)** en memoria usando FastAPI.

## 🌳 ¿Qué es un Árbol AVL?

Un **Árbol AVL** es un árbol binario de búsqueda **auto-balanceado** que garantiza operaciones eficientes mediante rotaciones automáticas.

### Características Principales:

- ✅ **Auto-balanceo**: Se reajusta automáticamente después de cada inserción/eliminación
- ✅ **Factor de Balance**: Mantiene `-1 ≤ BF ≤ 1` en cada nodo
- ✅ **Rotaciones**: Implementa 4 tipos (LL, RR, LR, RL)
- ✅ **Eficiencia Garantizada**: Alto rendimiento en todas las operaciones
- ✅ **Rendimiento Predecible**: No se degenera en lista enlazada

### Ventajas sobre ABB Simple:

| Característica | ABB Simple | AVL |
|----------------|------------|-----|
| **Inserción** | Bueno en promedio, lento en peor caso | **Siempre rápido** |
| **Búsqueda** | Bueno en promedio, lento en peor caso | **Siempre rápido** |
| **Eliminación** | Bueno en promedio, lento en peor caso | **Siempre rápido** |
| **Balanceo** | No garantizado | **Auto-balanceado** |
| **Caso peor** | Lista enlazada (datos ordenados) | **Árbol balanceado** |

---

## 🚀 Características de la API

- ✅ Almacenamiento en memoria usando Árbol AVL
- ✅ Ordenación automática por número de documento
- ✅ Auto-balanceo con rotaciones (LL, RR, LR, RL)
- ✅ Operaciones CRUD completas
- ✅ Tres tipos de recorrido: Inorden, Preorden, Postorden
- ✅ Documentación automática con Swagger UI
- ✅ Validación de datos con Pydantic
- ✅ Códigos de estado HTTP apropiados
- ✅ Endpoint de estadísticas del árbol

---

## 📋 Requisitos

- Python 3.10+
- FastAPI
- Uvicorn
- Pydantic

---

## 🔧 Instalación

1. **Instalar dependencias**
```bash
pip install -r requirements.txt
```

---

## ▶️ Ejecución

Ejecutar el servidor AVL:

```bash
python -m uvicorn umanizales_edu.main_avl:app --reload
```

El servidor estará disponible en: `http://127.0.0.1:8000`

---

## 📚 Documentación

Una vez el servidor esté corriendo, accede a:

- **Swagger UI**: http://127.0.0.1:8000/docs
- **ReDoc**: http://127.0.0.1:8000/redoc

---

## 🔌 Endpoints

### 1. **POST /children** - Insertar un nuevo niño
Crea un nuevo registro con auto-balanceo del árbol.

**Request Body:**
```json
{
  "documento": 1234567890,
  "nombre": "Juan Pérez",
  "edad": 10,
  "acudiente": "María Pérez",
  "notas": "Alumno destacado"
}
```

**Response:** `201 Created`

---

### 2. **GET /children/{documento}** - Obtener un niño
Búsqueda rápida garantizada.

**Response:** `200 OK`

---

### 3. **GET /children?order=in|pre|post** - Listar todos
Lista con el recorrido especificado.

**Query Parameters:**
- `order=in` (default): Inorden - Ordenado ascendente
- `order=pre`: Preorden
- `order=post`: Postorden

---

### 4. **PUT /children/{documento}** - Actualizar un niño
Actualiza datos manteniendo el balanceo.

---

### 5. **DELETE /children/{documento}** - Eliminar un niño
Elimina con auto-balanceo del árbol.

---

### 6. **GET /children/stats/tree** - Estadísticas del árbol
Obtiene información del estado del árbol AVL.

**Response:**
```json
{
  "tree_height": 4,
  "is_balanced": true,
  "tree_type": "AVL (Auto-balanceado)"
}
```

---

## 🔄 Rotaciones AVL

El árbol implementa 4 tipos de rotaciones para mantener el balanceo:

### 1. **Rotación Simple Derecha (LL)**
Cuando el subárbol izquierdo-izquierdo está desbalanceado.

### 2. **Rotación Simple Izquierda (RR)**
Cuando el subárbol derecho-derecho está desbalanceado.

### 3. **Rotación Doble Izquierda-Derecha (LR)**
Cuando el subárbol izquierdo-derecho está desbalanceado.

### 4. **Rotación Doble Derecha-Izquierda (RL)**
Cuando el subárbol derecho-izquierdo está desbalanceado.

---

## 📊 Ejemplo de Auto-balanceo

### Inserción en orden ascendente (1000, 2000, 3000, 4000, 5000, 6000, 7000):

**ABB Simple (sin balanceo):**
```
1000
    \
    2000
        \
        3000
            \
            4000
                \
                5000
                    \
                    6000
                        \
                        7000
```
**Altura: 7** (degenerado en lista enlazada) ❌

**AVL (con auto-balanceo):**
```
        4000
       /    \
    2000    6000
   /   \    /   \
1000 3000 5000 7000
```
**Altura: 3** (balanceado) ✅

---

## 🧪 Pruebas

Ejecutar el script de pruebas:

```bash
python test_avl.py
```

Este script prueba:
- ✅ Inserción con auto-balanceo
- ✅ Rotaciones LL, RR, LR, RL
- ✅ Búsqueda eficiente
- ✅ Actualización
- ✅ Eliminación con rebalanceo
- ✅ Recorridos del árbol
- ✅ Verificación de balanceo

---

## 📁 Estructura del Proyecto

```
fastapi_scaffold/
├── umanizales_edu/
│   ├── main_avl.py                # Aplicación AVL FastAPI
│   ├── controller/
│   │   └── avl_controller.py      # Endpoints AVL
│   ├── service/
│   │   └── avl_service.py         # Lógica del AVL
│   └── model/
│       └── schemas.py             # Modelos Pydantic
├── test_avl.py                    # Pruebas del AVL
├── README_AVL.md                  # Esta documentación
└── requirements.txt
```

---

## 🎯 Ejemplos de Uso

### Insertar varios niños:
```bash
curl -X POST "http://127.0.0.1:8000/children" \
  -H "Content-Type: application/json" \
  -d '{"documento": 5000, "nombre": "Carlos Ruiz", "edad": 10, "acudiente": "Ana Ruiz", "notas": "Buen estudiante"}'

curl -X POST "http://127.0.0.1:8000/children" \
  -H "Content-Type: application/json" \
  -d '{"documento": 3000, "nombre": "María López", "edad": 8, "acudiente": "Pedro López", "notas": "Excelente en arte"}'

curl -X POST "http://127.0.0.1:8000/children" \
  -H "Content-Type: application/json" \
  -d '{"documento": 8000, "nombre": "Juan Pérez", "edad": 12, "acudiente": "Laura Pérez", "notas": "Destacado en deportes"}'
```

### Listar todos (ordenado):
```bash
curl -X GET "http://127.0.0.1:8000/children?order=in"
```

### Obtener estadísticas del árbol:
```bash
curl -X GET "http://127.0.0.1:8000/children/stats/tree"
```

---

## 📊 Complejidad Temporal

| Operación | AVL | ABB Simple (peor caso) |
|-----------|-----|------------------------|
| Insertar | **Rápido** | Lento |
| Buscar | **Rápido** | Lento |
| Actualizar | **Rápido** | Lento |
| Eliminar | **Rápido** | Lento |
| Recorrido | Normal | Normal |

---

## 🔍 Factor de Balance

**BF = altura(subárbol derecho) - altura(subárbol izquierdo)**

- **BF = 0**: Perfectamente balanceado
- **BF = 1**: Subárbol derecho más alto
- **BF = -1**: Subárbol izquierdo más alto
- **|BF| > 1**: ⚠️ Requiere rotación (el AVL lo hace automáticamente)

---

## ✅ Validaciones

- **documento**: Debe ser un entero positivo y único
- **nombre**: Cadena de 1-100 caracteres (requerido)
- **edad**: Entero entre 0 y 18 (requerido)
- **acudiente**: Cadena de máximo 100 caracteres (opcional)
- **notas**: Cadena de máximo 500 caracteres (opcional)

---

## 🛠️ Tecnologías Utilizadas

- **FastAPI**: Framework web moderno
- **Pydantic**: Validación de datos
- **Uvicorn**: Servidor ASGI
- **Python 3.10+**: Lenguaje de programación
- **Árbol AVL**: Estructura de datos auto-balanceada

---

## 📝 Notas Importantes

- Los datos se almacenan **en memoria** y se pierden al reiniciar el servidor
- El árbol se **auto-balancea** después de cada inserción/eliminación
- El factor de balance se mantiene entre **-1 y 1** en todo momento
- Las rotaciones son **automáticas y transparentes** para el usuario
- Ideal para datos que pueden llegar **ordenados o semi-ordenados**

---

## 🆚 Cuándo Usar AVL vs ABB

### Usar AVL cuando:
- ✅ Las búsquedas son **muy frecuentes**
- ✅ Se requiere **rendimiento predecible**
- ✅ Los datos pueden llegar **ordenados**
- ✅ La aplicación es **crítica** en tiempo de respuesta

### Usar ABB simple cuando:
- ✅ Los datos son **aleatorios**
- ✅ Las operaciones son **poco frecuentes**
- ✅ Se prefiere **simplicidad** de implementación

---

## 👨‍💻 Autor

Universidad de Manizales - Programación 3

---

## 📖 Referencias

- [Árbol AVL - Wikipedia](https://es.wikipedia.org/wiki/%C3%81rbol_AVL)
- [FastAPI Documentation](https://fastapi.tiangolo.com/)
- [Pydantic Documentation](https://docs.pydantic.dev/)
