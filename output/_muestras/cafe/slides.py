# Muestras de portada con el café agregado a la paleta
ESTILO = "vende"
CAMISA = "fotos_creador/avatar_camisa.png"
CAFE = "#8a4232"

SLIDES = [
# A — Fondo café, títulos crema/amarillo/rosado
f'''<div style="position:absolute;inset:0;background:{CAFE};background-image:radial-gradient(rgba(255,236,143,.16) 3px,transparent 3px);background-size:44px 44px"></div>
<span class="etq" style="background:var(--fucsia);color:#fff">✨ Opción A · fondo café</span>
<h1 class="grande" style="margin-top:40px;font-size:104px;text-shadow:4px 4px 0 #5a2a20">Crea tu<br><span style="color:var(--lila)">avatar 3D</span><br><span style="color:var(--fucsia)">estilo</span><br>muñeca</h1>
{recorte(CAMISA, derecha=30, alto=940)}''',
# B — Fondo crema con títulos y detalles en café
f'''<div style="position:absolute;inset:0;background:#fff4e6;background-image:radial-gradient(rgba(138,66,50,.12) 3px,transparent 3px);background-size:44px 44px"></div>
<style>.firma{{color:#8a4232 !important}} .firma .n{{color:var(--fucsia) !important}}</style><span class="etq" style="background:{CAFE};color:var(--lila)">✨ Opción B · crema y café</span>
<h1 class="grande" style="margin-top:40px;font-size:104px;color:{CAFE};text-shadow:4px 4px 0 var(--lila)">Crea tu<br><span style="color:var(--fucsia);text-shadow:4px 4px 0 #d0438a">avatar 3D</span><br>estilo<br>muñeca</h1>
{recorte(CAMISA, derecha=30, alto=940)}''',
# C — Rosado con franja café y título amarillo
f'''<div style="position:absolute;left:0;right:0;bottom:0;height:430px;background:{CAFE}"></div>
<span class="etq">✨ Opción C · rosado + café</span>
<h1 class="grande" style="margin-top:40px;font-size:104px">Crea tu<br><span class="amar">avatar 3D</span><br>estilo<br>muñeca</h1>
{recorte(CAMISA, derecha=30, alto=940)}''',
]
