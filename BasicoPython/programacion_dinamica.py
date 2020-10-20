def run():
    import sys
    sys.setrecursionlimit(10002)
    n = int(input('Escoge un número: '))
    # def fibonacci_recursivo(n):
    #     if n == 0 or n == 1:
    #         return 1
    #     else:
    #         return fibonacci_recursivo(n-1) + fibonacci_recursivo(n-2)
    
    # resultado = fibonacci_recursivo(n)
    # print(resultado)

    def fibonacci_dinamico(n, memo ={}):
        if n == 0 or n == 1:
            return 1
        else:
            try:
                return memo[n]
            except KeyError:
                resultado = fibonacci_dinamico(n-1, memo) + fibonacci_dinamico(n-2, memo)
                memo[n] = resultado

                return resultado
    resultado = fibonacci_dinamico(n)
    print(resultado)


if __name__ == '__main__':
    run()