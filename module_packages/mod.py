# aqui criamos um arquivo com codigo simples como exemplo
# ele será importado no arquivo jupyter

s = "This is a string"
a = [100, 200, 300]


def printy(arg):
    print(f'arg = {arg}')


class Classy:
    pass


x = Classy()

# esses comandos abaixo vão ser executados se vc importar o
# módulo mod no terminal de python interativo
#print(x)
#print('\nacima é a classe')
#print('\ngood day!')

# ao importar mod, talvez vc não queira que este código de print acima seja executado
# este bloco de código pode ser somente para fazer algum teste
# podemos fazer com q esse output seja opcional
# vamos comentar o código acima e colocá-lo dentro do bloco __name__ == '__main__'
# geralmente esse tipo de estrutura é feito quando se quer executar testes
if (__name__ == '__main__'):
    print(x)
    print('\nacima é a classe')
    print('\ngood day!')
