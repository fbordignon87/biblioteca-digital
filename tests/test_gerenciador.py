import unittest
import os
import shutil
from biblioteca import gerenciador

class TestGerenciador(unittest.TestCase):
    def setUp(self):
        self.test_dir = "test_docs"
        os.makedirs(self.test_dir, exist_ok=True)
        # Criar arquivos de exemplo
        with open(os.path.join(self.test_dir, "artigo_2023.pdf"), "w") as f:
            f.write("PDF")
        with open(os.path.join(self.test_dir, "livro_2022.epub"), "w") as f:
            f.write("EPUB")
        with open(os.path.join(self.test_dir, "outro.txt"), "w") as f:
            f.write("Não permitido")

    def tearDown(self):
        shutil.rmtree(self.test_dir)

    def test_listar_documentos_filtra_por_tipo(self):
        docs = gerenciador.listar_documentos(self.test_dir)
        nomes = [doc['nome'] for doc in docs]
        self.assertIn("artigo_2023.pdf", nomes)
        self.assertIn("livro_2022.epub", nomes)
        self.assertNotIn("outro.txt", nomes)

    def test_renomear_documento(self):
        original = os.path.join(self.test_dir, "artigo_2023.pdf")
        novo_nome = "renomeado_2023.pdf"
        gerenciador.renomear_documento(original, novo_nome)
        novo_caminho = os.path.join(self.test_dir, novo_nome)
        self.assertTrue(os.path.exists(novo_caminho))

if __name__ == '__main__':
    unittest.main()
