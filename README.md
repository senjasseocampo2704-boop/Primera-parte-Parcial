# Children Management API - Binary Search Tree

API REST para gestionar registros de niños almacenados en un Árbol Binario de Búsqueda (ABB/BST) en memoria usando FastAPI.

## 🚀 Características

- ✅ Almacenamiento en memoria usando Árbol Binario de Búsqueda (ABB)
- ✅ Ordenación automática por número de documento
- ✅ Operaciones CRUD completas
- ✅ Tres tipos de recorrido: Inorden, Preorden, Postorden
- ✅ Documentación automática con Swagger UI
- ✅ Validación de datos con Pydantic
- ✅ Códigos de estado HTTP apropiados

## 📋 Requisitos

- Python 3.10+
- FastAPI
- Uvicorn
- Pydantic

## 🔧 Instalación

1. **Clonar o descargar el proyecto**

2. **Crear un entorno virtual**
```bash
python -m venv venv
```

3. **Activar el entorno virtual**
- Windows:
```bash
venv\Scripts\activate
```
- Linux/Mac:
```bash
source venv/bin/activate
```

4. **Instalar dependencias**
```bash
pip install -r requirements.txt
```

## ▶️ Ejecución

Ejecutar el servidor de desarrollo:

```bash
uvicorn umanizales_edu.main:app --reload
```

El servidor estará disponible en: `http://127.0.0.1:8000`

## 📚 Documentación

Una vez el servidor esté corriendo, accede a:

- **Swagger UI**: http://127.0.0.1:8000/docs
- **ReDoc**: http://127.0.0.1:8000/redoc

## 🔌 Endpoints

### 1. **POST /children** - Insertar un nuevo niño
Crea un nuevo registro de niño en el árbol.

**Request Body:**
```json
{
  "documento": 1234567890,
  "nombre": "Juan Pérez",
  "edad": 10,


}
```

**Response:** `201 Created`
```json
{
  "documento": 1234567890,
  "nombre": "Juan Pérez",
  "edad": 10,
}
```

---

### 2. **GET /children/{documento}** - Obtener un niño por documento
Busca y retorna un niño específico.

**Response:** `200 OK`
```json
{
  "documento": 1234567890,
  "nombre": "Juan Pérez",
  "edad": 10,
}
```

**Error:** `404 Not Found`
```json
{
  "detail": "Niño con documento 1234567890 no encontrado"
}
```

---

### 3. **GET /children?order=in|pre|post** - Listar todos los niños
Lista todos los niños usando el tipo de recorrido especificado.

**Query Parameters:**
- `order` (opcional): Tipo de recorrido
  - `in` (default): Inorden - Ordenado por documento ascendente
  - `pre`: Preorden
  - `post`: Postorden

**Ejemplos:**
```bash
GET /children
GET /children?order=in
GET /children?order=pre
GET /children?order=post
```

**Response:** `200 OK`
```json
[
  {
    "documento": 1234567890,
    "nombre": "Juan Pérez",
    "edad": 10,
  },
  {
    "documento": 9876543210,
    "nombre": "Ana Gómez",
    "edad": 12,
  }
]
```

---

### 4. **PUT /children/{documento}** - Actualizar un niño
Actualiza los datos de un niño existente. El campo `documento` no puede ser modificado.

**Request Body:**
```json
{
  "nombre": "Juan Pérez Actualizado",
  "edad": 11,
}
```

**Response:** `200 OK`
```json
{
  "documento": 1234567890,
  "nombre": "Juan Pérez Actualizado",
  "edad": 11,
}
```

---

### 5. **DELETE /children/{documento}** - Eliminar un niño
Elimina un niño del sistema.

**Response:** `200 OK`
```json
{
  "message": "Niño con documento 1234567890 eliminado correctamente"
}
```

**Error:** `404 Not Found`
```json
{
  "detail": "Niño con documento 1234567890 no encontrado"
}
```

---

## 🌳 Estructura del Árbol Binario de Búsqueda

El ABB mantiene la siguiente propiedad de orden basada en el campo `documento`:

```
                 5000
               /      \
           3000        8000
          /    \      /    \
       2000   4000  6000   9000
```

- **Subárbol izquierdo**: Documentos menores
- **Subárbol derecho**: Documentos mayores

### Recorridos:

1. **Inorden (Izquierda → Raíz → Derecha)**
   - Resultado: `[2000, 3000, 4000, 5000, 6000, 8000, 9000]`
   - Útil para obtener datos ordenados

2. **Preorden (Raíz → Izquierda → Derecha)**
   - Resultado: `[5000, 3000, 2000, 4000, 8000, 6000, 9000]`
   - Útil para copiar el árbol

3. **Postorden (Izquierda → Derecha → Raíz)**
   - Resultado: `[2000, 4000, 3000, 6000, 9000, 8000, 5000]`
   - Útil para eliminar el árbol

---

## 📁 Estructura del Proyecto

```
fastapi_scaffold/
├── umanizales_edu/
│   ├── __init__.py
│   ├── main.py                    # Aplicación principal FastAPI
│   ├── controller/
│   │   ├── __init__.py
│   │   └── item_controller.py     # Endpoints de la API
│   ├── service/
│   │   ├── __init__.py
│   │   └── item_service.py        # Lógica del ABB
│   └── model/
│       ├── __init__.py
│       └── schemas.py             # Modelos Pydantic
├── Docs/
│   ├── ABB.md                     # Especificación del ABB
│   └── AVL.md                     # Especificación del AVL
├── requirements.txt
└── README.md
```

---

## 🧪 Ejemplos de Uso con cURL

### Insertar un niño
```bash
curl -X POST "http://127.0.0.1:8000/children" \
  -H "Content-Type: application/json" \
  -d '{
    "documento": 1234567890,
    "nombre": "Juan Pérez",
    "edad": 10,
  }'
```

### Obtener un niño
```bash
curl -X GET "http://127.0.0.1:8000/children/1234567890"
```

### Listar todos los niños (inorden)
```bash
curl -X GET "http://127.0.0.1:8000/children?order=in"
```

### Actualizar un niño
```bash
curl -X PUT "http://127.0.0.1:8000/children/1234567890" \
  -H "Content-Type: application/json" \
  -d '{
    "nombre": "Juan Pérez Actualizado",
    "edad": 11
  }'
```

### Eliminar un niño
```bash
curl -X DELETE "http://127.0.0.1:8000/children/1234567890"
```

---

## 📊 Códigos de Estado HTTP

| Código | Descripción |
|--------|-------------|
| `200` | Operación exitosa |
| `201` | Recurso creado correctamente |
| `400` | Error de validación o documento duplicado |
| `404` | Niño no encontrado |
| `500` | Error interno del servidor |

---

## 🔍 Validaciones

- **documento**: Debe ser un entero positivo y único
- **nombre**: Cadena de 1-100 caracteres (requerido)
- **edad**: Entero entre 0 y 18 (requerido)

---

## 🛠️ Tecnologías Utilizadas

- **FastAPI**: Framework web moderno y rápido
- **Pydantic**: Validación de datos
- **Uvicorn**: Servidor ASGI
- **Python 3.10+**: Lenguaje de programación

---

## 📝 Notas

- Los datos se almacenan **en memoria**, por lo que se perderán al reiniciar el servidor
- El árbol se ordena automáticamente por el campo `documento`
- No se permite duplicar documentos
- El campo `documento` no puede ser modificado después de la creación

---

## 👨‍💻 Autor

Universidad de Manizales - Programación 3
