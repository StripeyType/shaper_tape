## Printable shaper fiducials for use with the Shaper Origin
(https://shapertools.com/)

Inferred fiducial features:
- there are always 10 dots
- the left-most and right-most columns are always present

Most (~97%) but not all generated fiducials appear to be accepted by the Origin.

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

