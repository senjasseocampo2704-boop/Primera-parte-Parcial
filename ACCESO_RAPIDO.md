# 🎯 Acceso Rápido a las APIs

## ✅ Servidores Activos

Ambos servidores están **ejecutándose** en este momento:

---

## 🌳 ABB - Árbol Binario de Búsqueda

### 📍 Puerto: 8000

| Recurso | URL | Descripción |
|---------|-----|-------------|
| 🏠 **Root** | http://127.0.0.1:8000/ | Información de la API |
| 📖 **Swagger UI** | http://127.0.0.1:8000/docs | Interfaz interactiva |
| 📚 **ReDoc** | http://127.0.0.1:8000/redoc | Documentación alternativa |

### 🔗 Haz clic aquí:
**→ [ABRIR SWAGGER ABB](http://127.0.0.1:8000/docs) ←**

---

## 🔄 AVL - Árbol Auto-balanceado

### 📍 Puerto: 8001

| Recurso | URL | Descripción |
|---------|-----|-------------|
| 🏠 **Root** | http://127.0.0.1:8001/ | Información de la API |
| 📖 **Swagger UI** | http://127.0.0.1:8001/docs | Interfaz interactiva |
| 📚 **ReDoc** | http://127.0.0.1:8001/redoc | Documentación alternativa |

### 🔗 Haz clic aquí:
**→ [ABRIR SWAGGER AVL](http://127.0.0.1:8001/docs) ←**

---

## 🚀 Endpoints Principales

### ABB (8000) - 5 Endpoints:
```
POST   /children                    → Insertar niño
GET    /children/{documento}        → Obtener niño
GET    /children?order=in|pre|post  → Listar todos
PUT    /children/{documento}        → Actualizar niño
DELETE /children/{documento}        → Eliminar niño
```

### AVL (8001) - 6 Endpoints:
```
POST   /children                    → Insertar niño (auto-balanceo)
GET    /children/{documento}        → Obtener niño
GET    /children?order=in|pre|post  → Listar todos
PUT    /children/{documento}        → Actualizar niño
DELETE /children/{documento}        → Eliminar niño (auto-balanceo)
GET    /children/stats/tree         → Estadísticas AVL ⭐
```

---

## 🧪 Prueba Rápida con Swagger

### 1. Abre ambos Swagger en pestañas diferentes
- [ABB Swagger](http://127.0.0.1:8000/docs)
- [AVL Swagger](http://127.0.0.1:8001/docs)

### 2. Inserta un niño en ABB (Puerto 8000)
```json
{
  "documento": 1001,
  "nombre": "Juan Pérez",
  "edad": 10,
  "acudiente": "María Pérez",
  "notas": "Estudiante destacado"
}
```

### 3. Inserta el mismo niño en AVL (Puerto 8001)
```json
{
  "documento": 1001,
  "nombre": "Juan Pérez",
  "edad": 10,
  "acudiente": "María Pérez",
  "notas": "Estudiante destacado"
}
```

### 4. Compara las respuestas
- Ambos deben retornar `201 Created`
- Los datos son independientes (memoria separada)

### 5. Prueba el endpoint exclusivo de AVL
```
GET http://127.0.0.1:8001/children/stats/tree
```

Verás:
```json
{
  "total_nodes": 1,
  "tree_height": 1,
  "is_balanced": true,
  "min_age": 10,
  "max_age": 10
}
```

---

## 💡 Experimento Sugerido

### Inserta estos documentos en orden en ambos servidores:

```
1000, 2000, 3000, 4000, 5000, 6000, 7000
```

### Luego compara:

**ABB (8000):**
- Árbol degenerado (lista enlazada)
- Altura = 7
- Búsqueda lenta

**AVL (8001):**
- Árbol balanceado
- Altura = 3
- Búsqueda rápida
- Verifica con `/stats/tree`

---

## 🛑 Detener los Servidores

Para detener los servidores:
1. Ve a las terminales donde están ejecutándose
2. Presiona `Ctrl + C`
3. O cierra las ventanas de terminal

---

## 🔄 Reiniciar los Servidores

Si necesitas reiniciar:

**Terminal 1:**
```bash
cd "c:\Users\senja\Desktop\universidad\IV semestre\Programacion 3\fastapi_scaffold"
python -m uvicorn main_abb:app --reload --port 8000
```

**Terminal 2:**
```bash
cd "c:\Users\senja\Desktop\universidad\IV semestre\Programacion 3\fastapi_scaffold"
python -m uvicorn main_avl:app --reload --port 8001
```

---

## 📊 Estado de los Servidores

| Servidor | Puerto | Estado | Swagger |
|----------|--------|--------|---------|
| **ABB** | 8000 | ✅ Activo | [Abrir](http://127.0.0.1:8000/docs) |
| **AVL** | 8001 | ✅ Activo | [Abrir](http://127.0.0.1:8001/docs) |

---

## 🎓 Documentación Completa

- 📘 `README.md` - Guía ABB
- 📘 `README_AVL.md` - Guía AVL
- 📊 `ABB_VS_AVL.md` - Comparación detallada
- 📚 `PROYECTO_COMPLETO.md` - Documentación completa
- 🚀 `SERVIDORES_SIMULTANEOS.md` - Gestión de servidores

---

## ✨ ¡Todo Listo!

Los servidores están ejecutándose y listos para usar.

**¡Haz clic en los enlaces de Swagger y comienza a explorar!** 🚀
