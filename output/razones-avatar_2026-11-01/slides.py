# Dom 1 nov · 📚 Enseña — "3 razones para tener tu avatar 3D" (portada café)
CAMISA = "fotos_creador/avatar_camisa.png"
TABLET = "fotos_creador/avatar_tablet.png"
CELULAR = "fotos_creador/avatar_celular.png"

def razon(n, titulo, texto, visual):
    return f'''
<h1 class="titulo" style="font-size:84px"><span class="linea">Razón #{n}</span><span class="pincel">{titulo}</span></h1>
{rayitas(980,40,70,giro=100)}
<div class="caja" style="margin-top:80px;max-width:560px;font-size:46px">{texto}</div>
{chispa(90,1000,54)}{chispa(560,820,44,"var(--fucsia)")}
{visual}
'''

SLIDES = [
f'''<div class="fondo-cafe"></div>
<h1 class="titulo"><span class="linea">3 razones</span><span class="linea">para tener</span><span class="pincel">tu avatar 3D</span></h1>
{chispa(980,320,54,"var(--lila)")}
<p class="mano" style="margin-top:50px;max-width:470px">Y por qué cada vez más emprendedoras <span class="subraya">lo están usando</span> ✨</p>
{flecha(110,1020,220,130,giro=-15,color="var(--lila)")}
<div class="mano" style="position:absolute;left:70px;top:1170px;font-size:36px">Desliza →</div>
{recorte(TABLET, derecha=-30, alto=930)}''',
razon(1, "Sin cámara", "Creas contenido <b>sin grabarte</b> y sin pena. Tu avatar da la cara por ti.", polaroid("fotos_creador/avatar_gym_batido.jpg", 580, 470, 440, 700, 4, "Hoy: gym 💪", enfoque="center 20%")),
razon(2, "Más constancia", "Publicas <b>más rápido</b> y todos los días, sin depender de cómo te ves ese día.", recorte(CELULAR, derecha=-20, alto=760)),
razon(3, "Te recuerdan", "Tu marca se vuelve <b>única y fácil de reconocer</b> en el feed.", polaroid("fotos_creador/avatar_escritorio.jpg", 600, 520, 420, 600, 4, "Mi avatar ✨", enfoque="center 20%")),
f'''
<h1 class="titulo"><span class="linea">¿Cuál razón</span><span class="pincel">te convenció?</span></h1>
{rayitas(980,40,70,giro=100)}
<p class="mano" style="margin-top:50px;max-width:520px">Cuéntame: <span class="subraya">1, 2 o 3</span> 👇</p>
<div class="caja" style="position:absolute;left:60px;top:760px;max-width:480px;font-size:40px">💛 Sígueme: esta semana te enseño todo sobre avatares 3D.</div>
{recorte(TABLET, derecha=-30, alto=900)}''',
]
