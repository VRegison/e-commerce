from django.template import Library
from utils import utils
register = Library()

@register.filter
def formata_preco(val):
   return utils.formata_preco(val)

@register.filter
def diminuir(str):
    max = 100 # Numero Maximo de caracteres Permitidos.
    if len(str) > max:
        return str[:max]
    else:
        return str