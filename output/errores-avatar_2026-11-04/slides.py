# Mié 4 nov · 📚 Enseña — "5 errores al crear tu avatar 3D"
CAMISA = "fotos_creador/avatar_camisa.png"
BLAZER = "fotos_creador/avatar_tablet.png"  # pose con tablet (reemplaza la que señalaba)
REAL = "fotos_creador/diana_real_cara.jpg"

def error(n, titulo, mal, bien, visual):
    return f'''
<h1 class="titulo" style="font-size:80px"><span class="linea">Error #{n}</span><span class="pincel">{titulo}</span></h1>
{rayitas(980,40,70,giro=100)}
<div class="mano" style="margin-top:60px;max-width:560px;font-size:38px">❌ {mal}</div>
<div class="caja" style="margin-top:40px;max-width:560px;font-size:38px">✅ {bien}</div>
<div style="position:absolute;left:70px;bottom:110px;font-family:'Permanent Marker';font-size:340px;line-height:1;color:var(--lila);-webkit-text-stroke:4px var(--fucsia);text-shadow:10px 10px 0 var(--fucsia);transform:rotate(-6deg);z-index:1">{n}</div>{visual}
'''

SLIDES = [
f'''<div class="fondo-rosa"></div>
<h1 class="titulo"><span class="linea">5 errores</span><span class="linea">al crear</span><span class="pincel">tu avatar 3D</span></h1>
{rayitas(30,40,70)}{chispa(980,320,54,"var(--fucsia)")}
<p class="mano" style="margin-top:50px;max-width:470px">(y cómo evitarlos para que <span class="subraya">se parezca a ti</span>)</p>
<div class="mano" style="position:absolute;left:70px;top:1170px;font-size:36px">Desliza →</div>
{recorte(CAMISA, derecha=-40, alto=900)}
''',
error(1, "Foto borrosa", "Usar una foto oscura, con filtros o de lejos.", "Usa una foto <b>clara, de frente</b> y con buena luz.",
      polaroid(REAL, 640, 520, 380, 470, 4, "Así sí") + chispa(580,460,50)),
error(2, "Cambiar la referencia", "Usar una imagen distinta cada vez.", "Crea tu <b>hoja de referencia</b> y úsala siempre.",
      polaroid("fotos_creador/ref_cara.jpg", 90, 860, 900, 400, -2, "Mi hoja de referencia")),
error(3, "Prompt vago", "Escribir solo “hazme un avatar bonito”.", "Describe <b>rasgos, cabello, estilo, luz</b> y lo que no debe cambiar.",
      recorte(BLAZER, derecha=-40, alto=760)),
error(4, "Que no te parezca", "Crear un personaje que ya no eres tú.", "Mantén tus <b>rasgos reales</b>: cabello, ojos, piel y tu sonrisa.",
      polaroid("fotos_creador/ref_cara_frente.jpg", 660, 540, 360, 520, 3, "Mi avatar", check=True)),
error(5, "Usarlo una vez", "Crearlo y dejarlo guardado.", "Úsalo <b>todos los días</b>: imágenes, videos y carruseles.",
      polaroid("fotos_creador/avatar_escritorio.jpg", 600, 520, 420, 600, 4, "Todos los días ✨", enfoque="center 20%")),
f'''
<h1 class="titulo"><span class="linea">¿Cuál de estos</span><span class="pincel">cometías tú?</span></h1>
{rayitas(980,40,70,giro=100)}
<p class="mano" style="margin-top:50px;max-width:520px">Te leo en los comentarios 👇</p>
<div class="caja" style="position:absolute;left:60px;top:700px;max-width:480px;font-size:40px">💛 Guarda este post y compártelo con una amiga que quiera su avatar.</div>
{recorte(BLAZER, derecha=-30, alto=900)}
''',
]
