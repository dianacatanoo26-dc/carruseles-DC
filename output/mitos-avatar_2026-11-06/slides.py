# Vie 6 nov · 📚 Enseña — "Mitos sobre los avatares 3D" (portada rosado claro)
CAMISA = "fotos_creador/avatar_camisa.png"
TABLET = "fotos_creador/avatar_tablet.png"
CELULAR = "fotos_creador/avatar_celular.png"

def mito(titulo, mito_txt, realidad, visual):
    return f'''
<h1 class="titulo" style="font-size:84px"><span class="linea">Mito</span><span class="pincel">{titulo}</span></h1>
{rayitas(980,40,70,giro=100)}
<div class="mano" style="margin-top:70px;max-width:560px;font-size:44px">❌ “{mito_txt}”</div>
<div class="caja" style="margin-top:50px;max-width:560px;font-size:44px">✅ {realidad}</div>
{visual}
'''

SLIDES = [
f'''<div class="fondo-rosa"></div>
<h1 class="titulo"><span class="linea">4 mitos</span><span class="linea">sobre los</span><span class="pincel">avatares 3D</span></h1>
{chispa(980,320,54,"var(--fucsia)")}
<p class="mano" style="margin-top:50px;max-width:470px">Que te están frenando a <span class="subraya">crear el tuyo</span> 👀</p>
<div class="mano" style="position:absolute;left:70px;top:1170px;font-size:36px">Desliza →</div>
{recorte(CAMISA, derecha=-30, alto=930)}''',
mito("Se ven falsos", "Nadie va a conectar con un muñeco.", "Si se parece a ti, <b>te reconocen</b> y conectan con tu mensaje.", polaroid("fotos_creador/avatar_gym_cara.jpg", 580, 470, 440, 700, 4, "¿Se ve falso? 😉", enfoque="center 30%")),
mito("Hay que saber diseñar", "Eso es solo para expertas.", "Se aprende <b>paso a paso</b>, sin experiencia previa.", recorte(TABLET, derecha=-40, alto=800)),
mito("Solo sirve para fotos", "Es solo una imagen bonita.", "Lo usas en <b>imágenes, videos y carruseles</b>.", polaroid("fotos_creador/avatar_plataformas.jpg", 420, 760, 600, 340, 3)),
mito("Pierdes tu esencia", "Ya no vas a ser tú.", "Tu avatar <b>lleva tu estilo</b>: tu cabello, tu sonrisa, tu forma de vestir.", recorte(CELULAR, derecha=-20, alto=740)),
f'''
<h1 class="titulo"><span class="linea">Mañana te cuento</span><span class="pincel">cómo crear el tuyo</span></h1>
{rayitas(980,40,70,giro=100)}
<p class="mano" style="margin-top:50px;max-width:500px">¿Cuál de estos mitos <span class="subraya">creías tú</span>? 👇</p>
<div class="caja" style="position:absolute;left:60px;top:760px;max-width:470px;font-size:40px">🔔 Activa las notificaciones para no perdértelo 💛</div>
{recorte(TABLET, derecha=-30, alto=900)}''',
]
