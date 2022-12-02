def diminuir(str):
    max = 1000 # Numero Maximo de caracteres Permitidos.
    if len(str) > max:
        return str[:max]
    else:
        return str