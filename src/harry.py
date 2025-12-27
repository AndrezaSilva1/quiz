import json
from pathlib import Path
from datetime import datetime
import os
import platform

# função que limpar a tela
def limpar_tela():
    equipamento = platform.system()
    if equipamento == "Windows":
        os.system("cls")
    else:
        os.system("clear")

# função parar carregar as perguntas
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
    
# função principal do quiz
def praticar_quiz():
    questionamentos = exercutar_quiz()
    if not questionamentos:
        return
    
    casas = {
        "Grifinória": 0,
        "Sonserina": 0,
        "Corvinal": 0,
        "Lufa-Lufa": 0
    }

    regresso = []

    limpar_tela()

    print("🏰 Seja bem-vindo no Quiz de Hogwarts!")
    input("\ndigite ENTER para iniciar o quiz")

    for h, p in enumerate(questionamentos):
        limpar_tela()
        print(f"Questão {h + 1} - {p['pergunta']}\n")

        for idx, alt in enumerate(p["alternativas"], start=1):
            print(f"{idx} - {alt}")

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
    
    casa_destino = max(casas, key=casas.get)
    gerar_conclusao(casa_destino, casas, regresso)

# função para gerar o relatorio
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

# execução 
if __name__ == "__main__":
    praticar_quiz()





