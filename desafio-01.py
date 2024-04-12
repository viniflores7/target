#Ao final do processamento, qual será o valor da variável SOMA?

def soma(num, e=False):
    '''Def soma:
    num=índice
    para colocar o cálculo por extenso, coloque o e =True'''
    soma=0
    k=0
    for k in range(0,num+1):
        if e:
            print(f'K = {k} | SOMA = {soma} + {k}')
        soma+=k
    print(f'\n\nAo final do processamento, o valor da variável SOMA será: {soma}')

soma(13, True)
