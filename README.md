# reuso_de_software_final

# Desenvolvimento de API para a Universidade Federal do Ceará (UFC)

Você foi contratado para desenvolver uma API para a **Universidade Federal do Ceará (UFC)** que permita acessar informações sobre os cursos disponíveis.  

A API pode ser implementada na **linguagem desejada**, mas deve usar **alguma base de dados alimentada por você**. A tecnologia da base de dados também é uma escolha do aluno.  

O código deve ser **comentado detalhadamente**.

## Funcionalidades da API

A API RESTful deve contemplar os seguintes serviços:

- **Listar todos os cursos** (`GET /cursos`)
- **Obter um curso específico pelo ID** (`GET /cursos/{curso_id}`)
- **Adicionar um novo curso** (`POST /cursos`)
- **Atualizar um curso existente pelo ID** (`PUT /cursos/{curso_id}`)
- **Remover um curso pelo ID** (`DELETE /cursos/{curso_id}`)

## Estrutura do Banco de Dados

A base de dados deve conter as seguintes informações:

- **ID** (chave primária, autoincrementada)
- **Nome do curso**
- **Descrição**
- **Duração** (em semestres)
- **Modalidade** (Presencial ou EAD)

## Requisitos

Implemente o código correspondente e explique o funcionamento de cada endpoint.
