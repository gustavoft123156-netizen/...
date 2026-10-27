<!DOCTYPE html>
<html lang="es">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<meta name="theme-color" content="#101510">
<title>TITAN FIT LAB | Centro de Alto Rendimiento</title>
<style>
:root{--bg:#0b0e0b;--panel:#151b15;--panel2:#1d261d;--green:#b7ff35;--text:#f4f7f1;--muted:#b7c0b3;--line:#303a2d}
*{box-sizing:border-box;scroll-behavior:smooth}
body{margin:0;background:var(--bg);color:var(--text);font-family:Arial,Helvetica,sans-serif;line-height:1.6}
a{color:inherit;text-decoration:none}
header{padding:42px 20px 35px;text-align:center;background:radial-gradient(ellipse at top,#273c1d 0%,#101510 65%);border-bottom:1px solid var(--line)}
.logo{font-size:clamp(2rem,5vw,3.4rem);font-weight:900;letter-spacing:2px;color:var(--green)}
.slogan{margin:3px 0;color:var(--muted);letter-spacing:3px;text-transform:uppercase;font-size:.85rem}
nav{position:sticky;top:0;z-index:10;background:#0b0e0bed;backdrop-filter:blur(12px);border-bottom:1px solid var(--line)}
nav ul{list-style:none;display:flex;gap:8px;justify-content:center;flex-wrap:wrap;margin:0;padding:12px}
nav a{display:block;padding:8px 13px;border-radius:7px;font-weight:bold;font-size:.92rem}
nav a:hover{background:var(--green);color:#101510}
main{max-width:1150px;margin:auto;padding:24px 18px 50px}
section{scroll-margin-top:85px}
.card{background:var(--panel);border:1px solid var(--line);border-radius:18px;padding:clamp(20px,4vw,36px);margin:22px 0;box-shadow:0 12px 35px #0003}
h2{margin:0 0 18px;color:var(--green);font-size:clamp(1.45rem,3vw,2rem);line-height:1.2}
h3{margin-top:0}
.hero{display:grid;grid-template-columns:1.1fr .9fr;gap:25px;align-items:center}
.hero h2{font-size:clamp(2rem,4vw,3.2rem)}
.hero p{color:var(--muted);font-size:1.08rem}
.hero-visual{position:relative;border-radius:14px;overflow:hidden;border:1px solid #47652c;min-height:300px}
.hero-visual img{width:100%;height:100%;object-fit:cover;display:block}
.hero-overlay{position:absolute;inset:0;background:linear-gradient(to top, rgba(11,14,11,0.9), transparent);display:flex;flex-direction:column;justify-content:flex-end;padding:20px;text-align:center}
.hero-overlay strong{color:var(--green);font-size:1.4rem}
.btn,button{background:var(--green);color:#101510;border:0;border-radius:8px;padding:12px 17px;font-weight:800;cursor:pointer;transition:.2s;display:inline-block}
.btn:hover,button:hover{transform:translateY(-2px);filter:brightness(1.08)}
.btn-sec{background:transparent;color:var(--green);border:1px solid var(--green);margin-left:7px}
.grid-servicios,.grid-planes,.grid-trainers,.grid-beneficios{display:grid;grid-template-columns:repeat(4,1fr);gap:14px}
.servicio,.plan,.trainer,.beneficio,.herramienta-box,.info-box{background:var(--panel2);border:1px solid var(--line);padding:20px;border-radius:12px;display:flex;flex-direction:column}
.servicio p,.plan p,.trainer p,.beneficio p,.muted{color:var(--muted)}
.servicio h3{font-size:1.05rem}
.card-img{width:100%;height:160px;object-fit:cover;border-radius:8px;margin-bottom:14px}
.grid-planes{grid-template-columns:repeat(3,1fr)}
.plan{position:relative}
.plan.destacado{border:1px solid var(--green);box-shadow:0 0 25px #b7ff3517}
.precio{font-size:2rem;font-weight:900;color:var(--green);margin:8px 0}
.plan ul{padding-left:20px;color:var(--muted);flex-grow:1}
.grid-trainers{grid-template-columns:repeat(3,1fr)}
.trainer-img{width:100%;height:200px;object-fit:cover;border-radius:8px;margin-bottom:12px}
.grid-beneficios{grid-template-columns:repeat(3,1fr)}
.form-grid{display:grid;grid-template-columns:repeat(2,1fr);gap:15px}
.form-group{margin:12px 0}
label{display:block;margin-bottom:6px;font-weight:bold}
input,select,textarea{width:100%;padding:12px;border:1px solid #46513f;border-radius:8px;background:#0e120e;color:var(--text);font:inherit}
textarea{min-height:110px;resize:vertical}
.resultado-box{padding:14px;margin-top:14px;border:1px solid var(--green);border-radius:9px;background:#1b2914}
.oculto{display:none!important}
.divisor{border:0;border-top:1px solid var(--line);margin:25px 0}
table{width:100%;border-collapse:collapse;margin-top:10px}
th,td{text-align:left;padding:12px;border-bottom:1px solid var(--line)}
th{color:var(--green)}
details{padding:14px 0;border-bottom:1px solid var(--line)}
summary{font-weight:bold;cursor:pointer}
details p{color:var(--muted);margin-bottom:0}
#mensajePase{margin-top:18px;padding:20px;border:1px dashed var(--green);border-radius:12px}
footer{text-align:center;color:var(--muted);padding:28px 15px;border-top:1px solid var(--line)}
footer strong{color:var(--green)}
.small{font-size:.88rem;color:var(--muted)}
@media(max-width:850px){.grid-servicios{grid-template-columns:repeat(2,1fr)}.grid-planes,.grid-trainers,.grid-beneficios{grid-template-columns:repeat(2,1fr)}.hero{grid-template-columns:1fr}}
@media(max-width:560px){nav ul{gap:2px}nav a{padding:7px 8px;font-size:.8rem}.grid-servicios,.grid-planes,.grid-trainers,.grid-beneficios,.form-grid{grid-template-columns:1fr}.btn-sec{margin:9px 0 0;display:inline-block}.card{padding:20px}}
</style>
</head>
<body>
<header>
  <div class="logo">⚡ TITAN FIT LAB</div>
  <p class="slogan">El laboratorio del alto rendimiento</p>
</header>
<nav aria-label="Navegación principal">
<ul>
<li><a href="#inicio">Inicio</a></li><li><a href="#programas">Programas</a></li><li><a href="#planes">Membresías</a></li><li><a href="#horarios">Horarios</a></li><li><a href="#entrenadores">Entrenadores</a></li><li><a href="#herramientas">Herramientas</a></li><li><a href="#pase">Pase VIP</a></li><li><a href="#contacto">Contacto</a></li>
</ul>
</nav>
<main>
<section id="inicio" class="card hero">
<div>
  <p style="color:var(--green);font-weight:bold;letter-spacing:2px">ENTRENA CON PROPÓSITO</p>
  <h2>BIENVENIDO A TITAN FIT LAB</h2>
  <p>En nuestro laboratorio no solo entrenas: desarrollas fuerza, constancia y confianza. Encuentra un espacio equipado, programas para diferentes niveles y una comunidad que te impulsa a mejorar a tu ritmo.</p>
  <a class="btn" href="#planes">Ver membresías</a><a class="btn btn-sec" href="#programas">Explorar programas</a>
</div>
<div class="hero-visual">
  <img src="https://images.unsplash.com/photo-1534438327276-14e5300c3a48?q=80&w=800&auto=format&fit=crop" alt="Instalaciones del gimnasio">
  <div class="hero-overlay">
    <strong>SUPERA TU PROPIA MARCA</strong>
    <p class="small">Fuerza · Técnica · Disciplina</p>
  </div>
</div>
</section>

<section class="card">
<h2>ENTRENA A TU MANERA</h2>
<div class="grid-beneficios">
<div class="beneficio">
  <img class="card-img" src="https://images.unsplash.com/photo-1584735935682-2f2b69dff9d2?q=80&w=500&auto=format&fit=crop" alt="Equipamiento de gimnasio">
  <h3>⚡ Equipamiento</h3>
  <p>Áreas pensadas para fuerza, cardio y entrenamiento funcional.</p>
</div>
<div class="beneficio">
  <img class="card-img" src="https://images.unsplash.com/photo-1483721024893-41f49110a750?q=80&w=500&auto=format&fit=crop" alt="Metas de entrenamiento">
  <h3>🎯 Metas claras</h3>
  <p>Organiza tus sesiones y registra tus avances de forma constante.</p>
</div>
<div class="beneficio">
  <img class="card-img" src="https://images.unsplash.com/photo-1517838277536-f5f99be501cd?q=80&w=500&auto=format&fit=crop" alt="Comunidad de entrenamiento">
  <h3>🤝 Comunidad</h3>
  <p>Un ambiente de respeto, apoyo y motivación para todos los niveles.</p>
</div>
</div>
</section>

<section id="programas" class="card">
<h2>NUESTROS PROGRAMAS ESPECIALIZADOS</h2>
<div class="grid-servicios">
<div class="servicio">
  <img class="card-img" src="https://images.unsplash.com/photo-1581009146145-b5ef050c2e1e?q=80&w=500&auto=format&fit=crop" alt="Musculación y fuerza">
  <h3>🏋️ Musculación y fuerza</h3>
  <p>Rutinas con peso libre y máquinas para practicar técnica y desarrollar fuerza de forma progresiva.</p>
</div>
<div class="servicio">
  <img class="card-img" src="https://images.unsplash.com/photo-1517963879433-6ad2b056d712?q=80&w=500&auto=format&fit=crop" alt="Entrenamiento funcional">
  <h3>🔥 Entrenamiento funcional</h3>
  <p>Ejercicios de movilidad, coordinación, equilibrio y resistencia adaptados a tu experiencia.</p>
</div>
<div class="servicio">
  <img class="card-img" src="https://images.unsplash.com/photo-1549719386-74dfcbf7dbed?q=80&w=500&auto=format&fit=crop" alt="Boxeo y acondicionamiento">
  <h3>🥊 Boxeo y acondicionamiento</h3>
  <p>Trabajo de coordinación, desplazamientos y condición física con enfoque técnico y seguro.</p>
</div>
<div class="servicio">
  <img class="card-img" src="https://images.unsplash.com/photo-1506126613408-eca07ce68773?q=80&w=500&auto=format&fit=crop" alt="Movilidad y recuperación">
  <h3>🧘 Movilidad y recuperación</h3>
  <p>Sesiones para mejorar el rango de movimiento y apoyar la recuperación entre entrenamientos.</p>
</div>
<div class="servicio">
  <img class="card-img" src="https://images.unsplash.com/photo-1538805060514-97d9cc17730c?q=80&w=500&auto=format&fit=crop" alt="Entrenamiento Cardio">
  <h3>🏃 Cardio</h3>
  <p>Caminadoras, bicicletas y sesiones cardiovasculares para diferentes ritmos.</p>
</div>
<div class="servicio">
  <img class="card-img" src="https://images.unsplash.com/photo-1571019613454-1cb2f99b2d8b?q=80&w=500&auto=format&fit=crop" alt="Entrenamiento guiado">
  <h3>👥 Entrenamiento guiado</h3>
  <p>Acompañamiento para aprender a usar el equipo y adaptar ejercicios a tu nivel.</p>
</div>
</div>
</section>

<section id="planes" class="card">
<h2>MEMBRESÍAS TITAN</h2><p class="muted">Planes de ejemplo para presentar los servicios. Confirma precios y disponibilidad directamente con el gimnasio.</p>
<div class="grid-planes">
<div class="plan">
  <h3>⚙️ Básico</h3>
  <div class="precio">$399 <small>/ mes</small></div>
  <p>Para entrenar a tu ritmo.</p>
  <ul><li>Acceso al área de pesas</li><li>Zona de cardio</li><li>Rutina inicial de orientación</li></ul>
  <a class="btn" href="#contacto">Me interesa</a>
</div>
<div class="plan destacado">
  <h3>⚡ Pro</h3>
  <div class="precio">$599 <small>/ mes</small></div>
  <p>Para una experiencia más completa.</p>
  <ul><li>Todo lo del plan Básico</li><li>Clases funcionales grupales</li><li>Seguimiento mensual de objetivos</li></ul>
  <a class="btn" href="#contacto">Elegir Pro</a>
</div>
<div class="plan">
  <h3>👑 Elite</h3>
  <div class="precio">$799 <small>/ mes</small></div>
  <p>Más acompañamiento en tu proceso.</p>
  <ul><li>Todo lo del plan Pro</li><li>Sesión de orientación individual</li><li>Prioridad para reservar clases</li></ul>
  <a class="btn" href="#contacto">Me interesa</a>
</div>
</div>
<p class="small">*Los precios mostrados son ilustrativos y pueden editarse según los costos reales del proyecto.</p>
</section>

<section id="horarios" class="card">
<h2>HORARIOS DE ATENCIÓN</h2>
<div style="overflow-x:auto"><table><thead><tr><th>Día</th><th>Horario</th><th>Actividades sugeridas</th></tr></thead><tbody>
<tr><td>Lunes a viernes</td><td>6:00 a. m. – 10:00 p. m.</td><td>Pesas, cardio y funcional</td></tr>
<tr><td>Sábado</td><td>8:00 a. m. – 6:00 p. m.</td><td>Fuerza y clases grupales</td></tr>
<tr><td>Domingo</td><td>9:00 a. m. – 2:00 p. m.</td><td>Cardio y movilidad</td></tr>
</tbody></table></div><p class="small">Horario de muestra para el proyecto; reemplázalo por el horario oficial si es necesario.</p>
</section>

<section id="entrenadores" class="card">
<h2>ÁREA DE ENTRENADORES</h2>
<div class="grid-trainers">
<div class="trainer">
  <img class="trainer-img" src="https://images.unsplash.com/photo-1567013127542-490d757e51fc?q=80&w=500&auto=format&fit=crop" alt="Entrenador de fuerza">
  <h3>Entrenamiento de fuerza</h3>
  <p>Enfoque: técnica, control del movimiento y progresión gradual.</p>
</div>
<div class="trainer">
  <img class="trainer-img" src="https://images.unsplash.com/photo-1594381898411-846e7d193883?q=80&w=500&auto=format&fit=crop" alt="Entrenadora de condición física">
  <h3>Condición física</h3>
  <p>Enfoque: resistencia, coordinación y trabajo funcional adaptado.</p>
</div>
<div class="trainer">
  <img class="trainer-img" src="https://images.unsplash.com/photo-1518611012118-696072aa579a?q=80&w=500&auto=format&fit=crop" alt="Entrenador de movilidad">
  <h3>Movilidad y bienestar</h3>
  <p>Enfoque: calentamiento, movilidad y recuperación responsable.</p>
</div>
</div>
</section>

<section id="herramientas" class="card">
<h2>HERRAMIENTAS FITNESS INTERACTIVAS</h2>
<div class="herramienta-box">
<h3>📊 Calculadora de IMC</h3><p class="small">El IMC es una medida orientativa; por sí solo no determina la salud ni sustituye una evaluación profesional.</p>
<div class="form-grid"><div class="form-group"><label for="pesoIMC">Peso (kg)</label><input type="number" id="pesoIMC" min="1" max="500" step=".1" placeholder="Ej. 70"></div><div class="form-group"><label for="estaturaIMC">Estatura (cm)</label><input type="number" id="estaturaIMC" min="50" max="250" placeholder="Ej. 170"></div></div>
<button id="btnIMC">Calcular IMC</button><div id="resultadoIMC" class="resultado-box oculto" aria-live="polite"></div>
</div>
<hr class="divisor">
<div class="herramienta-box">
<h3>🔥 Estimador de calorías</h3><p class="small">Estimación general con fines educativos, no una prescripción nutricional.</p>
<div class="form-grid"><div class="form-group"><label for="objetivoCalorias">Objetivo</label><select id="objetivoCalorias"><option value="mantener">Mantener energía</option><option value="ganar">Apoyar ganancia muscular</option><option value="rendimiento">Mejorar rendimiento</option></select></div><div class="form-group"><label for="actividadCalorias">Actividad semanal</label><select id="actividadCalorias"><option value="ligero">Ligera (1–2 días)</option><option value="moderado">Moderada (3–4 días)</option><option value="intenso">Intensa (5 o más días)</option></select></div></div>
<button id="btnCalorias">Ver recomendación</button><div id="resultadoCalorias" class="resultado-box oculto" aria-live="polite"></div>
</div>
<hr class="divisor">
<div class="herramienta-box">
<h3>🎲 Generador de entrenamiento</h3><p>Elige el tipo de sesión y recibe una idea para organizar tu práctica.</p>
<div class="form-group"><label for="tipoRutina">Tipo de entrenamiento</label><select id="tipoRutina"><option value="fuerza">Fuerza general</option><option value="cardio">Cardio</option><option value="funcional">Funcional</option><option value="movilidad">Movilidad</option></select></div>
<button id="btnRutina">Generar sesión</button><div id="resultadoRutina" class="resultado-box oculto" aria-live="polite"></div>
</div>
</section>

<section id="pase" class="card">
<h2>🎟️ PASE DE PRUEBA TITAN</h2><p>¿Quieres conocer el espacio antes de elegir una membresía? Genera un pase de muestra para esta página.</p>
<button id="btnPase">Generar pase</button><div id="mensajePase" class="oculto" aria-live="polite"><h3>⚡ ¡PASE DE PRUEBA GENERADO!</h3><p>Presenta este código en recepción para consultar las condiciones de una visita de prueba.</p><p><strong id="codigoPase" style="color:var(--green)"></strong></p><p class="small">Este pase es una demostración del sitio y no garantiza acceso real ni una promoción vigente.</p></div>
</section>

<section class="card">
<h2>PREGUNTAS FRECUENTES</h2>
<details><summary>¿Necesito experiencia para comenzar?</summary><p>No. Puedes comenzar con ejercicios básicos y pedir orientación para aprender la técnica y el uso correcto del equipo.</p></details>
<details><summary>¿Qué debo llevar a mi entrenamiento?</summary><p>Ropa cómoda, calzado deportivo, agua y una toalla personal.</p></details>
<details><summary>¿Puedo combinar fuerza y cardio?</summary><p>Sí. La combinación depende de tus objetivos, tu descanso y tu nivel de experiencia. Aumenta la carga gradualmente.</p></details>
<details><summary>¿Cómo puedo pedir información?</summary><p>Completa el formulario de contacto de esta página. En esta versión de demostración, el mensaje se prepara en pantalla, pero no se envía a un servidor.</p></details>
</section>

<section id="contacto" class="card">
<h2>CONTACTO E INFORMACIÓN</h2><p class="muted">Déjanos tus datos y el motivo de tu consulta.</p>
<form id="formContacto">
<div class="form-grid"><div class="form-group"><label for="nombre">Nombre</label><input id="nombre" name="nombre" required maxlength="70" placeholder="Tu nombre"></div><div class="form-group"><label for="correo">Correo electrónico</label><input id="correo" name="correo" type="email" required placeholder="tu@correo.com"></div></div>
<div class="form-group"><label for="motivo">¿Qué te interesa?</label><select id="motivo" name="motivo"><option>Información de membresías</option><option>Clases y horarios</option><option>Entrenamiento guiado</option><option>Otra consulta</option></select></div>
<div class="form-group"><label for="mensaje">Mensaje</label><textarea id="mensaje" name="mensaje" required maxlength="600" placeholder="Escribe tu pregunta..."></textarea></div>
<button type="submit">Preparar mensaje</button><div id="resultadoContacto" class="resultado-box oculto" aria-live="polite"></div>
</form>
</section>
</main>
<footer><p>© 2026 <strong>TITAN FIT LAB</strong> — Proyecto escolar de programación web.</p><p class="small">Fuerza con técnica. Progreso con constancia.</p></footer>
<script>
const $ = id => document.getElementById(id);
$('btnIMC').addEventListener('click',()=>{
 const peso=parseFloat($('pesoIMC').value), cm=parseFloat($('estaturaIMC').value), out=$('resultadoIMC');
 out.classList.remove('oculto');
 if(!(peso>0&&cm>=50&&cm<=250)){out.textContent='Ingresa un peso y una estatura válidos.';return}
 const imc=peso/Math.pow(cm/100,2);
 out.innerHTML='<strong>Tu IMC estimado es '+imc.toFixed(1)+'</strong><br>Este número no es un diagnóstico. En adolescentes se interpreta con criterios de edad y desarrollo; consulta a un profesional para una valoración adecuada.';
});
$('btnCalorias').addEventListener('click',()=>{
 const objetivo=$('objetivoCalorias').value, actividad=$('actividadCalorias').value, out=$('resultadoCalorias');
 const textos={mantener:'Prioriza comidas variadas, hidratación y energía suficiente para tus actividades.',ganar:'Combina alimentación suficiente, descanso y entrenamiento progresivo con orientación profesional.',rendimiento:'Organiza tus comidas, hidratación y recuperación alrededor de tus sesiones.'};
 const act={ligero:'Empieza con una rutina manejable y aumenta poco a poco.',moderado:'Alterna sesiones exigentes con días de recuperación.',intenso:'Programa descansos y presta atención a la fatiga.'};
 out.classList.remove('oculto');out.textContent=textos[objetivo]+' '+act[actividad]+' No se calcula una cifra de calorías porque las necesidades dependen de la edad, el crecimiento y otros factores individuales.';
});
const rutinas={
 fuerza:'Calentamiento suave; practica sentadilla a una silla, empuje contra pared y remo con banda si tienes una. Mantén técnica cómoda y descansa entre series.',
 cardio:'Comienza con 5 minutos suaves; alterna caminata a ritmo cómodo con periodos algo más rápidos y termina bajando el ritmo.',
 funcional:'Haz un circuito moderado de sentarse y levantarse de una silla, marcha en el sitio y empujes contra pared. Descansa cuando lo necesites.',
 movilidad:'Dedica unos minutos a movilidad suave de hombros, tobillos y cadera, sin rebotes ni dolor.'
};
$('btnRutina').addEventListener('click',()=>{const out=$('resultadoRutina');out.classList.remove('oculto');out.textContent=rutinas[$('tipoRutina').value]});
$('btnPase').addEventListener('click',()=>{
 const codigo='TITAN-'+Math.random().toString(36).slice(2,7).toUpperCase();
 $('codigoPase').textContent=codigo;$('mensajePase').classList.remove('oculto');
});
$('formContacto').addEventListener('submit',e=>{
 e.preventDefault();
 const datos=new FormData(e.currentTarget);
 const out=$('resultadoContacto');out.classList.remove('oculto');
 out.textContent='Mensaje preparado para '+datos.get('nombre')+'. Esta demostración no envía ni almacena tus datos. Para recibir mensajes, conecta el formulario a un servicio o servidor.';
});
</script>
</body>
</html>
