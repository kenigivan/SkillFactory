from django import template

# если мы не зарегистрируем наши фильтры, то Django никогда не узнает, где именно их искать и фильтры потеряются
register = template.Library()


@register.filter(name='Censor')
def Censor(value, arg):
    variants = ['mat', 'мат', 'перемат', 'блбл']
    for variant in variants:
        value = value.replace(variant, '*ПИП*')
    return value
