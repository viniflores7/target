def reverse_string(str):
    '''str = string a ser revertida'''
    str_reverse = ''
    letras = len(str)
    qnt = 1
    while qnt <= letras:
        str_reverse+=str[-qnt]        
        qnt+=1
    return str_reverse

print(reverse_string('bau'))
