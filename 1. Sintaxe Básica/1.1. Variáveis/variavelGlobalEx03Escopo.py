# Escopo Global 

#Ex : 01
num1=10

def testeDeVariavelEx01():
    print(num1)
testeDeVariavelEx01()


# Ex : 02
def testeDeVariavelEx02():
    global num2;num2=20  #Declara a váriavel global e depois o valor na mesma linha usando o (;) ou na outra linha 
testeDeVariavelEx02()
print(num2)