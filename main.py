"""Travel poster: VELDROS — The Crystal Valleys. make.fun entry."""
from PIL import Image, ImageDraw, ImageFont
import math, os, random
random.seed(42)
W, H = 800, 1200
img = Image.new('RGB', (W, H), (0, 0, 0))
d = ImageDraw.Draw(img)
# Sky gradient
for y in range(H):
    t = y / H
    if t < 0.45: r, g, b = int(15+65*t/0.45), int(5+15*t/0.45), int(40+90*t/0.45)
    elif t < 0.7: s=(t-0.45)/0.25; r,g,b=int(80+175*s),int(20+100*s),int(130-70*s)
    else: s=(t-0.7)/0.3; r,g,b=int(255-75*s),int(120-60*s),int(60-40*s)
    d.line([(0,y),(W,y)], fill=(r,g,b))
# Sun
sx, sy = W//2, int(H*0.55)
for rad in range(120,30,-2): d.ellipse([sx-rad,sy-rad,sx+rad,sy+rad], fill=(255,220,180))
d.ellipse([sx-30,sy-30,sx+30,sy+30], fill=(255,240,220))
# Mountains
for lay in range(4):
    by=int(H*(0.58+lay*0.08)); col=(int(40+lay*20),int(15+lay*10),int(60-lay*10))
    pts=[(0,H)]
    for x in range(0,W+1,8):
        h=by-int(30+random.random()*(80+lay*40)*math.sin(x/200+lay)*math.sin(x/80+lay*1.7))
        pts.append((x,h))
    pts.append((W,H)); d.polygon(pts,fill=col)
# Crystals
CC=[(140,200,255),(180,160,255),(255,180,220),(160,255,220),(255,255,200)]
def K(cx,cy,w,h,col):
    dark=tuple(max(0,c-80)for c in col); light=tuple(min(255,c+60)for c in col)
    pts=[(cx,cy-h),(cx+w,cy+h*0.3),(cx+w*0.7,cy+h),(cx-w*0.7,cy+h),(cx-w,cy+h*0.3)]
    d.polygon(pts,fill=col)
    d.polygon([(cx,cy-h),(cx-w,cy+h*0.3),(cx-w*0.3,cy+h*0.3)],fill=dark)
    d.polygon([(cx,cy-h),(cx+w,cy+h*0.3),(cx+w*0.3,cy+h*0.3)],fill=light)
for i in range(5): K(int(150+random.random()*200),int(850+random.random()*100),int(15+random.random()*30),int(80+random.random()*200),random.choice(CC))
for i in range(6): K(int(500+random.random()*250),int(820+random.random()*120),int(18+random.random()*35),int(100+random.random()*250),random.choice(CC))
for i in range(4): K(int(280+random.random()*240),int(780+random.random()*80),int(10+random.random()*20),int(60+random.random()*150),random.choice(CC))
# Ground
gp=[(0,H)]
for x in range(0,W+1,5): gp.append((x,H-int(30+random.random()*40*math.sin(x/150))))
gp.append((W,H)); d.polygon(gp,fill=(20,10,30))
# Stars
for _ in range(80):
    px=int(random.random()*W); py=int(random.random()*H*0.5)
    d.ellipse([px-2,py-2,px+2,py+2],fill=(255,255,240))
# Typography
fn=None
for fp in ['/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf','/usr/share/fonts/truetype/liberation/LiberationSans-Bold.ttf']:
    if os.path.exists(fp): fn=fp; break
tf=ImageFont.truetype(fn,90)if fn else ImageFont.load_default()
sf=ImageFont.truetype(fn,32)if fn else ImageFont.load_default()
bf=ImageFont.truetype(fn,24)if fn else ImageFont.load_default()
def CT(txt,y,font,color):
    bb=d.textbbox((0,0),txt,font=font); x=(W-(bb[2]-bb[0]))//2
    d.text((x+3,y+3),txt,font=font,fill=(40,10,30)); d.text((x,y),txt,font=font,fill=color)
CT("VELDROS",420,tf,(255,240,210))
CT("T H E   C R Y S T A L   V A L L E Y S",530,sf,(220,200,255))
tl="A LAND BEYOND IMAGINATION"
bb=d.textbbox((0,0),tl,font=bf); d.text(((W-(bb[2]-bb[0]))//2,H-80),tl,font=bf,fill=(255,220,150))
d.line([(W//2-150,H-95),(W//2+150,H-95)],fill=(200,180,120),width=2)
d.line([(W//2-120,570),(W//2+120,570)],fill=(180,160,220),width=1)
os.makedirs('/output',exist_ok=True)
img.save('/output/entry.png','PNG')
