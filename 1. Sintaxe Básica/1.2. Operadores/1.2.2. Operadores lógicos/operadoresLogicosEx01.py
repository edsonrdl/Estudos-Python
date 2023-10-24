#Operador and (E lógico):
#O operador and retorna verdadeiro se ambas as condições forem verdadeiras.

#Ex: 01
verdadeiro01 = True
falso01 = False

resultado01 = verdadeiro01 and falso01
#print("Resultado vai ser ",resultado01,",porque para ser verdadeiro as duas tem que ser verdadeiras")  # Resultado: False

#Ex :02
verdadeiro02 = True
verdadeiro022 = True

resultado02 = verdadeiro01 and verdadeiro022
#print("Resultado vai ser ",resultado02,",porque as duas são verdadeiras")  # Resultado: true

#Operador or (OU lógico):
#O operador or retorna verdadeiro se pelo menos uma for verdadeira.

#Ex:01
a = True
b = False
resultado1 = a or b
resultado2 = b or b

#print("Resultado vai ser ",resultado1,",porque a primeira é verdadeira") # Resultado: true
#print("Resultado vai ser ",resultado2,",porque as duas são falsas") # Resultado: false


#Operador not (NÃO lógico):
#O operador not inverte o valor de uma expressão booleana. Ou seja, se a expressão for verdadeira, not a torna falsa, e vice-versa.

num=10>50;
print("O reultado  vai ser ",num,",porque antes de usar o not") # Resultado: false
testeNot=not num
##print("Resultado vai ser ",testeNot,",após usar o not") # Resultado: True