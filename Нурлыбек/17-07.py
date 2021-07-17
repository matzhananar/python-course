ferzx = int(input())
ferzy = int(input())

figurx = int(input())
figury = int(input())

difx = ferzx - figurx
dify = ferzy - figury

if difx<0:
    difx = -difx
if dify<0:
    dify = -dify

if difx == dify or (ferzx == figurx or ferzy == figury):
    print("Ферзь бьет")
else:
    ("ферзь не бьет")