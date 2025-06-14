import argparse
from biblioteca.gerenciador import listar_documentos, adicionar_documento, renomear_documento, remover_documento

def main():
    parser = argparse.ArgumentParser(description="Sistema de Gerenciamento de Biblioteca Digital")
    subparsers = parser.add_subparsers(dest="comando")

    parser_listar = subparsers.add_parser("listar")
    parser_listar.add_argument("diretorio", help="Diretório base")

    parser_adicionar = subparsers.add_parser("adicionar")
    parser_adicionar.add_argument("origem", help="Caminho do arquivo de origem")
    parser_adicionar.add_argument("destino", help="Caminho de destino")

    parser_renomear = subparsers.add_parser("renomear")
    parser_renomear.add_argument("caminho", help="Caminho do arquivo a ser renomeado")
    parser_renomear.add_argument("novo_nome", help="Novo nome do arquivo")

    parser_remover = subparsers.add_parser("remover")
    parser_remover.add_argument("caminho", help="Caminho do arquivo a ser removido")

    args = parser.parse_args()

    if args.comando == "listar":
        arquivos = listar_documentos(args.diretorio)
        for a in arquivos:
            print(f"{a['nome']} - {a['extensao']} - {a['ano']} - {a['caminho']}")
    elif args.comando == "adicionar":
        adicionar_documento(args.origem, args.destino)
        print("Documento adicionado com sucesso.")
    elif args.comando == "renomear":
        renomear_documento(args.caminho, args.novo_nome)
        print("Documento renomeado com sucesso.")
    elif args.comando == "remover":
        remover_documento(args.caminho)
        print("Documento removido com sucesso.")
    else:
        parser.print_help()
