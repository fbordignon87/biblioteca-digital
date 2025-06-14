import os
import shutil

def listar_documentos(diretorio_base, extensoes_permitidas=None):
    if extensoes_permitidas is None:
        extensoes_permitidas = ['.pdf', '.epub']

    arquivos = []
    for root, dirs, files in os.walk(diretorio_base):
        for file in files:
            ext = os.path.splitext(file)[1].lower()
            if ext not in extensoes_permitidas:
                continue  # Pula arquivos que não são pdf ou epub
            caminho_completo = os.path.join(root, file)
            ano = extrair_ano(file) or "Desconhecido"
            arquivos.append({"nome": file, "extensao": ext, "ano": ano, "caminho": caminho_completo})
    return arquivos


def extrair_ano(nome_arquivo):
    for parte in nome_arquivo.split("_"):
        if parte.isdigit() and len(parte) == 4:
            return parte
    return None

def adicionar_documento(origem, destino):
    shutil.copy2(origem, destino)

def renomear_documento(caminho_antigo, novo_nome):
    pasta = os.path.dirname(caminho_antigo)
    novo_caminho = os.path.join(pasta, novo_nome)
    os.rename(caminho_antigo, novo_caminho)

def remover_documento(caminho):
    os.remove(caminho)
