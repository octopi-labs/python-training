import json
import dicttoxml
from xml.dom.minidom import parseString

product_file = open('product.json', 'r')

product_json = json.loads(product_file.read())

# Normal
xml = dicttoxml.dicttoxml(product_json)

# Custom Root
# xml = dicttoxml.dicttoxml(product_json, custom_root='list')

# CDATA
# xml = dicttoxml.dicttoxml(product_json, cdata=True)

# Disable Type Attribute
# xml = dicttoxml.dicttoxml(product_json, attr_type=False)

# XML Snippet
# xml = dicttoxml.dicttoxml(product_json, root=False)
# print(xml)

# XML with Unique Ids
# xml = dicttoxml.dicttoxml(product_json, ids=True)

# Custom Item Name
# item_func = lambda x: 'product'
# xml = dicttoxml.dicttoxml(product_json, item_func=item_func)

# Pretty Printing
dom = parseString(xml)
xml = dom.toprettyxml()

xml_file = open("product_list_3.xml", 'w')
xml_file.write(xml)
xml_file.close()