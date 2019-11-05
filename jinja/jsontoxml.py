import json

from jinja2 import Environment, PackageLoader, select_autoescape

product_file = open('product.json', 'r')

product_json = json.loads(product_file.read())

package_loader = PackageLoader('testapp', 'templates')
env = Environment(
    loader=package_loader,
    autoescape=select_autoescape(
        enabled_extensions=['html', 'xml'],
        default_for_string=True
    )
)

template = env.get_template('product.xml')
result = template.render(product_list=product_json['products'])

xml_file = open("product_list.xml", 'w')
xml_file.write(result)
xml_file.close()
