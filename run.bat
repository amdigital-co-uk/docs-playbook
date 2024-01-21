echo off
py -m pip install mkdocs-material
py -m pip install mkdocs-awesome-pages-plugin
pip install mkdocs-glightbox

py -m mkdocs serve
exit