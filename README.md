# 📚 Servidor Biblioteca - Trabalho 3 (Sistemas Distribuídos)

Este projeto é parte do **Trabalho 3 da disciplina de Sistemas Distribuídos** e implementa uma aplicação no estilo **cliente-servidor via API REST**, com o servidor em **Java (Spring Boot)** e o cliente em **JavaScript (HTML + Fetch API)**.

---
## Autores
Maria Eduarda Santana Marques

Mauricio Miranda Carneiro

## 🔧 Tecnologias Usadas

### Servidor (Back-end)
- Java 17+
- Spring Boot
- Spring Web
- Spring Data JPA
- Banco de dados em memória (H2)

### Cliente (Front-end)
- HTML, CSS e JavaScript
- Fetch API
- SweetAlert2
- Python
---

## ⚙️ Como Executar

### 1. Clonar o projeto
```bash
git clone https://github.com/seu-usuario/servidor-biblioteca.git
cd servidor-biblioteca
```

### 2. Iniciar o servidor Spring Boot
```bash
./mvnw spring-boot:run
```
> O servidor inicia em `http://localhost:8080`.

### 3. Abrir a interface Web
Abra o arquivo `index.html` no navegador (ou com extensão Live Server no VSCode).

---

## 📌 Endpoints REST

| Método | Rota                | Ação                       |
|--------|---------------------|----------------------------|
| GET    | `/itens`            | Listar todos os itens      |
| POST   | `/itens`            | Cadastrar novo item        |
| GET    | `/itens/{id}`       | Buscar item por ID         |
| PUT    | `/itens/{id}`       | Atualizar item existente   |
| DELETE | `/itens/{id}`       | Deletar item por ID        |

---

## 📁 Estrutura do Servidor

```
servidor-biblioteca/
├── controller/
│   └── ItemController.java
├── model/
│   └── Item.java
├── repository/
│   └── ItemRepository.java
└── ServidorBibliotecaApplication.java
```

---

## 💡 Funcionalidades da Interface Web

- Cadastro de **livros**, **revistas** e **publicações**
- Listagem dos itens com estilização por tipo
- Edição com modal interativo (SweetAlert)
- Exclusão com confirmação
- Comunicação via `fetch()` com o servidor Java

---

## 🧪 Teste com outro cliente

Você pode usar `curl` ou Postman para testar:

```bash
curl -X POST http://localhost:8080/itens \
  -H "Content-Type: application/json" \
  -d '{"titulo": "Teste", "autor": "Fulano", "tipo": "livro"}'
```

---

## 🤝 Dupla e Integração

- Cliente implementado em **HTML + JS**
- Servidor em **Java Spring Boot**
- Comunicação entre diferentes linguagens
- A aplicação segue o modelo cliente-servidor via **Web Services REST**
