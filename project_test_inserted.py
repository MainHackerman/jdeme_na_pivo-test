if __name__ == '__main__':
    pivo = 80

    pocet_lidi = int(input())
    rozpocet_osoba = int(input())
    zastupce = input()
    studeti = int(input())

    rozpocet_vsichni = rozpocet_osoba * pocet_lidi
    rozpocet_studenti = rozpocet_osoba * studeti
    rozpocet_ostatni = rozpocet_vsichni - rozpocet_studenti

    stud_pivo = int(pivo * 0.65)

    piva_studenti = rozpocet_studenti // stud_pivo
    piva_ostatni = rozpocet_ostatni // pivo
    piva_vsichni = piva_studenti + piva_ostatni

    cena_studenti = piva_studenti * stud_pivo
    cena_ostatni = piva_ostatni * pivo
    cena_vsichni = cena_studenti + cena_ostatni

    print('Zodpovedna osoba', zastupce, 'zaplati za', piva_vsichni, 'piv', cena_vsichni, 'korun.')
