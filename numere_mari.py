def citeste_numere(nume_fisier):
    try:
        f = open(nume_fisier, "r")
        linii = f.readlines()
        f.close()
    except FileNotFoundError:
        print("Eroare: fisierul numere.txt nu exista.")
        return None, None

    numere = []
    for linie in linii:
        curat = linie.strip()
        if curat != "":
            numere.append(curat)

    if len(numere) < 2:
        print("Eroare: fisierul trebuie sa contina doua numere, cate unul pe linie.")
        return None, None

    a = numere[0]
    b = numere[1]

    if not a.isdigit() or not b.isdigit():
        print("Eroare: fisierul trebuie sa contina doar numere naturale.")
        return None, None

    if len(a) > 200 or len(b) > 200:
        print("Eroare: numerele pot avea cel mult 200 de cifre.")
        return None, None

    a = a.lstrip("0")
    if a == "":
        a = "0"

    b = b.lstrip("0")
    if b == "":
        b = "0"

    return a, b


def aduna_mari(a, b):
    i = len(a) - 1
    j = len(b) - 1
    transport = 0
    rezultat = ""

    while i >= 0 or j >= 0 or transport > 0:
        cifra_a = int(a[i]) if i >= 0 else 0
        cifra_b = int(b[j]) if j >= 0 else 0

        suma = cifra_a + cifra_b + transport
        cifra_rez = suma % 10
        transport = suma // 10

        rezultat = str(cifra_rez) + rezultat
        i -= 1
        j -= 1

    rezultat = rezultat.lstrip("0")
    if rezultat == "":
        return "0"
    return rezultat


def inmulteste_mari(a, b):
    if a == "0" or b == "0":
        return "0"
    if a == "1":
        return b
    if b == "1":
        return a

    n = len(a)
    m = len(b)
    rezultat = [0] * (n + m)

    for i in range(n - 1, -1, -1):
        for j in range(m - 1, -1, -1):
            produs = int(a[i]) * int(b[j])
            suma = produs + rezultat[i + j + 1]

            rezultat[i + j + 1] = suma % 10
            rezultat[i + j] += suma // 10

    rezultat_str = ""
    for cifra in rezultat:
        rezultat_str += str(cifra)

    rezultat_str = rezultat_str.lstrip("0")
    if rezultat_str == "":
        return "0"
    return rezultat_str


def main():
    a, b = citeste_numere("numere.txt")
    if a is None or b is None:
        return

    suma = aduna_mari(a, b)
    produs = inmulteste_mari(a, b)

    print("Primul numar:", a)
    print("Al doilea numar:", b)
    print("Suma:", suma)
    print("Produsul:", produs)


main()