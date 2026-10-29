# Jue 5 nov · 💬 Conecta — "Antes y después: mi foto vs. mi avatar"
REAL = "fotos_creador/diana_real.jpg"
REAL_CARA = "fotos_creador/diana_real_cara.jpg"
PODCAST = "fotos_creador/diana_podcast.jpg"
CAMISA = "fotos_creador/avatar_camisa.png"
CELULAR = "fotos_creador/avatar_celular.png"

SLIDES = [
f'''<div class="fondo-cafe"></div>
<h1 class="titulo"><span class="linea">Mi foto</span><span class="pincel">vs. mi avatar 3D</span></h1>
{rayitas(30,40,70)}{rayitas(980,30,70,giro=100)}
<p class="mano" style="margin-top:40px;max-width:600px">¿Nos parecemos? 👀</p>
{polaroid(REAL, 70, 470, 420, 560, -5, "Yo", enfoque="center 20%")}
{flecha(400,1040,200,120,giro=-15)}
{recorte(CAMISA, derecha=-40, alto=860)}
''',
f'''
<h1 class="titulo" style="font-size:84px"><span class="linea">La cara</span><span class="pincel">mis rasgos</span></h1>
{chispa(960,60,54,"var(--fucsia)")}
{polaroid(REAL_CARA, 70, 420, 430, 520, -4, "Yo")}
{polaroid("fotos_creador/ref_cara_frente.jpg", 560, 450, 430, 520, 4, "Mi avatar")}
<div class="caja" style="position:absolute;left:150px;top:1080px;font-size:38px">Mismos ojos, cejas y sonrisa 😊</div>
''',
f'''
<h1 class="titulo" style="font-size:84px"><span class="linea">El estilo</span><span class="pincel">mi esencia</span></h1>
{chispa(960,60,54,"var(--fucsia)")}
{polaroid(PODCAST, 70, 430, 420, 600, -4, "Yo", enfoque="center 25%")}
<div class="mano" style="position:absolute;left:80px;top:1110px;max-width:440px;font-size:36px">Pelo negro largo, aretes dorados y <span class="subraya">mucho estilo</span> ✨</div>
{recorte(CELULAR, derecha=-20, alto=780)}
''',
f'''
<h1 class="titulo"><span class="linea">Lo que</span><span class="pincel">mantuve igual</span></h1>
{rayitas(980,40,70,giro=100)}
<ul class="lista" style="margin-top:60px;max-width:560px">
<li><span class="ico">💇‍♀️</span><span class="txt">Mi cabello negro largo</span></li>
<li><span class="ico">👁️</span><span class="txt">Mis ojos cafés</span></li>
<li><span class="ico">✨</span><span class="txt">Mis cejas y mi sonrisa</span></li>
<li><span class="ico">💛</span><span class="txt">Mi tono de piel</span></li>
<li><span class="ico">👗</span><span class="txt">Mi forma de vestir</span></li>
</ul>
{recorte(CAMISA, derecha=-40, alto=800)}
''',
f'''
<h1 class="titulo"><span class="linea">Tu avatar</span><span class="pincel">debe ser TÚ</span></h1>
{rayitas(30,40,70)}
<p class="mano" style="margin-top:50px;max-width:540px">Cuando se parece a ti, tu audiencia <span class="subraya">te reconoce</span> aunque no salgas en cámara.</p>
<div class="caja" style="position:absolute;left:60px;top:800px;max-width:480px;font-size:40px">💛 ¿Quieres el tuyo? Te dejo el link en mi bio.</div>
{recorte(CELULAR, derecha=-20, alto=780)}
''',
]
