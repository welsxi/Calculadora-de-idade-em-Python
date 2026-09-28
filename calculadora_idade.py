from datetime import date

def calcular_idade(dia, mes, ano):
    hoje = date.today()
    nascimento = date(ano, mes, dia)

    idade = hoje.year - nascimento.year

    # Verifica se já fez aniversário este ano
    fez_aniversario = (hoje.month, hoje.day) >= (nascimento.month, nascimento.day)
    if not fez_aniversario:
        idade -= 1

    return idade


def main():
    print("=== Calculadora de Idade ===")

    try:
        dia = int(input("Digite o dia de nascimento: "))
        mes = int(input("Digite o mês de nascimento: "))
        ano = int(input("Digite o ano de nascimento: "))

        idade = calcular_idade(dia, mes, ano)

        print(f"\nVocê tem {idade} anos.")

    except ValueError as erro:
        print(f"\nData inválida! Verifique se o dia, mês e ano existem de verdade.")
        print(f"Detalhe do erro: {erro}")

    input("\nPressione ENTER para sair...")


if __name__ == "__main__":
    main()
