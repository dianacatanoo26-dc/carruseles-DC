# Muestra estilo CONECTA con el carrusel del jueves 5 (Mi foto vs. mi avatar)
ESTILO = "conecta"
REAL = img("fotos_creador/diana_real.jpg")
REAL_CARA = img("fotos_creador/diana_real_cara.jpg")
PODCAST = img("fotos_creador/diana_podcast.jpg")
CAMISA = img("fotos_creador/avatar_camisa.png")
CELULAR = img("fotos_creador/avatar_celular.png")
CARA_AV = img("fotos_creador/ref_cara_frente.jpg")

SLIDES = [
f'''<div class="mitad izq"><img src="{REAL}" style="object-position:center 20%"></div>
<div class="mitad der rosa"><img src="{CAMISA}"></div>
<div class="vs">VS</div>
<span class="cinta" style="left:60px;top:70px">Yo</span><span class="cinta rosa" style="right:60px;top:70px;background:var(--lila);color:var(--fucsia)">Mi avatar 3D</span>
<div class="nota"><div class="frase">¿Nos parecemos? 👀</div><p>Mi foto vs. mi avatar 3D. Desliza →</p></div>''',
f'''<div class="mitad izq"><img src="{REAL_CARA}"></div>
<div class="mitad der"><img src="{CARA_AV}"></div>
<span class="cinta" style="left:60px;top:70px">Yo</span><span class="cinta rosa" style="right:60px;top:70px">Mi avatar</span>
<div class="nota"><div class="frase">Mis rasgos</div><p>Mismos ojos, cejas y sonrisa 😊</p></div>''',
f'''<div class="foto-fondo"><img src="{PODCAST}" style="object-position:center 25%"></div>
<div class="nota"><div class="frase">Mi esencia ✨</div><p>Pelo negro largo, aretes dorados y mucho estilo. Eso no podía faltar en mi avatar.</p></div>''',
f'''<div class="foto-fondo"><img src="{REAL}" style="object-position:center 15%"></div>
<div class="nota"><div class="frase">Lo que mantuve igual</div><p>💇‍♀️ Mi cabello · 👁️ mis ojos · ✨ mi sonrisa · 💛 mi tono de piel · 👗 mi forma de vestir</p></div>''',
f'''<div class="mitad izq amarilla" style="width:100%"><img src="{CELULAR}" style="object-position:right bottom;padding-left:380px"></div>
<div class="nota" style="bottom:auto;top:110px;right:400px"><div class="frase">Tu avatar debe ser TÚ</div><p>Así tu audiencia te reconoce aunque no salgas en cámara. ¿Quieres el tuyo? Te dejo el link en mi bio 💛</p></div>''',
]
