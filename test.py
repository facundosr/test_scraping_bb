
lista = [1,8,26,4,2,9,45,33,52,11,18,13]
par = []
impar = []
suma=0

for i in lista:
    suma += i
    if i % 2==0:
        par.append(i)
    else:
        impar.append(i)

print(par)
print(impar)
print(len(lista))
print(suma)      



# En base a la lista informada

#Crear una lista llamada "Par", agregando de la lista original los números pares

#Crear una lista llamada "Impar", agregando de la lista original los números impares

#Imprimir la cantidad y la suma de elementos de la lista inicial