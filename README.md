# FastAPI Aula - API de Soma

Uma API simples desenvolvida em **FastAPI** para demonstrar conceitos de desenvolvimento web, testes automatizados e containerização.

## 📋 Descrição

Esta aplicação disponibiliza endpoints para realizar operações de soma de números inteiros. É um projeto educacional que implementa boas práticas como testes automatizados, pipeline CI/CD e containerização com Docker.

## 🚀 Funcionalidades

- ✅ Endpoint raiz com mensagem de status
- ✅ Endpoint para soma de dois números via URL
- ✅ Testes automatizados com pytest
- ✅ Containerização com Docker (multi-stage build)
- ✅ Pipeline CI/CD com GitHub Actions

## 📂 Estrutura do Projeto

```
.
├── app.py                          # Aplicação FastAPI principal
├── test_app.py                     # Testes com pytest
├── requirements.txt                # Dependências do projeto
├── Dockerfile                      # Configuração Docker
├── .gitignore                      # Arquivos ignorados pelo git
├── .dockerignore                   # Arquivos ignorados pelo Docker
└── .github/workflows/test.yml      # Pipeline CI/CD
```

## 🛠️ Tecnologias

- **FastAPI** - Framework web moderno e rápido
- **Python 3.13** - Linguagem de programação
- **pytest** - Framework de testes
- **Docker** - Containerização
- **GitHub Actions** - CI/CD

## 📦 Dependências

Principais dependências do projeto:
- fastapi==0.135.2
- pytest==9.0.2
- uvicorn (incluído no fastapi)

Veja [requirements.txt](requirements.txt) para a lista completa.

## ⚙️ Instalação

### Localmente

1. Clone o repositório:
```bash
git clone https://github.com/suethttps/fast_api-soma.git
cd fast_api_aula
```

2. Crie um ambiente virtual (opcional, mas recomendado):
```bash
python -m venv venv
source venv/bin/activate  # No Windows: venv\Scripts\activate
```

3. Instale as dependências:
```bash
pip install -r requirements.txt
```

### Com Docker

```bash
docker build -t fast-api-aula .
docker run -p 8000:8000 fast-api-aula
```

## 🏃 Como Executar

### Executar a aplicação localmente

```bash
python app.py
```

A API estará disponível em `http://localhost:8000`

### Executar os testes

```bash
pytest -v
```

Para ver a cobertura de testes:
```bash
pytest -v --cov=.
```

## 📡 Endpoints

### 1. Raiz da API
```
GET /
```
Retorna uma mensagem de status da API.

**Resposta:**
```json
{
  "message": "API de soma funcionando"
}
```

### 2. Soma de dois números
```
GET /sum/{a}/{b}
```
Retorna a soma de dois números inteiros.

**Parâmetros:**
- `a` (integer): Primeiro número
- `b` (integer): Segundo número

**Exemplo:**
```bash
curl http://localhost:8000/sum/10/5
```

**Resposta:**
```json
{
  "result": 15
}
```

## 🧪 Testes

O projeto inclui testes automatizados para:
- Função de soma (`sum_values`)
- Endpoint raiz (`GET /`)
- Endpoint de soma (`GET /sum/{a}/{b}`)

Para executar:
```bash
pytest -v
```

## 🔄 Pipeline CI/CD

A aplicação possui uma pipeline automática (GitHub Actions) que:
- Executa automaticamente quando há push na branch `master`
- Instala as dependências
- Roda todos os testes com pytest
- Valida a qualidade do código

Veja [.github/workflows/test.yml](.github/workflows/test.yml) para mais detalhes.

## 🐳 Docker

O projeto utiliza um **Dockerfile multi-stage** para otimizar o tamanho da imagem:

1. **Builder stage**: Instala as dependências
2. **Runtime stage**: Cria a imagem final com apenas o necessário

Também inclui um **HEALTHCHECK** para monitorar a saúde da aplicação.

```bash
# Build
docker build -t fast-api-aula .

# Run
docker run -p 8000:8000 fast-api-aula

# Verificar health
docker ps  # Verifique o status do HEALTHCHECK
```

## 📖 Documentação Interativa

Quando a API está rodando, acesse:
- **Swagger UI**: `http://localhost:8000/docs`
- **ReDoc**: `http://localhost:8000/redoc`

## 🤝 Contribuindo

1. Faça um Fork do projeto
2. Crie uma branch para sua feature (`git checkout -b feature/MinhaFeature`)
3. Commit suas mudanças (`git commit -m 'Add MinhaFeature'`)
4. Push para a branch (`git push origin feature/MinhaFeature`)
5. Abra um Pull Request

## 📝 Licença

Este projeto é um projeto educacional.

## 👨‍💻 Autor

Criado como material de aula.

---

**Dúvidas?** Abra uma issue no repositório!
