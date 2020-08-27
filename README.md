`git clone https://github.com/b1narylife/nmr.git`

`cd nmr`

`docker build -t rightmove_scraper . && docker run -v "$PWD"/data:/data rightmove_scraper`
