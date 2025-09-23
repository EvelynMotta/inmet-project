from datetime import datetime, date

from filtro import Filtro
from leitor import Leitor
from modelos.estacao import EstacaoMeteorologica
from modelos.estatisticas import Estatistica


def limpar():
    from os import name,system
    comando = "cls" if name == "nt" else "clear"
    system(comando)

def definir_filtros_estacoes(estacoes_filtro: set[str], leitor: Leitor):
    opcoes = tuple(leitor.estacoes_lidas())
    for n, opcao in enumerate(opcoes):
        print(f"{n}. {opcao}")

    estacoes = input("Entre com a(s) estaçãos(ões) desejada(s):")
    estacoes2 = estacoes.strip().split(",")

    for estacao in estacoes2:
        try:
            estacao = int(estacao)
            estacoes_filtro.add(opcoes[estacao])

        except ValueError:
            print("Estaçãos(ões) inválida(s), tente novamente.")
            continue

def definir_filtros_data(datas_filtro: dict[str, date]) -> bool:
    data_inicio = input("Entre com a data inicial(dd/mm/yyyy):")
    data_fim = input("Entre com a data final(dd/mm/yyyy):")

    try:
        data_inicio = datetime.strptime(data_inicio, "%d/%m/%Y").date()
        data_fim = datetime.strptime(data_fim, "%d/%m/%Y").date()

        datas_filtro["inicio"] = data_inicio
        datas_filtro["fim"] = data_fim

    except ValueError:
        print("Datas inválidas, tente novamente.")
        return False
    return True

def mostrar_estatisticas(anos_e_estacoes:  dict[str, list[EstacaoMeteorologica]]):
    for ano, estacoes in anos_e_estacoes.items():
        if len(estacoes) == 0:
            continue
        print(f"===== {ano} =====")
        for estacao in estacoes:
            estatistica = Estatistica(estacao.registros)
            print(f"--- {estacao.nome} ---")
            print(f"Temperatura média: {estatistica.media_temperatura():.1f}")
            print(f"Umidade máxima: {estatistica.max_umidade()}")
            print(f"Precipitação total: {estatistica.total_precipitacao()}\n")
        print()

def exportar_relatorio(anos_e_estacoes: dict[str, list[EstacaoMeteorologica]]):
    with open("Relatório.txt", "w", encoding="utf-8") as arquivo:
        for ano, estacoes in anos_e_estacoes.items():
            if len(estacoes) == 0:
                continue
            arquivo.write(f"===== {ano} =====\n")
            for estacao in estacoes:
                estatistica = Estatistica(estacao.registros)
                arquivo.write(f"--- {estacao.nome} ---\n")
                arquivo.write(f"Temperatura média: {estatistica.media_temperatura():.1f}\n")
                arquivo.write(f"Umidade máxima: {estatistica.max_umidade()}\n")
                arquivo.write(f"Precipitação total: {estatistica.total_precipitacao()}\n\n")
            arquivo.write("\n")
    print("\033[1;32m" + "Relatório exportado com sucesso!" + "\033[0m")

def main():
    anos_e_estacoes: dict[str, list[EstacaoMeteorologica]] | None = None
    leitor = Leitor("dados")
    estacoes_filtro = set()
    datas_filtro: dict[str, date] = {}

    while True:
        print("MENU PRINCIPAL:")

        if len(estacoes_filtro) > 0:
            print(f"\nFiltrando por estações: {", ".join(estacoes_filtro)}")

        if len(datas_filtro) > 0:
            inicio = datas_filtro['inicio'].strftime("%d/%m/%Y")
            fim = datas_filtro['fim'].strftime("%d/%m/%Y")

            print(f"Filtrando por datas: {inicio} à {fim}")

        print("\n1. Carregar arquivos da pasta;")
        print("2. Visualizar estações;")
        print("3. Exibir estatísticas (média, máximo etc.);")
        print("4. Filtrar dados por estação(ões);")  # .split(",")
        print("5. Filtrar dados por data;")
        print("6. Exportar relatório;")
        print("7. Sair\n")


        entrada = input("Digite uma opção: ").strip()
        limpar()

        if entrada == "1":
            anos_e_estacoes = leitor.carregar_arquivos()

            if not anos_e_estacoes:
                print("Falha ao carregar arquivos, tente novamente!")

        elif not anos_e_estacoes and entrada != "7":
            print("Arquivos não carregados. Para usar estas opções, carregue os CSVs primeiro.\n")

        elif entrada == "2":
            anos_e_estacoes_filtrados = Filtro.filtrar_estacoes(anos_e_estacoes, datas_filtro, estacoes_filtro)
            for ano, estacoes in anos_e_estacoes_filtrados.items():
                print(f"===== {ano} =====")
                for estacao in estacoes:
                    print(estacao)

        elif entrada == "3":
            anos_e_estacoes_filtrados = Filtro.filtrar_estacoes(anos_e_estacoes, datas_filtro, estacoes_filtro)
            mostrar_estatisticas(anos_e_estacoes_filtrados)

        elif entrada == "4":
            definir_filtros_estacoes(estacoes_filtro, leitor)

        elif entrada == "5":
            ok = definir_filtros_data(datas_filtro)
            if not ok:
                continue

        elif entrada == "6":
            anos_e_estacoes_filtrados = Filtro.filtrar_estacoes(anos_e_estacoes, datas_filtro, estacoes_filtro)
            exportar_relatorio(anos_e_estacoes_filtrados)

        elif entrada == "7":
            break

        else:
            print("Comando inválido, tente novamente.")

        input("Pressione ENTER para continuar...")
        limpar()

if __name__ == '__main__':
    main()

