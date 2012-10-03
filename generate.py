#! /usr/bin/env python
from markdown import markdown

template = open('./template.html').read().decode('utf8')
index = open('./index.md').read().decode('utf8')
output = open('./index.html', 'w')

html = markdown(index, extras=[])
output.write(template.replace('{body}', html).encode('utf8'))
