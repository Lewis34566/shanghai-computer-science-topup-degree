import pathlib
from pypdf import PdfReader

d = pathlib.Path("sources/2026章程")
for p in sorted(d.glob("*.pdf")):
    try:
        r = PdfReader(str(p))
        txt = "\n".join((pg.extract_text() or "") for pg in r.pages)
        out = p.with_suffix(".txt")
        out.write_text(txt, encoding="utf-8")
        print(f"{p.stem}: {len(r.pages)}p {len(txt)}chars")
    except Exception as e:
        print(f"{p.stem}: ERROR {type(e).__name__} {e}")
