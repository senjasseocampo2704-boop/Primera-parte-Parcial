# ABB (Árbol Binario de Búsqueda) - Binary Search Tree

## Propósito

Almacenar y ordenar objetos **"Kid"** para optimizar la búsqueda mediante una estructura de árbol binario de búsqueda basada en la edad (`age`).

---

## Estructura del Nodo

Cada nodo del árbol representa un **Kid** y contiene las siguientes propiedades:

### Propiedades del Nodo:

| Propiedad | Tipo | Descripción |
|-----------|------|-------------|
| `id` | `int` | Identificador único del niño |
| `age` | `int` | Edad del niño (criterio de ordenación) |
| `name` | `str` | Nombre del niño |
| `gender` | `str` | Género del niño |
| `left` | `Node` | Referencia al hijo izquierdo (age menor) |
| `right` | `Node` | Referencia al hijo derecho (age mayor) |

### Criterio de Ordenación:

El árbol se ordena basándose en el campo **`age`**:
- **Subárbol izquierdo**: Contiene nodos con `age` menor que el nodo actual
- **Subárbol derecho**: Contiene nodos con `age` mayor que el nodo actual

---

## Funcionalidades (API)

Se requiere el soporte de las siguientes operaciones para la entidad **"Kid"** integradas con **FastAPI**:

### 1. **Insertar (Create)**
- **Operación**: `POST /kids`
- **Descripción**: Agregar un nuevo nodo "Kid" al árbol
- **Entrada**: Objeto Kid con `id`, `age`, `name`, `gender`
- **Salida**: Confirmación de inserción exitosa
- **Comportamiento**: El nodo se inserta en la posición correcta según su `age`

### 2. **Buscar (Read)**
- **Operación**: `GET /kids/{id}` o `GET /kids?age={age}`
- **Descripción**: Encontrar un Kid por su `id` o `age`
- **Entrada**: 
  - `id` (int): Búsqueda por identificador único
  - `age` (int): Búsqueda por edad
- **Salida**: Objeto Kid encontrado o mensaje de error si no existe
- **Comportamiento**: Búsqueda optimizada aprovechando la estructura del ABB

### 3. **Actualizar (Update)**
- **Operación**: `PUT /kids/{id}` o `PATCH /kids/{id}`
- **Descripción**: Modificar los datos de un Kid existente
- **Entrada**: `id` del Kid y campos a actualizar (`name`, `gender`, `age`)
- **Salida**: Objeto Kid actualizado
- **Comportamiento Especial**: 
  - Si se modifica el `age`, puede requerir **re-insertar el nodo** en una nueva posición del árbol para mantener la propiedad de ordenación del ABB
  - Proceso: Eliminar nodo → Actualizar datos → Re-insertar en posición correcta

### 4. **Borrar (Delete)**
- **Operación**: `DELETE /kids/{id}`
- **Descripción**: Eliminar un nodo "Kid" del árbol
- **Entrada**: `id` del Kid a eliminar
- **Salida**: Confirmación de eliminación exitosa
- **Comportamiento**: 
  - Manejar los 3 casos de eliminación en ABB:
    1. Nodo hoja (sin hijos)
    2. Nodo con un hijo
    3. Nodo con dos hijos (reemplazar con sucesor inorden)

### 5. **Recorrido (Read All)**
- **Operación**: `GET /kids` o `GET /kids/inorder`
- **Descripción**: Obtener todos los niños ordenados por edad
- **Entrada**: Ninguna (opcional: parámetros de paginación)
- **Salida**: Lista de Kids ordenados por `age` (ascendente)
- **Comportamiento**: Implementar **recorrido Inorden** (Left → Root → Right) para obtener los elementos en orden ascendente por edad

---

## Recorridos del Árbol

### Recorrido Inorden (In-Order Traversal)
**Orden**: Izquierda → Raíz → Derecha

**Resultado**: Lista de Kids ordenados por `age` de menor a mayor

**Pseudocódigo**:
```python
def inorder(node):
    if node is not None:
        inorder(node.left)
        visit(node)  # Procesar el nodo actual
        inorder(node.right)
```

### Otros Recorridos (Opcionales)
- **Preorden** (Root → Left → Right): Útil para copiar el árbol
- **Postorden** (Left → Right → Root): Útil para eliminar el árbol

---

## Complejidad Temporal

| Operación | Mejor Caso | Caso Promedio | Peor Caso |
|-----------|------------|---------------|--------|
| Insertar | Rápido | Rápido | Lento |
| Buscar | Rápido | Rápido | Lento |
| Actualizar | Rápido | Rápido | Lento |
| Borrar | Rápido | Rápido | Lento |
| Recorrido | Normal | Normal | Normal |

**Nota**: El peor caso ocurre cuando el árbol está desbalanceado (degenerado en lista enlazada).

---

## Ejemplo de Estructura

```
        Kid(age=10)
       /           \
   Kid(age=5)    Kid(age=15)
   /        \         \
Kid(age=3) Kid(age=7) Kid(age=20)
```

**Recorrido Inorden**: [3, 5, 7, 10, 15, 20]

---

## Consideraciones de Implementación

1. **Validación de datos**: Verificar que `id` sea único y `age` sea válido
2. **Manejo de duplicados**: Definir política para `age` duplicados (permitir o rechazar)
3. **Balanceo**: Considerar migrar a AVL si el árbol se desbalancea frecuentemente
4. **Persistencia**: Definir estrategia de almacenamiento (memoria, base de datos, archivo)
5. **Concurrencia**: Implementar locks si se requiere acceso concurrente

---

## Endpoints FastAPI Sugeridos

```
POST   /kids              # Crear nuevo Kid
GET    /kids              # Obtener todos los Kids (inorden)
GET    /kids/{id}         # Obtener Kid por ID
GET    /kids?age={age}    # Buscar Kids por edad
PUT    /kids/{id}         # Actualizar Kid completo
PATCH  /kids/{id}         # Actualizar Kid parcial
DELETE /kids/{id}         # Eliminar Kid
```

---

## Modelos de Datos (Especificación)

### Modelos Pydantic Requeridos:

#### **KidBase** (Modelo Base)
- `id`: int - Identificador único del niño
- `age`: int - Edad del niño (0-18 años)
- `name`: str - Nombre del niño (1-100 caracteres)
- `gender`: str - Género del niño (valores: "male", "female", "other")

#### **KidCreate** (Modelo para Crear)
- Hereda todos los campos de KidBase
- Usado en la operación POST /kids

#### **KidUpdate** (Modelo para Actualizar)
- `age`: Optional[int] - Edad del niño (0-18 años)
- `name`: Optional[str] - Nombre del niño (1-100 caracteres)
- `gender`: Optional[str] - Género del niño (valores: "male", "female", "other")
- Todos los campos son opcionales
- Usado en las operaciones PUT/PATCH /kids/{id}

#### **KidResponse** (Modelo de Respuesta)
- Hereda todos los campos de KidBase
- Usado para retornar datos en las respuestas de la API