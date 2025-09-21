from datetime import date, time, datetime
from pathlib import Path
from os import listdir, path as ospath
import csv

from modelos.estacao import EstacaoMeteorologica
from modelos.registro import RegistroMeteorologico


class Leitor:
    def __init__(self, pasta_dados: str):
        self.__pasta = Path(f"{pasta_dados}/")
        self.__subpastas = [nome for nome in listdir(pasta_dados)  # Serão anos, como '2025'.
                            if ospath.isdir(ospath.join(pasta_dados, nome))]
        self.__estacoes_lidas: set[str] = set()

    def carregar_arquivos(self) -> dict[str, list[EstacaoMeteorologica]]:
        dados: dict[str, list[EstacaoMeteorologica]] = {}
        for ano in self.__subpastas:
            subpasta = Path(f"{self.__pasta}/{ano}/")
            arquivos = subpasta.glob("*.csv")
            estacoes: list[EstacaoMeteorologica] = []

            print(f"Lendo pasta de {ano}...")
            for arquivo in arquivos:
                estacao = self.__processar_estacao(arquivo)
                estacoes.append(estacao)
                self.__estacoes_lidas.add(estacao.nome)

            if len(estacoes) == 0:
                print(f"-- Nenhum CSV encontrado para o ano de {ano}.\n")
                continue
            dados[ano] = estacoes
            print()

        print("\033[1;32m" + "Leitura finalizada!" + "\033[0m")
        return dados

    def estacoes_lidas(self) -> set[str]:
        return self.__estacoes_lidas

    def __processar_estacao(self, arquivo) -> EstacaoMeteorologica:
        with arquivo.open() as arq:
            leitor = csv.reader(arq, delimiter=";")
            registros: list[RegistroMeteorologico] = []
            dados_estacao = {}

            cont_linha = -1
            for linha in leitor:
                cont_linha += 1

                if 0 <= cont_linha < 7:
                    self.__verificar_cabecalho(cont_linha, linha, dados_estacao)
                if cont_linha == 8:
                    break

            print(f"-- Lendo registros da estação {dados_estacao['estacao']}.")
            for linha in leitor:
                registro = self.__processar_registro(linha)
                registros.append(registro)

            estacao = EstacaoMeteorologica(
                dados_estacao['estacao'], dados_estacao['codigo'],
                dados_estacao['regiao'], dados_estacao['uf'],
                dados_estacao['latitude'], dados_estacao['longitude'],
                dados_estacao['altitude'], registros
            )
            return estacao

    @staticmethod
    def __processar_registro(valores: list[str]) -> RegistroMeteorologico:
        data: date | None
        hora: time | None
        precipitacao: float | None
        temperatura: float | None
        umidade: float | None

        # Validando o formato da data
        try:
            data = datetime.strptime(valores[0], "%Y/%m/%d").date()
        except ValueError:
            data = None

        # Validando o formato da hora
        try:
            hora = datetime.strptime(valores[1], "%H%M UTC").time()
        except ValueError:
            hora = None

        # Validando a temperatura
        try:
            temperatura = float(valores[7])
        except ValueError:
            temperatura = None

        # Validando a precipitacao
        try:
            precipitacao = float(valores[2])
        except ValueError:
            precipitacao = None

        # Validando a umidade
        try:
            umidade = float(valores[14])
        except ValueError:
            umidade = None

        return RegistroMeteorologico(data, hora, temperatura, umidade, precipitacao)

    @staticmethod
    def __verificar_cabecalho(numeracao: int, valores: list[str], dados: dict):
        if numeracao == 0:
            dados['regiao'] = valores[1]
        elif numeracao == 1:
            dados['uf'] = valores[1]
        elif numeracao == 2:
            dados['estacao'] = valores[1]
        elif numeracao == 3:
            dados['codigo'] = valores[1]
        elif numeracao == 4:
            dados['latitude'] = valores[1]
        elif numeracao == 5:
            dados['longitude'] = valores[1]
        elif numeracao == 6:
            dados['altitude'] = valores[1]
