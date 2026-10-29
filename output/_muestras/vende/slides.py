# Muestra estilo VENDE con el carrusel del sábado 7 (Crea tu avatar 3D)
ESTILO = "vende"
CAMISA = "fotos_creador/avatar_camisa.png"
BLAZER = "fotos_creador/avatar_blazer.png"
CELULAR = "fotos_creador/avatar_celular.png"

SLIDES = [
f'''<span class="etq">✨ Curso</span>
<h1 class="grande" style="margin-top:40px">Crea tu<br><span class="amar">avatar 3D</span><br>estilo<br>muñeca</h1>
{recorte(BLAZER, derecha=-90, alto=820)}''',
f'''<div class="fondo-amarillo"></div>
<h1 class="grande rosa" style="font-size:96px">¿Es para ti?</h1>
<ul class="limpia" style="max-width:600px">
<li>Quieres una imagen profesional</li><li>Te da pena salir en cámara</li><li>Quieres crear más rápido</li><li>Quieres destacar</li></ul>
{recorte(CELULAR, derecha=-60, alto=640)}''',
f'''<h1 class="grande" style="font-size:96px">Vas a<br><span class="amar">aprender</span></h1>
<ul class="limpia" style="max-width:620px">
<li>Diseñar tu avatar</li><li>Cambiar su ropa</li><li>Crear escenarios</li><li>Animarlo en videos</li><li>Usarlo en tus redes</li></ul>
{recorte(CAMISA, derecha=-60, alto=760)}''',
f'''<div class="fondo-amarillo"></div>
<h1 class="grande rosa" style="font-size:96px">Un avatar,<br>todas las redes</h1>
<div class="marco" style="left:70px;right:70px;top:430px"><img src="{img("fotos_creador/avatar_plataformas.jpg")}"></div>
<span class="etq" style="position:absolute;left:70px;top:1010px;background:var(--fucsia);color:#fff">Sin experiencia previa ✨</span>''',
f'''<h1 class="grande" style="font-size:96px;max-width:620px">Tu avatar<br>te está<br><span class="amar">esperando</span></h1>
<p class="bio-txt" style="margin-top:40px;max-width:520px">Pago seguro y acceso inmediato 🔒</p>
<p class="bio-txt" style="margin-top:30px;max-width:520px;color:var(--lila)">Te dejo el link en mi bio 💛</p>
{recorte(BLAZER, derecha=-90, alto=780)}''',
]
