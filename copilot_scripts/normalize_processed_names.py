from pathlib import Path
import os

root = Path('images/processed')
for p in root.glob('*.png'):
    if p.name.endswith('.png.png'):
        os.rename(p, root / p.name[:-4])
