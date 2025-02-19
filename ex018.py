from math import sin, cos, tan, radians

an = float(input("Digite o ângulo: "))
print("O Ângulo de {} tem o SENO de {:.2f}".format(an, sin(radians(an))))
print("O Ângulo de {} tem o COSSENO de {:.2f}".format(an, cos(radians(an))))
print("O Ângulo de {} tem o TANGENTE de {:.2f}".format(an, tan(radians(an))))
