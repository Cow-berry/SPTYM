settings.outformat ="png";
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
}
grid(-2,4,-2,5);
b();
b();
b();
a();
B();
B();
a();
B();
A();
A();
