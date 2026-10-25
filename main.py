"""Gerenciador de Tarefas - projeto simples em Python (terminal).

Permite adicionar, listar, concluir e remover tarefas.
As tarefas ficam salvas no arquivo tarefas.json.
"""

import json
from pathlib import Path

ARQUIVO = Path("tarefas.json")


def carregar_tarefas():
    """Lê as tarefas do arquivo. Se não existir, retorna uma lista vazia."""
    if ARQUIVO.exists():
        with open(ARQUIVO, "r", encoding="utf-8") as f:
            return json.load(f)
    return []


def salvar_tarefas(tarefas):
    """Grava a lista de tarefas no arquivo."""
    with open(ARQUIVO, "w", encoding="utf-8") as f:
        json.dump(tarefas, f, ensure_ascii=False, indent=2)


def adicionar(tarefas):
    titulo = input("Digite a nova tarefa: ").strip()
    if not titulo:
        print("A tarefa não pode ser vazia.")
        return
    tarefas.append({"titulo": titulo, "concluida": False})
    salvar_tarefas(tarefas)
    print("Tarefa adicionada!")


def listar(tarefas):
    if not tarefas:
        print("Nenhuma tarefa cadastrada.")
        return
    print("\n--- Suas tarefas ---")
    for i, tarefa in enumerate(tarefas, start=1):
        status = "[x]" if tarefa["concluida"] else "[ ]"
        print(f"{i}. {status} {tarefa['titulo']}")


def pedir_numero(tarefas, acao):
    """Pergunta o número da tarefa e valida. Retorna o índice ou None."""
    listar(tarefas)
    if not tarefas:
        return None
    try:
        numero = int(input(f"Número da tarefa para {acao}: "))
    except ValueError:
        print("Digite um número válido.")
        return None
    if not 1 <= numero <= len(tarefas):
        print("Número fora da lista.")
        return None
    return numero - 1


def concluir(tarefas):
    indice = pedir_numero(tarefas, "concluir")
    if indice is not None:
        tarefas[indice]["concluida"] = True
        salvar_tarefas(tarefas)
        print("Tarefa concluída!")


def remover(tarefas):
    indice = pedir_numero(tarefas, "remover")
    if indice is not None:
        removida = tarefas.pop(indice)
        salvar_tarefas(tarefas)
        print(f"Tarefa removida: {removida['titulo']}")


def menu():
    tarefas = carregar_tarefas()
    while True:
        print("\n=== Gerenciador de Tarefas ===")
        print("1 - Adicionar tarefa")
        print("2 - Listar tarefas")
        print("3 - Concluir tarefa")
        print("4 - Remover tarefa")
        print("0 - Sair")
        opcao = input("Escolha uma opção: ").strip()

        if opcao == "1":
            adicionar(tarefas)
        elif opcao == "2":
            listar(tarefas)
        elif opcao == "3":
            concluir(tarefas)
        elif opcao == "4":
            remover(tarefas)
        elif opcao == "0":
            print("Até logo!")
            break
        else:
            print("Opção inválida. Tente novamente.")


if __name__ == "__main__":
    menu()
