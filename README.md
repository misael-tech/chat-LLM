#  Chat LLM — Assistente Inteligente

Aplicação web desenvolvida com Python e Django, integrada à Inteligência Artificial do Google Gemini, permitindo interações em linguagem natural e consultas a informações cadastradas no sistema.

O projeto explora a integração entre aplicações backend tradicionais e modelos de linguagem (LLMs), utilizando ferramentas Python para executar consultas aos dados da aplicação.

## Funcionalidades

- Chat interativo com Inteligência Artificial.
- Integração com Google Gemini.
- Cadastro de vendedores.
- Cadastro de metas individuais.
- Consulta de vendedores cadastrados.
- Integração entre IA e funções Python do backend.

##  Integração com Inteligência Artificial

O sistema utiliza um modelo de linguagem (LLM) para interpretar as mensagens enviadas pelo usuário.

Através de ferramentas disponibilizadas pelo backend, a IA pode solicitar consultas aos dados armazenados no banco de dados.

### Exemplo de interação

**Usuário:**
Quantos vendedores estão cadastrados?

**Fluxo de execução:**

1. O usuário envia uma mensagem pelo chat.
2. O Django recebe a solicitação.
3. A mensagem é encaminhada ao modelo Gemini.
4. A IA identifica a necessidade de consultar os vendedores.
5. O backend executa a ferramenta Python responsável pela consulta.
6. Os dados são retornados ao modelo.
7. A IA apresenta a resposta em linguagem natural.

## 🛠️ Tecnologias utilizadas

- Python
- Django
- Google Gemini API
- SQLite
- HTML
- CSS
- JavaScript

##  Estrutura do projeto

```text
chat-LLM/
├── chat/
│   ├── templates/
│   │   └── index.html
│   ├── views.py
│   └── models.py
├── metricas/
│   ├── migrations/
│   ├── models.py
│   └── views.py
├── config/
│   ├── settings.py
│   └── urls.py
├── manage.py
├── requirements.txt
└── README.md
```

##  Objetivo do projeto

Projeto desenvolvido para aprofundar conhecimentos em:

- Desenvolvimento Backend com Python e Django.
- Integração com APIs de Inteligência Artificial.
- Fundamentos de LLMs.
- Function Calling e execução de ferramentas.
- Comunicação entre aplicações e banco de dados.
- Manipulação de dados através do ORM do Django.

##  Desenvolvedor

**Misael Alves**

- GitHub: [misael-tech](https://github.com/misael-tech)

