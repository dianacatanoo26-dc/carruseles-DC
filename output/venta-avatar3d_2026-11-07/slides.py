# Sáb 7 nov · 💰 Vende — "Crea Tu Avatar 3D Estilo Muñeca"
CAMISA = "fotos_creador/avatar_camisa.png"
BLAZER = "fotos_creador/avatar_blazer.png"
CELULAR = "fotos_creador/avatar_celular.png"
PLATAF = "fotos_creador/avatar_plataformas.jpg"

SLIDES = [
f'''
<h1 class="titulo"><span class="linea">Crea tu</span><span class="pincel">avatar 3D</span><span class="linea" style="margin-top:12px">estilo muñeca</span></h1>
{rayitas(30,40,70)}{chispa(980,320,54,"var(--fucsia)")}
<p class="mano" style="margin-top:40px;max-width:470px">Y conviértelo en <span class="subraya">la cara de tu contenido</span> 💛</p>
<div class="mano" style="position:absolute;left:70px;top:1170px;font-size:36px">Desliza →</div>
{recorte(BLAZER, derecha=-30, alto=900)}
''',
f'''
<h1 class="titulo" style="font-size:84px"><span class="linea">Este curso es</span><span class="pincel">para ti si…</span></h1>
<ul class="lista" style="margin-top:60px;max-width:600px">
<li><span class="ico">✓</span><span class="txt">Quieres una imagen profesional</span></li>
<li><span class="ico">✓</span><span class="txt">Te da pena salir en cámara</span></li>
<li><span class="ico">✓</span><span class="txt">Quieres crear contenido más rápido</span></li>
<li><span class="ico">✓</span><span class="txt">Buscas destacar con algo diferente</span></li>
</ul>
{recorte(CELULAR, derecha=-60, alto=640)}
''',
f'''
<h1 class="titulo" style="font-size:84px"><span class="linea">Vas a</span><span class="pincel">aprender a…</span></h1>
<ul class="lista" style="margin-top:60px;max-width:620px">
<li><span class="ico">🎨</span><span class="txt">Diseñar tu avatar paso a paso</span></li>
<li><span class="ico">👗</span><span class="txt">Cambiar su vestuario</span></li>
<li><span class="ico">🌎</span><span class="txt">Crear sus escenarios</span></li>
<li><span class="ico">🎬</span><span class="txt">Animarlo en videos</span></li>
<li><span class="ico">📱</span><span class="txt">Usarlo en todas tus redes</span></li>
</ul>
{recorte(CAMISA, derecha=-60, alto=700)}
''',
f'''
<h1 class="titulo" style="font-size:84px"><span class="linea">Un avatar</span><span class="pincel">todas las redes</span></h1>
{chispa(960,60,54,"var(--fucsia)")}
{polaroid(PLATAF, 70, 420, 940, 530, -2)}
<div class="caja" style="position:absolute;left:150px;top:1060px;font-size:40px">✨ Sin experiencia previa</div>
''',
f'''
<h1 class="titulo"><span class="linea">Tu avatar</span><span class="pincel">te está esperando</span></h1>
{rayitas(30,40,70)}
<p class="mano" style="margin-top:50px;max-width:520px">Pago seguro y <span class="subraya">acceso inmediato</span> 🔒</p>
<div class="pincel" style="position:absolute;left:70px;top:700px;font-family:'Permanent Marker';font-size:44px;margin-left:0;max-width:470px;line-height:1.15">Te dejo el link en mi bio 💛</div>
<div class="caja" style="position:absolute;left:60px;top:920px;max-width:440px;font-size:36px">¿Dudas? Escríbeme por DM y te ayudo.</div>
{recorte(BLAZER, derecha=-40, alto=860)}
''',
]
