# Carrusel estilo libreta: "Que tu avatar siga siendo tú" (5 slides)
REAL = img("fotos_creador/diana_podcast.jpg")
CUERPO = img("fotos_creador/avatar_cuerpo.png")

def parada(derecha=0, alto=880):
    """Avatar en licra negra, en polaroid grande a la derecha.
    (Cuando haya una imagen en licra con fondo liso, se cambia por el recorte de cuerpo entero.)"""
    return (f'<div class="polaroid" style="right:{derecha + 50}px;bottom:120px;width:{int(alto * .52)}px;'
            f'height:{int(alto * .8)}px;transform:rotate(3deg)"><img src="{BICI}" style="object-position:center 8%"></div>')
BICI = img("fotos_creador/avatar.jpg")
SENALA = img("fotos_creador/avatar_señala.jpg")
PLATAF = img("fotos_creador/avatar_plataformas.jpg")

SLIDES = [
# 1 — Portada
f'''
<h1 class="titulo"><span class="linea">Que tu avatar</span><span class="pincel">siga siendo tú</span></h1>
{rayitas(30,40,70)}{rayitas(960,30,70,giro=100)}
<p class="mano" style="margin-top:44px;max-width:620px">No se trata de crear a otra persona <span class="subraya">completamente diferente</span>…</p>
<div class="polaroid" style="left:70px;top:520px;width:310px;height:420px;transform:rotate(-6deg)"><img src="{REAL}" style="object-position:center 25%"><span class="etiqueta">Yo</span></div>
{flecha(330,900,220,140,giro=-10)}
{parada(10,900)}
<span class="etiqueta" style="left:auto;right:40px;bottom:auto;top:470px;transform:rotate(-3deg);z-index:4">Mi avatar 3D</span>
{chispa(420,440,56)}{chispa(980,330,44,"var(--fucsia)")}{chispa(440,1120,48)}
<div class="caja" style="position:absolute;left:60px;top:1060px;max-width:470px;font-size:38px">Es convertir <b>tu imagen</b> en un personaje que <b>te represente</b>.</div>
''',

# 2 — Qué puede hacer
f'''
<h1 class="titulo"><span class="linea">Tu avatar puede</span><span class="pincel" style="font-size:84px">hacer mucho más</span></h1>
{rayitas(980,150,70,giro=100)}
<ul class="lista" style="margin-top:56px;max-width:520px">
<li><span class="ico">📸</span><span class="txt">Crear imágenes</span></li>
<li><span class="ico">🎬</span><span class="txt">Crear videos</span></li>
<li><span class="ico">🌎</span><span class="txt">Cambiar de escenario</span></li>
<li><span class="ico">📱</span><span class="txt">Hacer contenido diario</span></li>
<li><span class="ico">💼</span><span class="txt">Vender por tu marca</span></li>
</ul>
<div class="polaroid" style="left:600px;top:360px;width:400px;height:520px;transform:rotate(4deg)"><img src="{SENALA}"></div>
<div class="polaroid" style="left:300px;top:880px;width:640px;height:370px;transform:rotate(-3deg)"><img src="{PLATAF}"></div>
{flecha(470,700,170,110,giro=20)}{chispa(560,330,48)}{chispa(150,880,52,"var(--fucsia)")}
<div class="mano" style="position:absolute;left:64px;top:1000px;max-width:240px;font-size:38px">Sin empezar <span class="subraya">desde cero</span> cada vez.</div>
''',

# 3 — Consistencia
f'''
<h1 class="titulo" style="font-size:76px"><span class="linea">¿Quieres que se vea</span><span class="pincel">siempre igual?</span></h1>
{rayitas(20,40,70)}
<p class="mano" style="margin-top:40px;max-width:900px;font-size:40px">Usa <span class="subraya">siempre la misma imagen</span> de referencia y cuida sus rasgos principales.</p>
<div class="polaroid" style="left:90px;top:520px;width:380px;height:480px;transform:rotate(-5deg)"><img src="{SENALA}"><span class="check">✓</span><span class="etiqueta">Contenido</span></div>
{parada(-40,800)}<span class="check" style="right:420px;top:560px;left:auto;z-index:4">✓</span><span class="etiqueta" style="left:auto;right:150px;bottom:100px;z-index:4">Gym</span>{chispa(560,470,50)}{chispa(980,440,44,"var(--fucsia)")}
<div class="mano" style="position:absolute;left:70px;top:1100px;font-size:38px;max-width:560px">⚠️ <span style="color:var(--fucsia);font-family:'Permanent Marker'">No cambies</span> tu imagen de referencia a cada rato.</div>
''',

# 4 — El prompt
f'''
<h1 class="titulo"><span class="linea">El secreto está</span><span class="pincel" style="font-size:112px">en el prompt</span></h1>
{chispa(940,40,60,"var(--fucsia)")}
<div class="caja" style="margin-top:40px;font-family:'Permanent Marker';font-size:46px;text-transform:uppercase">Dale instrucciones claras</div>
<ul class="lista" style="margin-top:60px;max-width:600px">
<li><span class="ico" style="border-color:var(--fucsia);color:var(--fucsia)">✦</span><span class="txt">Rasgos de tu cara</span></li>
<li><span class="ico" style="border-color:var(--fucsia);color:var(--fucsia)">✦</span><span class="txt">Cabello y detalles</span></li>
<li><span class="ico" style="border-color:var(--fucsia);color:var(--fucsia)">✦</span><span class="txt">Estilo visual</span></li>
<li><span class="ico" style="border-color:var(--fucsia);color:var(--fucsia)">✦</span><span class="txt">Luz y calidad</span></li>
<li><span class="ico" style="border-color:var(--fucsia);color:var(--fucsia)">✦</span><span class="txt">Lo que NO debe cambiar</span></li>
</ul>
{parada(-30,760)}
{chispa(600,600,50)}{chispa(620,1180,46)}
''',

# 5 — Cierre
f'''
<h1 class="titulo"><span class="linea">🎁 Te regalo mi</span><span class="pincel" style="font-size:170px">prompt</span></h1>
{rayitas(980,60,70,giro=100)}
<p class="mano" style="margin-top:36px;max-width:640px">El mismo que usé para <span class="subraya">crear mi avatar 3D</span>.</p>
<div class="polaroid" style="left:600px;top:430px;width:420px;height:600px;transform:rotate(4deg)"><img src="{SENALA}"></div>
{chispa(520,440,56)}{chispa(1000,380,44,"var(--fucsia)")}{rayitas(40,560,60)}
<div style="position:absolute;left:60px;top:620px;z-index:4">
<div class="pincel" style="font-family:'Permanent Marker';font-size:52px;margin-left:0">Comenta “AVATAR”</div>
<div class="caja" style="display:block;margin-top:22px;font-size:40px;width:fit-content">y te lo envío gratis 💌</div>
</div>
{flecha(330,860,200,120,giro=-20)}
<div class="mano" style="position:absolute;left:64px;top:1100px;max-width:960px;font-size:38px">➕ Sígueme y aprende a crear <span class="subraya">contenido con IA</span>.</div>
''',
]
