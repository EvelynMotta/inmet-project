from modelos.estacao import EstacaoMeteorologica
from datetime import date

from modelos.registro import RegistroMeteorologico


class Filtro:

    @staticmethod
    def filtrar_estacoes(
        anos_e_estacoes: dict[str, list[EstacaoMeteorologica]],
        filtro_data: dict[str, date],
        filtro_estacoes: set[str]
    ) -> dict[str, list[EstacaoMeteorologica]]:
        if len(filtro_data) == 0 and len(filtro_estacoes) == 0:
            return anos_e_estacoes

        anos_e_estacoes_novos: dict[str, list[EstacaoMeteorologica]] = {}
        if len(filtro_estacoes) > 0:
            for ano, estacoes in anos_e_estacoes.items():
                anos_e_estacoes_novos[ano] = [estacao for estacao in estacoes if estacao.nome in filtro_estacoes]

        if len(filtro_data) > 0:
            dict_ref = anos_e_estacoes_novos if len(anos_e_estacoes_novos) > 0 else anos_e_estacoes
            for ano, estacoes in dict_ref.items():
                com_registros_filtrados = [EstacaoMeteorologica(
                    estacao.nome,
                    estacao.codigo,
                    estacao.regiao,
                    estacao.uf,
                    estacao.latitude,
                    estacao.longitude,
                    estacao.altitude,
                    registros=Filtro.__filtrar_registros(estacao.registros, filtro_data)
                ) for estacao in estacoes]
                anos_e_estacoes_novos[ano] = [estacao for estacao in com_registros_filtrados if len(estacao.registros) > 0]

        return anos_e_estacoes_novos

    @staticmethod
    def __filtrar_registros(registros: list[RegistroMeteorologico], filtro_data: dict[str, date]) -> list[RegistroMeteorologico]:
        registros_filtrados = [registro for registro in registros
                               if registro.data and (filtro_data['inicio'] <= registro.data <= filtro_data['fim'])]
        return registros_filtrados