import argparse
import os
from biblioteca.gerenciador import (
    listar_documentos,
    adicionar_documento,
    renomear_documento,
    remover_documento
)

def main():
    parser = argparse.ArgumentParser(
        description="📚 Sistema de Gerenciamento de Biblioteca Digital"
    )

    subparsers = parser.add_subparsers(dest="comando")

    # Subcomando: listar
    parser_listar = subparsers.add_parser("listar", help="Listar documentos PDF/EPUB no diretório")
    parser_listar.add_argument("diretorio", help="Diretório base onde estão os arquivos")

    # Subcomando: adicionar
    parser_adicionar = subparsers.add_parser("adicionar", help="Adicionar novo documento")
    parser_adicionar.add_argument("origem", help="Caminho do arquivo de origem (ex: Downloads/arquivo.pdf)")
    parser_adicionar.add_argument("destino", help="Caminho de destino final (ex: biblioteca/arquivo.pdf)")

    # Subcomando: renomear
    parser_renomear = subparsers.add_parser("renomear", help="Renomear documento")
    parser_renomear.add_argument("caminho", help="Caminho atual do documento (ex: biblioteca/arquivo.pdf)")
    parser_renomear.add_argument("novo_nome", help="Novo nome do arquivo (ex: artigo_2024.pdf)")

    # Subcomando: remover
    parser_remover = subparsers.add_parser("remover", help="Remover documento existente")
    parser_remover.add_argument("caminho", help="Caminho completo do documento a ser removido")

    args = parser.parse_args()

    if args.comando == "listar":
        if not os.path.isdir(args.diretorio):
            print("❌ Diretório não encontrado.")
            return
        arquivos = listar_documentos(args.diretorio)
        if not arquivos:
            print("⚠️ Nenhum documento PDF ou EPUB encontrado.")
        for a in arquivos:
            print(f"{a['nome']} - {a['extensao']} - {a['ano']} - {a['caminho']}")

    elif args.comando == "adicionar":
        if not os.path.exists(args.origem):
            print("❌ Arquivo de origem não encontrado.")
            return
        try:
            adicionar_documento(args.origem, args.destino)
            print("✅ Documento adicionado com sucesso.")
        except Exception as e:
            print(f"Erro ao adicionar documento: {e}")

    elif args.comando == "renomear":
        if not os.path.exists(args.caminho):
            print("❌ Caminho do arquivo não encontrado.")
            return
        try:
            renomear_documento(args.caminho, args.novo_nome)
            print("✅ Documento renomeado com sucesso.")
        except Exception as e:
            print(f"Erro ao renomear documento: {e}")

    elif args.comando == "remover":
        if not os.path.exists(args.caminho):
            print("❌ Caminho do arquivo não encontrado.")
            return
        try:
            remover_documento(args.caminho)
            print("✅ Documento removido com sucesso.")
        except Exception as e:
            print(f"Erro ao remover documento: {e}")

    else:
        parser.print_help()
