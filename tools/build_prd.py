"""
Assembles the PRD from docs/prd/*.md into:
  docs/PRD_Election_Intelligence_Command_Center.md          (GitHub-readable)
  deliverables/Election_Intelligence_Command_Center_PRD.docx (styled Word)
  deliverables/Election_Intelligence_Command_Center_PRD.pdf  (via LibreOffice, if available)
Requires: pypandoc_binary, python-docx. Run from repo root after the deck has been rendered
(the PRD embeds a few slide images from deliverables/slides/).
"""
from __future__ import annotations

import glob
import os
import re
import shutil
import subprocess
import tempfile

import pypandoc
from docx import Document
from docx.oxml import OxmlElement
from docx.oxml.ns import qn
from docx.shared import Inches, Pt, RGBColor

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DOCS = os.path.join(ROOT, "docs")
OUT = os.path.join(ROOT, "deliverables")
NAVY, SAFFRON, INK, MUTED = "0B1F3A", "E2711D", "1B2330", "5B6573"

parts = sorted(glob.glob(os.path.join(DOCS, "prd", "[0-9][0-9]_*.md")))
raw = "\n\n".join(open(p, encoding="utf-8").read().strip() for p in parts) + "\n"

# 1. GitHub markdown
gh = re.sub(r"^\\newpage[ \t]*$", "", raw, flags=re.M)
md_path = os.path.join(DOCS, "PRD_Election_Intelligence_Command_Center.md")
with open(md_path, "w", encoding="utf-8") as f:
    f.write(gh)

# 2. DOCX source: page breaks + image widths
PB = '```{=openxml}\n<w:p><w:r><w:br w:type="page"/></w:r></w:p>\n```'
dx = re.sub(r"^\\newpage[ \t]*$", PB, raw, flags=re.M)
dx = re.sub(r"^(!\[[^\]]*\]\([^)]+\))[ \t]*$", r"\1{width=6.9in}", dx, flags=re.M)



def proportional_tables(text: str) -> str:
    """Rewrite pipe-table separator rows so docx column widths follow content length."""
    lines = text.split("\n")
    out = list(lines)
    i = 0
    while i < len(lines) - 1:
        if lines[i].startswith("|") and re.match(r"^\|(\s*:?-{3,}:?\s*\|)+\s*$", lines[i + 1]):
            j = i + 2
            while j < len(lines) and lines[j].startswith("|"):
                j += 1
            rows = [[c.strip() for c in l.strip().strip("|").split("|")] for l in [lines[i]] + lines[i + 2:j]]
            n = len(rows[0])
            w = [0.0] * n
            for r in rows:
                for k in range(min(n, len(r))):
                    w[k] = max(w[k], min(len(r[k]), 90) ** 0.85)
            w = [max(x, 12) for x in w]
            tot = sum(w)
            out[i + 1] = "|" + "|".join("-" * max(3, round(100 * x / tot)) for x in w) + "|"
            i = j
        else:
            i += 1
    return "\n".join(out)


dx = proportional_tables(dx)
# static contents list (LibreOffice does not refresh Word TOC fields)
heads = re.findall(r"^# (.+)$", raw, flags=re.M)
toc = "# Contents\n\n" + "\n".join("- " + re.sub(r"^(\d+)\.", r"\1\\.", h) for h in heads if h not in ("Document Control",)) + "\n\n" + PB + "\n\n"
dx = dx.replace("# Document Control", toc + "# Document Control", 1)
tmp = tempfile.mkdtemp()
ref = os.path.join(tmp, "ref.docx")
with open(ref, "wb") as f:
    f.write(subprocess.run([pypandoc.get_pandoc_path(), "--print-default-data-file", "reference.docx"],
                           capture_output=True, check=True).stdout)

# style the reference document
rd = Document(ref)
st = rd.styles


def style_font(name, size=None, color=None, bold=None, font="Arial", space_before=None, space_after=None):
    try:
        s = st[name]
    except KeyError:
        return
    s.font.name = font
    rpr = s.element.get_or_add_rPr()
    rfonts = rpr.find(qn("w:rFonts"))
    if rfonts is None:
        rfonts = OxmlElement("w:rFonts")
        rpr.append(rfonts)
    for a in ("w:ascii", "w:hAnsi", "w:cs", "w:eastAsia"):
        rfonts.set(qn(a), font)
    for a in ("w:asciiTheme", "w:hAnsiTheme", "w:cstheme", "w:eastAsiaTheme"):
        if rfonts.get(qn(a)) is not None:
            del rfonts.attrib[qn(a)]
    if size:
        s.font.size = Pt(size)
    if color:
        s.font.color.rgb = RGBColor.from_string(color)
    if bold is not None:
        s.font.bold = bold
    if not hasattr(s, "paragraph_format"):
        return
    pf = s.paragraph_format
    if space_before is not None:
        pf.space_before = Pt(space_before)
    if space_after is not None:
        pf.space_after = Pt(space_after)


style_font("Normal", 10, INK, space_after=4)
style_font("Body Text", 10, INK, space_before=2, space_after=5)
style_font("First Paragraph", 10, INK, space_before=2, space_after=5)
style_font("Compact", 9.5, INK)
style_font("Title", 26, NAVY, True, space_after=6)
style_font("Subtitle", 13, SAFFRON, False, space_after=18)
style_font("Author", 11, MUTED)
style_font("Date", 11, MUTED)
style_font("Heading 1", 18, NAVY, True, space_before=18, space_after=8)
style_font("Heading 2", 13.5, NAVY, True, space_before=14, space_after=5)
style_font("Heading 3", 11.5, SAFFRON, True, space_before=10, space_after=4)
style_font("Block Text", 10, NAVY)
style_font("Source Code", 6.3, INK, font="Courier New")
style_font("Verbatim Char", 6.3, INK, font="Courier New")
style_font("Caption", 8.5, MUTED)
style_font("Image Caption", 8.5, MUTED)
style_font("TOC Heading", 16, NAVY, True)
for sec in rd.sections:
    sec.left_margin = sec.right_margin = Inches(0.75)
    sec.top_margin = sec.bottom_margin = Inches(0.8)
rd.save(ref)

docx_path = os.path.join(OUT, "Election_Intelligence_Command_Center_PRD.docx")
pypandoc.convert_text(dx, "docx", format="markdown+pipe_tables+raw_attribute+yaml_metadata_block",
                      outputfile=docx_path,
                      extra_args=[f"--reference-doc={ref}",
                                  f"--resource-path={DOCS}:{ROOT}"])

# 3. post-process tables and add footer
d = Document(docx_path)


def shade(cell, hex_):
    tcPr = cell._tc.get_or_add_tcPr()
    shd = OxmlElement("w:shd")
    shd.set(qn("w:val"), "clear")
    shd.set(qn("w:color"), "auto")
    shd.set(qn("w:fill"), hex_)
    tcPr.append(shd)


def borders(tbl):
    tblPr = tbl._tbl.tblPr
    b = OxmlElement("w:tblBorders")
    for edge in ("top", "left", "bottom", "right", "insideH", "insideV"):
        e = OxmlElement(f"w:{edge}")
        e.set(qn("w:val"), "single")
        e.set(qn("w:sz"), "4")
        e.set(qn("w:color"), "D5DAE1")
        b.append(e)
    tblPr.append(b)
    w = OxmlElement("w:tblW")
    w.set(qn("w:w"), "5000")
    w.set(qn("w:type"), "pct")
    for old in tblPr.findall(qn("w:tblW")):
        tblPr.remove(old)
    tblPr.append(w)


for t in d.tables:
    borders(t)
    for r_i, row in enumerate(t.rows):
        for cell in row.cells:
            if r_i == 0:
                shade(cell, NAVY)
            elif r_i % 2 == 0:
                shade(cell, "F4F6F9")
            for p in cell.paragraphs:
                p.paragraph_format.space_after = Pt(1)
                p.paragraph_format.space_before = Pt(1)
                for run in p.runs:
                    run.font.size = Pt(8.5)
                    run.font.name = "Arial"
                    if r_i == 0:
                        run.font.bold = True
                        run.font.color.rgb = RGBColor(0xFF, 0xFF, 0xFF)

for sec in d.sections:
    fp = sec.footer.paragraphs[0] if sec.footer.paragraphs else sec.footer.add_paragraph()
    fp.text = ""
    r = fp.add_run("[COMPANY NAME] · Election Intelligence & Analytics Command Center — PRD v1.0 · Confidential · "
                   "Not legal advice · DEMO DATA is synthetic")
    r.font.size = Pt(7.5)
    r.font.color.rgb = RGBColor.from_string(MUTED)
d.save(docx_path)
print("docx:", docx_path)

# 4. PDF via LibreOffice (optional)
if shutil.which("soffice"):
    subprocess.run(["soffice", "-env:UserInstallation=file:///tmp/lo_profile_prd", "--headless", "--convert-to", "pdf",
                    "--outdir", OUT, docx_path], capture_output=True, timeout=600)
    pdf = docx_path.replace(".docx", ".pdf")
    if os.path.exists(pdf):
        print("pdf:", pdf)
print("md:", md_path, f"({len(gh.split()):,} words)")
