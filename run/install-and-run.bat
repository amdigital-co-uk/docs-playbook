@echo off
py -m pip install mkdocs-material --upgrade
py -m pip install mkdocs-awesome-pages-plugin
py -m pip install mkdocs-glightbox
py -m mkdocs serve
exit

