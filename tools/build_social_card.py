from pathlib import Path
assets = Path(__file__).resolve().parent.parent/'dist/assets'
# A locally rendered sharing graphic uses the same original eye motif and palette.
from PIL import Image, ImageDraw, ImageFont
image = Image.new('RGB', (1200, 630), '#000000')
draw = ImageDraw.Draw(image)
headline = ImageFont.truetype(str(assets/'bebas-neue.ttf'), 145)
small = ImageFont.truetype(str(assets/'bebas-neue.ttf'), 24)
draw.text((65, 70), 'SE RØDT', font=headline, fill='#ffc348')
draw.text((65, 240), 'GYS I ALLE', font=headline, fill='#f5e9d2')
draw.text((65, 365), 'FARVER.', font=headline, fill='#ffc348')
draw.text((70, 550), '30.–31. OKTOBER · REFSHALEØEN · 18+', font=small, fill='#f5e9d2')
draw.rounded_rectangle((785, 80, 1140, 530), radius=4, fill='#dfa0a3', outline='#291419', width=5)
draw.polygon([(805, 300),(850, 245),(960, 205),(1070, 245),(1120, 300),(1070, 355),(960, 395),(850, 355)], fill='#f5e9d2', outline='#291419', width=8)
draw.ellipse((892, 205, 1028, 395), fill='#ffc348', outline='#291419', width=8)
draw.ellipse((930, 245, 990, 355), fill='#291419')
draw.ellipse((968, 260, 985, 286), fill='#f5e9d2')
image.save(assets/'social-card.png', optimize=True)
print('Delingsbillede opdateret.')
