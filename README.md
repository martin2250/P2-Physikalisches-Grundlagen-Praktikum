# P2-Physikalisches-Grundlagen-Praktikum

#### installing dependencies
```
sudo apt-get install python-pip python-dev build-essential
pip install --upgrade pip
sudo pip install setuptools
sudo pip install matplotlib numpy scipy

sudo apt-get install texlive texlive-fonts-recommended texlive-lang-german texlive-latex-base texlive-latex-extra texlive-latex-recommended lmodern latexmk
```

#### building
* run make at least once to generate common/emails.tex
* replace fake emails in common/emails.tex (not pusblished to prevent spam from crawlers)
```
cd XX-{Versuchsname}
make
```

#### other targets
* upload: uploads pdf to gdrive (credentials are stored in home folder)
* share: uploads pdf to transfer.sh
