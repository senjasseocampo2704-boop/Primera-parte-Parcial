# 🎓 Proyecto Completo: API de Gestión de Niños

## Universidad de Manizales - Programación 3

---

## 📋 Descripción del Proyecto

Sistema completo de gestión de registros de niños implementado con **dos estructuras de datos diferentes**:

1. **ABB (Árbol Binario de Búsqueda)** - Implementación básica
2. **AVL (Árbol Auto-balanceado)** - Implementación optimizada

Ambas implementaciones utilizan **FastAPI** y almacenan datos **en memoria**.

---

## 🗂️ Estructura del Proyecto

```
fastapi_scaffold/
├── umanizales_edu/
│   ├── __init__.py
│   ├── main.py                      # API con ABB
│   ├── main_avl.py                  # API con AVL
│   ├── controller/
│   │   ├── __init__.py
│   │   ├── item_controller.py       # Controlador ABB
│   │   └── avl_controller.py        # Controlador AVL
│   ├── service/
│   │   ├── __init__.py
│   │   ├── item_service.py          # Lógica ABB
│   │   └── avl_service.py           # Lógica AVL
│   └── model/
│       ├── __init__.py
│       └── schemas.py               # Modelos Pydantic
├── Docs/
│   ├── ABB.md                       # Especificación ABB
│   └── AVL.md                       # Especificación AVL
├── test_api.py                      # Pruebas ABB
├── test_avl.py                      # Pruebas AVL
├── requirements.txt                 # Dependencias
├── README.md                        # Documentación ABB
├── README_AVL.md                    # Documentación AVL
├── API_EXAMPLES.md                  # Ejemplos ABB
├── AVL_EXAMPLES.md                  # Ejemplos AVL
├── ABB_VS_AVL.md                    # Comparación
└── .gitignore
```

---

## 🚀 Instalación y Ejecución

### 1. Instalar Dependencias

```bash
pip install -r requirements.txt
```

### 2. Ejecutar API con ABB

```bash
python -m uvicorn umanizales_edu.main:app --reload
```

Acceder a: http://127.0.0.1:8000/docs

### 3. Ejecutar API con AVL

```bash
python -m uvicorn umanizales_edu.main_avl:app --reload
```

Acceder a: http://127.0.0.1:8000/docs

### 4. Ejecutar Pruebas

```bash
# Pruebas ABB
python test_api.py

# Pruebas AVL
python test_avl.py
```

---

## 📚 Documentación Disponible

| Archivo | Descripción |
|---------|-------------|
| `README.md` | Documentación completa de la API con ABB |
| `README_AVL.md` | Documentación completa de la API con AVL |
| `API_EXAMPLES.md` | Ejemplos de uso con ABB (curl, PowerShell) |
| `AVL_EXAMPLES.md` | Ejemplos de uso con AVL (curl, PowerShell) |
| `ABB_VS_AVL.md` | Comparación detallada entre ABB y AVL |
| `Docs/ABB.md` | Especificación técnica del ABB |
| `Docs/AVL.md` | Especificación técnica del AVL |

---

## 🔌 Endpoints Implementados

Ambas APIs (ABB y AVL) implementan los mismos endpoints:

### 1. POST /children
**Descripción**: Insertar un nuevo niño  
**Código**: 201 Created  
**Auto-balanceo**: Solo en AVL

### 2. GET /children/{documento}
**Descripción**: Obtener un niño por documento  
**Código**: 200 OK / 404 Not Found  
**Rendimiento**: Variable en ABB, Rápido en AVL

### 3. GET /children?order=in|pre|post
**Descripción**: Listar todos los niños  
**Parámetros**:
- `order=in`: Inorden (ordenado)
- `order=pre`: Preorden
- `order=post`: Postorden

### 4. PUT /children/{documento}
**Descripción**: Actualizar un niño  
**Código**: 200 OK / 404 Not Found

### 5. DELETE /children/{documento}
**Descripción**: Eliminar un niño  
**Código**: 200 OK / 404 Not Found  
**Auto-balanceo**: Solo en AVL

### 6. GET /children/stats/tree (Solo AVL)
**Descripción**: Estadísticas del árbol  
**Retorna**: Altura, si está balanceado, tipo de árbol

---

## 📊 Modelo de Datos

```python
class Child(BaseModel):
    documento: int        # Número de documento (único, positivo)
    nombre: str          # Nombre completo (1-100 caracteres)
    edad: int            # Edad (0-18 años)
    acudiente: str       # Acudiente (opcional, max 100 caracteres)
    notas: str           # Notas (opcional, max 500 caracteres)
```

---

## 🌳 Implementaciones

### 1. ABB (Árbol Binario de Búsqueda)

**Archivo**: `umanizales_edu/service/item_service.py`

**Características**:
- ✅ Inserción, búsqueda, actualización, eliminación
- ✅ Tres tipos de recorrido (inorden, preorden, postorden)
- ✅ Ordenación por documento
- ❌ No garantiza balanceo
- ❌ Peor caso lento con datos ordenados

**Clases**:
- `BSTNode`: Nodo del árbol
- `ChildrenBST`: Árbol binario de búsqueda

**Rendimiento**:
- Mejor caso: Rápido
- Caso promedio: Rápido
- Peor caso: Lento

---

### 2. AVL (Árbol Auto-balanceado)

**Archivo**: `umanizales_edu/service/avl_service.py`

**Características**:
- ✅ Inserción, búsqueda, actualización, eliminación
- ✅ Tres tipos de recorrido (inorden, preorden, postorden)
- ✅ Ordenación por documento
- ✅ **Auto-balanceo garantizado**
- ✅ **Rendimiento rápido en todos los casos**
- ✅ **4 tipos de rotaciones** (LL, RR, LR, RL)

**Clases**:
- `AVLNode`: Nodo del árbol con altura
- `ChildrenAVL`: Árbol AVL auto-balanceado

**Rendimiento**:
- Mejor caso: Rápido
- Caso promedio: Rápido
- Peor caso: **Rápido** ✅

**Rotaciones Implementadas**:
1. Rotación Simple Derecha (LL)
2. Rotación Simple Izquierda (RR)
3. Rotación Doble Izquierda-Derecha (LR)
4. Rotación Doble Derecha-Izquierda (RL)

---

## 🧪 Pruebas Implementadas

### Pruebas ABB (`test_api.py`)

✅ Inserción de múltiples niños  
✅ Rechazo de documentos duplicados  
✅ Búsqueda por documento  
✅ Recorridos (inorden, preorden, postorden)  
✅ Actualización de registros  
✅ Eliminación de nodos (3 casos)  

### Pruebas AVL (`test_avl.py`)

✅ Inserción con auto-balanceo  
✅ Verificación de balanceo después de cada operación  
✅ Prueba de rotaciones LL, RR, LR, RL  
✅ Inserción en orden ascendente (peor caso para ABB)  
✅ Eliminación con rebalanceo  
✅ Visualización de estructura del árbol  
✅ Cálculo de factores de balance  

---

## 📈 Comparación de Rendimiento

### Caso: Insertar 7 niños en orden ascendente (1000-7000)

| Métrica | ABB | AVL |
|---------|-----|-----|
| **Altura del árbol** | 7 | 3 |
| **Está balanceado** | ❌ No | ✅ Sí |
| **Búsqueda del último** | 7 comparaciones | 3 comparaciones |
| **Rendimiento** | Lento | Rápido |
| **Rotaciones** | 0 | 3-4 |

**Conclusión**: AVL es **2.3x más eficiente** en este caso.

---

## 🎯 Casos de Uso Recomendados

### Usar ABB cuando:
- ✅ Datos aleatorios
- ✅ Pocas operaciones (< 100 nodos)
- ✅ Simplicidad prioritaria
- ✅ Memoria muy limitada

### Usar AVL cuando:
- ✅ Datos ordenados o semi-ordenados
- ✅ Búsquedas muy frecuentes
- ✅ Rendimiento crítico
- ✅ Escalabilidad requerida (> 1000 nodos)
- ✅ **Documentos de identidad secuenciales** ← Nuestro caso

---

## 💡 Características Técnicas

### FastAPI
- ✅ Documentación automática con Swagger UI
- ✅ Validación automática con Pydantic
- ✅ Respuestas tipadas
- ✅ Códigos HTTP apropiados
- ✅ Ejemplos en la documentación

### Pydantic
- ✅ Validación de tipos
- ✅ Validación de rangos (edad 0-18)
- ✅ Validación de longitud (nombre 1-100)
- ✅ Campos opcionales
- ✅ Ejemplos en esquemas

### Estructura de Código
- ✅ Separación de responsabilidades (MVC)
- ✅ Modelos en `model/schemas.py`
- ✅ Lógica de negocio en `service/`
- ✅ Controladores en `controller/`
- ✅ Código documentado
- ✅ Type hints completos

---

## 📊 Estadísticas del Proyecto

### Líneas de Código

| Componente | Líneas |
|------------|--------|
| ABB Service | ~220 |
| AVL Service | ~380 |
| ABB Controller | ~300 |
| AVL Controller | ~320 |
| Schemas | ~60 |
| Tests ABB | ~90 |
| Tests AVL | ~180 |
| **Total** | **~1550** |

### Archivos Creados

- **Código Python**: 8 archivos
- **Documentación**: 7 archivos
- **Pruebas**: 2 archivos
- **Configuración**: 2 archivos
- **Total**: 19 archivos

---

## 🔐 Validaciones Implementadas

### Documento
- ✅ Debe ser entero positivo
- ✅ Debe ser único
- ✅ No puede ser modificado después de creación

### Nombre
- ✅ Requerido
- ✅ Longitud: 1-100 caracteres
- ✅ Tipo: string

### Edad
- ✅ Requerida
- ✅ Rango: 0-18 años
- ✅ Tipo: entero

### Acudiente
- ✅ Opcional
- ✅ Longitud máxima: 100 caracteres
- ✅ Tipo: string

### Notas
- ✅ Opcional
- ✅ Longitud máxima: 500 caracteres
- ✅ Tipo: string

---

## 🚦 Códigos HTTP Implementados

| Código | Descripción | Cuándo se usa |
|--------|-------------|---------------|
| **200** | OK | Operación exitosa (GET, PUT, DELETE) |
| **201** | Created | Niño creado correctamente (POST) |
| **400** | Bad Request | Documento duplicado, validación fallida |
| **404** | Not Found | Niño no encontrado |
| **422** | Unprocessable Entity | Error de validación Pydantic |
| **500** | Internal Server Error | Error interno del servidor |

---

## 📖 Ejemplos de Uso Rápido

### Insertar un niño:
```bash
curl -X POST "http://127.0.0.1:8000/children" \
  -H "Content-Type: application/json" \
  -d '{"documento": 5000, "nombre": "Carlos Ruiz", "edad": 10, "acudiente": "Ana Ruiz", "notas": "Buen estudiante"}'
```

### Listar todos (ordenado):
```bash
curl -X GET "http://127.0.0.1:8000/children?order=in"
```

### Buscar por documento:
```bash
curl -X GET "http://127.0.0.1:8000/children/5000"
```

### Actualizar:
```bash
curl -X PUT "http://127.0.0.1:8000/children/5000" \
  -H "Content-Type: application/json" \
  -d '{"edad": 11}'
```

### Eliminar:
```bash
curl -X DELETE "http://127.0.0.1:8000/children/5000"
```

---

## 🎓 Conceptos Aprendidos

### Estructuras de Datos
- ✅ Árbol Binario de Búsqueda (ABB/BST)
- ✅ Árbol AVL (Auto-balanceado)
- ✅ Rotaciones de árboles
- ✅ Factor de balance
- ✅ Recorridos de árboles (inorden, preorden, postorden)

### Desarrollo de APIs
- ✅ FastAPI framework
- ✅ REST API design
- ✅ Documentación con OpenAPI/Swagger
- ✅ Validación con Pydantic
- ✅ Códigos de estado HTTP
- ✅ Manejo de errores

### Buenas Prácticas
- ✅ Separación de responsabilidades (MVC)
- ✅ Type hints en Python
- ✅ Documentación de código
- ✅ Testing
- ✅ Git ignore
- ✅ README completo

---

## 🏆 Logros del Proyecto

✅ **Dos implementaciones completas** (ABB y AVL)  
✅ **APIs REST funcionales** con FastAPI  
✅ **Documentación Swagger** automática  
✅ **Validación de datos** con Pydantic  
✅ **Pruebas exhaustivas** de ambas estructuras  
✅ **Documentación completa** (7 archivos MD)  
✅ **Ejemplos de uso** con curl y PowerShell  
✅ **Comparación detallada** ABB vs AVL  
✅ **Auto-balanceo** implementado correctamente  
✅ **4 tipos de rotaciones** AVL funcionando  

---

## 📚 Referencias y Recursos

### Documentación del Proyecto
- `README.md` - Guía completa ABB
- `README_AVL.md` - Guía completa AVL
- `ABB_VS_AVL.md` - Comparación detallada
- `API_EXAMPLES.md` - Ejemplos ABB
- `AVL_EXAMPLES.md` - Ejemplos AVL

### Especificaciones Técnicas
- `Docs/ABB.md` - Especificación ABB
- `Docs/AVL.md` - Especificación AVL

### Código Fuente
- `umanizales_edu/service/item_service.py` - ABB
- `umanizales_edu/service/avl_service.py` - AVL
- `umanizales_edu/controller/item_controller.py` - Controlador ABB
- `umanizales_edu/controller/avl_controller.py` - Controlador AVL

### Pruebas
- `test_api.py` - Pruebas ABB
- `test_avl.py` - Pruebas AVL

---

## 👨‍💻 Autor

**Universidad de Manizales**  
Programación 3 - IV Semestre  
2025

---

## 📝 Notas Finales

Este proyecto demuestra:
1. Implementación correcta de estructuras de datos avanzadas
2. Desarrollo de APIs REST con FastAPI
3. Comparación práctica entre ABB y AVL
4. Documentación profesional y completa
5. Testing y validación exhaustiva

**Recomendación**: Usar la implementación **AVL** para producción debido a su rendimiento rápido garantizado en todos los casos.
