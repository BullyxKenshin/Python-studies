import random

myscore, itsscore = 0, 0

while True:
    print("-"*50)
    print("\n1 - Taş\n2 - Kağıt\n3 - Makas\n")
    kullanici = input("Seçimini yap: ")
    rakip= random.choice(["1", "2", "3"])

    if kullanici == "1":
        if rakip== "1":
            print("Rakibin seçimi: Taş\nBerabere. Skor yok!")

        elif rakip== "2":
            print("Rakibin seçimi: Kağıt\nKaybettin!")
            itsscore += 100
            print("\nSenin skorun: {}\nRakibin skoru: {}".format(myscore, itsscore))

        elif rakip== "3":
            print("Rakibin seçimi: Makas\nKazandın!")
            myscore += 100
            print("\nSenin skorun: {}\nRakibin skoru: {}".format(myscore, itsscore))

    elif kullanici == "2":
        if rakip== "1":
            print("Rakibin seçimi: Taş\nKazandın!")
            myscore += 100
            print("\nSenin skorun: {}\nRakibin skoru: {}".format(myscore, itsscore))

        elif rakip== "2":
            print("Rakibin seçimi: Paper\nBerabere. Skor yok!")

        elif rakip== "3":
            print("Rakibin seçimi: Makas\nKaybettin!")
            itsscore += 100
            print("\nSenin skorun: {}\nRakibin skoru: {}".format(myscore, itsscore))

    elif kullanici == "3":
        if rakip== "1":
            print("Rakibin seçimi: Taş\nKaybettin!")
            itsscore += 100
            print("\nSenin skorun: {}\nRakibin skoru: {}".format(myscore, itsscore))

        elif rakip== "2":
            print("Rakibin seçimi: Kağıt\nKazandın!")
            myscore += 100
            print("\nSenin skorun: {}\nRakibin skoru: {}".format(myscore, itsscore))

        elif rakip== "3":
            print("Rakibin seçimi: Makas\nBerabere. Skor yok!")

    else:
        break
