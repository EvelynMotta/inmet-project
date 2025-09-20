from registro import RegistroMeteorologico

class Estatistica:
    def __init__(self, registros: list[RegistroMeteorologico]):
        self.__registros = registros


    @property
    def registros(self) -> list[RegistroMeteorologico]:
        return self.__registros

    @registros.setter
    def registros(self, outro):
        if not isinstance(outro, list):
            raise TypeError("Registro inválido, tente novamente!")

        self.__registros = outro


    def media_temperatura(self) -> float:
        """Faz a média de temperatura dos registros."""
        soma: float = 0
        quantidade_temperaturas: int = 0

        for registro in self.__registros:
            soma += registro.temperatura
            quantidade_temperaturas += 1

        return soma / quantidade_temperaturas


    def max_umidade(self) -> float:
        """Seleciona a maior umidade encontrada nos registros."""
        maior_registro = max(self.registros, key=lambda registro: registro.umidade)
        return maior_registro.umidade


    def total_precipitacao(self) -> float:
        """Faz a soma da precipitação de todos os registros."""
        total = sum(registro.precipitacao for registro in self.registros)
        return total
