"""Genera un carrusel en estilo "libreta" (4:5, 1080×1350).

Uso:  python3 plantillas/libreta/libreta.py output/<carpeta>
La carpeta debe tener un archivo slides.py con una lista SLIDES de HTML (uno por slide)
y, opcionalmente, ESTILO = "libreta" | "conecta" | "vende" (por defecto "libreta").
Las imágenes se escriben con img('fotos_creador/archivo.jpg').
"""
import json
import os
import runpy
import subprocess
import sys

RAIZ = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
AQUI = os.path.dirname(os.path.abspath(__file__))

# Filtro SVG que le da a las cajas bordes de pincelada.
FILTRO = ('<svg width="0" height="0" style="position:absolute"><filter id="pincel">'
          '<feTurbulence type="fractalNoise" baseFrequency="0.035 0.9" numOctaves="3" seed="4"/>'
          '<feDisplacementMap in="SourceGraphic" scale="22"/></filter></svg>')


def img(ruta):
    return "file://" + os.path.join(RAIZ, ruta)


def chispa(x, y, tam=50, color="var(--morado)", giro=0):
    """Estrellita de cuatro puntas dibujada."""
    return (f'<svg class="doodle" style="left:{x}px;top:{y}px;width:{tam}px;height:{tam}px;transform:rotate({giro}deg)" '
            f'viewBox="0 0 40 40"><path d="M20 2 C22 14 26 18 38 20 C26 22 22 26 20 38 C18 26 14 22 2 20 C14 18 18 14 20 2Z" '
            f'fill="none" stroke="{color}" stroke-width="3" stroke-linejoin="round"/></svg>')


def rayitas(x, y, tam=70, color="var(--fucsia)", giro=0):
    """Tres rayitas de énfasis."""
    return (f'<svg class="doodle" style="left:{x}px;top:{y}px;width:{tam}px;height:{tam}px;transform:rotate({giro}deg)" '
            f'viewBox="0 0 40 40" stroke="{color}" stroke-width="4" stroke-linecap="round">'
            f'<path d="M6 30 L16 22"/><path d="M4 14 L16 15"/><path d="M14 2 L20 11"/></svg>')


def flecha(x, y, ancho=200, alto=120, color="var(--fucsia)", giro=0, voltear=False):
    """Flecha curva hecha a mano."""
    esc = "scaleX(-1)" if voltear else ""
    return (f'<svg class="doodle" style="left:{x}px;top:{y}px;width:{ancho}px;height:{alto}px;transform:rotate({giro}deg) {esc}" '
            f'viewBox="0 0 200 120" fill="none" stroke="{color}" stroke-width="7" stroke-linecap="round" stroke-linejoin="round">'
            f'<path d="M10 10 C 30 90, 110 110, 180 90"/><path d="M150 70 L182 90 L152 112"/></svg>')


def recorte(ruta, derecha=None, izquierda=None, alto=900, abajo=0):
    """Avatar recortado (PNG sin fondo), de pie sobre la hoja y saliendo por el borde inferior."""
    lado = f"right:{derecha}px" if izquierda is None else f"left:{izquierda}px"
    return (f'<img src="{img(ruta)}" style="position:absolute;{lado};bottom:{abajo}px;height:{alto}px;z-index:3;'
            f'filter:drop-shadow(0 8px 18px rgba(21,23,53,.18))">')


def polaroid(ruta, x, y, ancho, alto, giro=0, etiqueta="", check=False, enfoque="center"):
    """Foto con marco blanco, opcionalmente con etiqueta abajo y ✓ arriba."""
    extra = (f'<span class="etiqueta">{etiqueta}</span>' if etiqueta else "") + ('<span class="check">✓</span>' if check else "")
    return (f'<div class="polaroid" style="left:{x}px;top:{y}px;width:{ancho}px;height:{alto}px;transform:rotate({giro}deg)">'
            f'<img src="{img(ruta)}" style="object-position:{enfoque}">{extra}</div>')


def firma(i, total):
    return f'<div class="firma"><span>DIANA CATAÑO</span><span class="n">{i}/{total}</span></div>'


def main(carpeta):
    carpeta = os.path.abspath(carpeta)
    ayudas = dict(img=img, chispa=chispa, rayitas=rayitas, flecha=flecha, recorte=recorte, polaroid=polaroid)
    datos = runpy.run_path(os.path.join(carpeta, "slides.py"), init_globals=ayudas)
    slides = datos["SLIDES"]
    estilo = datos.get("ESTILO", "libreta")
    hojas = f'<link rel="stylesheet" href="file://{AQUI}/libreta.css">'
    if estilo != "libreta":
        hojas += f'<link rel="stylesheet" href="file://{RAIZ}/plantillas/{estilo}/{estilo}.css">'

    build = os.path.join(carpeta, ".build")
    os.makedirs(build, exist_ok=True)
    trabajos = []
    for i, cuerpo in enumerate(slides, 1):
        doc = (f'<!doctype html><html><head><meta charset="utf-8">'
               f'{hojas}</head>'
               f'<body class="{estilo}">{FILTRO}{cuerpo}{firma(i, len(slides))}</body></html>')
        ruta = os.path.join(build, f"slide_{i:02d}.html")
        open(ruta, "w", encoding="utf-8").write(doc)
        trabajos.append([ruta, os.path.join(carpeta, f"slide_{i:02d}.png")])
    subprocess.run(["node", os.path.join(RAIZ, "plantillas", "render.js"), json.dumps(trabajos), "1080x1350"],
                   check=True, cwd="/tmp")
    print(f"{len(slides)} slides generados en {carpeta}")


if __name__ == "__main__":
    main(sys.argv[1])
