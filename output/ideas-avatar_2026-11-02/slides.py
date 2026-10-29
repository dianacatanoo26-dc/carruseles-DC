# Lun 2 nov · 📚 Enseña — "5 ideas de contenido con tu avatar 3D"
CAMISA = "fotos_creador/avatar_camisa.png"
BLAZER = "fotos_creador/avatar_tablet.png"  # pose con tablet (reemplaza la que señalaba)
CELULAR = "fotos_creador/avatar_celular.png"

def idea(n, titulo, texto, pose, ancho_txt=560):
    return f'''
<h1 class="titulo" style="font-size:84px"><span class="linea">Idea #{n}</span><span class="pincel">{titulo}</span></h1>
{rayitas(980,40,70,giro=100)}
<div class="caja" style="margin-top:80px;max-width:{ancho_txt}px;font-size:48px">{texto}</div>
{chispa(80,1000,54)}{chispa(560,820,44,"var(--fucsia)")}
{pose}
'''

SLIDES = [
f'''<div class="fondo-crema"></div>
<h1 class="titulo"><span class="linea">5 ideas de</span><span class="linea">contenido con</span><span class="pincel">tu avatar 3D</span></h1>
{rayitas(30,40,70)}{chispa(980,300,54,"var(--fucsia)")}
<p class="mano" style="margin-top:50px;max-width:470px">Para que <span class="subraya">nunca más</span> te quedes sin qué publicar ✨</p>
{flecha(120,1020,220,130,giro=-15)}
<div class="mano" style="position:absolute;left:70px;top:1170px;font-size:36px">Desliza →</div>
{recorte(BLAZER, derecha=-30, alto=930)}
''',
idea(1, "Tips de tu nicho", "Tu avatar explica en <b>30 segundos</b> lo que tú sabes hacer.", recorte(BLAZER, derecha=-40, alto=820)),
idea(2, "Tu día a día", "Muestra tu rutina, tu trabajo o tu café de la mañana <b>sin grabarte</b>.", recorte(CELULAR, derecha=-20, alto=760)),
idea(3, "Tus productos", "Tu avatar <b>presenta y recomienda</b> lo que vendes.", recorte(CAMISA, derecha=-40, alto=820)),
idea(4, "Preguntas frecuentes", "Responde lo que más te preguntan en DM, <b>una por video</b>.", recorte(CELULAR, derecha=-20, alto=760), 520),
idea(5, "Tendencias", "Súmate a los audios y retos del momento <b>con tu avatar</b>.", recorte(CAMISA, derecha=-40, alto=820)),
f'''
<h1 class="titulo"><span class="linea">¿Cuál vas a</span><span class="pincel">probar primero?</span></h1>
{rayitas(980,40,70,giro=100)}
<p class="mano" style="margin-top:50px;max-width:520px">Cuéntame en los comentarios: <span class="subraya">1, 2, 3, 4 o 5</span> 👇</p>
<div class="caja" style="position:absolute;left:60px;top:760px;max-width:480px;font-size:40px">💛 Guarda este post para cuando no sepas qué publicar.</div>
{chispa(470,620,54)}
{recorte(BLAZER, derecha=-30, alto=900)}
''',
]
