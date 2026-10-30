import random


class Auto:
    def __init__(self, rekisteri, huippunopeus):
        self.rekisteri = rekisteri
        self.huippunopeus = huippunopeus
        self.nopeus = 0
        self.matka = 0

    def kiihdyta(self, muutos):
        self.nopeus += muutos
        if self.nopeus > self.huippunopeus:
            self.nopeus = self.huippunopeus
        if self.nopeus < 0:
            self.nopeus = 0

    def kulje(self, tunnit):
        self.matka += self.nopeus * tunnit


class Kilpailu:
    def __init__(self, nimi, pituus, autot):
        self.nimi = nimi
        self.pituus = pituus
        self.autot = autot

    def tunti_kuluu(self):
        for auto in self.autot:
            auto.kiihdyta(random.randint(-10, 15))
            auto.kulje(1)

    def tulosta_tilanne(self):
        for a in self.autot:
            print(f"{a.rekisteri}: {a.matka} km")

    def kilpailu_ohi(self):
        for a in self.autot:
            if a.matka >= self.pituus:
                return True
        return False


# Testi
if __name__ == "__main__":
    autot = [Auto(f"Auto-{i}", random.randint(120, 200)) for i in range(1, 11)]
    kisa = Kilpailu("Suuri romuralli", 8000, autot)

    tunnit = 0
    while not kisa.kilpailu_ohi():
        kisa.tunti_kuluu()
        tunnit += 1
        if tunnit % 100 == 0:
            print(f"Tunteja mennyt: {tunnit}")

    print(f"Loppu! Tunteja kului: {tunnit}")
    kisa.tulosta_tilanne()