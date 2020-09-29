n1=int(input('Qual primeiro número: '))
n2=int(input('Qual segundo número: '))
s=n1+n2
d=n1/n2
m=n1*n2
e=n1**n2
print('A calculos números {0} e {1} é:\nSoma {2};\nMutiplicação {3}; \nDivisão {4:0.3f};\nProtência {5}.' .format(n1,n2,s,m,d,e))
