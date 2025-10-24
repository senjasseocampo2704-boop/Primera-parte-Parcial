# Ejemplos de Uso de la API - Children Management

## 🚀 Iniciar el Servidor

```bash
python -m uvicorn umanizales_edu.main:app --reload
```

El servidor estará disponible en: **http://127.0.0.1:8000**

---

## 📚 Acceder a la Documentación

- **Swagger UI (Interactiva)**: http://127.0.0.1:8000/docs
- **ReDoc**: http://127.0.0.1:8000/redoc
- **Root**: http://127.0.0.1:8000/

---

## 🧪 Ejemplos con cURL

### 1. Insertar Niños (POST /children)

```bash
# Insertar primer niño
curl -X POST "http://127.0.0.1:8000/children" ^
  -H "Content-Type: application/json" ^
  -d "{\"documento\": 5000, \"nombre\": \"Carlos Ruiz\", \"edad\": 10, \"acudiente\": \"Ana Ruiz\", \"notas\": \"Buen estudiante\"}"

# Insertar segundo niño
curl -X POST "http://127.0.0.1:8000/children" ^
  -H "Content-Type: application/json" ^
  -d "{\"documento\": 3000, \"nombre\": \"María López\", \"edad\": 8, \"acudiente\": \"Pedro López\", \"notas\": \"Excelente en arte\"}"

# Insertar tercer niño
curl -X POST "http://127.0.0.1:8000/children" ^
  -H "Content-Type: application/json" ^
  -d "{\"documento\": 8000, \"nombre\": \"Juan Pérez\", \"edad\": 12, \"acudiente\": \"Laura Pérez\", \"notas\": \"Destacado en deportes\"}"

# Insertar cuarto niño
curl -X POST "http://127.0.0.1:8000/children" ^
  -H "Content-Type: application/json" ^
  -d "{\"documento\": 2000, \"nombre\": \"Ana García\", \"edad\": 7, \"acudiente\": \"José García\", \"notas\": \"Muy aplicada\"}"

# Insertar quinto niño
curl -X POST "http://127.0.0.1:8000/children" ^
  -H "Content-Type: application/json" ^
  -d "{\"documento\": 9000, \"nombre\": \"Pedro Sánchez\", \"edad\": 13, \"acudiente\": \"Elena Sánchez\", \"notas\": \"Excelente en matemáticas\"}"
```

**Respuesta esperada (201 Created):**
```json
{
  "documento": 5000,
  "nombre": "Carlos Ruiz",
  "edad": 10,
  "acudiente": "Ana Ruiz",
  "notas": "Buen estudiante"
}
```

---

### 2. Obtener un Niño por Documento (GET /children/{documento})

```bash
# Buscar niño con documento 5000
curl -X GET "http://127.0.0.1:8000/children/5000"

# Buscar niño con documento 3000
curl -X GET "http://127.0.0.1:8000/children/3000"

# Buscar niño que no existe
curl -X GET "http://127.0.0.1:8000/children/9999"
```

**Respuesta exitosa (200 OK):**
```json
{
  "documento": 5000,
  "nombre": "Carlos Ruiz",
  "edad": 10,
  "acudiente": "Ana Ruiz",
  "notas": "Buen estudiante"
}
```

**Respuesta error (404 Not Found):**
```json
{
  "detail": "Niño con documento 9999 no encontrado"
}
```

---

### 3. Listar Todos los Niños (GET /children)

```bash
# Listar con recorrido Inorden (ordenado por documento - default)
curl -X GET "http://127.0.0.1:8000/children"

# Listar con recorrido Inorden (explícito)
curl -X GET "http://127.0.0.1:8000/children?order=in"

# Listar con recorrido Preorden
curl -X GET "http://127.0.0.1:8000/children?order=pre"

# Listar con recorrido Postorden
curl -X GET "http://127.0.0.1:8000/children?order=post"
```

**Respuesta (200 OK):**
```json
[
  {
    "documento": 2000,
    "nombre": "Ana García",
    "edad": 7,
    "acudiente": "José García",
    "notas": "Muy aplicada"
  },
  {
    "documento": 3000,
    "nombre": "María López",
    "edad": 8,
    "acudiente": "Pedro López",
    "notas": "Excelente en arte"
  },
  {
    "documento": 5000,
    "nombre": "Carlos Ruiz",
    "edad": 10,
    "acudiente": "Ana Ruiz",
    "notas": "Buen estudiante"
  }
]
```

---

### 4. Actualizar un Niño (PUT /children/{documento})

```bash
# Actualizar nombre y edad
curl -X PUT "http://127.0.0.1:8000/children/5000" ^
  -H "Content-Type: application/json" ^
  -d "{\"nombre\": \"Carlos Ruiz Actualizado\", \"edad\": 11}"

# Actualizar solo las notas
curl -X PUT "http://127.0.0.1:8000/children/3000" ^
  -H "Content-Type: application/json" ^
  -d "{\"notas\": \"Promovida al siguiente grado\"}"

# Actualizar todos los campos
curl -X PUT "http://127.0.0.1:8000/children/8000" ^
  -H "Content-Type: application/json" ^
  -d "{\"nombre\": \"Juan Pérez García\", \"edad\": 13, \"acudiente\": \"Laura Pérez García\", \"notas\": \"Capitán del equipo\"}"
```

**Respuesta (200 OK):**
```json
{
  "documento": 5000,
  "nombre": "Carlos Ruiz Actualizado",
  "edad": 11,
  "acudiente": "Ana Ruiz",
  "notas": "Buen estudiante"
}
```

---

### 5. Eliminar un Niño (DELETE /children/{documento})

```bash
# Eliminar niño con documento 2000
curl -X DELETE "http://127.0.0.1:8000/children/2000"

# Eliminar niño con documento 8000
curl -X DELETE "http://127.0.0.1:8000/children/8000"

# Intentar eliminar niño que no existe
curl -X DELETE "http://127.0.0.1:8000/children/9999"
```

**Respuesta exitosa (200 OK):**
```json
{
  "message": "Niño con documento 2000 eliminado correctamente"
}
```

**Respuesta error (404 Not Found):**
```json
{
  "detail": "Niño con documento 9999 no encontrado"
}
```

---

## 🧪 Secuencia Completa de Prueba

```bash
# 1. Insertar varios niños
curl -X POST "http://127.0.0.1:8000/children" -H "Content-Type: application/json" -d "{\"documento\": 5000, \"nombre\": \"Carlos Ruiz\", \"edad\": 10, \"acudiente\": \"Ana Ruiz\", \"notas\": \"Buen estudiante\"}"
curl -X POST "http://127.0.0.1:8000/children" -H "Content-Type: application/json" -d "{\"documento\": 3000, \"nombre\": \"María López\", \"edad\": 8, \"acudiente\": \"Pedro López\", \"notas\": \"Excelente en arte\"}"
curl -X POST "http://127.0.0.1:8000/children" -H "Content-Type: application/json" -d "{\"documento\": 8000, \"nombre\": \"Juan Pérez\", \"edad\": 12, \"acudiente\": \"Laura Pérez\", \"notas\": \"Destacado en deportes\"}"

# 2. Listar todos (inorden - ordenado)
curl -X GET "http://127.0.0.1:8000/children?order=in"

# 3. Buscar uno específico
curl -X GET "http://127.0.0.1:8000/children/5000"

# 4. Actualizar
curl -X PUT "http://127.0.0.1:8000/children/5000" -H "Content-Type: application/json" -d "{\"edad\": 11}"

# 5. Verificar actualización
curl -X GET "http://127.0.0.1:8000/children/5000"

# 6. Eliminar
curl -X DELETE "http://127.0.0.1:8000/children/3000"

# 7. Listar de nuevo
curl -X GET "http://127.0.0.1:8000/children?order=in"
```

---

## 🌐 Usando PowerShell (Windows)

Si prefieres usar PowerShell en lugar de curl:

```powershell
# Insertar un niño
Invoke-RestMethod -Uri "http://127.0.0.1:8000/children" -Method Post -ContentType "application/json" -Body '{"documento": 5000, "nombre": "Carlos Ruiz", "edad": 10, "acudiente": "Ana Ruiz", "notas": "Buen estudiante"}'

# Obtener un niño
Invoke-RestMethod -Uri "http://127.0.0.1:8000/children/5000" -Method Get

# Listar todos
Invoke-RestMethod -Uri "http://127.0.0.1:8000/children?order=in" -Method Get

# Actualizar
Invoke-RestMethod -Uri "http://127.0.0.1:8000/children/5000" -Method Put -ContentType "application/json" -Body '{"edad": 11}'

# Eliminar
Invoke-RestMethod -Uri "http://127.0.0.1:8000/children/5000" -Method Delete
```

---

## 📊 Estructura del Árbol Después de Inserciones

Después de insertar los documentos: 5000, 3000, 8000, 2000, 9000

```
         5000 (Carlos)
        /            \
    3000 (María)    8000 (Juan)
    /                    \
2000 (Ana)              9000 (Pedro)
```

**Recorrido Inorden**: [2000, 3000, 5000, 8000, 9000] ← Ordenado ascendente
**Recorrido Preorden**: [5000, 3000, 2000, 8000, 9000]
**Recorrido Postorden**: [2000, 3000, 9000, 8000, 5000]

---

## ✅ Validaciones

- **Documento duplicado**: Retorna error 400
- **Documento no encontrado**: Retorna error 404
- **Edad fuera de rango (0-18)**: Retorna error 422
- **Documento negativo**: Retorna error 422
- **Nombre vacío**: Retorna error 422

---

## 🎯 Recomendaciones

1. **Usa Swagger UI** (http://127.0.0.1:8000/docs) para probar la API de forma interactiva
2. **Revisa los ejemplos** en la documentación automática
3. **Prueba los diferentes recorridos** para entender cómo funciona el ABB
4. **Verifica las validaciones** intentando insertar datos inválidos

---

## 📝 Notas Importantes

- Los datos se almacenan **en memoria** y se pierden al reiniciar el servidor
- El árbol se ordena automáticamente por el campo `documento`
- El recorrido **Inorden** siempre retorna los datos ordenados por documento (ascendente)
- No se pueden duplicar documentos
- El campo `documento` no puede ser modificado después de la creación
