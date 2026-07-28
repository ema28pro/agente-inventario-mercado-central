# Ejemplos de Preguntas y Respuestas del Agente de Inventario

A continuación se presentan los ejemplos de consultas reales probadas sobre el dataset de `inventario.xlsx` de Mercado Central 24h mediante el agente Pandas + Gemini.

---

## 1. Total de Productos
**Pregunta:** ¿Cuántos productos hay en total en el inventario?  
**Respuesta del agente:**
```
El inventario cuenta con un total de 200 productos registrados en la base de datos de Mercado Central 24h.
```

---

## 2. Producto con Mayor Stock
**Pregunta:** ¿Cuál es el producto con mayor stock actual?  
**Respuesta del agente:**
```
El producto con mayor stock actual en el inventario es 'Cerveza Clara Lata 355ml', con un stock disponible de 500 unidades.
```

---

## 3. Productos por Debajo de Stock Mínimo
**Pregunta:** ¿Qué productos están por debajo de su stock mínimo?  
**Respuesta del agente:**
```
Actualmente no hay productos cuyo stock actual sea menor que su stock mínimo requerido. Todos los productos se encuentran con niveles de stock adecuados.
```

---

## 4. Precio Promedio por Categoría
**Pregunta:** ¿Cuál es el precio promedio de los productos de la categoría Lácteos?  
**Respuesta del agente:**
```
El precio de venta promedio para los productos pertenecientes a la categoría Lácteos es de $13.00.
```

---

## 5. Producto con Mayor Margen de Ganancia
**Pregunta:** ¿Qué producto tiene el margen de ganancia más alto (Precio de Venta Unitario − Costo Unitario)?  
**Respuesta del agente:**
```
El producto con el mayor margen de ganancia es 'Queso Oaxaca / Mozzarella Trozo', con un margen de ganancia de $34.90 por unidad (Precio de Venta: $89.90, Costo Unitario: $55.00).
```

---

## 6. Proveedores Distintos
**Pregunta:** ¿Cuántos proveedores distintos abastecen el inventario?  
**Respuesta del agente:**
```
El inventario del supermercado es abastecido por un total de 92 proveedores distintos.
```

---

## 7. Próximos Vencimientos
**Pregunta:** ¿Qué productos vencen antes de una fecha determinada (ejemplo: 2027-01-01)?  
**Respuesta del agente:**
```
Las fechas de vencimiento del inventario varían entre junio de 2026 y mayo de 2031. Para la fecha límite del 01/01/2027, los productos próximos a vencer son aquellos cuyos lotes vencen entre junio y diciembre de 2026.
```

---

## 8. Proveedor Principal con Más Productos
**Pregunta:** ¿Cuál es el proveedor con más productos suministrados?  
**Respuesta del agente:**
```
El proveedor que suministra la mayor cantidad de productos al inventario es Sigma Alimentos, abasteciendo un total de 15 productos distintos.
```
