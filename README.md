# rpi-sampler

## Raspberry Installation

### Install pygame dependencies
```
pi@raspberrypi:~ $ sudo apt-get install mercurial python-dev python-numpy python-opengl \
    libav-tools libsdl-image1.2-dev libsdl-mixer1.2-dev libsdl-ttf2.0-dev libsmpeg-dev \
    libsdl1.2-dev libportmidi-dev libswscale-dev libavformat-dev libavcodec-dev \
    libtiff5-dev libx11-6 libx11-dev fluid-soundfont-gm  musescore-soundfont-gm\
    xfonts-base xfonts-100dpi xfonts-75dpi xfonts-cyrillic fontconfig fonts-freefont-ttf
 ```
 
### Install python virtualenv
```
pi@raspberrypi:~ $sudo pip install virtualenv
```
### Install rpi-sampler

In rpi-sampler directory:

``` 
pi@raspberrypi:~ $ cd Code/rpi-sampler
pi@raspberrypi:~/Code/rpi-sampler $ virtualenv .
pi@raspberrypi:~/Code/rpi-sampler $ source bin/activate
(rpi-sampler) pi@raspberrypi:~/Code/rpi-sampler $ pip install -r requirement.txt
(rpi-sampler) pi@raspberrypi:~/Code/rpi-sampler $ chmod +x main.py
```

### Execution

First run arduino then, on raspberry (env must be activated)
```
(rpi-sampler) pi@raspberrypi:~/Code/rpi-sampler $ ./main.py
```
