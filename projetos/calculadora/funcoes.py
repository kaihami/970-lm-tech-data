

def soma(a, b):
    if isinstance(a, (int, float)) and isinstance(b, (int, float)):
        return a + b
    else:
        raise TypeError(f"O input 'a' e 'b' devem ser um número, recebido a={a}, tipo({type(a)}), b={b} tipo ({type(b)})")

