import unittest
from envio import calcular_envio


class TestCalcularEnvio(unittest.TestCase):

    def test_estandar_menor_a_5kg_cuesta_50(self):
        self.assertEqual(calcular_envio(3, "estandar"), 50)

    def test_estandar_6kg_cuesta_60(self):
        self.assertEqual(calcular_envio(6, "estandar"), 60)
    
    def test_estandar_exactamente_5kg_cuesta_50(self):
        self.assertEqual(calcular_envio(5, "estandar"), 50)

    def test_estandar_7kg_cuesta_70(self):
        self.assertEqual(calcular_envio(7, "estandar"), 70)
    
    def test_express_menor_a_5kg_cuesta_100(self):
        self.assertEqual(calcular_envio(3, "express"), 100)
    
    def test_express_mayor_a_5kg_cuesta_140(self):
        self.assertEqual(calcular_envio(7, "express"), 140)

    def test_peso_cero_lanza_error(self):
        with self.assertRaises(ValueError):
            calcular_envio(0, "estandar")

    def test_peso_negativo_lanza_error(self):
        with self.assertRaises(ValueError):
            calcular_envio(-2, "express")
    
    def test_tipo_invalido_lanza_error(self):
        with self.assertRaises(ValueError):
            calcular_envio(3, "urgente")


if __name__ == "__main__":
    unittest.main()