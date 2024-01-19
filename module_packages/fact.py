# este módulo pode ser importado e sua função utilizada normalmente
# ou ele também pode ser utilizado e executado se rodar o script diretamente
# isso graças ao bloco de código __name__ == '__main__'
# isso torna muito útil para execução de testes
def fact(n):
    return 1 if n == 1 else n * fact(n-1)


if (__name__ == '__main__'):
    import sys
    if len(sys.argv) > 1:
        print(fact(int(sys.argv[1])))