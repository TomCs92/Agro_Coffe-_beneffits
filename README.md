# ☕ InnovaKit × Sense AI — Visualizador Ecosistema IoT Finca Cafetera

> **Dashboard isométrico interactivo** que visualiza el ecosistema de tecnología IoT de **InnovaKit** aplicado a una finca cafetera sostenible: desde el monitoreo climático hasta la restauración ecológica.
>
> *Una herramienta comercial y educativa para presentar soluciones inteligentes a caficultores.*

[![Versión](https://img.shields.io/badge/Versión-3.0-00A4EF?style=for-the-badge)](./)
[![Tecnología](https://img.shields.io/badge/Tech-HTML5%20%7C%20CSS3%20%7C%20ES6-blue?style=for-the-badge)](https://developer.mozilla.org/es/)
[![Estado](https://img.shields.io/badge/Estado-Producción-success?style=for-the-badge)](./)
[![Zonas](https://img.shields.io/badge/Zonas%20IoT-11-orange?style=for-the-badge)](./)

---

## 📸 Vista Previa

![Dashboard Ecosistema Finca Cafetera](Beneficios%20del%20cafe.png)

**Características principales:**
- 🎯 **11 zonas interactivas** con hotspots pulsantes y código de color único
- 📱 **Panel lateral dinámico** con foto + descripción + métricas por dispositivo
- 🐦 **Biomonitoreo** — Cámaras trampa + sensor acústico para fauna y avifauna
- 🌱 **Restauración forestal** — Dendrometría digital + monitoreo aéreo con drones
- 💧 **Calidad del agua** — Sensores multiparámetro en el proceso de beneficio
- 🔥 **Seguridad en biodigestor** — Detección de metano y gases del proceso
- 📲 **100% responsivo** (desktop, tablet, móvil — landscape)
- ⚡ **Sin dependencias externas** — HTML5 + CSS3 + Vanilla JS puro

---

## 🗺️ Las 11 Zonas del Ecosistema

| # | Zona | Color | Dispositivos | Propósito |
|---|------|-------|-------------|-----------|
| 1 | **🏗️ Gateway** | Cyan | Gateway IoT + Starlink | Conectividad LTE/LoRa y sincronización con nube |
| 2 | **☀️ Marquesina** | Dorado | Secafé + Sense Atmos | Temperatura, humedad y ventilación del secadero |
| 3 | **💧 Beneficio** | Rojo | Sense Flow + Válvula + Atmos View | Control de agua, fermentación y lavado |
| 4 | **🌦️ Est. Clima** | Verde | Sense Weather | Microclima, viento, lluvia, radiación solar |
| 5 | **🌿 Restauración** | Esmeralda | Dendrómetros + Drone | Crecimiento forestal y monitoreo aéreo |
| 6 | **🔥 Biodigestor** | Naranja | Sensor de Gases | Metano (CH₄), presión y seguridad del proceso |
| 7 | **🚰 Bocatoma** | Azul | Sensores Calidad Agua | Turbidez, pH, conductividad y oxígeno disuelto |
| 8 | **🦅 Conservación** | Turquesa | Cámara Trampa + Sensor Acústico | Fauna silvestre e identificación de aves por canto |
| 9 | **♻️ Compostaje** | Café/Tierra | Báscula Inteligente + Sense Atmos | Peso y temperatura de pilas de compostaje |
| 10 | **🏭 Bodega** | Amarillo-verde | Atmos View + Sensor Puerta | Condiciones internas y control de acceso |
| 11 | **🍃 Bodega café** | — | — | Zona de almacenamiento de grano |

---

## 📁 Estructura del Proyecto

```
Agro_Coffe-_beneffits/
│
├── index.html                    # 🚀 App completa (HTML + CSS + JS en un archivo)
├── hotspot-editor.html           # 🛠️ Herramienta visual para ajustar posición de hotspots
│
├── Beneficios del cafe.png       # Imagen isométrica principal (fondo del mapa)
├── Ecosistema beneficio cafe IoT.png  # Versión alternativa / materiales de presentación
├── finca-isometrica.jpg          # Imagen de referencia anterior
│
├── gatewat-iot.jpg.png           # Foto dispositivo — Gateway IoT
├── secafe.jpg.png                # Foto dispositivo — Secafé
├── sense-atmos.jpg.png           # Foto dispositivo — Sense Atmos
├── sense-flow.jpg.png            # Foto dispositivo — Sense Flow
├── sense-atmos-view.jpg.png      # Foto dispositivo — Atmos View
├── sense-weather.jpg.png         # Foto dispositivo — Sense Weather
│
├── generate_dashboard.py         # 🐍 Script generador de versiones del dashboard
├── README.md                     # 📖 Documentación (este archivo)
└── .gitignore                    # Configuración de Git
```

---

## 🚀 Cómo Usar

### 📖 Flujo de usuario
1. **Abre `index.html`** en tu navegador
2. **Observa el mapa isométrico** — 11 puntos pulsantes representan cada zona IoT
3. **Haz clic en un hotspot** o en un **pill de navegación** (barra inferior)
4. Se abre un **popup flotante** con los dispositivos de esa zona
5. Selecciona un dispositivo para ver el **panel lateral** con:
   - 📷 Foto del dispositivo
   - 📝 Descripción del equipo y su función
   - 📊 Grid de métricas en tiempo real (valores, barras, estados)

### 💻 Ver Localmente
```bash
# Clona el repo
git clone https://github.com/TomCs92/Agro_Coffe-_beneffits.git
cd Agro_Coffe-_beneffits

# Windows — abrir directamente
start index.html

# macOS
open index.html

# Linux
xdg-open index.html
```

> ℹ️ **No requiere servidor ni instalación** — funciona 100% en el navegador

### 🛠️ Editor de Hotspots
Para ajustar posiciones de puntos de interés visualmente, abre `hotspot-editor.html` en el navegador. Permite arrastrar los hotspots y copiar las coordenadas resultantes.

---

## 🏗️ Cómo Funciona

### Flujo de interacción

```
Usuario toca hotspot o pill
    ↓
openPopup(zoneId) → Popup flotante con tarjetas de dispositivos
    ↓
Click en dispositivo (dev-card)
    ↓
openPanel(zoneId, index) → Panel lateral animado con:
    - Header: ícono + nombre + badge Online
    - Foto del dispositivo
    - Descripción técnica
    - Grid de métricas (2 columnas por defecto)
    ↓
closePanel() → Cierra panel con animación
```

### Posicionamiento de hotspots

Los hotspots usan **coordenadas relativas a la imagen**, no al viewport. Esto garantiza precisión sin importar el tamaño de pantalla:

```html
<div class="hotspot"
     data-zone="gateway"
     data-rel-top="24.41"     <!-- % del alto de la imagen renderizada -->
     data-rel-left="31.29"    <!-- % del ancho de la imagen renderizada -->
     onclick="openPopup('gateway', event)">
```

Un `ResizeObserver` recalcula las posiciones en píxeles en cada cambio de tamaño.

### Estructura de datos

```javascript
const DATA = {
    gateway: {
        color: 'var(--c1)',
        devices: [{
            name: 'Gateway IoT',
            img: './gatewat-iot.jpg.png',
            icon: 'fa-tower-broadcast',
            title: 'Gateway IoT',
            sub: 'Infraestructura de comunicaciones',
            desc: 'Descripción del dispositivo...',
            metrics: [
                { icon: 'fa-cloud', label: 'AWS Sync', value: 'ACTIVO', status: 'on' },
                { icon: 'fa-signal', label: 'Señal 4G', value: '–87', unit: 'dBm', bar: 72 },
                // ...
            ]
        }]
    },
    // ... 10 zonas más
}
```

### Tipos de métricas

```javascript
// Valor con barra de progreso
{ icon: 'fa-droplet', label: 'Humedad', value: '72', unit: '%', bar: 72 }

// Estado ON / OFF / PENDIENTE
{ icon: 'fa-wifi', label: 'WiFi', value: 'ACTIVO', status: 'on' }

// Valor con nota descriptiva
{ icon: 'fa-clock', label: 'Próximo vuelo', value: '06:30', note: 'Mañana' }
```

---

## 🛠️ Stack Tecnológico

| Capa | Tecnología | Uso |
|------|-----------|-----|
| **Estructura** | HTML5 | Semántica, atributos `data-*`, accesibilidad |
| **Estilos** | CSS3 Vanilla | Variables CSS, Flexbox, Grid, `backdrop-filter`, animaciones |
| **Lógica** | JavaScript ES6 | Arrow functions, template literals, `ResizeObserver` |
| **Tipografía** | DM Sans (Google Fonts) | UI moderna y legible |
| **Iconos** | Font Awesome 6.4 | Iconografía temática por dispositivo y métrica |
| **Imágenes** | PNG / JPG | Fondo isométrico y fotos de dispositivos |

**Sin frameworks — Sin npm — Sin build step**

---

## 🎨 Colores del Sistema

```css
:root {
    --c1:  #26C6DA;   /* Gateway       — Cyan          */
    --c2:  #F4B41A;   /* Marquesina    — Dorado        */
    --c3:  #E53935;   /* Beneficio     — Rojo          */
    --c4:  #4CAF50;   /* Clima         — Verde         */
    --c5:  #9B59B6;   /* Drone (legacy)— Violeta       */
    --c6:  #27AE60;   /* Restauración  — Esmeralda     */
    --c7:  #E67E22;   /* Biodigestor   — Naranja       */
    --c8:  #2980B9;   /* Bocatoma      — Azul          */
    --c9:  #1ABC9C;   /* Conservación  — Turquesa      */
    --c10: #C0892B;   /* Compostaje    — Café/Tierra   */
    --c11: #BDC81E;   /* Bodega        — Amarillo-verde */
}
```

---

## 🌐 Despliegue en GitHub Pages

1. Asegúrate de que `index.html` esté en la raíz del repositorio
2. Ve a **Settings → Pages** en GitHub
3. Selecciona branch `main` y carpeta `/ (root)`
4. En ~1 minuto obtendrás la URL pública:
   ```
   https://TomCs92.github.io/Agro_Coffe-_beneffits/
   ```

---

## 🚀 Roadmap

- [ ] Conexión a API real de sensores (ThingsBoard / Ubidots / AWS IoT)
- [ ] Histórico de métricas con gráficas (Chart.js)
- [ ] Alertas push al superar umbrales configurables
- [ ] Exportación de reportes en PDF
- [ ] Modo PWA — instalable en móvil como app nativa
- [ ] Soporte multiidioma (ES / EN)

---

## 👥 Créditos

| Rol | Responsable |
|-----|-------------|
| **Concepto & Productos IoT** | InnovaKit |
| **Plataforma & Visualización** | Sense AI |
| **Diseño Isométrico** | Equipo Creativo InnovaKit |
| **Desarrollo Frontend** | TomCS92 |

---

## 📄 Licencia

**Propiedad Intelectual:** Este dashboard y el ecosistema de InnovaKit son propiedad de **InnovaKit × Sense AI**. Todos los derechos reservados © 2024–2026.

**Uso permitido:** Demostración comercial a clientes · Modificación interna · Despliegue en servidores propios

**Uso no permitido:** Redistribución pública sin autorización · Comercialización como producto propio · Remoción de atribuciones

---

<p align="center">
  <strong>☕ Hecho con pasión para el café colombiano</strong><br>
  <sub>InnovaKit × Sense AI — 2024–2026</sub>
</p>
