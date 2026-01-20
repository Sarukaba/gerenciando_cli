# 🗂️ Task Manager CLI com Dashboard de Progresso

Sistema de gerenciamento de tarefas em **Python**, executado via **linha de comando (CLI)**, com persistência em arquivo e um **dashboard simples de acompanhamento de progresso**.

O projeto foi desenvolvido com foco em **boas práticas**, **organização de código**, **tratamento de exceções** e **pensamento de evolução de sistema**, simulando um cenário real de desenvolvimento backend.

---

## 🎯 Objetivo do Projeto

- Praticar Python em nível intermediário/avançado
- Consolidar conceitos fundamentais da linguagem
- Simular um sistema real, organizado e evolutivo
- Criar uma base sólida para portfólio e entrevistas técnicas

---

## 🧠 Conceitos Trabalhados

- Sintaxe avançada de Python
- Funções e escopo
- Listas, dicionários e conjuntos (set)
- Compreensão de listas
- Módulos e pacotes
- Virtualenv
- PEP8 (boas práticas)
- Tratamento de exceções
- Separação entre lógica, dados e visualização

---

## 🏗️ Estrutura do Projeto

```text
task_manager/
│
├── cli/
│   └── main.py          # Interface de linha de comando
│
├── core/
│   ├── tasks.py         # Regras de negócio das tarefas
│   ├── storage.py      # Persistência em arquivo JSON
│   └── metrics.py      # Cálculo de métricas e progresso
│
├── dashboard/
│   └── dashboard.py    # Visualização do progresso
│
├── data/
│   └── tasks.json      # Base de dados das tarefas
│
├── venv/               # Ambiente virtual
├── README.md
└── requirements.txt


---

## 🧩 Funcionalidades

### 📌 Gerenciamento de Tarefas (CLI)
O sistema permite:
- Criar tarefas  
- Listar tarefas  
- Atualizar tarefas  
- Remover tarefas  
- Filtrar tarefas por critérios específicos  

Cada tarefa possui os seguintes campos:
```json
{
    "id": int,
    "titulo": str,
    "descricao": str,
    "status": "pendente" | "em andamento" | "concluída",
    "prioridade": "baixa" | "media" | "alta",
    "tags": set[str]
}

