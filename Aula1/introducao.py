import statistics as es

historia_n1 = float(input('digite a primeira nota: ')) 
historia_n2 = float(input('digite a segunda nota: '))

lista_notas = [historia_n1, historia_n2]
media = es.mean(lista_notas)
print(media)

if media >=7:
    print('aprovado')

elif media >=5 and media < 7:
    print('recuperacao')

else:
    print('reprovado')