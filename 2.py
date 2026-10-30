class Hissi:
    def __init__(self, alin, ylin):
        self.alin = alin
        self.ylin = ylin
        self.kerros = alin

    def kerros_ylös(self):
        if self.kerros < self.ylin:
            self.kerros += 1

    def kerros_alas(self):
        if self.kerros > self.alin:
            self.kerros -= 1

    def siirry_kerrokseen(self, kohde):
        while self.kerros < kohde:
            self.kerros_ylös()
        while self.kerros > kohde:
            self.kerros_alas()
        print(f"Hissi meni kerrokseen {self.kerros}")

class Talo:
    def __init__(self, alin, ylin, maara):
        self.alin = alin
        self.ylin = ylin
        self.hissit = []
        for i in range(maara):
            self.hissit.append(Hissi(alin, ylin))

    def aja_hissii(self, numero, kohde):
        print(f"Ajetaan hissiä {numero} kerrokseen {kohde}")
        self.hissit[numero].siirry_kerrokseen(kohde)

# Testi
if __name__ == "__main__":
    talo = Talo(1, 10, 3)
    talo.aja_hissii(0, 5)
    talo.aja_hissii(1, 7)