from django import template

register = template.Library()

@register.filter
def get_food_class(food_type):
    classes = {
        'lunch': 'bg-warning text-dark',
        'dinner': 'bg-dark text-white',
        'drinks': 'bg-info text-white',
        'desserts': 'bg-success text-white',
    }
    return classes.get(food_type, 'bg-secondary text-white')
