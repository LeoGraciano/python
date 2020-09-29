import math
an=float (input('Qual o Angulo que deseja: '))
se = math.sin(math.radians(an))
co = math.cos(math.radians(an))
tg = math.tan(math.radians(an))
print ('Seno do anglo é {:.2f};\nCosseno do Anglo é {:.2f};\nTangente anglo é {:.2f}.'.format(se,co,tg))