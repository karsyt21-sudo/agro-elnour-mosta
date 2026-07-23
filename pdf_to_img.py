import fitz, os
from pathlib import Path

pdf_dir = Path('produits')
img_dir = Path('produits/img')
img_dir.mkdir(exist_ok=True)

for pdf_file in pdf_dir.glob('*.pdf'):
    doc = fitz.open(pdf_file)
    base = pdf_file.stem
    for i, page in enumerate(doc, 1):
        pix = page.get_pixmap(matrix=fitz.Matrix(1.2, 1.2))
        img = pix.tobytes('png')
        from PIL import Image
        from io import BytesIO
        im = Image.open(BytesIO(img))
        out = img_dir / f"{base}-page{i}.jpg"
        im = im.convert('RGB')
        im.save(out, 'JPEG', quality=75, optimize=True)
        print(out, round(out.stat().st_size/1024), 'KB')
    doc.close()

print('DONE')
