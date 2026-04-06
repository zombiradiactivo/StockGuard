# Security Audit Report: stockguard.py

## Vulnerabilidades Identificadas

| # | Vulnerabilidad | Severidad |
|---|----------------|-----------|
| 1 | Sin validación de entrada | Alta |
| 2 | Sin manejo de JSON corrupto | Alta |
| 3 | Valores negativos permitidos | Media |
| 4 | Sin codificación de archivo | Baja |
| 5 | Condición de carrera | Media |
| 6 | Sin mecanismo de respaldo | Baja |

---

## Descripción de Riesgos y Propuestas de Corrección

### 1. Sin validación de entrada (Alta)

**Ubicación:** Líneas 17-19, 22-27

**Descripción:** Las funciones `add_item` y `update_price` no validan los parámetros recibidos. Un atacante podría pasar tipos de datos incorrectos o valores maliciosos.

**Propuesta:**
```python
def add_item(name, qty, price):
    if not isinstance(name, str) or not name.strip():
        raise ValueError("El nombre debe ser una cadena no vacía")
    if not isinstance(qty, int) or qty <= 0:
        raise ValueError("La cantidad debe ser un entero positivo")
    if not isinstance(price, (int, float)) or price < 0:
        raise ValueError("El precio debe ser un número no negativo")
    # ...
```

### 2. Sin manejo de JSON corrupto (Alta)

**Ubicación:** Línea 11

**Descripción:** Si el archivo `inventory.json` está corrupto, `json.load()` lanzara una excepción no manejada que puede bloquear la aplicación.

**Propuesta:**
```python
def load_inventory():
    if not os.path.exists(INVENTORY_FILE):
        return []
    try:
        with open(INVENTARIO_FILE, encoding='utf-8') as f:
            data = json.load(f)
            return list(data) if isinstance(data, list) else []
    except (json.JSONDecodeError, IOError):
        return []
```

### 3. Valores negativos permitidos (Media)

**Ubicación:** Líneas 20, 26

**Descripción:** Permite valores negativos para `qty` y `price`, lo cual es lógicamente inválido y podría ser explotado para manipulaciones financieras.

**Propuesta:** Agregar validación en `add_item` y `update_price` (ver propuesta #1).

### 4. Sin codificación de archivo (Baja)

**Ubicación:** Líneas 10, 14

**Descripción:** `open()` sin parámetro `encoding` puede causar problemas de compatibilidad entre plataformas.

**Propuesta:** Especificar `encoding='utf-8'` en todas las operaciones de archivo.

### 5. Condición de carrera (Media)

**Ubicación:** Líneas 18-20, 23-27

**Descripción:** Entre `load_inventory()` y `save_inventory()` hay una ventana donde otro proceso podría modificar el archivo, causando pérdida de datos.

**Propuesta:** Usar bloqueo de archivo:
```python
import fcntl

def save_inventory(items):
    with open(INVENTORY_FILE, 'a+') as f:
        fcntl.flock(f.fileno(), fcntl.LOCK_EX)
        f.seek(0)
        f.truncate()
        json.dump(items, f)
        fcntl.flock(f.fileno(), fcntl.LOCK_UN)
```

### 6. Sin mecanismo de respaldo (Baja)

**Descripción:** Si ocurre un error durante `save_inventory()`, los datos existentes podrían perderse.

**Propuesta:** Implementar escritura atómica:
```python
def save_inventory(items):
    temp_file = INVENTORY_FILE + '.tmp'
    with open(temp_file, 'w', encoding='utf-8') as f:
        json.dump(items, f)
    os.replace(temp_file, INVENTORY_FILE)
```
