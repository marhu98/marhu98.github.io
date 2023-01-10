#!/usr/bin/env bash
pandoc --template default.html5 -i static/blog/*.md -o public/html/*.html
pandoc --template default.html5 -i static/blog/liesofhighschool/*.md -o public/html/*.html
