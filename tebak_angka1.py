from random import randint
print("Hai.. Saya A1 Bot, saya telah memilih sebuah bilangan bulat secara acak antara 0 s/d 10. Silakan tebak ya :P")
score = 10
AngkaRahasia = randint(0, 10)
while(True):
    if(score < 1):
        print("\nAnda sudah tidak diperbolehkan bermain karena score sudah habis")
        break
    tebak = int(input("Tebakan Anda: "))
    if(tebak > AngkaRahasia):
        print("Bilangan tebakan anda terlalu besar")
    elif(tebak < AngkaRahasia):
        print("Bilangan tebakan anda terlalu kecil")
    else:
        print("Hore.... Bilangan tebakan anda BENAR :-)")
        print("\nScore Anda: ",score)
        break
    score -= 2