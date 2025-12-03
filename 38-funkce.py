import math
def obvod_kruhu(r):
    # jaké budou vstupní parametry
    # jaký bude výpočet (O=2πr,S=πr2 )
    # navratová hodnota
    # + test 
    
    return 2 * math.pi * r

print(obvod_kruhu(9))

def obsah_kruhu(r):
     return math.pi * r * r

print(obsah_kruhu(6))



def get_quadrangle_type(a, b, c, d):
    """
    pokud jsou všechny strany stejné tak je to čtverec
    pokud jsou protilehlé strany stejné tak je to odbdelník
    jinak to bude nepravidlný čtyřúhelník
    """

def get_quadrangle_type(a, b, c, d):
    # pokud jsou všechny strany stejné tak je to čtverec
    if a == b == c == d:
        return "čtverec"

    # pokud jsou protilehlé strany stejné tak je to odbdelník
    if a == c and b == d:
        return "obdélník"

    # jinak nepravidelný
    return "nepravidelný čtyřúhelník"

print(get_quadrangle_type(5, 5, 5, 5))
print(get_quadrangle_type(8, 5, 8, 5))
print(get_quadrangle_type(5, 6, 7, 8))