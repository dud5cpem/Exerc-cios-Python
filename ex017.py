co = float(input('Digite o valor do cateto oposto: '))
ca = float(input('Digite o valor do cateto adjacente: '))
s1 = co * co
s2 = ca * ca
soma = s1 + s2
hip = soma ** (1/2)
print("A hipotenusa irá medir: {:.2f}".format(hip))
