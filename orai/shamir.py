import random
from functools import reduce
from operator import mul

# Polinom generálása adott küszöbértékkel (k fokú polinom)
# A polinom első tagja maga a titok, a többi véletlenszerű együttható
def polinom_generálás(titok, küszöbérték, prime):
    # A titok a polinom első tagja, a többi együttható véletlen
    együtthatók = [titok] + [random.randint(0, prime - 1) for _ in range(küszöbérték - 1)]
    return együtthatók

# Titokrészek generálása a polinom alapján
# A részes felek száma (n) meghatározza, hogy hány rész készüljön
def titok_reszek_generálás(polinom, n, prime):
    részek = []
    # Minden részes fél kap egy (x, y) párt, ahol x az adott fél indexe,
    # y pedig a polinom értéke az adott x-nél
    for x in range(1, n + 1):
        # Polinom értéke az adott x-nél: P(x) = a0 + a1*x + a2*x^2 + ... mod prime
        érték = sum([polinom[i] * (x ** i) for i in range(len(polinom))]) % prime
        részek.append((x, érték))  # Tároljuk az (x, P(x)) párt
    return részek

# Lagrange interpoláció a titok visszaállításához
# Ehhez legalább k titokrész kell, hogy rekonstruálni tudjuk a polinomot
def lagrange_interpoláció(részek, prime):
    titok = 0
    # Minden titokrész (xi, yi) alapján számítunk egy interpolációs tagot
    for i, (xi, yi) in enumerate(részek):
        li = 1
        for j, (xj, _) in enumerate(részek):
            if i != j:
                # Lagrange interpolációs tag: li = Π (xj * (xj - xi)^(-1)) mod prime
                # Pow használatával számítjuk az inverz műveletet moduló szerint
                li *= (xj * pow(xj - xi, -1, prime)) % prime
        # Hozzáadjuk az aktuális tagot a titokhoz
        titok = (titok + yi * li) % prime
    return titok

# Példa használat
prime = 2087  # Egy nagy prímszám, ami biztosítja a moduláris aritmetika helyes működését
titok = 1234  # A titok, amit meg szeretnénk osztani
n = 5         # A részes felek száma (akik megkapják a titokrészeket)
k = 3         # A küszöbérték: ennyi részt kell kombinálni a titok visszanyeréséhez

# 1. Polinom generálása: a titok és a véletlenszerű együtthatók
polinom = polinom_generálás(titok, k, prime)
print("Generált polinom együtthatók:", polinom)

# 2. Titokrészek generálása: n darab (x, P(x)) pár
részek = titok_reszek_generálás(polinom, n, prime)
print("Generált titokrészek:", részek)

# 3. Titok visszaállítása k darab titokrészből (Lagrange interpolációval)
k_rész = részek[:k]  # Az első k részt használjuk a visszaállításhoz
visszaállított_titok = lagrange_interpoláció(k_rész, prime)
print("Visszaállított titok:", visszaállított_titok)
