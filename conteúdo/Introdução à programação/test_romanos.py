import unittest
from romanos import num_romanos


class TesteRomanos(unittest.TestCase):
    def test_um(self):
        um = num_romanos(1)
        self.assertEqual('I', um)  # add assertion here

    def test_zero(self):
        zero = num_romanos(0)
        self.assertEqual('', zero)

    def test_dois(self):
        dois = num_romanos(2)
        self.assertEqual('II', dois)

    def test_tres(self):
        tres = num_romanos(3)
        self.assertEqual('III', tres)

    def test_quatro(self):
        quatro = num_romanos(4)
        self.assertEqual('IV', quatro)

    def test_cinco(self):
        cinco = num_romanos(5)
        self.assertEqual('V', cinco)

    def test_seis(self):
        seis = num_romanos(6)
        self.assertEqual('VI', seis)

    def test_sete(self):
        sete = num_romanos(7)
        self.assertEqual('VII', sete)

    def test_oito(self):
        oito = num_romanos(8)
        self.assertEqual('VIII', oito)

    def test_nove_ou_mais(self):
        rom = num_romanos(9)
        self.assertEqual('IX', rom)
        # rom = num_romanos(10)

if __name__ == '__main__':
    unittest.main()
