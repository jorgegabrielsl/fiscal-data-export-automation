# Automação de Exportação de Dados Fiscais

Sistema de automação desenvolvido em Python para geração e exportação
de dados fiscais utilizados por empresas multinacionais.

O script conecta a um banco de dados PostgreSQL, extrai informações
de faturamento e estrutura os dados no formato exigido por parceiros
comerciais, gerando arquivos TXT padronizados.

Os arquivos são gerados automaticamente e enviados diariamente,
permitindo a integração com sistemas de fornecedores e indústrias.

## Contexto

Empresas multinacionais como indústrias e fornecedores exigem
o envio periódico de dados de faturamento para acompanhamento
de vendas e controle comercial.

Para automatizar esse processo, foi desenvolvido um sistema que:

- consulta dados no banco PostgreSQL
- aplica regras de transformação
- gera arquivos TXT no layout exigido
- organiza os arquivos por fornecedor
- executa automaticamente via agendador de tarefas

## Funcionalidades

- Extração de dados via SQL
- Processamento e tratamento com Pandas
- Geração de arquivos TXT estruturados
- Automação do processo de exportação
- Execução automática via agendador do sistema

## Tecnologias

- Python
- PostgreSQL
- Pandas
- SQL
- Automação de processos
