from math import comb


def require(ok, message):
    if not ok:
        raise RuntimeError(message)


p = 17
C = {j: comb(20, j) for j in (2, 4, 10)}
D = {0: -comb(20, 3), **{j: -C[j] * comb(20-j, 3) for j in C}}
E = {0: -1-D[0], **{j: -C[j]-D[j] for j in C}}
c1 = {0: 19+2*D[0], **{j: (19-j)*C[j]+2*D[j] for j in C}}
c2 = {0: 190+3*D[0], **{j: comb(20-j, 2)*C[j]+3*D[j] for j in C}}
require(D == {0:-1140,2:-155040,4:-2713200,10:-22170720}, 'D identity')
require(E == {0:1139,2:154850,4:2708355,10:21985964}, 'E identity')
require(c1 == {0:-2261,2:-306850,4:-5353725,10:-42678636}, 'c1 identity')
require(c2 == {0:-3230,2:-436050,4:-7558200,10:-58198140}, 'c2 identity')
require(all(x % p == 0 for x in c1.values()), 'c1 divisibility')
require(all(x % p == 0 for x in c2.values()), 'c2 divisibility')
require({j:c1[j]//p % p for j in (0,4,10)} == {0:3,4:0,10:1}, 'c1 residues')
require({j:E[j]//p % p for j in (0,4,10)} == {0:16,4:8,10:0}, 'E residues')
row1 = []
for rho4 in (0,1):
    A = -pow(rho4,4,p) % p
    for rho10 in (0,1):
        b = (-pow(rho10,10,p)-comb(10,4)*A*pow(rho10,6,p)) % p
        row1.append((A,b,(b+8*A) % p))
require(row1 == [(0,0,0),(0,16,16),(16,0,9),(16,5,14)], 'row1 census')
require(all(v != 15 for _,_,v in row1), 'row1 empty filter')

B = {0:comb(19,3)-190*comb(17,3),4:4845*comb(15,3),10:184756*comb(9,3)}
require(B == {0:-128231,4:2204475,10:15519504}, 'row2 B identity')
require(all(v % p == 0 for v in B.values()), 'row2 B divisibility')
require({j:v//p % p for j,v in B.items()} == {0:5,4:16,10:12}, 'row2 B residues')
row2 = []
for rho4_square in (1,3):
    A = (-rho4_square**2+6*rho4_square) % p
    for rho10_square in (1,3):
        b = (-rho10_square**5+45*rho10_square**4-210*A*rho10_square**3) % p
        row2.append((A,b,(5+16*A+12*b) % p))
require(row2 == [(5,14,15),(5,8,11),(9,7,12),(9,6,0)], 'row2 census')
require(all((A+5*b) % p != 6 for A,b,_ in row1), 'row1 both-unit filter')
require([(A,b) for A,b,_ in row1 if (9*A+6*b)%p == 4] == [(16,5)], 'row1 small-H1 filter')
require({j:c2[j]//p % p for j in (0,4,10)} == {0:14,4:1,10:6}, 'c2 residues')
jet = [(t,u,v) for t in range(p) for u in range(p) for v in range(p)
       if (2*t+u+v)%p == 0 and (13*t*t+10*t*u+2*v*v)%p == 0]
require(jet == [(0,0,0)], 'complete corrected second jet')
require(3 not in {i*i%p for i in range(p)}, 'nonsquare discriminant')
D0=D[0]-D[4]+209*D[10]
Dh=D[2]-6*D[4]+1215*D[10]
K0=-c2[0]+c2[4]-209*c2[10]
Kh=-c2[2]+6*c2[4]-1215*c2[10]
E0=E[0]-E[4]+209*E[10]-K0
Eh=E[2]-6*E[4]+1215*E[10]-Kh
require((D0,Dh)==(-4630968420,-26921300640), 'final D')
require((K0,Kh)==(12155856290,70665826950), 'final K')
require((E0,Eh)==(-7563497030,-43968975970), 'final E')
require(K0%17==0 and K0//17%17==8, 'final K residue')
require(E0%289==0 and E0//289%17==9 and Eh%17==14, 'final E residues')
require((9+14+8*4+16*16)%17==5, 'nonzero small-root residue')
print('PASS: row1 exact identities, complete first sieves, corrected 4913-marking jet, final residue 5; row2 sole residue survivor (9,6).')
