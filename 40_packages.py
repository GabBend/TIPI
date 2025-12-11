
import vypocet
from vypocet import tipi
from vypocet import lining

print(vypocet.XYZ)

r = 770      # velikost tipi
v = 200      # celková výška liningu
s = 50      # horní část kortexinu

vysledky = lining.get_lining(r, v, s)

#výpočty jsou ověřeny :) 
print("Horní díl Z2:", vysledky["horni_dil"])
print("Spodní díl Z1:", vysledky["spodni_dil"])
print("Horní část kortexinu Z3:", vysledky["spodni_cast_kortexinu"])

print("\n")

r = 600
a = 145

delky = tipi.get_delky_pruhu(r, a)

print("Délky pruhů:")
for i, L in enumerate(delky, start=1):
    print(f"Pruh {i}: {L:.2f} cm")