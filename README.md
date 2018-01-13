## Printable shaper fiducials for use with the Shaper Origin
(https://shapertools.com/)

Inferred fiducial features:
- there are always 10 dots
- the left-most and right-most columns are always present
- must not be rotationally-symmetric

#### Dependencies
```bash
sudo pip3 install svgwrite
```

#### Usage
```bash
./generate.py <rows> <cols> <output path/foo.svg>
```

#### Example 3x3 output:
<img src="./test.svg">

