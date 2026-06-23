"""
Modul 450 - Code, der getestet werden soll.  (NICHT veraendern.)
"""


def ist_sicher(passwort):
    """
    Gibt True zurueck, wenn das Passwort als sicher gilt:
      - mindestens 8 Zeichen lang
      - enthaelt mindestens eine Ziffer (0-9)
      - enthaelt mindestens einen Grossbuchstaben (A-Z)
    Sonst False.
    """
    if len(passwort) < 8:
        return False
    hat_ziffer = any(zeichen.isdigit() for zeichen in passwort)
    hat_gross = any(zeichen.isupper() for zeichen in passwort)
    return hat_ziffer and hat_gross
