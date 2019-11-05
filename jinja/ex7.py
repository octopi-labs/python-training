# -*- coding: utf-8 -*-
import math
from datetime import datetime

from jinja2 import Environment, PackageLoader, select_autoescape


def is_prime(n):
    if n == 2:
        return True
    for i in range(2, int(math.ceil(math.sqrt(n))) + 1):
        if n % i == 0:
            return False
    return True


package_loader = PackageLoader('testapp', 'templates')
env = Environment(
    loader=package_loader,
    autoescape=select_autoescape(
        enabled_extensions=['html', 'xml'],
        default_for_string=True
    )
)
env.tests['prime'] = is_prime

template = env.get_template('tests.html')

print(template.render(name='Rahul', number=24))
