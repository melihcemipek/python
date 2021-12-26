burclar = {
    "Ocak": {
        "Oğlak": list(range(1, 21)),
        "Kova": list(range(21, 32)),
    },
    "Şubat": {
        "Kova": list(range(1, 19)),
        "Kova": list(range(21, 30)),
    },
    "Mart": {
        "Balık": list(range(1, 21)),
        "Koç": list(range(21, 32)),
    },
    "Nisan": {
        "Koç": list(range(1, 21)),
        "Boğa": list(range(21, 32)),
    },
    "Mayıs": {
        "Boğa": list(range(1, 21)),
        "İkizler": list(range(21, 32)),
    },
    "Haziran": {
        "İkizler": list(range(1, 22)),
        "Yengeç": list(range(21, 32)),
    },
    "Temmuz": {
        "Yengeç": list(range(1, 23)),
        "Aslan": list(range(21, 32)),
    },
    "Ağustos": {
        "Aslan": list(range(1, 23)),
        "Başak": list(range(21, 32)),
    },
    "Eylül": {
        "Başak": list(range(1, 23)),
        "Terazi": list(range(21, 32)),
    },
    "Ekim": {
        "Terazi": list(range(1, 24)),
        "Akrep": list(range(21, 32)),
    },
    "Kasım": {
        "Akrep": list(range(1, 23)),
        "Yay": list(range(21, 32)),
    },
    "Aralık": {
        "Yay": list(range(1, 22)),
        "Oğlak": list(range(21, 32)),
    }
}

gun = int(input("Gün: "))
ay = input("Ay: ").title()

cs = burclar[ay]

for burc, gunler in cs.items():
    if gun in gunler:
        print(f"{gun} günü {ay} ayı {burc} burcudur.")
        break