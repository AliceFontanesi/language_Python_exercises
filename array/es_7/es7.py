arr = []
num = input("Inserisci numero: ")
while num!=0:
    arr.append(num)
    num = int(input("Inserisci numero: "))

if len(arr)%2 == 0:
    print("La dimensione dell'array � pari")
else:
    print("La dimensione dell'array � dispari")
    
