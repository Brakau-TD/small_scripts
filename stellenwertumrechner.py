"""einfaches Skript um Dezimalzahlen in Hexadezimal umzurechnen"""


def konvertiere_dec_zu_hex(dezimalzahl: int|str) -> str:
    """nimmt eine dezimalzahl und konvertiert sie in eine hexadezimalzahl"""
    try:
        dezimalzahl = int(dezimalzahl)
    except ValueError:
        return "Falsche Eingabe"
    hexadezimalzahl = ""
    while dezimalzahl > 0:
        rest = dezimalzahl % 16
        if rest < 10:
            hexadezimalzahl = str(rest) + hexadezimalzahl
        else:
            hexadezimalzahl = chr(ord("A") + rest - 10) + hexadezimalzahl
        dezimalzahl //= 16
    return hexadezimalzahl

def konvertiere_dec_zu_dual(dezimalzahl: int|str) -> str:
    """
    nimmt eine Dezimalzahl als Integer oder String 
    und konvertiert sie in eine Dualzahl als String
    """
    try:
        dezimalzahl = int(dezimalzahl)
    except ValueError:
        return "Falsche Eingabe"
    dualzahl = ""
    wert = 1
    while wert != 0:
        wert, rest = gib_wert_und_rest(dezimalzahl, 2)
        dualzahl += str(rest)
        dezimalzahl = wert
    return dualzahl[::-1]

def konvertiere_hex_zu_dec(hexa: str) -> int|str:
    '''konvertiert eine hexadezimalzahl zu ganzer Zahl'''
    hexadezimalzahl = hexa.upper()
    dezimalzahl = 0
    for i, wertzeichen in enumerate(hexadezimalzahl[::-1]):
        if 47 < ord(wertzeichen) < 58:
            a = abs(48-ord(wertzeichen))
        elif 64 < ord(wertzeichen) < 71:
            a = (abs(55-ord(wertzeichen)))
        else:
            return "Falsche Eingabe"
        dezimalzahl += a*(16**i)
    return dezimalzahl



def konvertiere_dual_zu_dec(dualzahl: str) -> int|str:
    '''konvertiert eine dualzahl zu ganzer Zahl'''
    wert, ergebnis = 0,0
    for i, number in enumerate(dualzahl[::-1]):
        if number not in ["0", "1"]:
            return "Falsche Eingabe"
        wert = int(number)*(2**i)
        ergebnis += wert
    return ergebnis


def konvertiere_dual_zu_hex(dualzahl: str) -> str:
    '''konvertiert eine dualzahl zu hexadezimalzahl'''
    dezimalzahl = konvertiere_dual_zu_dec(dualzahl)
    hexadezimalzahl = konvertiere_dec_zu_hex(dezimalzahl)
    return hexadezimalzahl

def konvertiere_hex_zu_dual(hexadezimalzahl: str) -> str:
    '''konvertiert eine hexadezimalzahl zu dualzahl'''
    dezimalzahl = konvertiere_hex_zu_dec(hexadezimalzahl)
    dualzahl = konvertiere_dec_zu_dual(dezimalzahl)
    return dualzahl


def gib_wert_und_rest(zahl, divisor) -> tuple[int, int]:
    """
    nimmt eine Zahl und dividiert durch Divisor
    gibt ein Tuple von ganzer Zahl und Rest nach Modulo zurück
    """
    wert = zahl // divisor
    rest = zahl % divisor
    return wert, rest
