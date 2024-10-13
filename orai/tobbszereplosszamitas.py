from random import randrange

# A és B vagyona rendre
I = 6
J = 4

# RSA paraméterei
e = 79
d = 1019
N = 3337
z = 631
# U = 0,2000, A által generált random szám
U = randrange(0,2000)

C = pow(U, e) % N
m = C - J + 1

Z = []  # Initialize Z as an empty list

for x in range(0, 10):
    val = (pow((m + x), d, N)) % z
    if x > I - 1:
        Z.append(val + 1)  # Add val + 1 to Z if x > I - 1
    else:
        Z.append(val)  # Add val to Z otherwise

G = U % z

# Compare G with Z[J-1] (which is Z[3] if J=4)
if G == Z[J-1]:
    print("Alice-nak több, vagy ugyanannyi pénze van, mint Bobnak.")
else:
    print("Bobnak van több pénze.")
