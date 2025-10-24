# 🚀 Ejecución de Servidores Simultáneos

## ✅ Estado Actual

Ambos servidores FastAPI están **ACTIVOS** y ejecutándose en puertos diferentes:

---

## 🌳 Servidor ABB (Árbol Binario de Búsqueda)

### Configuración:
- **Archivo**: `main_abb.py`
- **Puerto**: `8000`
- **Estado**: ✅ ACTIVO

### URLs de Acceso:
| Recurso | URL |
|---------|-----|
| **API Root** | http://127.0.0.1:8000/ |
| **Swagger UI** | http://127.0.0.1:8000/docs |
| **ReDoc** | http://127.0.0.1:8000/redoc |
| **OpenAPI JSON** | http://127.0.0.1:8000/openapi.json |

### Comando de Ejecución:
```bash
python -m uvicorn main_abb:app --reload --port 8000
```

---

## 🔄 Servidor AVL (Árbol Auto-balanceado)

### Configuración:
- **Archivo**: `main_avl.py`
- **Puerto**: `8001`
- **Estado**: ✅ ACTIVO

### URLs de Acceso:
| Recurso | URL |
|---------|-----|
| **API Root** | http://127.0.0.1:8001/ |
| **Swagger UI** | http://127.0.0.1:8001/docs |
| **ReDoc** | http://127.0.0.1:8001/redoc |
| **OpenAPI JSON** | http://127.0.0.1:8001/openapi.json |

### Comando de Ejecución:
```bash
python -m uvicorn main_avl:app --reload --port 8001
```

---

## 🎯 Acceso Rápido a Swagger

### Opción 1: Hacer clic en los enlaces
- [Swagger ABB - Puerto 8000](http://127.0.0.1:8000/docs)
- [Swagger AVL - Puerto 8001](http://127.0.0.1:8001/docs)

### Opción 2: Copiar y pegar en el navegador
```
http://127.0.0.1:8000/docs
http://127.0.0.1:8001/docs
```

---

## 📋 Endpoints Disponibles

### ABB (Puerto 8000):
- `POST /children` - Insertar niño
- `GET /children/{documento}` - Obtener niño por documento
- `GET /children?order=in|pre|post` - Listar todos
- `PUT /children/{documento}` - Actualizar niño
- `DELETE /children/{documento}` - Eliminar niño

### AVL (Puerto 8001):
- `POST /children` - Insertar niño (con auto-balanceo)
- `GET /children/{documento}` - Obtener niño por documento
- `GET /children?order=in|pre|post` - Listar todos
- `PUT /children/{documento}` - Actualizar niño
- `DELETE /children/{documento}` - Eliminar niño (con auto-balanceo)
- `GET /children/stats/tree` - **Estadísticas del árbol AVL** ⭐

---

## 🔧 Gestión de Servidores

### Iniciar Ambos Servidores (Manual):

**Terminal 1 - ABB:**
```bash
cd "c:\Users\senja\Desktop\universidad\IV semestre\Programacion 3\fastapi_scaffold"
python -m uvicorn main_abb:app --reload --port 8000
```

**Terminal 2 - AVL:**
```bash
cd "c:\Users\senja\Desktop\universidad\IV semestre\Programacion 3\fastapi_scaffold"
python -m uvicorn main_avl:app --reload --port 8001
```

### Iniciar con Script PowerShell:
```powershell
.\start_servers.ps1
```

### Detener Servidores:
- Presiona `Ctrl + C` en cada terminal
- O cierra las ventanas de terminal

---

## 🧪 Prueba Rápida

### Probar ABB (Puerto 8000):
```bash
# Insertar un niño
curl -X POST "http://127.0.0.1:8000/children" -H "Content-Type: application/json" -d "{\"documento\":1001,\"nombre\":\"Juan Pérez\",\"edad\":10}"

# Obtener el niño
curl "http://127.0.0.1:8000/children/1001"
```

### Probar AVL (Puerto 8001):
```bash
# Insertar un niño
curl -X POST "http://127.0.0.1:8001/children" -H "Content-Type: application/json" -d "{\"documento\":2001,\"nombre\":\"María García\",\"edad\":12}"

# Obtener estadísticas del árbol
curl "http://127.0.0.1:8001/children/stats/tree"
```

---

## 📊 Comparación en Tiempo Real

Puedes comparar el comportamiento de ambas implementaciones:

1. **Abre ambos Swagger** en pestañas diferentes del navegador
2. **Inserta los mismos datos** en ambos servidores
3. **Observa las diferencias** en las estadísticas (solo AVL tiene `/stats/tree`)
4. **Compara el rendimiento** con datos ordenados vs aleatorios

---

## ⚠️ Notas Importantes

- ✅ Ambos servidores usan **almacenamiento en memoria independiente**
- ✅ Los datos insertados en ABB **NO afectan** a AVL y viceversa
- ✅ Cada servidor tiene su **propia instancia** del árbol
- ✅ El modo `--reload` detecta cambios automáticamente
- ⚠️ Los datos se **pierden al reiniciar** el servidor (in-memory)

---

## 🎓 Casos de Uso Educativos

### Experimento 1: Datos Ordenados
1. Inserta documentos en orden: 1000, 2000, 3000, 4000, 5000
2. Compara la altura del árbol en ambos servidores
3. ABB: altura = 5 (lista enlazada)
4. AVL: altura = 3 (balanceado)

### Experimento 2: Datos Aleatorios
1. Inserta documentos aleatorios: 5000, 2000, 7000, 1000, 9000
2. Observa que ambos tienen rendimiento similar
3. ABB: puede estar balanceado por casualidad
4. AVL: siempre balanceado garantizado

### Experimento 3: Estadísticas
1. Usa el endpoint `/stats/tree` del AVL (puerto 8001)
2. Observa: altura, total de nodos, factor de balance
3. Compara con el comportamiento esperado del ABB

---

## 📚 Documentación Relacionada

- `README.md` - Documentación ABB
- `README_AVL.md` - Documentación AVL
- `ABB_VS_AVL.md` - Comparación detallada
- `PROYECTO_COMPLETO.md` - Documentación completa del proyecto

---

## ✨ ¡Listo para Usar!

Ambos servidores están configurados y listos. Abre los enlaces de Swagger y comienza a explorar las APIs.

**¡Disfruta comparando ABB vs AVL en tiempo real!** 🚀
