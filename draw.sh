#!/bin/sh
python3 draw_app/draw.py
asy draw_app/asy.asy
mv asy.png pics/`cat draw_app/help.txt`.png
rm draw_app/help.txt

