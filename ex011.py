largura = float(input("Largura da parede: "))
altura = float(input("Altura da parede: "))
area = largura * altura
print("a dimensão da sua parede de {}x{} equivale a soma da sua área {}m²".format(largura, altura, area))
tinta = area /2
print("para pintar essa parede, você precisará de: {}l de tinta".format(tinta))