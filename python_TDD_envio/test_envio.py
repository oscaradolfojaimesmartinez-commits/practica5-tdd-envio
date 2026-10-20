import unittest
from envio import calcular_envio


class TestCalcularEnvio(unittest.TestCase):

    def test_estandar_menor_a_5kg_cuesta_50(self):
        self.assertEqual(calcular_envio(3, "estandar"), 50)


if __name__ == "__main__":
    unittest.main()