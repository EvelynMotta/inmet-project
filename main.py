from fileinput import close

from leitor import Leitor
from modelos.estacao import EstacaoMeteorologica


def main():
    anos_e_estacoes: dict[str, list[EstacaoMeteorologica]] = {}
    leitor = Leitor("dados")

    print("MENU PRINCIPAL:")
    print("1. Carregar arquivos da pasta;")
    print("2. Filtrar dados por estação(ões);")  # .split(",")
    print("3. Exibir estatísticas (média, máximo etc.);")
    print("4. Filtrar dados por data;")
    print("5. Exportar relatório;")
    print("6. Sair")


    entrada = input("Digite uma opção: ")

    if entrada == "1":
        anos_e_estacoes = leitor.carregar_arquivos()

        if not anos_e_estacoes:
            return "Falha ao carregar arquivos, tente novalemnte!"

        else:
            return "Arquivos carregados com sucesso!"

    elif entrada == "2":
        opcoes = leitor.estacoes_lidas()
        for opcao in opcoes:
            print(opcao)

        estacoes = input("Entre com a(s) estaçãos(ões) desejada(s):")
        estacoes2 = estacoes.strip().split(",")

        if estacoes2 in opcoes:
            print("")


    elif entrada == "3":
        pass

    elif entrada == "4":
        pass

    elif entrada == "5":
        pass

    elif entrada == "6":
        close()

    else:
        print("Comando inválido, tente novamente.")


if __name__ == '__main__':
    main()

