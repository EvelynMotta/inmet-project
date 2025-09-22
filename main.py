from datetime import datetime, date
from leitor import Leitor
from modelos.estacao import EstacaoMeteorologica

def limpar():
    from os import name,system
    comando = "cls" if name == "nt" else "clear"
    system(comando)

def filtrar_estacoes(estacoes_filtro: set[str], leitor: Leitor):
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

def main():
    anos_e_estacoes: dict[str, list[EstacaoMeteorologica]] = {}
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
        print("2. Filtrar dados por estação(ões);")  # .split(",")
        print("3. Exibir estatísticas (média, máximo etc.);")
        print("4. Filtrar dados por data;")
        print("5. Exportar relatório;")
        print("6. Sair\n")


        entrada = input("Digite uma opção: ")
        limpar()

        if entrada == "1":
            anos_e_estacoes = leitor.carregar_arquivos()

            if not anos_e_estacoes:
                print("Falha ao carregar arquivos, tente novamente!")

        elif entrada == "2":
            filtrar_estacoes(estacoes_filtro, leitor)

        elif entrada == "3":
            pass

        elif entrada == "4":
            data_inicio = input("Entre com a data inicial(dd/mm/yyyy):")
            data_fim = input("Entre com a data final(dd/mm/yyyy):")

            try:
                data_inicio = datetime.strptime(data_inicio, "%d/%m/%Y").date()
                data_fim = datetime.strptime(data_fim, "%d/%m/%Y").date()

                datas_filtro["inicio"] = data_inicio
                datas_filtro["fim"] = data_fim

            except ValueError:
                print("Datas inválidas, tente novamente.")
                continue

        elif entrada == "5":
            pass

        elif entrada == "6":
            break

        else:
            print("Comando inválido, tente novamente.")


if __name__ == '__main__':
    main()

