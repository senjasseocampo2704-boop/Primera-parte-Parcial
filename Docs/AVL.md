# AVL (Árbol Balanceado) - AVL Tree

## Propósito

**Extensión del ABB** para garantizar el auto-balanceo del árbol. Almacena y ordena objetos **"Kid"** de manera balanceada, asegurando operaciones de búsqueda, inserción y eliminación rápidas en todos los casos.

**Relación con ABB**: 
- El AVL **hereda** todas las funcionalidades del ABB
- **Añade** la propiedad de factor de balanceo
- **Implementa** lógica de rotaciones para mantener la eficiencia
- **Garantiza** que el árbol nunca se degenere en lista enlazada

---

## Estructura del Nodo

**Hereda la estructura del ABB** con una propiedad adicional para el balanceo.

### Propiedades del Nodo (Mismas que ABB + altura):

| Propiedad | Tipo | Descripción | Origen |
|-----------|------|-------------|--------|
| `id` | `int` | Identificador único del niño | **ABB** |
| `age` | `int` | Edad del niño (criterio de ordenación) | **ABB** |
| `name` | `str` | Nombre del niño | **ABB** |
| `gender` | `str` | Género del niño | **ABB** |
| `left` | `Node` | Referencia al hijo izquierdo (age menor) | **ABB** |
| `right` | `Node` | Referencia al hijo derecho (age mayor) | **ABB** |
| `height` | `int` | **Altura del nodo** (necesaria para balanceo) | **AVL (nueva)** |

### Criterio de Ordenación:

El árbol se ordena basándose en el campo **`age`**:
- **Subárbol izquierdo**: Contiene nodos con `age` menor que el nodo actual
- **Subárbol derecho**: Contiene nodos con `age` mayor que el nodo actual

### Propiedad de Balanceo AVL:

**Factor de Balance (BF)** = altura(subárbol derecho) - altura(subárbol izquierdo)

- Un árbol AVL está balanceado si para **cada nodo**: `-1 ≤ BF ≤ 1`
- Si el factor de balance es `-2` o `2`, se requiere una **rotación** para rebalancear

---

## Funcionalidades (API)

**Las funcionalidades son las mismas que el ABB**, pero con lógica adicional de balanceo.

Se requiere el soporte de las siguientes operaciones para la entidad **"Kid"** integradas con **FastAPI**:

### 1. **Insertar (Create)** - Heredado de ABB + Auto-balanceo
- **Operación**: `POST /kids`
- **Descripción**: Agregar un nuevo nodo "Kid" al árbol
- **Entrada**: Objeto Kid con `id`, `age`, `name`, `gender` (igual que ABB)
- **Salida**: Confirmación de inserción exitosa
- **Comportamiento ABB**: Insertar el nodo en la posición correcta según su `age`
- **Comportamiento AVL adicional**: 
  1. Actualizar alturas de los nodos ancestros
  2. Verificar factor de balance
  3. Aplicar rotaciones si es necesario para mantener el balanceo

### 2. **Buscar (Read)** - Heredado de ABB (sin cambios)
- **Operación**: `GET /kids/{id}` o `GET /kids?age={age}`
- **Descripción**: Encontrar un Kid por su `id` o `age`
- **Entrada**: 
  - `id` (int): Búsqueda por identificador único
  - `age` (int): Búsqueda por edad
- **Salida**: Objeto Kid encontrado o mensaje de error si no existe
- **Comportamiento**: Igual que ABB, pero con rendimiento **garantizado** rápido

### 3. **Actualizar (Update)** - Heredado de ABB + Auto-balanceo
- **Operación**: `PUT /kids/{id}` o `PATCH /kids/{id}`
- **Descripción**: Modificar los datos de un Kid existente
- **Entrada**: `id` del Kid y campos a actualizar (`name`, `gender`, `age`)
- **Salida**: Objeto Kid actualizado
- **Comportamiento ABB**: Re-insertar si cambia `age`
- **Comportamiento AVL adicional**: 
  - Si se modifica el `age`:
    1. Eliminar el nodo (con rebalanceo AVL)
    2. Actualizar los datos
    3. Re-insertar el nodo (con rebalanceo AVL)

### 4. **Borrar (Delete)** - Heredado de ABB + Auto-balanceo
- **Operación**: `DELETE /kids/{id}`
- **Descripción**: Eliminar un nodo "Kid" del árbol
- **Entrada**: `id` del Kid a eliminar
- **Salida**: Confirmación de eliminación exitosa
- **Comportamiento ABB**: Eliminar el nodo (3 casos: hoja, un hijo, dos hijos)
- **Comportamiento AVL adicional**: 
  1. Actualizar alturas de los nodos ancestros
  2. Verificar factor de balance
  3. Aplicar rotaciones si es necesario

### 5. **Recorrido (Read All)** - Heredado de ABB (sin cambios)
- **Operación**: `GET /kids` o `GET /kids/inorder`
- **Descripción**: Obtener todos los niños ordenados por edad
- **Entrada**: Ninguna (opcional: parámetros de paginación)
- **Salida**: Lista de Kids ordenados por `age` (ascendente)
- **Comportamiento**: Implementar **recorrido Inorden** (Left → Root → Right) - Igual que ABB

---

## Lógica de Rotaciones para Mantener Eficiencia

**Extensión AVL**: Las rotaciones son operaciones que rebalancean el árbol manteniendo la propiedad de ordenación del ABB.

### Tipos de Rotaciones Requeridas:

#### 1. **Rotación Simple a la Derecha (Right Rotation)**
- **Cuándo aplicar**: Factor de balance = -2 en nodo y -1 en hijo izquierdo (caso Left-Left)
- **Propósito**: Rebalancear cuando el subárbol izquierdo es más pesado
- **Efecto**: Reduce la altura del subárbol izquierdo

#### 2. **Rotación Simple a la Izquierda (Left Rotation)**
- **Cuándo aplicar**: Factor de balance = 2 en nodo y 1 en hijo derecho (caso Right-Right)
- **Propósito**: Rebalancear cuando el subárbol derecho es más pesado
- **Efecto**: Reduce la altura del subárbol derecho

#### 3. **Rotación Doble Izquierda-Derecha (Left-Right Rotation)**
- **Cuándo aplicar**: Factor de balance = -2 en nodo y 1 en hijo izquierdo (caso Left-Right)
- **Proceso**: Rotación izquierda en hijo + rotación derecha en nodo
- **Propósito**: Rebalancear casos complejos de desbalanceo izquierdo

#### 4. **Rotación Doble Derecha-Izquierda (Right-Left Rotation)**
- **Cuándo aplicar**: Factor de balance = 2 en nodo y -1 en hijo derecho (caso Right-Left)
- **Proceso**: Rotación derecha en hijo + rotación izquierda en nodo
- **Propósito**: Rebalancear casos complejos de desbalanceo derecho

---

## Algoritmo de Balanceo (Especificación)

**Proceso para mantener el balanceo después de cada operación:**

1. **Actualizar altura del nodo**: Calcular altura basándose en las alturas de los hijos
2. **Calcular factor de balance**: Diferencia entre altura del subárbol derecho e izquierdo
3. **Detectar desbalanceo**: Si el factor de balance es -2 o 2
4. **Aplicar rotación apropiada**:
   - Caso Left-Left: Rotación simple derecha
   - Caso Right-Right: Rotación simple izquierda
   - Caso Left-Right: Rotación doble izquierda-derecha
   - Caso Right-Left: Rotación doble derecha-izquierda
5. **Retornar nodo balanceado**


---

## Ejemplo de Estructura AVL

```
        Kid(age=10, h=2)
       /                \
   Kid(age=5, h=1)    Kid(age=15, h=1)
   /        \              \
Kid(age=3) Kid(age=7)    Kid(age=20)
(h=0)      (h=0)         (h=0)
```

**Factores de Balance**: Todos entre -1 y 1 (árbol balanceado)

---

## Consideraciones de Implementación

1. **Altura del nodo**: Debe actualizarse después de cada inserción/eliminación
2. **Factor de balance**: Calcular en cada operación para detectar desbalanceo
3. **Rotaciones**: Implementar correctamente los 4 tipos de rotaciones
4. **Validación**: Verificar que el árbol mantenga la propiedad AVL
5. **Testing**: Probar casos extremos (inserción ordenada, eliminaciones múltiples)

---

## Endpoints FastAPI (Mismos que ABB)

**Los endpoints son idénticos al ABB**, la diferencia está en la implementación interna:

```
POST   /kids              # Crear nuevo Kid (con auto-balanceo interno)
GET    /kids              # Obtener todos los Kids (inorden)
GET    /kids/{id}         # Obtener Kid por ID
GET    /kids?age={age}    # Buscar Kids por edad
PUT    /kids/{id}         # Actualizar Kid completo (con rebalanceo si cambia age)
PATCH  /kids/{id}         # Actualizar Kid parcial (con rebalanceo si cambia age)
DELETE /kids/{id}         # Eliminar Kid (con auto-balanceo interno)
GET    /kids/stats        # Obtener estadísticas del árbol (altura, balance) - OPCIONAL
```

---

## Modelos de Datos (Mismos que ABB)

**Los modelos Pydantic son idénticos al ABB**:

### Modelos Requeridos:
- **KidBase**: Modelo base con `id`, `age`, `name`, `gender`
- **KidCreate**: Modelo para crear un nuevo Kid (hereda de KidBase)
- **KidUpdate**: Modelo para actualizar un Kid (campos opcionales)
- **KidResponse**: Modelo de respuesta (hereda de KidBase)

### Modelo Adicional (Opcional):
- **TreeStats**: Estadísticas del árbol AVL
  - `total_nodes`: Número total de nodos
  - `tree_height`: Altura del árbol
  - `is_balanced`: Indicador si el árbol está balanceado
  - `min_age`: Edad mínima en el árbol
  - `max_age`: Edad máxima en el árbol

---

## Cuándo Usar AVL

### Usar AVL cuando:
- ✅ Las búsquedas son **muy frecuentes**
- ✅ Se requiere **rendimiento predecible** (garantizado)
- ✅ Los datos pueden llegar **ordenados o semi-ordenados**
- ✅ La aplicación es **crítica** en tiempo de respuesta

### Usar ABB simple cuando:
- ✅ Los datos son **aleatorios**
- ✅ Las operaciones son **poco frecuentes**
- ✅ Se prefiere **simplicidad** de implementación
- ✅ El overhead de balanceo no es justificable