# importação das bibliotecas padrão do python
# json: leitura do arquivo de perguntas
# pathlib: manipulação de caminhos de arquivos e pastas
# gerar a data e hora no relatorio em arquivo txt
# os e platform: limpeja de tela de acordo com sistema operacional
import json
from pathlib import Path
from datetime import datetime
import os
import platform


# função: limpa_tela
# limpar o terminal para melhora
# a vizualização do quiz durante a execução
# A função identifica qual o sistema operacional
# para usar o comando correto o (Windows ou Linux/Mac).
def limpar_tela():
    equipamento = platform.system()
    if equipamento == "Windows":
        os.system("cls")
    else:
        os.system("clear")


# função: executar o quiz
# responsavel por carregar as perguntas do quiz
# a partir de um arquivo JSON externo.
# Também executa o tratamento de erros, 
# garantir que o arquivo nãp quebre caso o arquivo não exista
# ou esteja mal formatado
def exercutar_quiz():
    passagens = Path("data/perguntas.json")
    try:
        with open(passagens, "r", encoding="utf-8") as registro:
            return json.load(registro)
    except FileNotFoundError:
        print("erro.registro de perguntas não achado")
        return []
    except json.JSONDecodeError:
        print("erro.registro json invalido")
        return []
    

# função principal: praticar quiz
# Esta é a função centra do programa
# Ela controla toda a logica do quiz:
# - carregar as perguntas
# -Interação com usuario
# -Calculo da pontuação
# -Armazenamento de historicos e perguntas
# -Definição de sua casa principal
def praticar_quiz():
    questionamentos = exercutar_quiz()
    if not questionamentos:
        return

    # Dicionario que guarda a pontuação das casas
    casas = {
        "Grifinória": 0,
        "Sonserina": 0,
        "Corvinal": 0,
        "Lufa-Lufa": 0
    }


    # Lista reposovel por guarda historico de perguntas 
    # e reposta do usuario
    regresso = []

    limpar_tela()

    print("🏰 Seja bem-vindo no Quiz de Hogwarts!")
    input("\ndigite ENTER para iniciar o quiz")

    for h, p in enumerate(questionamentos):
        limpar_tela()
        print(f"Questão {h + 1} - {p['pergunta']}\n")


        # Exibição da altenativas enumeradas
        for idx, alt in enumerate(p["alternativas"], start=1):
            print(f"{idx} - {alt}")


        # Loop que garantir que o usuario
        # informe uma reposta valida
        while True:
            try:
                resposta = int(input("\nDigite sua resposta: "))
                if 1 <= resposta <= len(p["alternativas"]):
                    casa_opcao = p["casa"][resposta - 1]
                    casas[casa_opcao] += 1
                    regresso.append((p["pergunta"], p["alternativas"][resposta - 1]))
                    break
                else:
                    print("reposta invalida")
            except ValueError:
                print("digite os numeros")


    # Apos o usuario reponde as perguntas, 
    # o programa identifica a casa com maior pontuação
    casa_destino = max(casas, key=casas.get)


    # Chamada da função reponsavel por gerar o relatorio final do quiz
    # o relatorio final e exibir o resultado
    gerar_conclusao(casa_destino, casas, regresso)


# função: gerar_conclusão
# resposavel por gerar o relatorio final do quiz
# Cria a pasta de resultados, escreve o arquivo TXT
# com a data e hora, exibe o resultado no terminal
# e apresenta historico completo de perguntas e repostas
def gerar_conclusao(casa, pontuacao, regresso):
    pasta = Path("resultados")
    pasta.mkdir(exist_ok=True)

    nome_anexo = pasta / f"relatorio_{datetime.now().strftime('%d-%m-%Y_%H-%M')}.txt"

    with open(nome_anexo, "w", encoding="utf-8") as arq:
        arq.write("Relatorio do quiz de Hogwartss\n")
        arq.write("============================\n\n")
        arq.write(f"Sua casa e: {casa}\n\n")
        arq.write("Pontuação:\n")
        for r, p in pontuacao.items():
            arq.write(f"{r}: {p}\n")

        arq.write("\nHistórico de Respostas:\n")
        for a in regresso:
            arq.write(f"- {a[0]} | Resposta: {a[1]}\n")

    limpar_tela()
    print(f"✨ Sua casa em Hogwarts é: {casa}!")
    print(f"\nRelatório salvo em: {nome_anexo}")


# Bloco principal da execução
# Garantir que o programa so executara
# quando o arquivo for rodado diretamente
# e não for importado como modulo
if __name__ == "__main__":
    praticar_quiz()





