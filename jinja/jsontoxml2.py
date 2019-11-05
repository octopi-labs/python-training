import json
from jinja2 import Template

product_file = open('product.json', 'r')

product_json = json.loads(product_file.read())

xml = ['<?xml version="1.0" encoding="UTF-8"?>']
product_list = []
root = "<{key}>\n{desc}\n</{key}>"
group_item = "<Item>\n{element_list}\n</Item>"
line_item = "<{tag}>{desc}</{tag}>"
for key, value in product_json.items():
    if type(value) == list:
        for item in value:
            element_list = []
            if type(item) == dict:
                for tag, desc in item.items():
                    element = line_item.format(tag=tag.title(), desc=desc.title())
                    element_list.append(element)
            product_list.append(group_item.format(element_list='\n'.join(element_list)))
    xml.append(root.format(key=key.title(), desc='\n'.join(product_list)))

template = Template('\n'.join(xml))
result = template.render()

xml_file = open("product_list_2.xml", 'w')
xml_file.write(result)
xml_file.close()
