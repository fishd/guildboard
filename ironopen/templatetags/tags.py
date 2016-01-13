from django import template

register = template.Library()

@register.simple_tag
def boostrap_me(field_html):

# @register.simple_tag
# def record_as_row(record):
    
