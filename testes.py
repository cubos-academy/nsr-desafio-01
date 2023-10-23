import unittest
from nasa import get_apod, DataForaDoIntervalo
from main import formatar_data


class TestNasaAPI(unittest.TestCase):
    def teste_data_valida(self):
        data_valida = "2023-10-20"
        url, titulo, explicacao = get_apod(data_valida)
        self.assertIsInstance(url, str)
        self.assertIsInstance(titulo, str)
        self.assertIsInstance(explicacao, str)

    def teste_data_fora_do_intervalo(self):
        data_fora_intervalo = "1990-01-01"
        with self.assertRaises(DataForaDoIntervalo):
            get_apod(data_fora_intervalo)

    def teste_erro_formatacao_data(self):
        data_formato_invalido = "20/10/2023"
        with self.assertRaises(DataForaDoIntervalo):
            get_apod(data_formato_invalido)


class TestMain(unittest.TestCase):
    def teste_formatar_data(self):
        data_formatada = formatar_data("20/10/2023")
        self.assertEqual(data_formatada, "2023-10-20")


if __name__ == '__main__':
    unittest.main()
