print ('Qual numero deseja ver o antecessor, o sucessor a raiz quadrada?')
a = int (input ('Qual numero: '))
print ('Numero é: {};\nAntecessor: {};\nSucessor: {};\nRaiz: {:0.2f}.' .format(a,a-1,a+1,a**(1/2)))