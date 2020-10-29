from django import template

register = template.Library()


@register.filter(name='cut')
def cut(value, arg):
    """
    This cuts out all the values of arg from string
    :param value:
    :param arg:
    :return:
    """
    return value.replace(arg, '')

# you can use this or code line 6
# register.filter('cut', cut)
