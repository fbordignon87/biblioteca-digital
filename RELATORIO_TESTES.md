# Relatório de Testes e Feedback

## Testes Realizados

| Funcionalidade         | Resultado Esperado                       | Resultado Obtido   | Status  |
|------------------------|------------------------------------------|--------------------|---------|
| Listar documentos      | Exibir todos os PDFs disponíveis         | Funcionando        | ✅       |
| Adicionar documento    | Inserir novo arquivo na pasta            | Funcionando        | ✅       |
| Renomear documento     | Alterar o nome de um arquivo existente   | Funcionando        | ✅       |
| Remover documento      | Deletar um arquivo da lista              | Funcionando        | ✅       |

---

## Feedback Recebido (Simulado)

> “Seria útil mostrar o ano de publicação ao lado de cada documento, para facilitar a localização e o contexto do conteúdo.”

---

## Como o Feedback foi Incorporado

- Foi decidido que o ano de publicação será incluído no **nome do arquivo** no momento do upload.
- A lógica do sistema será adaptada para **extrair o ano do nome do arquivo** (ex: `artigo_2022.pdf`) e exibir essa informação ao lado do título.
- Atualizações futuras incluirão parsing automático de metadados do PDF, quando disponíveis, para capturar o ano com maior precisão.
- A interface foi ajustada para exibir o tipo de arquivo e status "Desconhecido" até que a lógica de ano seja implementada dinamicamente.

---

## Considerações Finais

O sistema atendeu aos requisitos principais de manipulação de arquivos e interface amigável. A estrutura do projeto e repositório estão prontos para melhorias contínuas com base no uso real e feedback dos usuários.
