
class Konto:
    def __init__(self):
        self.kontonr = ""
        self.saldo = 0
        self.pinkod = ""

    def Withdraw(self,belopp):
        if  belopp > self.saldo:
            return False
        self.saldo = self.saldo - belopp
        return True
    


def findKonto(lista, kontonr):
    for k in lista:
        if(k.kontonr == kontonr):
            return k
    return None


def showKontoMeny(konto):
    while True:
        print(f"*** {konto.kontonr} *** ")
        print("1. Ta ut")
        print("4. Logga ut")
        sel = input("Selection:")
        if sel == "4":
            break
        if sel == "1":
            belopp = int(input("Ange belopp att ta ut:"))
            if konto.Withdraw(belopp) == True:
                print("Uttaget klart")
            else:
                print("Belopp ej tillåtet")



listaMedKonton = []



while True:
    print("1. Skapa konto")
    print("2. Visa alla konton")
    print("3. Login")
    sel = input("Selection:")
    if sel == "3":
        knr = input("Ange kontonummer:")
        valtKonto = findKonto(listaMedKonton, knr)
        if valtKonto == None:
            print("Ogiltigt konto")
        else:
            showKontoMeny(valtKonto)

    if sel == "1":
        knr = input("Ange kontonummer:")
        pin = input("Ange pinkod:")
        k = Konto()
        k.kontonr = knr
        k.pinkod = pin
        listaMedKonton.append(k)
    if sel == "2":
        for k in listaMedKonton:
            print(f"{k.kontonr} {k.saldo}")        



# MIXED RESPONSIBILITIES

# SRP 

def calculateSalary(age, hoursWorked, hourlySalary):
    result = 0
    if age > 48:
        result = hoursWorked * hourlySalary
        if hoursWorked > 10:
            result = result * 1.10 + 2000
    else:
        result = hoursWorked * hourlySalary
        if age < 21:
            result = result * 0.9 - 10
            if result < 0:
                result = 0
    return result
    #print(f"Lön:{result}")


while True:

    age = int(input("Enter age:"))
    hoursWorked = int(input("Enter hours:"))
    hoursSalary = int(input("Enter hourly salary:"))
    result = calculateSalary(age,hoursWorked,hoursSalary)



    age = int(input("Ange din ålder:"))
    hoursWorked = int(input("Hur många timmar:"))
    hoursSalary = int(input("Ange din timlön:"))
    result = calculateSalary(age,hoursWorked,hoursSalary)
    print(f"Lön:{result}")

    

