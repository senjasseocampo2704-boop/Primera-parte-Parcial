# Ejemplos de Uso - API AVL Tree

## 🚀 Iniciar el Servidor AVL

```bash
python -m uvicorn umanizales_edu.main_avl:app --reload
```

El servidor estará disponible en: **http://127.0.0.1:8000**

---

## 📚 Acceder a la Documentación

- **Swagger UI (Interactiva)**: http://127.0.0.1:8000/docs
- **ReDoc**: http://127.0.0.1:8000/redoc
- **Root**: http://127.0.0.1:8000/

---

## 🧪 Ejemplos con cURL (Windows)

### 1. Insertar Niños con Auto-balanceo

```bash
# Insertar en orden ascendente (causaría desbalanceo en ABB simple)
curl -X POST "http://127.0.0.1:8000/children" ^
  -H "Content-Type: application/json" ^
  -d "{\"documento\": 1000, \"nombre\": \"Ana García\", \"edad\": 7, \"acudiente\": \"José García\", \"notas\": \"Muy aplicada\"}"

curl -X POST "http://127.0.0.1:8000/children" ^
  -H "Content-Type: application/json" ^
  -d "{\"documento\": 2000, \"nombre\": \"Luis Martínez\", \"edad\": 9, \"acudiente\": \"Carmen Martínez\", \"notas\": \"Buen comportamiento\"}"

curl -X POST "http://127.0.0.1:8000/children" ^
  -H "Content-Type: application/json" ^
  -d "{\"documento\": 3000, \"nombre\": \"María López\", \"edad\": 8, \"acudiente\": \"Pedro López\", \"notas\": \"Excelente en arte\"}"

curl -X POST "http://127.0.0.1:8000/children" ^
  -H "Content-Type: application/json" ^
  -d "{\"documento\": 4000, \"nombre\": \"Carlos Ruiz\", \"edad\": 10, \"acudiente\": \"Ana Ruiz\", \"notas\": \"Buen estudiante\"}"

curl -X POST "http://127.0.0.1:8000/children" ^
  -H "Content-Type: application/json" ^
  -d "{\"documento\": 5000, \"nombre\": \"Sofia Torres\", \"edad\": 11, \"acudiente\": \"Miguel Torres\", \"notas\": \"Líder natural\"}"

curl -X POST "http://127.0.0.1:8000/children" ^
  -H "Content-Type: application/json" ^
  -d "{\"documento\": 6000, \"nombre\": \"Juan Pérez\", \"edad\": 12, \"acudiente\": \"Laura Pérez\", \"notas\": \"Destacado en deportes\"}"

curl -X POST "http://127.0.0.1:8000/children" ^
  -H "Content-Type: application/json" ^
  -d "{\"documento\": 7000, \"nombre\": \"Pedro Sánchez\", \"edad\": 13, \"acudiente\": \"Elena Sánchez\", \"notas\": \"Excelente en matemáticas\"}"
```

**Nota**: A pesar de insertar en orden ascendente, el árbol AVL se auto-balancea automáticamente.

---

### 2. Obtener un Niño por Documento

```bash
# Buscar niño con documento 4000
curl -X GET "http://127.0.0.1:8000/children/4000"

# Buscar niño con documento 1000
curl -X GET "http://127.0.0.1:8000/children/1000"
```

**Respuesta (200 OK):**
```json
{
  "documento": 4000,
  "nombre": "Carlos Ruiz",
  "edad": 10,
  "acudiente": "Ana Ruiz",
  "notas": "Buen estudiante"
}
```

---

### 3. Listar Todos los Niños

```bash
# Recorrido Inorden (ordenado por documento)
curl -X GET "http://127.0.0.1:8000/children?order=in"

# Recorrido Preorden
curl -X GET "http://127.0.0.1:8000/children?order=pre"

# Recorrido Postorden
curl -X GET "http://127.0.0.1:8000/children?order=post"
```

**Respuesta Inorden (ordenado):**
```json
[
  {"documento": 1000, "nombre": "Ana García", "edad": 7, ...},
  {"documento": 2000, "nombre": "Luis Martínez", "edad": 9, ...},
  {"documento": 3000, "nombre": "María López", "edad": 8, ...},
  {"documento": 4000, "nombre": "Carlos Ruiz", "edad": 10, ...},
  {"documento": 5000, "nombre": "Sofia Torres", "edad": 11, ...},
  {"documento": 6000, "nombre": "Juan Pérez", "edad": 12, ...},
  {"documento": 7000, "nombre": "Pedro Sánchez", "edad": 13, ...}
]
```

---

### 4. Actualizar un Niño

```bash
# Actualizar nombre y edad
curl -X PUT "http://127.0.0.1:8000/children/4000" ^
  -H "Content-Type: application/json" ^
  -d "{\"nombre\": \"Carlos Ruiz Actualizado\", \"edad\": 11}"

# Actualizar solo las notas
curl -X PUT "http://127.0.0.1:8000/children/3000" ^
  -H "Content-Type: application/json" ^
  -d "{\"notas\": \"Promovida al siguiente grado\"}"
```

---

### 5. Eliminar un Niño (con auto-balanceo)

```bash
# Eliminar niño con documento 1000
curl -X DELETE "http://127.0.0.1:8000/children/1000"

# Eliminar niño con documento 7000
curl -X DELETE "http://127.0.0.1:8000/children/7000"
```

**Respuesta (200 OK):**
```json
{
  "message": "Niño con documento 1000 eliminado correctamente"
}
```

**Nota**: El árbol se rebalancea automáticamente después de cada eliminación.

---

### 6. Obtener Estadísticas del Árbol AVL

```bash
curl -X GET "http://127.0.0.1:8000/children/stats/tree"
```

**Respuesta:**
```json
{
  "tree_height": 3,
  "is_balanced": true,
  "tree_type": "AVL (Auto-balanceado)"
}
```

---

## 🌐 Usando PowerShell (Windows)

```powershell
# Insertar un niño
Invoke-RestMethod -Uri "http://127.0.0.1:8000/children" -Method Post -ContentType "application/json" -Body '{"documento": 5000, "nombre": "Carlos Ruiz", "edad": 10, "acudiente": "Ana Ruiz", "notas": "Buen estudiante"}'

# Obtener un niño
Invoke-RestMethod -Uri "http://127.0.0.1:8000/children/5000" -Method Get

# Listar todos (inorden)
Invoke-RestMethod -Uri "http://127.0.0.1:8000/children?order=in" -Method Get

# Actualizar
Invoke-RestMethod -Uri "http://127.0.0.1:8000/children/5000" -Method Put -ContentType "application/json" -Body '{"edad": 11}'

# Eliminar
Invoke-RestMethod -Uri "http://127.0.0.1:8000/children/5000" -Method Delete

# Estadísticas del árbol
Invoke-RestMethod -Uri "http://127.0.0.1:8000/children/stats/tree" -Method Get
```

---

## 🧪 Prueba de Auto-balanceo

### Escenario: Inserción en orden ascendente

Este es el **peor caso** para un ABB simple (se convertiría en lista enlazada), pero el AVL lo maneja perfectamente.

```bash
# Insertar 1000, 2000, 3000, 4000, 5000, 6000, 7000 en orden
# (ejecutar los comandos de inserción del punto 1)

# Verificar que el árbol está balanceado
curl -X GET "http://127.0.0.1:8000/children/stats/tree"
```

**Resultado esperado:**
- Altura del árbol: **3** (óptimo para 7 nodos)
- Está balanceado: **true**

**Comparación:**
- **ABB simple**: Altura = 7 (lista enlazada) ❌
- **AVL**: Altura = 3 (balanceado) ✅

---

## 📊 Visualización del Auto-balanceo

### Después de insertar 1000, 2000, 3000, 4000, 5000, 6000, 7000:

**Estructura del árbol AVL:**
```
        4000
       /    \
    2000    6000
   /   \    /   \
1000 3000 5000 7000
```

**Factores de Balance:**
- Nodo 4000: BF = 0 (balanceado)
- Nodo 2000: BF = 0 (balanceado)
- Nodo 6000: BF = 0 (balanceado)
- Todos los nodos hoja: BF = 0

---

## 🔄 Ejemplo de Rotaciones

### Caso 1: Rotación Simple Derecha (LL)

```bash
# Insertar en orden descendente: 3000, 2000, 1000
curl -X POST "http://127.0.0.1:8000/children" -H "Content-Type: application/json" -d "{\"documento\": 3000, \"nombre\": \"Test1\", \"edad\": 10, \"acudiente\": \"Test\", \"notas\": \"\"}"
curl -X POST "http://127.0.0.1:8000/children" -H "Content-Type: application/json" -d "{\"documento\": 2000, \"nombre\": \"Test2\", \"edad\": 10, \"acudiente\": \"Test\", \"notas\": \"\"}"
curl -X POST "http://127.0.0.1:8000/children" -H "Content-Type: application/json" -d "{\"documento\": 1000, \"nombre\": \"Test3\", \"edad\": 10, \"acudiente\": \"Test\", \"notas\": \"\"}"

# Verificar balanceo
curl -X GET "http://127.0.0.1:8000/children/stats/tree"
```

**Resultado**: Rotación derecha automática, árbol balanceado.

---

### Caso 2: Rotación Doble LR (Left-Right)

```bash
# Insertar: 5000, 2000, 3000 (requiere rotación LR)
curl -X POST "http://127.0.0.1:8000/children" -H "Content-Type: application/json" -d "{\"documento\": 5000, \"nombre\": \"Test1\", \"edad\": 10, \"acudiente\": \"Test\", \"notas\": \"\"}"
curl -X POST "http://127.0.0.1:8000/children" -H "Content-Type: application/json" -d "{\"documento\": 2000, \"nombre\": \"Test2\", \"edad\": 10, \"acudiente\": \"Test\", \"notas\": \"\"}"
curl -X POST "http://127.0.0.1:8000/children" -H "Content-Type: application/json" -d "{\"documento\": 3000, \"nombre\": \"Test3\", \"edad\": 10, \"acudiente\": \"Test\", \"notas\": \"\"}"

# Verificar balanceo
curl -X GET "http://127.0.0.1:8000/children/stats/tree"
```

**Resultado**: Rotación doble LR automática, árbol balanceado.

---

## 🎯 Secuencia Completa de Prueba

```bash
# 1. Insertar 7 niños en orden ascendente
# (ejecutar comandos del punto 1)

# 2. Verificar estadísticas (debe estar balanceado)
curl -X GET "http://127.0.0.1:8000/children/stats/tree"

# 3. Listar todos (inorden - ordenado)
curl -X GET "http://127.0.0.1:8000/children?order=in"

# 4. Buscar uno específico
curl -X GET "http://127.0.0.1:8000/children/4000"

# 5. Actualizar
curl -X PUT "http://127.0.0.1:8000/children/4000" -H "Content-Type: application/json" -d "{\"edad\": 11}"

# 6. Eliminar varios (el árbol se rebalancea automáticamente)
curl -X DELETE "http://127.0.0.1:8000/children/1000"
curl -X DELETE "http://127.0.0.1:8000/children/7000"

# 7. Verificar que sigue balanceado
curl -X GET "http://127.0.0.1:8000/children/stats/tree"

# 8. Listar de nuevo
curl -X GET "http://127.0.0.1:8000/children?order=in"
```

---

## 📈 Comparación de Rendimiento

### Inserción de 7 elementos en orden ascendente:

| Métrica | ABB Simple | AVL |
|---------|------------|-----|
| Altura del árbol | 7 | 3 |
| Búsqueda de elemento | O(7) = O(n) | O(3) = O(log n) |
| Está balanceado | ❌ No | ✅ Sí |
| Rotaciones realizadas | 0 | 3-4 |

---

## 💡 Consejos de Uso

1. **Usa Swagger UI** (http://127.0.0.1:8000/docs) para probar interactivamente
2. **Verifica el balanceo** con `/children/stats/tree` después de operaciones
3. **Prueba casos extremos** como inserción ordenada para ver el auto-balanceo
4. **Compara con ABB** para entender las ventajas del AVL

---

## 🔍 Debugging

Para ver la estructura interna del árbol, ejecuta:

```bash
python test_avl.py
```

Este script muestra:
- Estructura visual del árbol
- Factores de balance de cada nodo
- Alturas de los nodos
- Verificación de balanceo

---

## 📝 Notas Importantes

- El árbol **siempre está balanceado** (factor de balance entre -1 y 1)
- Las rotaciones son **automáticas y transparentes**
- La altura del árbol es **logarítmica** respecto al número de nodos
- Ideal para **búsquedas frecuentes** y **datos ordenados**
