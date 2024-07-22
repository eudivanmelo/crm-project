# CRM PROJECT

Este projeto é um CRM (Customer Relationship Management) desenvolvido para gerenciar um supermercado. O sistema permitirá o cadastro, edição e remoção de produtos, gerenciamento de categorias de produtos e controle de estoque. O objetivo é criar uma aplicação robusta e eficiente que permita ao operador de caixa iniciar uma venda, adicionar/remover produtos e finalizar a venda por cancelamento ou pagamento, atualizando automaticamente o estoque e o faturamento total da empresa.

Este projeto faz parte da trilha Back-end do Nadic. Mais informações podem ser encontradas [aqui](https://nadic.notion.site/Back-end-c00f481699c448e49fb2578e30a527bd).

---

## **Parte 1: Git/Github**

### Conteúdo
1. Clone de Repositório
2. Criação de Repositório
3. Pull / Push
4. Criação de Branch
5. Merge
6. Gitflow

### Documentação
- [Git tutorial](https://www.atlassian.com/br/git/tutorials/comparing-workflows/gitflow-workflow)
- [Documentação git](https://git-scm.com/doc)
- [Documentação github](https://docs.github.com/pt)

## **Parte 2: Conceitos Básicos**

### Conteúdo
1. Variáveis
2. Estrutura condicional
3. Estrutura de repetição
4. Coleções no Python: Listas, Tuplas e Dicionários
5. Funções
6. Classes e Orientação a objetos

## **Parte 3: Banco de Dados**

### Conteúdo
1. Estudo sobre tipos de Bancos de Dados (relacionais, não relacionais, etc.)

2. Modelo Entidade Relacionamento (MER)
    - Entidade
    - Relacionamento
    - Cardinalidade
    - Atributos
    - Generalização / Especialização
    - Entidade Associativa
    - Criação de Diagrama Entidade Relacionamento (DER) na ferramenta brModelo (ou outra similar)

3. Modelo Relacional (MR)
    - Transformação entre modelos (MER - MR)
    - Restrições (chaves primárias, secundárias, etc.)
    - Normalização (até a terceira forma normal)

4. Comandos SQL (utilizar MySQL e/ou PostgreSQL e/ou SQLite)
    - Criação de Banco de Dados e Tabelas
    - Alterações e Restrições
    - Consultas Básicas e Avançadas (select e suas restrições)
    - INSERT, UPDATE e DELETE
    - Agrupamento de tabelas (JOINS)
    - GROUP BY, HAVING e Funções de Agregações

5. PROJETO
    - Criar um Projeto de Banco de Dados, desde um nível de abstração mais elevado, como Modelo ER (através do diagrama ER), passando para o modelo relacional (tabelas simples, tabelas com relacionamentos, etc.) até o projeto no Banco de Dados (pode usar MySQL e/ou PostgreSQL e/ou SQLite e/ou outro que você achar válido, o interessante é praticar, inclusive em mais de um). Nesse projeto, deverá ser possível consultar, inserir, deletar e atualizar informações em um Banco de Dados, respeitando o relacionamento entre os dados e as devidas restrições.

## **Parte 4: Framework Django**

### Conteúdo
1. Criação de ambiente virtual
2. Criação de um projeto e criação de apps
3. Urls
4. Models
5. Views
6. Templates
7. Forms
8. Utilização de Class based view (CBV) e function based view (FBV)

### PROJETO
- Criar um mecanismo de CRM para qualquer tipo de empresa, onde será possível cadastrar/remover/editar produtos, assim como definir quantidade em estoque e sempre que realizado uma venda o estoque e o faturamento total da empresa deve ser atualizado.

### Documentação
- [Documentação Django Framework](https://docs.djangoproject.com/en/4.1/)
- [Documentação Class Based Views (CBVs)](https://docs.djangoproject.com/en/4.1/topics/class-based-views/)

## **Parte 5: Django REST framework**

### Conteúdo
1. O que são Requests e Responses
2. O que é uma API REST
3. Model Serializers
4. APIView (Class-based views) e @api_view (Function Based views)
5. ViewSets e Routers
6. Criação de API com POST/GET/PUT/DELETE (CRUD)
7. Autenticação (Sessão/JWT/Oauth2)
8. Permissões (DRF permissions)

### PROJETO
- Continuar o projeto do CRM, agora criando sua API. Crie endpoints para criar conta e realizar login. Crie endpoints para listar/cadastrar/editar/remover produtos e estes endpoints só poderão ser acessados se o usuário estiver “logado”. Crie um endpoint para listar os detalhes do produto assim como seu estoque. Crie um endpoint para listar o faturamento da empresa, ele só deve ser acessado pelo dono da empresa.

### Documentação
- [Documentação Django REST framework](https://www.django-rest-framework.org/)
