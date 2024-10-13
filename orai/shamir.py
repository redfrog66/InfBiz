import random
from functools import reduce
from operator import mul

# Egy egyszerű polinom generálás, adott fokszámmal
def polinom_generálás(titok, küszöbérték, prime):
    # Random együtthatók generálása a polinomhoz (az első tag a titok lesz)
    együtthatók = [titok] + [random.randint(0, prime - 1) for _ in range(küszöbérték - 1)]
    return együtthatók

# Titokrészek generálása a polinom alapján
def titok_reszek_generálás(polinom, n, prime):
    részek = []
    for x in range(1, n + 1):
        # A polinom értéke az adott x-nél
        érték = sum([polinom[i] * (x ** i) for i in range(len(polinom))]) % prime
        részek.append((x, érték))
    return részek

# Interpoláció a titok visszaállításához, Lagrange interpolációs módszerrel
def lagrange_interpoláció(részek, prime):
    titok = 0
    for i, (xi, yi) in enumerate(részek):
        li = 1
        for j, (xj, _) in enumerate(részek):
            if i != j:
                # Lagrange interpolációs tag
                li *= (xj * pow(xj - xi, -1, prime)) % prime
        titok = (titok + yi * li) % prime
    return titok

# Példa használat
prime = 2087  # Egy nagy prímszám, amelynél a műveleteket végezzük
titok = 1234  # A megosztandó titok
n = 5         # A részes felek száma
k = 3         # A küszöbérték (hány rész szükséges a visszaállításhoz)

# 1. Polinom generálása
polinom = polinom_generálás(titok, k, prime)
print("Generált polinom együtthatók:", polinom)

# 2. Titokrészek generálása
részek = titok_reszek_generálás(polinom, n, prime)
print("Generált titokrészek:", részek)

# 3. Titok visszaállítása az interpoláció segítségével (k részből)
k_rész = részek[:k]
visszaállított_titok = lagrange_interpoláció(k_rész, prime)
print("Visszaállított titok:", visszaállított_titok)
