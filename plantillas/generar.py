"""Genera las imágenes de un carrusel a partir de su slides.json.

Uso:  python3 plantillas/generar.py output/<carpeta_del_carrusel>

Formato del texto en slides.json:
  [palabras]  -> resaltadas en amarillo mantequilla
  **palabras** -> en negrita
"""
import html
import json
import os
import re
import subprocess
import sys

RAIZ = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
PLANTILLAS = os.path.join(RAIZ, "plantillas")


def fmt(texto):
    t = html.escape(texto)
    t = re.sub(r"\*\*(.+?)\*\*", r"<b>\1</b>", t)
    t = re.sub(r"\[(.+?)\]", r'<span class="mark">\1</span>', t)
    return t


def img(ruta):
    return "file://" + os.path.join(RAIZ, ruta)


CSS_EXTRA = """
.portada h1{font-size:%(tam)spx;margin-top:40px;max-width:920px}
.portada .sub{font-size:38px;line-height:1.35;margin-top:32px;max-width:440px;opacity:.85}
.foto{position:absolute;right:0;bottom:150px;width:520px;height:%(alto)spx;border-radius:280px 0 0 0;overflow:hidden;border-left:10px solid var(--amarillo);border-top:10px solid var(--amarillo)}
.foto img{width:100%%;height:100%%;object-fit:cover;object-position:%(pos)s}
.flecha{position:absolute;left:88px;bottom:190px;font-weight:800;font-size:28px;letter-spacing:4px;color:var(--amarillo)}
.contenido{display:flex;flex-direction:column;justify-content:center;padding-bottom:190px}
.contenido .num{flex:none}
.num{width:120px;height:120px;border-radius:50%%;background:var(--amarillo);color:var(--negro);display:flex;align-items:center;justify-content:center;font-family:'Bricolage Grotesque',sans-serif;font-weight:800;font-size:52px}
h2{font-size:92px;margin:44px 0 60px}
ul{list-style:none;display:flex;flex-direction:column;gap:28px}
li{display:flex;gap:28px;align-items:flex-start;border-radius:28px;padding:34px 36px;font-size:36px;line-height:1.3}
.crema li{background:#fff}
.negro li{background:#1d1d1d;color:var(--crema)}
li b{font-weight:800}
.negro li b{color:var(--amarillo)}
.check{flex:none;width:52px;height:52px;border-radius:14px;background:var(--amarillo);color:var(--negro);display:flex;align-items:center;justify-content:center;font-weight:800;font-size:30px}
.parrafo{font-size:46px;line-height:1.4;max-width:860px}
.parrafo b{font-weight:800}
.negro .parrafo b{color:var(--amarillo)}
.imagen{width:100%%;border-radius:36px;overflow:hidden;border:8px solid var(--amarillo)}
.imagen img{width:100%%;display:block}
.nota{margin-top:44px;font-size:36px;font-weight:500}
.cta{display:flex;flex-direction:column;justify-content:center;padding-bottom:200px}
.cta h1{font-size:112px;margin-top:40px}
.cta .sub{font-size:38px;line-height:1.35;margin-top:40px;opacity:.85;max-width:820px}
.bio{margin-top:64px;padding-top:40px;border-top:2px solid var(--amarillo);align-self:flex-start;font-family:"Bricolage Grotesque",sans-serif;font-weight:700;font-size:44px;letter-spacing:-0.5px}
.extra{margin-top:56px;display:flex;gap:48px;font-size:28px;font-weight:500;color:var(--gris)}
.extra b{color:var(--crema);font-weight:700}
"""


def pie(i, total):
    return (f'<div class="rule"></div><div class="footer"><span>DIANA CATAÑO</span>'
            f'<span class="meta">{i} / {total}</span></div>')


def cuerpo(s, i, total):
    tipo = s["tipo"]
    if tipo == "portada":
        return (f'<span class="pill">{fmt(s["etiqueta"])}</span>'
                f'<h1>{fmt(s["titulo"])}</h1><p class="sub">{fmt(s.get("sub", ""))}</p>'
                f'<div class="foto"><img src="{img(s["foto"])}"></div>'
                f'<div class="flecha">DESLIZA →</div>' + pie(i, total))
    if tipo == "cta":
        return (f'<span class="pill" style="align-self:flex-start">{fmt(s["etiqueta"])}</span>'
                f'<h1>{fmt(s["titulo"])}</h1><p class="sub">{fmt(s.get("sub", ""))}</p>'
                f'<div class="bio">Te dejo el link en mi bio 💛</div>'
                f'<div class="extra"><span><b>Guarda</b> este post</span>'
                f'<span><b>Compártelo</b> con una amiga</span></div>' + pie(i, total))
    partes = [f'<div class="num">{i:02d}</div><h2>{fmt(s["titulo"])}</h2>']
    if "puntos" in s:
        marca = s.get("marca", "✓")
        items = "".join(
            f'<li><span class="check">{(str(n + 1) if marca == "num" else marca)}</span>'
            f'<span>{fmt(p)}</span></li>' for n, p in enumerate(s["puntos"]))
        partes.append(f"<ul>{items}</ul>")
    if "parrafo" in s:
        partes.append(f'<p class="parrafo">{fmt(s["parrafo"])}</p>')
    if "imagen" in s:
        partes.append(f'<div class="imagen"><img src="{img(s["imagen"])}"></div>')
    if "nota" in s:
        partes.append(f'<p class="nota">{fmt(s["nota"])}</p>')
    return "".join(partes) + pie(i, total)


def main(carpeta):
    carpeta = os.path.abspath(carpeta)
    datos = json.load(open(os.path.join(carpeta, "slides.json"), encoding="utf-8"))
    slides = datos["slides"]
    total = len(slides)
    build = os.path.join(carpeta, ".build")
    os.makedirs(build, exist_ok=True)
    trabajos = []
    for i, s in enumerate(slides, 1):
        extra = CSS_EXTRA % {"tam": s.get("tam_titulo", 112), "alto": s.get("alto_foto", 760),
                             "pos": s.get("pos_foto", "center top")}
        clase = s.get("fondo", "negro") + " " + s["tipo"]
        doc = (f'<!doctype html><html><head><meta charset="utf-8">'
               f'<link rel="stylesheet" href="file://{PLANTILLAS}/base.css"><style>{extra}</style></head>'
               f'<body class="{clase}">{cuerpo(s, i, total)}</body></html>')
        ruta_html = os.path.join(build, f"slide_{i:02d}.html")
        open(ruta_html, "w", encoding="utf-8").write(doc)
        trabajos.append([ruta_html, os.path.join(carpeta, f"slide_{i:02d}_{s['tipo']}.png")])
    subprocess.run(["node", os.path.join(PLANTILLAS, "render.js"), json.dumps(trabajos)],
                   check=True, cwd="/tmp")
    print(f"{total} slides generados en {carpeta}")


if __name__ == "__main__":
    main(sys.argv[1])
