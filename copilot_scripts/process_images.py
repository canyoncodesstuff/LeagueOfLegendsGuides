from pathlib import Path
from PIL import Image

root = Path('images')
processed = root / 'processed'
processed.mkdir(exist_ok=True)

mapping = {
    'ArcaneComet.png': 'arcane_comet.png',
    'Conqueror.png': 'conqueror.png',
    'FirstStrike.png': 'first_strike.png',
    'GlacialAugment.png': 'glacial_augment.png',
    'RunesIcon.png': 'runes_icon.png',
    'Seraphine_0.jpg': 'seraphine_render.png',
    'primary.png': 'custom_primary.png',
    'secondary.png': 'custom_secondary.png',
}

sources = [
    root / 'runes' / 'sorcery' / 'keystones' / 'ArcaneComet.png',
    root / 'runes' / 'precision' / 'keystones' / 'Conqueror.png',
    root / 'runes' / 'inspiration' / 'keystones' / 'FirstStrike.png',
    root / 'runes' / 'inspiration' / 'keystones' / 'GlacialAugment.png',
    root / 'runes' / 'RunesIcon.png',
    root / 'champions_centered' / 'Seraphine_0.jpg',
    root / 'custom_emojis' / 'primary.png',
    root / 'custom_emojis' / 'secondary.png',
]

for src in sources:
    if not src.exists():
        continue
    img = Image.open(src).convert('RGBA')
    size = 24
    canvas = Image.new('RGBA', (size, size), (0, 0, 0, 0))
    img.thumbnail((size, size))
    x = (size - img.width) // 2
    y = (size - img.height) // 2
    canvas.paste(img, (x, y), img)
    target_name = mapping.get(src.name, src.stem)
    target_path = processed / f'{target_name}.png'
    canvas.save(target_path)
    print(target_path)
