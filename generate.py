#! /usr/bin/env python3
from markdown import markdown

template = open('./template.html').read()#.decode('utf8')
index = open('./index.md').read()#.decode('utf8')
output = open('./index.html', 'w')

output.write(template.replace('{body}', markdown(index)))
