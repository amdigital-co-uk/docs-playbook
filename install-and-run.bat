@echo off
py -m pip install mkdocs-material
py -m pip install mkdocs-awesome-pages-plugin
py -m pip install mkdocs-blog-plugin
py -m pip install mkdocs-glightbox
py -m pip install mkdocs-git-revision-date-localized-plugin
py -m pip install mkdocs-git-committers-plugin-2

py -m mkdocs serve
exit