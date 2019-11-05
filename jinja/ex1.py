from jinja2 import Template

template = Template("Hello {{ name }}")
result = template.render(name="Rahul Shelke")
print(result)



'''
{% condifions/loops %} => Statements
{{ print }} => Expression
{# comment #} => Comments
'''