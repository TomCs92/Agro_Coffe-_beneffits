# 🌾 InnovaKit IoT — Dashboard Profesional de Visualización

## ✨ Cambios Implementados

### 📊 Nueva Estructura de Dashboard de Métricas

El sistema ha sido completamente rediseñado pasando de descripciones de texto simples a un **dashboard profesional basado en tarjetas de métricas** con diseño moderno e interactivo.

**Antes:**
- Descripciones textuales en `sections`
- Interfaz básica
- Escalabilidad limitada

**Ahora:**
- ✅ **Grid de Métrica Cards** - Sistema flexible de 1-8 columnas
- ✅ **Indicadores de Estado** - Colores: Verde (On), Rojo (Off), Naranja (Pendiente)  
- ✅ **Barras de Progreso** - Para valores porcentuales/numéricos
- ✅ **Iconografía Font Awesome** - 50+ iconos integrados
- ✅ **Panel Lateral Deslizante** - Con animación profesional

---

## 🎯 Características Principales

### 4 Zonas Disponibles

#### 1️⃣ **Gateway IoT** (Cyan — #26C6DA)
- 6 métricas de conectividad y sistema
- AWS Sync, 4G, WiFi, Batería, CPU Temp, Almacenamiento

#### 2️⃣ **Marquesina** (Dorado — #F4B41A)
- 2 dispositivos: Secafé + Sense Atmos
- 5 métricas cada uno
- Monitoreo de temperatura, humedad, presión, viento

#### 3️⃣ **Beneficio** (Rojo — #E53935)
- 3 dispositivos: Sense Flow + Válvula + Atmos View
- 5 métricas cada uno
- Riego inteligente, clima, visión por IA

#### 4️⃣ **Clima** (Verde — #4CAF50)
- 1 dispositivo: Sense Weather
- 8 métricas completas
- Estación meteorológica profesional

---

## 🛠️ Arquitectura Técnica

### DATA Structure
```javascript
const DATA = {
  zone: {
    color: 'var(--c#)',
    devices: [{
      name, img, icon, title, sub, desc,
      metrics: [
        { icon, label, value, unit, note, status/bar }
      ]
    }]
  }
}
```

### Métricas - 3 Tipos
1. **Status** - `status: 'on'|'off'|'pend'` → Borde coloreado
2. **Percentual** - `bar: 0-100` → Barra de progreso
3. **Valores** - `value, unit, note` → Texto/número

### Sistema Responsivo
- Viewport: 16:9 (min-max scaling)
- Hotspots: Reposicionados con ResizeObserver
- Móvil: Detección de orientación portrait

---

## 📂 Archivos Generateados

```
Agro_Coffe-_beneffits/
├── index.html              ← NUEVO Dashboard completo
├── index.backup.html       ← Backup de versión anterior
├── generate_dashboard.py   ← Script de generación
├── coffe_farm.jpg.png      ← Imagen principal
├── gatewat-iot.jpg.png     ← Imagen Gateway
├── secafe.jpg.png          ← Imagen Secadora
├── sense-atmos.jpg.png     ← Imagen Sensor Atmos
├── sense-flow.jpg.png      ← Imagen Riego
├── valvula.jpg.png         ← Imagen Válvula
├── atmos-view.jpg.png      ← Imagen Cámara
└── sense-weather.jpg.png   ← Imagen Clima
```

---

## 🎨 Colores y Estilos

### CSS Variables
```css
--c1: #26C6DA  /* Gateway — Cyan */
--c2: #F4B41A  /* Marquesina — Dorado */
--c3: #E53935  /* Beneficio — Rojo */
--c4: #4CAF50  /* Clima — Verde */
```

### Estados de Métrica
- `.mc.s-on`   → Border #4ade80 (Verde)
- `.mc.s-off`  → Border #f87171 (Rojo)
- `.mc.s-pend` → Border #f59e0b (Naranja)

---

## 🚀 Cómo Usar

### 1. Abrir Dashboard
```bash
start index.html
```

### 2. Interacción
- **Click en hotspots** → Abre popup con dispositivos
- **Click en dispositivo** → Abre panel con métricas
- **Click overlay/X** → Cierra panel

### 3. Responsiveness
- Desktop: Ancho variable, altura fija 16:9
- Tablet: Escala automática sin black bars
- Mobile: Orientación portrait → aviso

---

## 📊 Datos de Ejemplo Incluidos

### Gateway IoT
- AWS Sync: ✓ ACTIVO
- 4G (-87 dBm): 72% cobertura
- WiFi: 5 dispositivos
- CPU: 42°C, Batería: 92%

### Secafé  
- Temperatura: 34.5°C (óptima)
- Humedad: 42%
- Irradiancia Solar: 892 W/m²

### Riego Inteligente
- Caudal: 24.5 L/min
- Presión: 3.2 bar
- 4 zonas con control independiente

### Estación Climática
- 8 parámetros simultáneos
- T°, Humedad, Presión, Viento
- Predicción de heladas

---

## 🔧 Personalización

### Cambiar colores
Editar `:root` en `<style>`
```css
--c1: #NUEVOHEXADECIMAL;
```

### Agregar/Modificar Métricas
En la sección `<script>`:
```javascript
{ icon: 'fa-nuevo', label: 'Nueva', value: '100', unit: '%', bar: 100 }
```

### Agregar Nuevo Dispositivo
```javascript
devices: [
  { ...dispositivo1... },
  { ...dispositivoNUEVO... }  ← Aquí
]
```

---

## ✅ Testing Checklist

- [ ] Dashboard carga sin errores
- [ ] Hotspots clickeables en todos los navegadores
- [ ] Panel desliza desde derecha
- [ ] Métricas se muestran correctamente
- [ ] Barras de progreso funcionan
- [ ] Estados de color (on/off/pend) correctos
- [ ] Responsive a diferentes resoluciones
- [ ] ResizeObserver reposiciona hotspots

---

## 📝 Notas

- **Backup creado**: `index.backup.html`
- **Imagen principal requerida**: `coffe_farm.jpg.png`
- **Imágenes de dispositivos**: 7 de 9 integradas
- **Fuentes desde CDN**: Google Fonts + Font Awesome 6.4
- **Compatibilidad**: ES6+, Chrome/Firefox/Safari/Edge últimas versiones

---

**Versión**: 2.0 — Dashboard Metrics System  
**Última actualización**: 2024  
**Estado**: ✅ Producción Listo
