import datetime
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

            for arquivo in arquivos:
                estacao = self.__processar_estacao(arquivo)
                self.__estacoes_lidas.add(estacao.nome)

            if len(estacoes) == 0:
                continue
            dados[ano] = estacoes

        return dados


    def estacoes_lidas(self) -> set[str]:
        return self.__estacoes_lidas


    def __processar_estacao(self, arquivo) -> EstacaoMeteorologica:
        with arquivo.open(newline="", encoding="utf-8") as arq:
            leitor = csv.reader(arq, delimiter=";")
            dados_estacao = {}
            registros: list[RegistroMeteorologico] = []

            cont_linha = -1
            for linha in leitor:
                cont_linha += 1
                
                if 0 <= cont_linha < 8:
                    self.__verificar_cabecalho(cont_linha, linha, dados_estacao)
                if cont_linha < 9:
                    continue
                registro = self.__processar_registro(linha)
                registros.append(registro)

            estacao = EstacaoMeteorologica(
                dados_estacao['nome'], dados_estacao['codigo'],
                dados_estacao['regiao'], dados_estacao['uf'],
                dados_estacao['latitude'], dados_estacao['longitude'],
                dados_estacao['altitude'], registros
            )
            return estacao

    
    def __processar_registro(self, valores: list[str]) -> RegistroMeteorologico:
        pass  # Work In Progress


    def __verificar_cabecalho(self, numeracao: int, valores: list[str], dados: dict):
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
