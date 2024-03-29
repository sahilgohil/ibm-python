from bs4 import BeautifulSoup
import requests

html = "<!DOCTYPE html><html><head><title>Page Title</title></head><body><h3> \
<b id='boldest'>Lebron James</b></h3><p> Salary: $ 92,000,000 </p> \
<h3>Stephen Curry</h3><p> Salary: $85,000,000</p> \
<h3>Kevin Durant</h3><p> Salary: $73,200,000</p></body></html>"

soup = BeautifulSoup(html, 'html5lib')

# print(soup.prettify())
tag_object = soup.title
print("tag object:", tag_object)
tag_object = soup.h3
print("tag object:", tag_object)

tag_child = tag_object.b
print("tag child:", tag_child)

tag_parent = tag_child.parent
print("tag parent:", tag_parent)

tag_sibling = tag_object.next_sibling
print("tag sibling:", tag_sibling)

sibling2 = tag_sibling.next_sibling
print("sibling2:", sibling2)

next_sibling = sibling2.next_sibling
print("next_sibling:", next_sibling)
