#!/usr/bin/env python3

import sys
from svgwrite import Drawing
from random import randint

if len(sys.argv) < 4:
    print('usage: {} <rows> <columns> <outfile>'.format(sys.argv[0]))
    raise SystemExit

dpi = 96
scale = dpi/25.4
fillet_rad = 2.5*scale
circle_rad = 1.25*scale
circle_grid = 5*scale
rect_w = 43.*scale
rect_h = 12.7*scale

border = 5*scale
xoff = rect_w/2 + border
yoff = rect_h/2 + border

def generate(d, rows, cols):
    vals = []
    while len(vals) < (rows*cols):
        rand = randint(0, 65536)
        rand |= 1 | (1<<7) | (1<<8) | (1<<15)
        top = bin(rand)[3:9]
        bottom = bin(rand)[10:16]
        if bin(rand).count('1') == 10 and (top != reversed(bottom)) and not rand in vals:
            vals.append(rand)

    row_col = []
    for r in range(rows):
        for c in range(cols):
            row_col.append((r,c))
    gen = zip(row_col, vals)

    for (r, c), spots in gen:
        xoff2 = xoff + c*(rect_w + border)
        yoff2 = yoff + r*(rect_h + border)

        # draw rounded rectangle
        cmds = [
            'M {} {}'.format(-rect_w/2 + fillet_rad + xoff2, rect_h/2 + yoff2),
            'A{},{} 0 0,1 {},{}'.format(fillet_rad, fillet_rad, -rect_w/2 + xoff2, rect_h/2 - fillet_rad + yoff2),
            'L {} {}'.format(-rect_w/2 + xoff2, -rect_h/2 + fillet_rad + yoff2),
            'A{},{} 0 0,1 {},{}'.format(fillet_rad, fillet_rad, -rect_w/2 + fillet_rad + xoff2, -rect_h/2 + yoff2),
            'L {} {}'.format(rect_w/2 - fillet_rad + xoff2, -rect_h/2 + yoff2),
            'A{},{} 0 0,1 {},{}'.format(fillet_rad, fillet_rad, rect_w/2 + xoff2, -rect_h/2 + fillet_rad + yoff2),
            'L {} {}'.format(rect_w/2 + xoff2, rect_h/2 - fillet_rad + yoff2),
            'A{},{} 0 0,1 {},{}'.format(fillet_rad, fillet_rad, rect_w/2 - fillet_rad + xoff2, rect_h/2 + yoff2),
            'z'
            ]

        d.add(dwg.path(d=''.join(cmds), fill='black', stroke='none'))

        for i in range(8):
            if spots & (1<<i):
                d.add(dwg.circle(center=((-3.5 + i)*circle_grid + xoff2, circle_grid/2 + yoff2), r=circle_rad, fill='white'))
            if spots & (1<<(i+8)):
                d.add(dwg.circle(center=((-3.5 + i)*circle_grid + xoff2, -circle_grid/2 + yoff2), r=circle_rad, fill='white'))

rows = int(sys.argv[1])
cols = int(sys.argv[2])
dwg = Drawing(filename=sys.argv[3], debug=True)
generate(dwg, rows, cols)

dwg.save()
