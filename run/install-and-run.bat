@echo off
py -m pip install mkdocs-material --upgrade
py -m pip install mkdocs-awesome-pages-plugin --upgrade
py -m pip install mkdocs-glightbox --upgrade
py -m mkdocs serve
exit

