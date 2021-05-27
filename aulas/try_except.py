"""
boloco try/except/ else/finally

- Utilizamos para tratar erros;
- A forma geral mais simples é:
try:
    //execução problematica
except:
    // o q deve ser feito caso ocorra o problema

(não é necessario usar oq vem a baixo para q o bloco funcione)

else:
    // não ocorreu o erro entao vai acontecer oq estiver aqui

finally:
    // sempre é executado (geralmente usado para fechar ou deslocar recursos, ex: banco de dados)

////////////////////////////////////////////////////////////////////////////////////////////////////
# Exemplo 1 - erro generico

try:
    sexo()
except:
    print('deu merda')
# tente executar a função sexo(), se der algum erro imprima a mensagem de erro

# Exemplo 2 - erro generico

try:
    len(42)
except:
    print('deu merda')
# tente executar a função sexo(), se der algum erro imprima a mensagem de erro
-------------------------------------------------------------------------------

# Exemplo 3 - erro expecifico

try:
    len(42)
except TypeError:
    print('vc esta utilizando uma função inexistente')

# Exemplo 4 - erro expecifico

try:
    sexo()
except NameError:
    print('vc esta utilizando uma função inexistente')
-------------------------------------------------------------
# Exemplo 5 - erro expecifico com detalhes do erro

try:
    len(42)
except TypeError as err:
    print(f'a aplicação gerou o seguinte erro: {err}')

# a aplicação gerou o seguinte erro: object of type 'int' has no len()
----------------------------------------------------------------------

# Exemplo 6 - podemos tratar diversos erros de uma vez
try:
    print('sexo'[42])
except NameError as erra:
    print(f'a aplicação gerou o seguinte erro: {erra}')
except TypeError as errb:
    print(f'a aplicação gerou o seguinte erro: {errb}')
except:
    print('deu algum erro diferente')
-------------------------------------------------------------
# Exemplo 7 - usando ele em uma função


def pega_valor(dicionario, chave):
    try:
        return dicionario[chave]
    except KeyError:
        return None
    except TypeError:
        return None


dic = {'nome': 'sexo'}

print(pega_valor(dic, 42))

////////////////////////////////////////////////

# Else

try:
    num = int(input('informe um numero: '))
except ValueError:
    print('valor incorreto! ')
else:
    print(f'voce digitou {num}')

//////////////////////////////////////////////////

# Finally

try:
    num = int(input('informe um numero: '))
except ValueError:
    print('vc nao digitou um valor valido! ')
else:
    print(f'voce digitou {num}')
finally:
    print('! executando o finally !')
# OBS: o finally SEMPRE vai ser EXECUTADO

///////////////////////////////////////////

# Exemplo de tratamento ERRADO


def divisao(a, b):
    return a / b


num1 = int(input('informe o primeiro numero: '))
try:
    num2 = int(input('informe o segundo numero: '))
except ValueError:
    print('o valor precisa ser numerico!')

try:
    print(divisao(num1,num2))
except NameError:
    print('valor incorreto!')
----------------------------------------

# Exemplo de tratamento CERTO
# vc é o responsavel por sua função e por tratar oq vai entrar nela!!!


def divisao(a, b):
    try:
        return int(a) / int(b)
    except ValueError:
        return 'valor incorreto!'
    except ZeroDivisionError:
        return 'Não é possivel dividir por zero!'


num1 = input('informe o primeiro numero: ')
num2 = input('informe o segundo numero: ')

print(divisao(num1, num2))

------------------------------------------------------------
# Exemplo de tratamento CERTO ( Completamente generico )


def divisao(a, b):
    try:
        return int(a) / int(b)
    except:
        return 'Ocorreu um problema!'


num1 = input('informe o primeiro numero: ')
num2 = input('informe o segundo numero: ')

print(divisao(num1, num2))
-------------------------------------------------

# Exemplo de tratamento CERTO ( Parcialmente Generico )


def divisao(a, b):
    try:
        return int(a) / int(b)
    except (ValueError, ZeroDivisionError) as err:
        return f'Ocorreu o problema: {err}'


num1 = input('informe o primeiro numero: ')
num2 = input('informe o segundo numero: ')

print(divisao(num1, num2))


"""

# Exemplo de tratamento CERTO ( Parcialmente Generico )


def divisao(a, b):
    try:
        return int(a) / int(b)
    except (ValueError, ZeroDivisionError) as err:
        return f'Ocorreu o problema: {err}'


num1 = input('informe o primeiro numero: ')
num2 = input('informe o segundo numero: ')

print(divisao(num1, num2))
