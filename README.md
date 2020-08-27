`git clone https://github.com/b1narylife/nmr.git`

`cd nmr`

`docker build -t rightmove_scraper . && docker run -v "$PWD"/data:/data rightmove_scraper`

### Example Console Output
```
--------
6 bedroom town house
New Mills Yard,Norwich,NR3
£2,640pcm
Added on 29/05/2020 by Kent Property Management Lettings & Sales, Norwich
01603 950040
--------
2 bedroom apartment
Unthank Road, NORWICH
£1,100pcm
Added on 28/05/2020 by William H. Brown - Lettings, Norwich  Lettings
01603 950091
--------
6 bedroom house
Colman Road, Norwich
£2,400pcm
Reduced on 26/05/2020 by abbotFox, Norwich
01603 950005
```