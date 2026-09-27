"""Small design-system helpers for the executive deck (python-pptx)."""
from __future__ import annotations

from pptx.dml.color import RGBColor
from pptx.enum.shapes import MSO_CONNECTOR, MSO_SHAPE
from pptx.enum.text import MSO_ANCHOR, PP_ALIGN
from pptx.oxml.ns import qn
from pptx.util import Emu, Inches, Pt
from lxml import etree

# ---- tokens -------------------------------------------------------------------------------
NAVY = "0B1F3A"
NAVY2 = "132C52"
INK = "1B2330"
MUTED = "5B6573"
LINE = "D5DAE1"
SURFACE = "F4F6F9"
WHITE = "FFFFFF"
SAFFRON = "E2711D"
SAFFRON_LT = "FCE9DA"
BLUE = "2F6DB5"
BLUE_LT = "E3ECF7"
TEAL = "1A9A8F"
TEAL_LT = "DDF1EF"
GOLD = "C9A227"
OCHRE = "A67C1A"
RED = "B3261E"
RED_LT = "F8E1DF"
AMBER = "B7791F"
AMBER_LT = "FBF0DC"
GREEN = "2E7D32"
GREEN_LT = "E3F1E4"
FONT = "Arial"

W, H = 13.333, 7.5
MX = 0.6  # side margin


def rgb(h: str) -> RGBColor:
    return RGBColor.from_string(h)


def _font(run, size=14, color=INK, bold=False, italic=False, name=FONT):
    f = run.font
    f.name = name
    f.size = Pt(size)
    f.bold = bold
    f.italic = italic
    f.color.rgb = rgb(color)


def set_bullet(p, char="•", color=SAFFRON, indent=0.18):
    pPr = p._p.get_or_add_pPr()
    pPr.set("marL", str(int(Inches(indent))))
    pPr.set("indent", str(-int(Inches(indent))))
    for tag in ("a:buNone", "a:buChar", "a:buAutoNum", "a:buClr", "a:buFont"):
        for el in pPr.findall(qn(tag)):
            pPr.remove(el)
    buClr = etree.SubElement(pPr, qn("a:buClr"))
    srgb = etree.SubElement(buClr, qn("a:srgbClr"))
    srgb.set("val", color)
    buFont = etree.SubElement(pPr, qn("a:buFont"))
    buFont.set("typeface", FONT)
    bu = etree.SubElement(pPr, qn("a:buChar"))
    bu.set("char", char)


def text(slide, x, y, w, h, paras, size=14, color=INK, bold=False, align="l", anchor="t",
         margin=0.0, spacing_after=4, line_spacing=None, italic=False, autofit=False):
    """paras: str | list[str | dict | list[run]]; dict keys: t, size, color, bold, bullet, italic, align, runs."""
    tb = slide.shapes.add_textbox(Inches(x), Inches(y), Inches(w), Inches(h))
    tf = tb.text_frame
    tf.word_wrap = True
    m = Inches(margin)
    tf.margin_left = tf.margin_right = tf.margin_top = tf.margin_bottom = m
    tf.vertical_anchor = {"t": MSO_ANCHOR.TOP, "m": MSO_ANCHOR.MIDDLE, "b": MSO_ANCHOR.BOTTOM}[anchor]
    if isinstance(paras, str):
        paras = [paras]
    for i, para in enumerate(paras):
        p = tf.paragraphs[0] if i == 0 else tf.add_paragraph()
        spec = para if isinstance(para, dict) else {"t": para}
        p.alignment = {"l": PP_ALIGN.LEFT, "c": PP_ALIGN.CENTER, "r": PP_ALIGN.RIGHT}[spec.get("align", align)]
        p.space_after = Pt(spec.get("after", spacing_after))
        if line_spacing:
            p.line_spacing = line_spacing
        runs = spec.get("runs") or [{"t": spec.get("t", "")}]
        for r in runs:
            run = p.add_run()
            run.text = r["t"]
            _font(run, size=r.get("size", spec.get("size", size)), color=r.get("color", spec.get("color", color)),
                  bold=r.get("bold", spec.get("bold", bold)), italic=r.get("italic", spec.get("italic", italic)))
        if spec.get("bullet"):
            set_bullet(p, char=spec.get("char", "•"), color=spec.get("bcolor", SAFFRON),
                       indent=spec.get("indent", 0.18))
    return tb


def shape(slide, kind, x, y, w, h, fill=None, line=None, line_w=0.75, radius=None, shadow=False,
          dash=False):
    shp = slide.shapes.add_shape(kind, Inches(x), Inches(y), Inches(w), Inches(h))
    if fill:
        shp.fill.solid()
        shp.fill.fore_color.rgb = rgb(fill)
    else:
        shp.fill.background()
    if line:
        shp.line.color.rgb = rgb(line)
        shp.line.width = Pt(line_w)
        if dash:
            from pptx.enum.dml import MSO_LINE
            shp.line.dash_style = MSO_LINE.DASH
    else:
        shp.line.fill.background()
    if radius is not None and kind == MSO_SHAPE.ROUNDED_RECTANGLE:
        shp.adjustments[0] = radius
    if not shadow:
        style = shp._element.find(qn("p:style"))
        if style is not None:
            eff = style.find(qn("a:effectRef"))
            if eff is not None:
                eff.set("idx", "0")
    return shp


def box(slide, x, y, w, h, fill=SURFACE, line=None, radius=0.08, **kw):
    return shape(slide, MSO_SHAPE.ROUNDED_RECTANGLE, x, y, w, h, fill=fill, line=line, radius=radius, **kw)


def rect(slide, x, y, w, h, fill=SURFACE, line=None, **kw):
    return shape(slide, MSO_SHAPE.RECTANGLE, x, y, w, h, fill=fill, line=line, **kw)


def shape_text(shp, paras, size=12, color=INK, bold=False, align="c", anchor="m", margin=0.08):
    tf = shp.text_frame
    tf.word_wrap = True
    m = Inches(margin)
    tf.margin_left = tf.margin_right = tf.margin_top = tf.margin_bottom = m
    tf.vertical_anchor = {"t": MSO_ANCHOR.TOP, "m": MSO_ANCHOR.MIDDLE, "b": MSO_ANCHOR.BOTTOM}[anchor]
    if isinstance(paras, str):
        paras = [paras]
    for i, para in enumerate(paras):
        p = tf.paragraphs[0] if i == 0 else tf.add_paragraph()
        spec = para if isinstance(para, dict) else {"t": para}
        p.alignment = {"l": PP_ALIGN.LEFT, "c": PP_ALIGN.CENTER, "r": PP_ALIGN.RIGHT}[spec.get("align", align)]
        p.space_after = Pt(spec.get("after", 2))
        runs = spec.get("runs") or [{"t": spec.get("t", "")}]
        for r in runs:
            run = p.add_run()
            run.text = r["t"]
            _font(run, size=r.get("size", spec.get("size", size)), color=r.get("color", spec.get("color", color)),
                  bold=r.get("bold", spec.get("bold", bold)), italic=r.get("italic", spec.get("italic", False)))
        if spec.get("bullet"):
            set_bullet(p, color=spec.get("bcolor", SAFFRON))
    return shp


def circle(slide, x, y, d, fill=SAFFRON, label=None, size=14, color=WHITE, bold=True, line=None):
    c = shape(slide, MSO_SHAPE.OVAL, x, y, d, d, fill=fill, line=line)
    if label is not None:
        shape_text(c, label, size=size, color=color, bold=bold, margin=0.0)
    return c


def arrow(slide, x1, y1, x2, y2, color=MUTED, width=1.5, head=True):
    c = slide.shapes.add_connector(MSO_CONNECTOR.STRAIGHT, Inches(x1), Inches(y1), Inches(x2), Inches(y2))
    c.line.color.rgb = rgb(color)
    c.line.width = Pt(width)
    if head:
        ln = c.line._get_or_add_ln()
        tail = etree.SubElement(ln, qn("a:tailEnd"))
        tail.set("type", "triangle")
        tail.set("w", "med")
        tail.set("len", "med")
    return c


def table(slide, x, y, w, data, col_w=None, row_h=0.36, size=11, header_fill=NAVY, header_color=WHITE,
          zebra=True, first_col_bold=False, fills=None, colors=None, bold_cells=None, align=None):
    rows, cols = len(data), len(data[0])
    gt = slide.shapes.add_table(rows, cols, Inches(x), Inches(y), Inches(w), Inches(row_h * rows))
    tbl = gt.table
    # strip default style banding
    tblPr = tbl._tbl.tblPr
    tblPr.set("firstRow", "0")
    tblPr.set("bandRow", "0")
    if col_w:
        for i, cw in enumerate(col_w):
            tbl.columns[i].width = Inches(cw)
    for r in range(rows):
        tbl.rows[r].height = Inches(row_h)
        for c in range(cols):
            cell = tbl.cell(r, c)
            cell.margin_left = cell.margin_right = Inches(0.08)
            cell.margin_top = cell.margin_bottom = Inches(0.03)
            cell.vertical_anchor = MSO_ANCHOR.MIDDLE
            val = data[r][c]
            tf = cell.text_frame
            tf.word_wrap = True
            p = tf.paragraphs[0]
            p.alignment = PP_ALIGN.LEFT if not align else {"l": PP_ALIGN.LEFT, "c": PP_ALIGN.CENTER, "r": PP_ALIGN.RIGHT}[align[c]]
            run = p.add_run()
            run.text = str(val)
            if r == 0:
                _font(run, size=size, color=header_color, bold=True)
                fill = header_fill
            else:
                col = (colors or {}).get((r, c), INK)
                b = (first_col_bold and c == 0) or ((r, c) in (bold_cells or set()))
                _font(run, size=size, color=col, bold=b)
                fill = (fills or {}).get((r, c)) or ((SURFACE if r % 2 == 0 else WHITE) if zebra else WHITE)
            cell.fill.solid()
            cell.fill.fore_color.rgb = rgb(fill)
    return gt


def image(slide, path, x, y, w=None, h=None):
    kw = {}
    if w:
        kw["width"] = Inches(w)
    if h:
        kw["height"] = Inches(h)
    return slide.shapes.add_picture(path, Inches(x), Inches(y), **kw)


def pill(slide, x, y, w, label, fill=SAFFRON_LT, color=SAFFRON, size=10, h=0.3, bold=True):
    b = box(slide, x, y, w, h, fill=fill, radius=0.5)
    shape_text(b, label, size=size, color=color, bold=bold, margin=0.02)
    return b
