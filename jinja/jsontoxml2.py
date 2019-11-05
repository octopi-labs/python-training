import json
from xml.dom.minidom import parseString

from jinja2 import Template

product_file = open('product.json', 'r')

product_json = json.loads(product_file.read())

xml = ['<?xml version="1.0" encoding="UTF-8"?>']
product_list = []
root = "<{key}>{desc}</{key}>"
group_item = "<Product>{element_list}</Product>"
line_item = "<{tag}>{desc}</{tag}>"
for key, value in product_json.items():
    if type(value) == list:
        for item in value:
            element_list = []
            if type(item) == dict:
                for tag, desc in item.items():
                    element = line_item.format(tag=tag.title(), desc=desc.title())
                    element_list.append(element)
            product_list.append(group_item.format(element_list=''.join(element_list)))
    xml.append(root.format(key=key.title(), desc=''.join(product_list)))

template = Template(''.join(xml))
result = template.render()

# Pretty Printing
dom = parseString(result)
result = dom.toprettyxml()

xml_file = open("product_list_2.xml", 'w')
xml_file.write(result)
xml_file.close()
