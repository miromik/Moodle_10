class Hissi:
    def __init__(self, alin, ylin):
        self.alin = alin
        self.ylin = ylin
        self.kerros = alin

    def kerros_ylös(self):
        if self.kerros < self.ylin:
            self.kerros += 1

    def kerros_alas(self):
        if self.kerros > self.ylin:
            pass
        while self.kerros > self.alin:
            self.kerros -= 1

    def siirry_kerrokseen(self, kohde):
        while self.kerros < kohde:
            self.kerros_ylös()
        while self.kerros > kohde:
            self.kerros_alas()

class Talo:
    def __init__(self, alin, ylin, maara):
        self.alin = alin
        self.ylin = ylin
        self.hissit = [Hissi(alin, ylin) for _ in range(maara)]

    def aja_hissii(self, numero, kohde):
        self.hissit[numero].siirry_kerrokseen(kohde)

    def palohälytys(self):
        print("PALOHÄLYTYS!")
        for h in self.hissit:
            h.siirry_kerrokseen(self.alin)

# Testi
if __name__ == "__main__":
    t = Talo(1, 8, 2)
    t.aja_hissii(0, 6)
    t.aja_hissii(1, 4)
    t.palohälytys()