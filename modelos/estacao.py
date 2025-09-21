from .registro import RegistroMeteorologico

class EstacaoMeteorologica:
    def __init__(self, nome: str, codigo: str, regiao: str, uf: str, latitude: float, longitude: float, altitude: float, registros: list[RegistroMeteorologico]):
        self.__nome = nome
        self.__codigo = codigo
        self.__regiao = regiao
        self.__uf = uf
        self.__latitude = latitude
        self.__longitude = longitude
        self.__altitude = altitude
        self.__registros = registros


    @property
    def nome(self) -> str:
        return self.__nome

    @nome.setter
    def nome(self, outro: str):
        if not isinstance(outro, str):
            raise TypeError("Nome inválido, tente novamente")

        self.__nome = outro


    @property
    def codigo(self) -> str:
        return self.__codigo

    @codigo.setter
    def codigo(self, outro: str):
        if not isinstance(outro, str):
            raise TypeError("Código inválido, tente novamente")

        self.__codigo = outro


    @property
    def regiao(self) -> str:
        return self.__regiao

    @regiao.setter
    def regiao(self, outro: str):
        if not isinstance(outro, str):
            raise TypeError("Regiao inválida, tente novamente")

        self.__regiao = outro


    @property
    def uf(self) -> str:
        return self.__uf

    @uf.setter
    def uf(self, outro: str):
        if not isinstance(outro, str):
            raise TypeError("UF inválido, tente novamente")

        self.__uf = outro


    @property
    def latitude(self) -> float :
        return self.__latitude

    @latitude.setter
    def latitude(self, outro: float):
        if not isinstance(outro, float):
            raise TypeError("Latitude inválida, tente novamente")

        self.__latitude = outro


    @property
    def longitude(self) -> float:
        return self.__longitude

    @longitude.setter
    def longitude(self, outro: float):
        if not isinstance(outro, float):
            raise TypeError("Longitude inválida, tente novamente")

        self.__longitude = outro


    @property
    def altitude(self) -> float:
        return self.__altitude

    @altitude.setter
    def altitude(self, outro):
        if not isinstance(outro, float):
            raise TypeError("Altitude inválida, tente novamente")

        self.__altitude = outro


    @property
    def registros(self) -> list[RegistroMeteorologico]:
        return self.__registros

    @registros.setter
    def registros(self, outro: list[RegistroMeteorologico]):
        if not isinstance(outro, list):
            raise TypeError("Registros inválidos, tente novamente")

        self.__registros = outro


    def adicionar_registro(self, registro: RegistroMeteorologico):
        self.__registros.append(registro)


    def obter_registros(self) -> list[RegistroMeteorologico]:
        return self.registros


    def __str__(self):
        estacao = "Estação Meteorológica\n"
        estacao += f"Nome: {self.nome}\n"
        estacao += f"Código: {self.codigo}\n"
        estacao += f"Região: {self.regiao}\n"
        estacao += f"Uf: {self.uf}\n"
        estacao += f"Latitude: {self.latitude}\n"
        estacao += f"Longitude: {self.longitude}\n"
        estacao += f"Altitude: {self.altitude}\n"

        return estacao
