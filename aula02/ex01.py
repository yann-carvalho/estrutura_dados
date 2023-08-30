import time

def soma1(n):
    soma = 0
    for i in range (n+1):
        soma = soma + i
    return soma
def soma2(n):
    return (n*(n+1))/2

inicio=time.time()
resultado=soma1(100)
termino=time.time()
execution_time=termino - inicio
print(f'O resultado foi de: {resultado}')
print(f'Tempo de início: {inicio:.5f} segundos')
print(f'Tempo de termino: {termino:.5f} segundos')
print(f'Tempo de execução: {execution_time:.10f} segundos')
print('--------------------------------------------------------')

inicio=time.time()
resultado=soma2(100)
termino=time.time()
execution_time=termino - inicio
print(f'O resultado foi de: {resultado}')
print(f'Tempo de início: {inicio:.5f} segundos')
print(f'Tempo de termino: {termino:.5f} segundos')
print(f'Tempo de execução: {execution_time:.10f} segundos')