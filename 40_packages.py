import vypocet
from vypocet import tipi
from vypocet import lining

print(vypocet.XYZ)
print(tipi.get_tipi())

r = 770      # velikost tipi
v = 200      # celková výška liningu
s = 50      # spodní část kortexinu

vysledky = lining.get_lining(r, v, s)

#výpočty jsou ověřeny :) 
print("Spodní díl Z1:", vysledky["spodni_dil"])
print("Horní díl Z2:", vysledky["horni_dil"])
print("Spodní část kortexinu Z3:", vysledky["spodni_cast_kortexinu"])