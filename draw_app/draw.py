s = input()

xl, xr, yd, yu = 0, 0, 0, 0
pos = [0, 0]

for i in s:
    if i == 'A':
        pos[0]-=1
        xl = min(xl, pos[0])
    elif i == 'a':
        pos[0]+=1
        xr = max(xr, pos[0])
    elif i == 'B':
        pos[1]-=1
        yd = min(yd, pos[1])
    else:
        pos[1]+=1
        yu = max(yu, pos[1])

args = [str(i) for i in [xl-2, xr+2, yd-2, yu+2]]

asy = open('draw_app/asy.asy', 'w')
asy.write('''settings.outformat ="png";
unitsize(2cm);

void grid(int xl, int xr, int yd, int yu) {
    for (int i = xl; i<=xr; ++i) {
        draw((i, yd) -- (i, yu));
    }

    for (int j = yd; j<=yu; ++j) {
        draw((xl, j) -- (xr, j));
    }
    draw((0, yd) -- (0, yu), arrow=ArcArrow(SimpleHead), blue + linewidth(3));
    draw((xl, 0) -- (xr, 0), arrow=ArcArrow(SimpleHead), blue + linewidth(3));
}

var pos = (0, 0);

void A(){
    draw(pos -- (pos + (-1, 0)), arrow = MidArrow(arrowhead = TeXHead), magenta + linewidth(2));
    pos = pos + (-1, 0);
}

void a(){
    draw(pos -- (pos + (1, 0)), arrow = MidArrow(arrowhead = TeXHead), magenta + linewidth(2));
    pos = pos + (1, 0);
}

void B(){
    draw(pos -- (pos + (0, -1)), arrow = MidArrow(arrowhead = TeXHead), red + linewidth(2));
    pos = pos + (0, -1);
}

void b(){
    draw(pos -- (pos + (0, 1)), arrow = MidArrow(arrowhead = TeXHead), red + linewidth(2));
    pos = pos + (0, 1);
}\n''')
asy.write('grid(%s);\n'%(','.join(args)))
for i in s:
    asy.write('%s();\n' %i)

asy.close()

help = open('draw_app/help.txt', 'w')
help.write(s)
help.close()

