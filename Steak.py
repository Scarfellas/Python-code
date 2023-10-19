#Melhoria sobre o cidgo inicial solicitado no ex01.


print("Escolha seu ponto preferido:")
print("Digite: (1)Mal passada, (2)Ao ponto para mal, (3)Ao ponto, (4)Ponto bem passado, (5)bem passada.")
ponto_da_carne = input("Qual o ponto da carne gostaria? ")

try:
   ponto_da_carne = int(ponto_da_carne)
except: 
   print("Digite um valor entre 1 e 5 para definir o ponto: ")
   ponto_da_carne = int(input("Qual o ponto da carne gostaria? "))

if ponto_da_carne <1:
   print("Digite um valor entre 1 e 5 para definir o ponto: ")
   ponto_da_carne = int(input("Qual o ponto da carne gostaria? "))
if ponto_da_carne >5:
   print("Digite um valor entre 1 e 5 para definir o ponto: ")
   ponto_da_carne = int(input("Qual o ponto da carne gostaria? "))


if ponto_da_carne == 1:
   print("Ola sua carne sera Mal passada.")
if ponto_da_carne == 2:
   print("Ola sua carne sera Ao ponto para mal.")
if ponto_da_carne == 3:
   print("Ola sua carne sera Ao ponto.")
if ponto_da_carne == 4:
   print("Ola sua carne sera: Ao ponto bem passado.")
if ponto_da_carne == 5:
   print("Ola sua carne sera: Bem passada.")