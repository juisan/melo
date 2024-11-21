# Biblioteca Django

Este é um projeto de exposição virtual de coleções de livros, desenvolvido como parte da Trilha 7 de Desenvolvimento Back-End (Python), onde o objetivo é implementar um sistema de gerenciamento de coleções de livros, com autenticação baseada em Token, permissões e testes automatizados.

## Índice

- [Descrição do Projeto](#descrição-do-projeto)
- [Tecnologias Utilizadas](#tecnologias-utilizadas)
- [Instalação](#instalação)
- [Como Usar](#como-usar)
- [Testes Automatizados](#testes-automatizados)
- [Contribuição](#contribuição)
- [Licença](#licença)

## Descrição do Projeto

Este projeto permite que os usuários criem e gerenciem suas coleções de livros, criando uma exposição virtual de suas obras favoritas. Cada coleção de livros está associada a um usuário (colecionador), que pode adicionar ou remover livros de sua coleção. Somente o colecionador pode gerenciar sua própria coleção.

### Funcionalidades principais:
- Criação, listagem, edição e exclusão de coleções de livros.
- Autenticação de usuários via Token.
- Permissões personalizadas para garantir que apenas o colecionador possa modificar suas coleções.
- Documentação da API com drf-spectacular.
- Testes automatizados para garantir a qualidade e funcionalidade da API.

## Tecnologias Utilizadas

- **Django**: Framework para o desenvolvimento web.
- **Django Rest Framework (DRF)**: Para a criação de APIs.
- **djangorestframework-simplejwt**: Para autenticação via JWT (Token).
- **drf-spectacular**: Para documentação da API.
- **django-cors-headers**: Para configuração de CORS.
- **pytest**: Para testes automatizados.
- **coverage.py**: Para medir a cobertura de testes.

## Instalação

Para rodar este projeto localmente, siga os passos abaixo:

1. **Clone o repositório:**

   ```bash
   git clone https://github.com/juisan/melo.git
   cd melo
