# -*- coding: utf-8 -*-
from jinja2 import Environment, PackageLoader, select_autoescape
from datetime import datetime

def datetimeformat(value, format='%H:%M / %d-%m-%Y'):
    return value.strftime(format)


package_loader = PackageLoader('testapp', 'templates')
env = Environment(
    loader=package_loader,
    autoescape=select_autoescape(
        enabled_extensions=['html', 'xml'],
        default_for_string=True
    )
)
env.filters['datetimeformat'] = datetimeformat

template = env.get_template('format.html')

print(template.render(name='Rahul', pub_date=datetime.now()))
