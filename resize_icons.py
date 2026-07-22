from PIL import Image
from pathlib import Path

size = 24
for rel_path in [Path('images/primary.png'), Path('images/secondary.png')]:
    img = Image.open(rel_path).convert('RGBA')
    print(f'Before {rel_path}: {img.size}')

    square = Image.new('RGBA', (size, size), (0, 0, 0, 0))
    img_resized = img.copy()
    img_resized.thumbnail((size, size))
    x = (size - img_resized.width) // 2
    y = (size - img_resized.height) // 2
    square.paste(img_resized, (x, y), img_resized)
    square.save(rel_path)
    print(f'After  {rel_path}: {square.size}')
