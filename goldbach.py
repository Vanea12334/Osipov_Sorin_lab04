def este_prim(n):
    if n < 2:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False

    limita = int(n ** 0.5) + 1
    for d in range(3, limita, 2):
        if n % d == 0:
            return False
    return True


def descompunere_goldbach(n):
    perechi = []
    for p in range(2, (n // 2) + 1):
        q = n - p
        if este_prim(p) and este_prim(q):
            perechi.append((p, q))
    return perechi


def main():
    while True:
        text = input("Introdu un numar natural par mai mare decat 2: ")
        try:
            n = int(text)
            if n <= 2:
                print("Eroare: numarul trebuie sa fie mai mare decat 2.")
            elif n % 2 != 0:
                print("Eroare: numarul trebuie sa fie par.")
            else:
                break
        except ValueError:
            print("Eroare: te rog introdu un numar intreg valid.")

    perechi = descompunere_goldbach(n)
    rezultat = ""
    for i in range(len(perechi)):
        p, q = perechi[i]
        rezultat += f"{p} + {q}"
        if i < len(perechi) - 1:
            rezultat += " = "

    print(f"Descompunerile pentru {n}: {rezultat}")


main()

#da
