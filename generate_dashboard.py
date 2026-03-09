#!/usr/bin/env python3
# -*- coding: utf-8 -*-

html_content = '''<!DOCTYPE html>
<html lang="es">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>InnovaKit — Ecosistema IoT</title>
    <link rel="preconnect" href="https://fonts.googleapis.com">
    <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
    <link href="https://fonts.googleapis.com/css2?family=DM+Sans:opsz,wght@9..40,300;400;500;600;700&display=swap" rel="stylesheet">
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.4.0/css/all.min.css">
    <style>
        :root {
            --sky: #daeaf6;
            --panel-bg: rgba(10,16,12,0.97);
            --text: #F4F4F2;
            --muted: #8A9BA8;
            --line: rgba(255,255,255,0.08);
            --c1: #26C6DA;
            --c2: #F4B41A;
            --c3: #E53935;
            --c4: #4CAF50;
        }
        *, *::before, *::after { box-sizing: border-box; margin: 0; padding: 0; }
        html, body { width: 100%; height: 100%; font-family: 'DM Sans', sans-serif; background: var(--sky); color: var(--text); overflow: hidden; }
        .app { position: relative; width: 100vw; height: 100vh; display: flex; justify-content: center; align-items: center; background: var(--sky); }
        .map-wrapper { position: relative; width: min(100vw, calc(100vh * 16 / 9)); height: min(100vh, calc(100vw * 9 / 16)); background: var(--sky); overflow: hidden; }
        .farm-img { width: 100%; height: 100%; object-fit: contain; filter: brightness(0.92) contrast(1.04); }
        .overlay { display: none; position: fixed; inset: 0; background: rgba(0,0,0,0.5); z-index: 100; }
        .overlay.on { display: block; }
        .hotspot { position: absolute; width: 60px; height: 60px; border-radius: 50%; cursor: pointer; border: 2px solid rgba(255,255,255,0.6); display: flex; align-items: center; justify-content: center; z-index: 10; }
        .hotspot-inner { width: 24px; height: 24px; border-radius: 50%; background: white; }
        .popup { display: none; position: fixed; width: clamp(220px, 35vw, 320px); background: var(--panel-bg); border-radius: 12px; padding: 16px; z-index: 200; }
        .popup.show { display: block; }
        .device-card { padding: 12px 10px; margin-bottom: 8px; background: rgba(255,255,255,0.04); border-radius: 8px; cursor: pointer; font-weight: 600; }
        .panel { display: none; position: fixed; right: 0; top: 0; width: min(90vw, 420px); height: 100vh; background: var(--panel-color, var(--c1)); z-index: 300; overflow-y: auto; }
        .panel.on { display: flex; flex-direction: column; }
        .pd-header { display: flex; align-items: center; gap: 12px; padding: 16px; background: rgba(0,0,0,0.3); }
        .pd-icon { width: 40px; height: 40px; border-radius: 8px; background: rgba(0,0,0,0.4); display: flex; align-items: center; justify-content: center; font-size: 18px; }
        .pd-photo { width: 100%; height: 180px; object-fit: cover; border-radius: 8px; }
        .pd-desc { padding: 16px; font-size: 11px; line-height: 1.6; }
        .pd-dashboard { flex: 1; display: flex; flex-direction: column; padding: 16px; overflow-y: auto; }
        .dash-label { font-size: 10px; font-weight: 600; text-transform: uppercase; letter-spacing: 1px; margin-bottom: 12px; }
        .metrics-grid { display: grid; grid-template-columns: 1fr 1fr; gap: 8px; }
        .mc { padding: 10px; background: rgba(0,0,0,0.3); border: 1px solid rgba(255,255,255,0.12); border-radius: 8px; }
        .mc-label { font-size: 8.5px; font-weight: 600; text-transform: uppercase; }
        .mc-val { font-size: 21px; font-weight: 700; color: white; }
        .mc-note { font-size: 9px; color: rgba(255,255,255,0.5); }
        .mc-bar { width: 100%; height: 2px; background: rgba(255,255,255,0.15); border-radius: 1px; overflow: hidden; }
        .mc-bar-fill { height: 100%; background: rgba(255,255,255,0.8); }
        .mc.s-on { border-left: 3px solid #4ade80; background: rgba(74,222,128,0.08); }
        .mc.s-off { border-left: 3px solid #f87171; background: rgba(248,113,113,0.08); }
        .mc.s-pend { border-left: 3px solid #f59e0b; background: rgba(245,158,11,0.08); }
        .close-panel-btn { position: absolute; top: 12px; right: 12px; width: 28px; height: 28px; border: none; background: rgba(255,255,255,0.1); border-radius: 6px; cursor: pointer; color: white; }
    </style>
</head>
<body>
    <div class="app">
        <div class="map-wrapper" id="mapWrapper">
            <img src="./coffe_farm.jpg.png" class="farm-img" alt="Finca">
            <div style="position:absolute;inset:0;z-index:1;">
                <div class="hotspot" data-zone="gateway" style="left:29.72%;top:30.64%;"><div class="hotspot-inner"></div></div>
                <div class="hotspot" data-zone="marquesina" style="left:49.72%;top:32.56%;"><div class="hotspot-inner"></div></div>
                <div class="hotspot" data-zone="beneficio" style="left:47.07%;top:54.75%;"><div class="hotspot-inner"></div></div>
                <div class="hotspot" data-zone="clima" style="left:28.07%;top:62.76%;"><div class="hotspot-inner"></div></div>
            </div>
        </div>
        <div class="overlay" id="overlay"></div>
        <div class="popup" id="popup"></div>
        <div class="panel" id="panel">
            <button class="close-panel-btn" id="closeBtn">✕</button>
            <div id="panel-body"></div>
        </div>
    </div>

    <script>
        const DATA = {
            gateway: {
                color: 'var(--c1)',
                devices: [{
                    name: 'Gateway IoT',
                    img: './gatewat-iot.jpg.png',
                    icon: 'fa-tower-broadcast',
                    title: 'Gateway IoT',
                    sub: 'Hub central de comunicaciones',
                    desc: 'Centraliza los datos de todos los dispositivos de la finca. Sincroniza automáticamente con AWS y mantiene conexión 4G redundante.',
                    metrics: [
                        { icon: 'fa-cloud', label: 'AWS Sync', value: 'ACTIVO', unit: '', note: 'Última sync hace 12s', status: 'on' },
                        { icon: 'fa-signal', label: 'Señal 4G', value: '-87', unit: 'dBm', note: 'Cobertura buena', bar: 72 },
                        { icon: 'fa-wifi', label: 'WiFi Local', value: '5', unit: 'disp.', note: 'Conectados a red', bar: 100 },
                        { icon: 'fa-battery-half', label: 'Batería Backup', value: '92', unit: '%', note: 'Sistema redundante', bar: 92 },
                        { icon: 'fa-temperature-half', label: 'CPU Temp', value: '42', unit: '°C', note: 'Dentro de rango', bar: 55 },
                        { icon: 'fa-database', label: 'Almacenamiento', value: '68', unit: 'GB', note: '4 semanas guardadas', bar: 68 }
                    ]
                }]
            },
            marquesina: {
                color: 'var(--c2)',
                devices: [
                    {
                        name: 'Secafé',
                        img: './secafe.jpg.png',
                        icon: 'fa-fan',
                        title: 'Secadora Secafé',
                        sub: 'Sistema de secado solar',
                        desc: 'Sistema semi-automático de secado que utiliza paneles solares para deshumidificar el café.',
                        metrics: [
                            { icon: 'fa-thermometer', label: 'T° Interior', value: '34.5', unit: '°C', note: 'Óptima para secado', bar: 78 },
                            { icon: 'fa-droplet', label: 'Humedad', value: '42', unit: '%', note: 'Dentro de rango', bar: 60 },
                            { icon: 'fa-sun', label: 'Irradiancia', value: '892', unit: 'W/m²', note: 'Condiciones solares', bar: 85 },
                            { icon: 'fa-fan', label: 'Ventiladores', value: '3/3', unit: 'activos', note: 'Todos operando', status: 'on' },
                            { icon: 'fa-clock', label: 'Ciclo Actual', value: '4h 23m', unit: '', note: 'En progreso', bar: 65 }
                        ]
                    },
                    {
                        name: 'Sense Atmos',
                        img: './sense-atmos.jpg.png',
                        icon: 'fa-cloud-rain',
                        title: 'Sense Atmos',
                        sub: 'Estación meteorológica',
                        desc: 'Sensor ambiental multi-parámetro que mide condiciones del aire.',
                        metrics: [
                            { icon: 'fa-wind', label: 'Velocidad Viento', value: '8.3', unit: 'm/s', note: 'Brisa moderada', bar: 40 },
                            { icon: 'fa-compass', label: 'Dirección Viento', value: 'NE', unit: '', note: '45° desde norte', bar: 45 },
                            { icon: 'fa-droplet', label: 'Humedad Aire', value: '65', unit: '%', note: 'Equilibrio', bar: 65 },
                            { icon: 'fa-gauge', label: 'Presión', value: '970.5', unit: 'mb', note: 'Normal para alt.', bar: 70 },
                            { icon: 'fa-cloud', label: 'Cobertura Nubes', value: '40', unit: '%', note: 'Mayormente soleado', bar: 40 }
                        ]
                    }
                ]
            },
            beneficio: {
                color: 'var(--c3)',
                devices: [
                    {
                        name: 'Sense Flow',
                        img: './sense-flow.jpg.png',
                        icon: 'fa-water',
                        title: 'Sense Flow',
                        sub: 'Sistema de riego inteligente',
                        desc: 'Controla el flujo de agua para riego automático. Mide caudal, presión y ejecuta ciclos programados.',
                        metrics: [
                            { icon: 'fa-droplet', label: 'Caudal Actual', value: '24.5', unit: 'L/min', note: 'Riego activo', bar: 75 },
                            { icon: 'fa-gauge', label: 'Presión Sistema', value: '3.2', unit: 'bar', note: 'Dentro de límite', bar: 85 },
                            { icon: 'fa-check-circle', label: 'Válvula Principal', value: 'ABIERTA', unit: '', note: 'Funcionando', status: 'on' },
                            { icon: 'fa-water', label: 'Consumo Hoy', value: '2340', unit: 'L', note: '6 ciclos complete', bar: 58 },
                            { icon: 'fa-alarm', label: 'Sensor Suelo', value: '-45', unit: 'kPa', note: 'Humedad buena', bar: 72 }
                        ]
                    },
                    {
                        name: 'Válvula Solenoide',
                        img: './valvula.jpg.png',
                        icon: 'fa-valve',
                        title: 'Válvula Solenoide',
                        sub: 'Expansor de riego de 4 zonas',
                        desc: 'Distribuidora de agua con 4 salidas independientes.',
                        metrics: [
                            { icon: 'fa-pipe', label: 'Zona A', value: 'ACTIVA', unit: '', note: 'Cultivo norte', status: 'on' },
                            { icon: 'fa-pipe', label: 'Zona B', value: 'INACTIVA', unit: '', note: 'Espera programada', status: 'off' },
                            { icon: 'fa-pipe', label: 'Zona C', value: 'INACTIVA', unit: '', note: 'Espera programada', status: 'off' },
                            { icon: 'fa-pipe', label: 'Zona D', value: 'ACTIVA', unit: '', note: 'Cultivo sur', status: 'on' },
                            { icon: 'fa-wrench', label: 'Mantenimiento', value: 'OK', unit: '', note: 'Próx. en 45 días', status: 'on' }
                        ]
                    },
                    {
                        name: 'Atmos View',
                        img: './atmos-view.jpg.png',
                        icon: 'fa-eye',
                        title: 'Atmos View',
                        sub: 'Cámara con reconocimiento',
                        desc: 'Sistema de visión con IA para detectar plagas, enfermedades y maleza.',
                        metrics: [
                            { icon: 'fa-image', label: 'Imágenes Hoy', value: '18', unit: '', note: 'Todas procesadas', status: 'on' },
                            { icon: 'fa-leaf', label: 'Salud Cultivo', value: '94', unit: '%', note: 'Excelente estado', bar: 94 },
                            { icon: 'fa-bug', label: 'Plagas Detectadas', value: '2', unit: 'focos', note: 'Controladas', status: 'pend' },
                            { icon: 'fa-virus', label: 'Enfermedad', value: 'NEGATIVO', unit: '', note: 'No detectada', status: 'on' },
                            { icon: 'fa-battery-full', label: 'Batería Cámara', value: '87', unit: '%', note: 'Panel solar OK', bar: 87 }
                        ]
                    }
                ]
            },
            clima: {
                color: 'var(--c4)',
                devices: [{
                    name: 'Sense Weather',
                    img: './sense-weather.jpg.png',
                    icon: 'fa-cloud-sun',
                    title: 'Estación Sense Weather',
                    sub: 'Monitor completo del clima',
                    desc: 'Estación meteorológica profesional con 8 parámetros simultáneos.',
                    metrics: [
                        { icon: 'fa-thermometer', label: 'T° Ambiente', value: '28.3', unit: '°C', note: 'Cálido', bar: 82 },
                        { icon: 'fa-droplet', label: 'Humedad Relativa', value: '58', unit: '%', note: 'Equilibrio', bar: 58 },
                        { icon: 'fa-droplets', label: 'Rocío Nocturno', value: '18.5', unit: '°C', note: 'Normal para época', bar: 65 },
                        { icon: 'fa-sun', label: 'Radiación UV', value: '7.2', unit: 'UVI', note: 'Moderado', bar: 72 },
                        { icon: 'fa-cloud-rain', label: 'Lluvia 24h', value: '12.4', unit: 'mm', note: 'Buena precipitación', bar: 60 },
                        { icon: 'fa-wind', label: 'Ráfagas Máximas', value: '15.8', unit: 'm/s', note: 'Sin daño esperado', bar: 55 },
                        { icon: 'fa-gauge', label: 'Presión Barométrica', value: '1013.2', unit: 'mb', note: 'Estable', bar: 72 },
                        { icon: 'fa-battery-full', label: 'Estación', value: 'OPERATIVA', unit: '', note: 'Solar + batería', status: 'on' }
                    ]
                }]
            }
        };

        const overlay = document.getElementById('overlay');
        const popup = document.getElementById('popup');
        const panel = document.getElementById('panel');
        const pbody = document.getElementById('panel-body');
        const closeBtn = document.getElementById('closeBtn');
        const mapWrapper = document.getElementById('mapWrapper');
        const hotspots = document.querySelectorAll('.hotspot');

        hotspots.forEach(hotspot => {
            hotspot.addEventListener('click', (e) => openPopup(hotspot.dataset.zone, e));
        });

        overlay.addEventListener('click', closePopup);
        closeBtn.addEventListener('click', closePanel);

        function openPopup(zoneId, event) {
            event?.stopPropagation();
            const zone = DATA[zoneId];
            popup.innerHTML = zone.devices.map((dev, idx) => `
                <div class="device-card" onclick="openPanel('${zoneId}', ${idx}, event)">
                    <div>${dev.name}</div>
                    <div style="font-size:10px;color:var(--muted);margin-top:4px">${dev.metrics.length} métricas</div>
                </div>
            `).join('');
            
            popup.classList.add('show');
            overlay.classList.add('on');
            
            const rect = event.target.getBoundingClientRect();
            popup.style.left = (rect.left - popup.offsetWidth - 10) + 'px';
            popup.style.top = (rect.top - popup.offsetHeight / 2) + 'px';
        }

        function openPanel(zoneId, idx, e) {
            e?.stopPropagation();
            popup.classList.remove('show');
            const zone = DATA[zoneId];
            const device = zone.devices[idx];
            panel.style.setProperty('--panel-color', zone.color);

            const metricsHTML = device.metrics.map(m => {
                const isStatus = m.status !== undefined;
                const statusClass = isStatus ? `mc s-${m.status}` : 'mc';
                const barHTML = (!isStatus && m.bar > 0) 
                    ? `<div class="mc-bar"><div class="mc-bar-fill" style="width:${m.bar}%"></div></div>`
                    : '';
                
                return `
                    <div class="${statusClass}">
                        <div style="font-size:10px;"><i class="fa-solid ${m.icon}"></i> ${m.label}</div>
                        <div class="mc-val">${m.value}${m.unit ? `<span style="font-size:11px">${m.unit}</span>` : ''}</div>
                        ${m.note ? `<div class="mc-note">${m.note}</div>` : ''}
                        ${barHTML}
                    </div>
                `;
            }).join('');

            pbody.innerHTML = `
                <div class="pd-header">
                    <div class="pd-icon"><i class="fa-solid ${device.icon}"></i></div>
                    <div>
                        <div style="font-size:13px;font-weight:600;color:white">${device.title}</div>
                        <div style="font-size:11px;color:rgba(255,255,255,0.7);margin-top:2px">${device.sub}</div>
                    </div>
                </div>
                <div style="padding:16px;border-bottom:1px solid rgba(255,255,255,0.1);">
                    <img src="${device.img}" class="pd-photo" alt="${device.name}">
                </div>
                <div class="pd-desc">${device.desc}</div>
                <div class="pd-dashboard">
                    <div class="dash-label">Variables de medición</div>
                    <div class="metrics-grid">${metricsHTML}</div>
                </div>
            `;

            panel.classList.add('on');
            overlay.classList.add('on');
        }

        function closePopup() {
            popup.classList.remove('show');
            if (!panel.classList.contains('on')) overlay.classList.remove('on');
        }

        function closePanel() {
            panel.classList.remove('on');
            closePopup();
            overlay.classList.remove('on');
        }

        const resizeObserver = new ResizeObserver(() => {
            const rect = mapWrapper.getBoundingClientRect();
            hotspots.forEach(hotspot => {
                const leftPct = parseFloat(hotspot.style.left);
                const topPct = parseFloat(hotspot.style.top);
                hotspot.style.left = (leftPct / 100 * rect.width) + 'px';
                hotspot.style.top = (topPct / 100 * rect.height) + 'px';
            });
        });
        resizeObserver.observe(mapWrapper);
    </script>
</body>
</html>'''

# Write the file
with open('index.html', 'w', encoding='utf-8') as f:
    f.write(html_content)

print("✓ Dashboard HTML creado exitosamente en index.html")
