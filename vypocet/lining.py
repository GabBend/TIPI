def get_lining(r, v, s):
    """
    r – velikost tipi
    v – celková výška liningu
    s – spodní část kortexinu
    """

    Z1 = (r + 40) / 5
    Z2 = (r + 40 - v) / 5
    Z3 = (r + 40 - s) / 5

    return {
        "spodni_dil": Z1,
        "horni_dil": Z2,
        "spodni_cast_kortexinu": Z3
    }