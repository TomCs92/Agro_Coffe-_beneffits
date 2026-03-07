# ☕ InnovaKit — Ecosistema Finca Cafetera IoT

> **Dashboard interactivo** que visualiza el ecosistema de tecnología IoT aplicado al proceso productivo del café, desde el beneficio hasta el secado.

[![GitHub Pages](https://img.shields.io/badge/Live%20Demo-GitHub%20Pages-brightgreen?style=for-the-badge&logo=github)](https://tu-usuario.github.io/Aggro_Coffe_beneffits/Dashboard_Coffe.html)
[![Tecnología](https://img.shields.io/badge/Tech-HTML%20%7C%20CSS%20%7C%20JS-blue?style=for-the-badge)](https://developer.mozilla.org/es/)
[![Licencia](https://img.shields.io/badge/Licencia-MIT-yellow?style=for-the-badge)](./LICENSE)

---

## 📸 Vista Previa

![Dashboard Ecosistema Finca Cafetera](Ecosistema%20beneficio%20cafe%20IoT.png)

---

## 🎯 ¿Qué es esto?

Una **aplicación web de una sola página** (`Dashboard_Coffe.html`) que sirve como herramienta comercial y educativa para presentar el ecosistema IoT de **InnovaKit** a caficultores y clientes. 

Cuando el usuario toca/hace clic en cualquier zona del mapa isométrico de la finca, se despliega un panel lateral con información detallada del dispositivo o sensor instalado en esa área.

### Zonas del Ecosistema

| Zona | Color | Dispositivo | Función |
|------|-------|------------|---------|
| 📡 **Gateway** | Turquesa | Gateway LoRaWAN + 4G | Centraliza todos los datos y los envía a la nube |
| ☀️ **Secafé** | Dorado | Secadero + Ventilador IoT | Control de temperatura, humedad y peso del grano |
| 🌦️ **Clima** | Verde | Estación Meteorológica | Monitoreo del microclima real de la finca |
| ⚙️ **Beneficio** | Rojo | Sensores + Caudalímetros + Válvulas | Control de fermentación, lavado y uso de agua |

---

## 🚀 Cómo usar

### Opción 1 — Ver en vivo (sin instalación)
Haz clic en el badge **Live Demo** de arriba ↑ o abre la URL de GitHub Pages del repositorio.

### Opción 2 — Ver localmente
1. Clona el repositorio:
   ```bash
   git clone https://github.com/tu-usuario/Aggro_Coffe_beneffits.git
   ```
2. Abre la carpeta descargada.
3. Haz **doble clic** en `Dashboard_Coffe.html`.  
   *(No necesitas servidor ni instalar nada — funciona directamente en el navegador)*

---

## 📁 Estructura del Proyecto

```
Aggro_Coffe_beneffits/
│
├── Dashboard_Coffe.html           # App completa (HTML + CSS + JS en un solo archivo)
├── Ecosistema beneficio cafe IoT.png  # Imagen isométrica de la finca (fondo del dashboard)
└── README.md                      # Este archivo
```

> **Diseño intencional de archivo único:** Toda la aplicación vive en `Dashboard_Coffe.html` para facilitar su distribución, alojamiento en GitHub Pages y uso sin servidor.

---

## 🏗️ Arquitectura del Código

El archivo `Dashboard_Coffe.html` está organizado en 3 bloques principales:

### 1. `<style>` — Diseño Visual (CSS)
Dividido en 6 secciones claramente comentadas:

```
1. Variables Globales (:root)    → Colores y tokens de diseño centralizados
2. Imagen de Fondo               → Cubre 100% de la pantalla como canvas
3. Barras de Navegación          → Top bar (logo) + Bottom bar (pills de zona)
4. Hotspots                      → Puntos interactivos pulsantes sobre la imagen
5. Panel Lateral                 → Drawer deslizable con info de cada zona
6. Media Queries                 → Adaptación a móviles y tablets
```

### 2. `<body>` — Estructura HTML
```
app-container
├── farm-image          (imagen de fondo)
├── top-bar             (logo + instrucción)
├── hotspot ×4          (Gateway, Secafé, Clima, Beneficio)
├── bottom-bar          (4 nav-pills)
├── side-panel-overlay  (fondo oscuro al abrir panel)
└── side-panel          (drawer con contenido dinámico)
```

### 3. `<script>` — Lógica JavaScript
```javascript
ecosistemaData    // Base de datos: info de las 4 zonas
openPanel(id)     // Construye e inyecta HTML del panel, activa animación
closePanel()      // Cierra panel y overlay
```

---

## 🎨 Personalización

### Cambiar colores de zona
En `:root` al inicio del CSS:
```css
--z1-color: #1ABC9C;  /* Gateway: turquesa */
--z2-color: #D4A017;  /* Secafé: dorado */
--z3-color: #27AE60;  /* Clima: verde */
--z4-color: #C0392B;  /* Beneficio: rojo */
```

### Mover un hotspot
Busca el `<div class="hotspot">` correspondiente y edita `top` y `left`:
```html
<div class="hotspot" id="hs-gateway" style="top: 15%; left: 18%;" ...>
```
Los valores son porcentajes del tamaño de la pantalla. Ajusta hasta que el punto quede sobre su zona en la imagen.

### Editar texto de una zona
En el objeto `ecosistemaData` dentro del `<script>`, cada zona tiene:
```javascript
gateway: {
    title: "Gateway LoRaWAN + 4G",    // Título del panel
    subtitle: "El cerebro...",         // Subtítulo
    sections: [                        // Array de secciones de contenido
        { label: "¿Qué hace?", content: "<p>...</p>" },
        ...
    ],
    valueBox: "✅ Beneficio 1<br>✅ Beneficio 2",  // Caja de valor
    price: "Precio referencia: $XXX COP"            // Precio
}
```

### Agregar una nueva zona
1. Añade un nuevo `<div class="hotspot">` en el HTML con un ID único.
2. Agrega una entrada nueva en `ecosistemaData` con el mismo ID.
3. Añade una nueva `nav-pill` en el `bottom-bar`.
4. Define el color `--currentzona-color` en `:root`.

### Cambiar la imagen de fondo
Reemplaza el archivo `Ecosistema beneficio cafe IoT.png` con tu nueva imagen (mismo nombre) **o** edita el `src` en el HTML:
```html
<img id="main-farm-image" class="farm-image" src="tu-nueva-imagen.png" ...>
```

---

## 🌐 Despliegue en GitHub Pages

1. Ve a **Settings** → **Pages** en tu repositorio de GitHub.
2. En *Branch*, selecciona `main` y carpeta `/ (root)`.
3. Guarda. En ~1 minuto tendrás una URL pública tipo:
   ```
   https://tu-usuario.github.io/Aggro_Coffe_beneffits/Dashboard_Coffe.html
   ```
4. *(Opcional)* Conecta un dominio propio en la misma sección "Pages" → "Custom domain".

---

## 🔧 Tecnologías Utilizadas

| Tecnología | Uso |
|-----------|-----|
| **HTML5** | Estructura semántica de la app |
| **CSS3** | Variables, animaciones, flexbox, backdrop-filter, media queries |
| **JavaScript (Vanilla)** | Lógica de apertura/cierre de panel e inyección dinámica de contenido |
| **Google Fonts** | Tipografía DM Sans (cuerpo) + Georgia nativa (títulos) |

> **Sin dependencias externas** (excepto Google Fonts para tipografía). No requiere Node.js, npm, ni ningún framework.

---

## 📋 Roadmap / Mejoras Futuras

- [ ] Conectar con API real de sensores IoT (ThingsBoard, Ubidots, AWS IoT)
- [ ] Agregar gráficas de histórico de datos por zona
- [ ] Modo multilingüe (ES / EN)
- [ ] Pantalla de login para clientes con su propia finca
- [ ] Versión PWA (instalable desde el navegador en móvil)

---

## 👥 Créditos

| Rol | Nombre |
|-----|--------|
| **Diseño de Ecosistema IoT** | InnovaKit |
| **Tecnología & Plataforma** | Sense AI |
| **Imagen Isométrica** | Ecosistema beneficio cafe IoT |

---

## 📄 Licencia

Este proyecto es propiedad de **InnovaKit × Sense AI**. Todos los derechos reservados.  
Para uso comercial o distribución, contactar al equipo de InnovaKit.

---

<p align="center">
  <strong>☕ Hecho con pasión por el café colombiano</strong><br>
  <em>InnovaKit — Tecnología por Sense AI</em>
</p>
