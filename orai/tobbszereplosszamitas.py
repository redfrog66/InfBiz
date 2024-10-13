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


# Egyéb magyarázat:
# - Az RSA egy aszimmetrikus titkosítási eljárás, ahol két kulcs (nyilvános és privát) van. 
# Itt a titkosítás nyilvános kulccsal történik (pow(U, e) % N), a dekódolás pedig privát kulccsal (pow(..., d, N)).
# - Ez a kód gyakorlatilag titkosítja Alice által választott véletlenszámot (U), 
# majd különböző "módosításokkal" (pl. hozzáadással, maradékosztással) dekódolja azt, hogy ne lehessen közvetlenül látni, mennyi Alice és Bob vagyona.
# ---------------
# - A pow(U, e) % N a maradékosztást használja arra, hogy a számok bizonyos tartományba kerüljenek, és ne legyenek túl nagyok (pl. ne haladják meg az N értékét). 
# A maradékosztás az RSA esetében a nagy számok kezelésére is szolgál, valamint segít az egész folyamatot titkosítani.
# ---------------
# - Az x-hez való hozzáadás (m + x) és az, hogy ha x nagyobb Alice vagyonánál, akkor +1-et hozzáadunk az eredményhez, egyfajta "zavaró tényező" a titkosításban. 
# Ez azt biztosítja, hogy ne lehessen egyértelműen visszafejteni az adatokat Alice és Bob vagyonáról.
# ---------------
# - A U = randrange(0, 2000) azt szolgálja, hogy minden futáskor egy új, véletlenszerű számot válasszunk Alice számára. 
# Ezáltal a kód minden futáskor más eredményre vezet, még akkor is, ha Alice és Bob vagyona változatlan. Ez a titkosítás biztonságának alapvető része.
# ---------------
# - A végső összehasonlítás (G == Z[J-1]) azt a célt szolgálja, hogy eldöntsük, Alice vagy Bob gazdagabb-e. Ez a megoldás titkosítva tárolja a vagyoni adatokat (nem közvetlen számokat használ), 
# majd az összehasonlítás segítségével csak annyi derül ki, hogy ki a gazdagabb, anélkül, hogy konkrét számok látszódnának.