import random
a1 = (input('Nome primeiro Aluno: '))
a2 = (input('Nome segundo Aluno: '))
a3 = (input('Nome terceiro Aluno: '))
a4 = (input('Nome do quarto Aluno: '))
l = [a1,a2,a3,a4]
luck = random.choice(l)
print ('O aluno escolhido foi: {}'.format(luck))