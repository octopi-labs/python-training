# -*- coding: utf-8 -*-
from jinja2 import Environment, PackageLoader, select_autoescape


package_loader = PackageLoader('testapp', 'templates')
env = Environment(
    loader=package_loader,
    autoescape=select_autoescape(['html', 'xml'])
)

template = env.get_template('variable.html')

print(template.render(name='<script>Rahul</script>'))
