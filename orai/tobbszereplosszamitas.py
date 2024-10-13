from random import randrange

# A és B vagyona rendre (I = Alice vagyona, J = Bob vagyona)
I = 6  # Alice vagyona
J = 4  # Bob vagyona

# RSA paraméterek:
# e = nyilvános kulcs, d = privát kulcs, N = modulus
e = 79
d = 1019
N = 3337
z = 631  # Ez egy modulus, amit a további lépésekhez használunk

# U = Alice által generált random szám 0 és 2000 között (ez titkosítandó adat lesz)
U = randrange(0, 2000)

# Alice RSA titkosítást végez a saját generált számán (U):
# pow(U, e) % N = U^e mod N, ami a titkosított üzenet
C = pow(U, e) % N

# Kiszámoljuk 'm'-et Bob vagyonával való összefüggésben:
# Itt az a cél, hogy a titkosított üzenetből levezetünk egy értéket, ami a vagyonok
# relatív összehasonlítását szolgálja. Bob vagyona (J) levonásra kerül, majd hozzáadunk 1-et.
m = C - J + 1

# Z lista lesz, amely az RSA dekriptált értékeket fogja tárolni
Z = []

# A következő ciklus 0-tól 9-ig megy, és minden m+x esetén végrehajtunk egy dekriptálást.
for x in range(0, 10):
    # pow((m + x), d, N): RSA dekriptálás, privát kulccsal (d)
    # Ez azt jelenti, hogy az 'm + x' értéket visszafejtjük az eredeti, titkosított üzenetből.
    # Ezután az eredményt még 'z' mod-ot vesszük, ami egy újabb titkosítási lépés, hogy
    # a számokat egy meghatározott tartományba szorítsuk.
    val = (pow((m + x), d, N)) % z
    
    # Ha az x nagyobb, mint Alice vagyonának mérete (I - 1), akkor hozzáadunk 1-et az értékhez,
    # ami egy kis eltérés az "igazi" értéktől, hogy tovább biztosítsuk a titkosítást.
    if x > I - 1:
        Z.append(val + 1)  # Ha Alice vagyonán túl vagyunk, növeljük az értéket
    else:
        Z.append(val)  # Egyébként simán hozzáadjuk a val eredeti értékét

# G: az Alice által generált véletlenszám (U) maradékosztás z-vel (U % z)
# Ez lesz az a "kulcs", amit a későbbi összehasonlításnál használunk.
G = U % z

# Most összehasonlítjuk G-t a Z listában lévő értékkel, konkrétan Z[J-1]-tel (Z[3], ha J=4):
# Ez azt nézi meg, hogy Bob és Alice vagyona közti relatív különbség alapján ki a gazdagabb.
if G == Z[J-1]:
    # Ha G megegyezik a dekriptált értékkel, akkor Alice-nak legalább annyi pénze van, mint Bobnak.
    print("Alice-nak több, vagy ugyanannyi pénze van, mint Bobnak.")
else:
    # Ha nem egyeznek, akkor Bob gazdagabb Alice-nál.
    print("Bobnak van több pénze.")
