"""
    Escribir una implementación propia de la función abs, que devuelva el valor absoluto
    de cualquier valor que reciba.
"""

def valor_absoluto(num):
    # Devuelve el valor absoluto de un número.

    if num<0:
        # num = num * -1
        num *= -1  
    
    print(num)


valor_absoluto(2)
valor_absoluto(-1)
valor_absoluto(-23)
valor_absoluto(25)
valor_absoluto(-1012)