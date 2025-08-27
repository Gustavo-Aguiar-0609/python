#importando a biblioteca math
import math
#entrada de catetos
ctt_oposto = float(input("Digite o cateto oposto -->"))
ctt_adjascente = float(input("Digite o cateto adjascente -->"))
#calculo dos catetos
hipotenusa = math.sqrt(ctt_oposto**2 + ctt_adjascente**2)
#imprime o resultado
print("O vgalor da hipotenusa é: ",hipotenusa)



