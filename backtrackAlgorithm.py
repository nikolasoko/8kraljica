import time
class kraljice:
    """
        Klasa za rjesavanje problema s n kraljica backtracking algoritmom.
    """

    def __init__(self,velicina,ispis):
        self.velicina = velicina
        self.brojac=0
        #Flag ispis koristimo ako želimo vidjeti rješenja grafički
        self.ispis=False
        self.brojRjesenja = 0
        self.rjesi()

    def rjesi(self):
        #Pobrisi prosli rezultat
        self.brojRjesenja=0

        #Inicijaliziraj plocu
        pozicije = [-1] * self.velicina
        #Zapocni rekurzivni poziv stavljanja kraljica na ploču
        self.stavi_kraljicu(pozicije, 0)
        print("Broj pronađenih rješenja", self.brojRjesenja)


    def stavi_kraljicu(self, pozicije, trenutni_red):
        # ako je trenutni red veci od maksimalnog povecaj broj rješenja
        if trenutni_red == self.velicina:
            self.brojRjesenja += 1
            if self.ispis:
                ispis_plocu(pozicije)
                input('Pritisni ENTER za nastavak traženja...')
        else:

            for stupac in range(self.velicina):
                # provjeri je li moguce staviti kraljicu na stupac u trenutnom redu u odabrani stupac
                if self.provjera(pozicije, trenutni_red, stupac):
                    pozicije[trenutni_red] = stupac
                    self.stavi_kraljicu(pozicije, trenutni_red + 1)
            # ako se vracamo korak untrag pobrisi zadnju kraljicu
            if self.ispis and self.brojac<7:
                #input()
                self.brojac+=1
            pozicije[trenutni_red] = -1

    def provjera(self, pozicije, zauzeti_redovi, stupac):
        # provjerava je li mjesto stavljanja kraljice pod napadom drugih kraljica
        for i in range(zauzeti_redovi):
            if pozicije[i] == stupac or \
                    pozicije[i] - i == stupac - zauzeti_redovi or \
                    pozicije[i] + i == stupac + zauzeti_redovi:
                return False
        return True


def ispis_plocu(pozicije):
    for red in range(len(pozicije)):
        line = ""
        for stupac in range(len(pozicije)):
            if pozicije[red] == stupac:
                line += "Q "
            else:
                line += ". "
        print(line)
    print("\n")


def main():
    # pozivamo za velicinu ploce 6
    kraljice(8,True)


if __name__ == "__main__":
    main()
