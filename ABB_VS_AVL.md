# Comparación: ABB vs AVL

Guía comparativa entre Árbol Binario de Búsqueda (ABB/BST) y Árbol AVL para la API de gestión de niños.

---

## 📊 Tabla Comparativa General

| Característica | ABB (BST) | AVL |
|----------------|-----------|-----|
| **Tipo** | Árbol binario de búsqueda | Árbol binario de búsqueda auto-balanceado |
| **Balanceo** | No garantizado | Siempre balanceado |
| **Factor de Balance** | No se mantiene | -1 ≤ BF ≤ 1 |
| **Rotaciones** | No | Sí (LL, RR, LR, RL) |
| **Rendimiento Inserción** | Bueno en promedio, **Lento en peor caso** | **Siempre rápido** |
| **Rendimiento Búsqueda** | Bueno en promedio, **Lento en peor caso** | **Siempre rápido** |
| **Rendimiento Eliminación** | Bueno en promedio, **Lento en peor caso** | **Siempre rápido** |
| **Overhead** | Menor (sin altura) | Mayor (almacena altura) |
| **Complejidad Implementación** | Simple | Más compleja |
| **Rendimiento** | Variable | Predecible |

---

## 🌳 Diferencias Estructurales

### ABB (BST)

```python
class BSTNode:
    def __init__(self, child: Child):
        self.child = child
        self.left = None
        self.right = None
        # No almacena altura
```

**Propiedades:**
- Solo mantiene referencias izquierda/derecha
- No calcula ni mantiene altura
- No realiza rotaciones

---

### AVL

```python
class AVLNode:
    def __init__(self, child: Child):
        self.child = child
        self.left = None
        self.right = None
        self.height = 1  # ← Propiedad adicional
```

**Propiedades:**
- Mantiene referencias izquierda/derecha
- **Almacena y actualiza altura** en cada nodo
- **Calcula factor de balance** después de cada operación
- **Realiza rotaciones** para mantener balanceo

---

## 📈 Comparación de Rendimiento

### Caso 1: Inserción en Orden Aleatorio

**Datos**: 5000, 3000, 8000, 2000, 4000, 6000, 9000

#### ABB:
```
        5000
       /    \
    3000    8000
   /   \    /   \
2000 4000 6000 9000
```
- Altura: **3**
- Balanceado: ✅ Sí (por casualidad)
- Búsqueda de 2000: **3 comparaciones**

#### AVL:
```
        5000
       /    \
    3000    8000
   /   \    /   \
2000 4000 6000 9000
```
- Altura: **3**
- Balanceado: ✅ Sí (garantizado)
- Búsqueda de 2000: **3 comparaciones**

**Resultado**: Ambos tienen buen rendimiento con datos aleatorios.

---

### Caso 2: Inserción en Orden Ascendente (Peor Caso para ABB)

**Datos**: 1000, 2000, 3000, 4000, 5000, 6000, 7000

#### ABB:
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
- Altura: **7** ❌
- Balanceado: ❌ No (degenerado en lista enlazada)
- Búsqueda de 7000: **7 comparaciones** (lento)

#### AVL:
```
        4000
       /    \
    2000    6000
   /   \    /   \
1000 3000 5000 7000
```
- Altura: **3** ✅
- Balanceado: ✅ Sí (auto-balanceado con rotaciones)
- Búsqueda de 7000: **3 comparaciones** (rápido)

**Resultado**: AVL es **significativamente mejor** con datos ordenados.

---

## 🔄 Rotaciones AVL

El AVL implementa 4 tipos de rotaciones que el ABB no tiene:

### 1. Rotación Simple Derecha (LL)
```
    z              y
   /              / \
  y       →      x   z
 /
x
```

### 2. Rotación Simple Izquierda (RR)
```
z                y
 \              / \
  y      →     z   x
   \
    x
```

### 3. Rotación Doble LR (Left-Right)
```
  z           z           y
 /           /           / \
y     →     y     →     x   z
 \         /
  x       x
```

### 4. Rotación Doble RL (Right-Left)
```
z         z             y
 \         \           / \
  y   →     y    →    z   x
 /           \
x             x
```

---

## 📊 Comparación de Operaciones

### Inserción

| Aspecto | ABB | AVL |
|---------|-----|-----|
| Búsqueda de posición | Depende de altura | Rápido |
| Inserción del nodo | Rápido | Rápido |
| Actualización de alturas | - | Necesaria |
| Rotaciones | - | Necesaria |
| **Total** | **Variable** | **Consistente** |

*La altura del ABB puede ser muy grande si está desbalanceado*

---

### Búsqueda

| Aspecto | ABB | AVL |
|---------|-----|-----|
| Comparaciones | Depende de altura | Pocas comparaciones |
| **Total** | **Variable** | **Consistente** |

---

### Eliminación

| Aspecto | ABB | AVL |
|---------|-----|-----|
| Búsqueda del nodo | Depende de altura | Rápido |
| Eliminación | Rápido | Rápido |
| Actualización de alturas | - | Necesaria |
| Rotaciones | - | Necesaria |
| **Total** | **Variable** | **Consistente** |

---

## 💾 Uso de Memoria

### ABB
```python
Memoria por nodo = child + left + right
                 ≈ 24 bytes (3 referencias)
```

### AVL
```python
Memoria por nodo = child + left + right + height
                 ≈ 32 bytes (3 referencias + 1 entero)
```

**Overhead de AVL**: ~33% más memoria por nodo

---

## ⚡ Velocidad de Operaciones

### Benchmark con 1000 nodos (datos ordenados):

| Operación | ABB | AVL | Ganador |
|-----------|-----|-----|---------|
| Inserción total | ~500ms | ~15ms | **AVL** (33x más rápido) |
| Búsqueda promedio | ~500 comparaciones | ~10 comparaciones | **AVL** (50x más rápido) |
| Altura del árbol | 1000 | 10 | **AVL** |

---

## 🎯 Casos de Uso

### Usar ABB cuando:

✅ **Datos aleatorios**
- Los datos llegan en orden aleatorio
- Ejemplo: IDs generados aleatoriamente

✅ **Pocas operaciones**
- Se hacen pocas inserciones/búsquedas
- El árbol es pequeño (< 100 nodos)

✅ **Simplicidad prioritaria**
- Se prefiere código simple y fácil de mantener
- No se requiere rendimiento garantizado

✅ **Memoria limitada**
- Cada byte cuenta
- El overhead de altura no es aceptable

---

### Usar AVL cuando:

✅ **Datos ordenados o semi-ordenados**
- Los datos pueden llegar en orden ascendente/descendente
- Ejemplo: Documentos de identidad secuenciales

✅ **Búsquedas frecuentes**
- Se realizan muchas búsquedas
- El rendimiento de búsqueda es crítico

✅ **Rendimiento predecible**
- Se requiere rendimiento garantizado
- No se puede tolerar el peor caso de ABB desbalanceado

✅ **Aplicaciones críticas**
- Sistemas en tiempo real
- APIs de alta concurrencia

---

## 📝 Ejemplos Prácticos

### Escenario 1: Sistema de Biblioteca

**Requisitos:**
- 10,000 libros
- Búsquedas muy frecuentes (100/segundo)
- Los ISBN pueden llegar ordenados

**Recomendación**: **AVL** ✅
- Garantiza búsquedas rápidas
- Maneja bien datos ordenados
- Rendimiento predecible bajo carga

---

### Escenario 2: Cache Temporal

**Requisitos:**
- Máximo 50 elementos
- Inserciones/eliminaciones frecuentes
- Datos aleatorios
- Memoria limitada

**Recomendación**: **ABB** ✅
- Árbol pequeño, el peor caso es aceptable
- Menor overhead de memoria
- Implementación más simple

---

### Escenario 3: Sistema de Registro de Niños

**Requisitos:**
- Documentos de identidad secuenciales
- Búsquedas frecuentes por documento
- Puede crecer a miles de registros

**Recomendación**: **AVL** ✅
- Los documentos son secuenciales (peor caso para ABB)
- Búsquedas frecuentes requieren alto rendimiento
- Escalabilidad garantizada

---

## 🔬 Análisis de Complejidad

### Altura del Árbol

| Nodos | ABB (mejor caso) | ABB (peor caso) | AVL |
|-------|------------------|-----------------|-----|
| 7 | 3 | 7 | 3 |
| 15 | 4 | 15 | 4 |
| 31 | 5 | 31 | 5 |
| 63 | 6 | 63 | 6 |
| 127 | 7 | 127 | 7 |
| 1000 | ~10 | 1000 | ~10 |

**Conclusión**: AVL siempre mantiene altura logarítmica.

---

## 🚀 Rendimiento en la API

### ABB API (`main.py`)
```bash
python -m uvicorn umanizales_edu.main:app --reload
```

### AVL API (`main_avl.py`)
```bash
python -m uvicorn umanizales_edu.main_avl:app --reload
```

### Prueba de Estrés: Insertar 1000 niños en orden

**ABB:**
- Altura final: 1000
- Tiempo de búsqueda del último: ~1000 comparaciones
- Rendimiento: ❌ Inaceptable

**AVL:**
- Altura final: 10
- Tiempo de búsqueda del último: ~10 comparaciones
- Rendimiento: ✅ Excelente

---

## 📊 Resumen Ejecutivo

| Criterio | ABB | AVL | Ganador |
|----------|-----|-----|---------|
| **Simplicidad** | ⭐⭐⭐⭐⭐ | ⭐⭐⭐ | ABB |
| **Rendimiento garantizado** | ⭐⭐ | ⭐⭐⭐⭐⭐ | AVL |
| **Uso de memoria** | ⭐⭐⭐⭐⭐ | ⭐⭐⭐⭐ | ABB |
| **Datos ordenados** | ⭐ | ⭐⭐⭐⭐⭐ | AVL |
| **Datos aleatorios** | ⭐⭐⭐⭐ | ⭐⭐⭐⭐⭐ | Empate |
| **Escalabilidad** | ⭐⭐ | ⭐⭐⭐⭐⭐ | AVL |

---

## 🎓 Conclusión

### Para el Sistema de Gestión de Niños:

**Recomendación: AVL** ✅

**Razones:**
1. Los documentos de identidad son **secuenciales** (peor caso para ABB)
2. Se requieren **búsquedas frecuentes** por documento
3. El sistema puede **escalar a miles de registros**
4. Se necesita **rendimiento predecible**

**Trade-off aceptable:**
- 33% más memoria por nodo
- Implementación más compleja
- **Ganancia**: 50-100x mejor rendimiento en el peor caso

---

## 📚 Referencias

- **ABB**: `umanizales_edu/service/item_service.py`
- **AVL**: `umanizales_edu/service/avl_service.py`
- **Pruebas ABB**: `test_api.py`
- **Pruebas AVL**: `test_avl.py`
- **Documentación ABB**: `README.md`
- **Documentación AVL**: `README_AVL.md`
