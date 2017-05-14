# P2-Physikalisches-Grundlagen-Praktikum

#### installing dependencies (debian)
```
sudo apt-get install python-pip python-dev build-essential inkscape dvipng
pip install --upgrade pip
sudo pip install setuptools
sudo pip install matplotlib numpy scipy

sudo apt-get install texlive texlive-fonts-recommended texlive-lang-german texlive-latex-base texlive-latex-extra texlive-latex-recommended lmodern latexmk
```

#### installing dependencies (arch)
```
sudo pacman -S python-pip ghostscript texlive-core texlive-latexextra texlive-science tk
sudo pip install matplotlib numpy scipy

updmap		#important! updates font cache to fix an error with pyplot
```



#### building
* run make at least once to generate common/emails.tex
* replace fake emails in common/emails.tex (not pusblished to prevent spam from crawlers)
```
cd XX-{Versuchsname}
make
```

#### other targets
* share: uploads pdf to transfer.sh
