import random

total_score = []


def main_lagi():
    main_lagi = input('mau main lagi? y/n:')
    if main_lagi.lower() == 'y':
        random_game()
    else:
        print('terima kasih telah bermain game')


def hitung_score(hasil):
    total_score.append(hasil)
    return total_score


def hitung_nilai_terbesar(list_nilai):
    nilai_minimal = min(list_nilai)
    return nilai_minimal


def random_game():
    percobaan = 0
    nomor_rahasia = int(random.randint(a=1, b=10))
    benar = False
    while benar != True:
        tebakan = int(input('masukkan tebakkan: '))
        if(tebakan == nomor_rahasia):
            benar = True
            hitung_score(percobaan)
            print('benar')
        elif tebakan < nomor_rahasia:
            percobaan += 1
            print('nomor anda lebih kecil dari nomor tebakan')
        elif tebakan > nomor_rahasia:
            percobaan += 1
            print('nomor anda lebih besar dari nomor tebakan')
    else:
        print('score anda: ', percobaan, 'percobaan')
        print('game selesai ')
        hasil = hitung_nilai_terbesar(total_score)
        print('nilai terbaik:', hasil, 'kali percobaa')
        main_lagi()


random_game()