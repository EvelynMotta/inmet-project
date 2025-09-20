from datetime import time, date


class RegistroMeteorologico:
    def __init__(self, data: date, hora: time, temperatura: float, umidade: float, precipitacao: float):
        self.__data = data
        self.__hora = hora
        self.__temperatura = temperatura
        self.__umidade = umidade
        self.__precipitacao = precipitacao

    @property
    def data(self) -> date:
        return self.__data

    @data.setter
    def data(self, outro: date):
        if not isinstance(outro, date):
            raise TypeError("Data inválida, tente novamente")

        self.__data = outro

    @property
    def hora(self) -> time:
        return self.__hora

    @hora.setter
    def hora(self, outro: time):
        if not isinstance(outro, time):
            raise TypeError("Horário inválida, tente novamente")

        self.__hora = outro

    @property
    def temperatura(self) -> float:
        return self.__temperatura

    @temperatura.setter
    def temperatura(self, outro: float):
        if not isinstance(outro, float):
            raise TypeError("Temperatura inválida, tente novamente")

        self.__temperatura = outro

    @property
    def umidade(self) -> float:
        return self.__umidade

    @umidade.setter
    def umidade(self, outro: float):
        if not isinstance(outro, float):
            raise TypeError("umidade inválida, tente novamente")

        self.__umidade = outro

    @property
    def precipitacao(self) -> float:
        return self.__precipitacao

    @precipitacao.setter
    def precipitacao(self, outro: float):
        if not isinstance(outro, float):
            raise TypeError("Precipitação inválida, tente novamente")

        self.__precipitacao = outro

    def __str__(self):
        registros = "Registros Meteorológicos\n"
        registros += f"Data: {self.data}\n"
        registros += f"Hora: {self.hora}\n"
        registros += f"Temperatura: {self.temperatura}\n"
        registros += f"Umidade: {self.umidade}\n"
        registros += f"Precipitação: {self.precipitacao}\n"

        return registros