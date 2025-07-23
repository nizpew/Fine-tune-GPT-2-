
## 🇧🇷 Fine-tune-GPT-2 (Versão em Português)

> *Este projeto utiliza **Flask** — um framework web leve em Python, comum para APIs e microsserviços — para criar sua própria API local, realizando chamadas e retornando as respostas do modelo treinado localmente com base no prompt fornecido.*

<details>
<summary><strong>Clique para expandir a versão em português</strong></summary>

---

### 🧠 Gerador Inteligente de Tarefas (Modelo GPT-2 Ajustado)

Uma versão ajustada do modelo de linguagem GPT-2, projetada para compreender comandos em linguagem natural e gerar descrições estruturadas de tarefas — com nomes de tarefas e horários apropriados — ideal para ferramentas de produtividade, assistentes virtuais e lembretes inteligentes.

---

### 🛠️ Como usar

```bash
# Instale se for a primeira vez
python3 -m venv ai-backend-env
pip install flask transformers torch
source ai-backend-env/bin/activate

# Caso já tenha instalado anteriormente, apenas ative:
source ai-backend-env/bin/activate

# Faça uma chamada para a API local:
curl -X POST http://localhost:5000/generate \
     -H "Content-Type: application/json" \
     -d '{"prompt": "Crie uma tarefa para ir ao dentista"}'
```

Resposta esperada:

```json
"response": "Tarefa de consulta no dentista adicionada.\n[TASK: Consulta no dentista | TIME: 10:00]"
```

---

### 📌 Descrição do Projeto

Este projeto apresenta uma implementação prática de ajuste fino do GPT-2 para um assistente de gerenciamento de tarefas em linguagem natural. Dado um prompt do usuário (ex.: *"me lembre de ligar para o médico"*), o modelo retorna uma resposta estruturada como:

```
Assistente:
Lembrete criado para ligar para o médico.
[TASK: Ligar para o médico | TIME: 10:30]
```

---

### ✅ Funcionalidades Principais

* 💬 Entende comandos em linguagem natural
* 📋 Gera tarefas estruturadas no formato `[TASK: ... | TIME: ...]`
* ⏰ Aprende alocar horários coerentes com o contexto
* 🤖 Modelo ajustado com dataset customizado
* 🧪 Pronto para uso com `transformers.pipeline`

---

### 📂 Conjunto de Dados

```json
{
  "text": "Usuário: me lembre de regar as plantas\nAssistente:\nLembrete criado para regar as plantas.\n[TASK: Regar plantas | TIME: 09:00]"
}
```

---

### 🛠️ Tecnologias Utilizadas

* Python 3.x
* 🤗 Transformers (`GPT2LMHeadModel`)
* Hugging Face Datasets
* PyTorch
* Google Colab + aceleração com CUDA

---

### 🚀 Como Funciona

1. Carrega e tokeniza o dataset customizado
2. Ajusta o GPT-2 com o `Trainer` da Hugging Face
3. Exporta e usa localmente ou em uma pipeline
4. Entrada: `"Usuário: terminar o relatório"`
5. Saída:

```
Assistente:
Tarefa de relatório adicionada.
[TASK: Terminar relatório | TIME: 16:00]
```

---

### 🧠 Proposta de Valor

Demonstra a capacidade de personalizar LLMs para tarefas reais, transformando modelos genéricos em assistentes de domínio específico. Ideal para:

* Ferramentas de produtividade/calendário inteligente
* Backends de assistentes virtuais
* Interfaces conversacionais
* Aplicativos de gerenciamento de tempo

---

### 📈 Resultados

* Compreende intenções do usuário
* Gera saídas claras e bem estruturadas
* Sugere horários realistas com base no tipo de tarefa

---

### 📥 Inferência Local

```python
from transformers import pipeline

generator = pipeline("text-generation", model="./gpt2-tasker", tokenizer="./gpt2-tasker")

prompt = "Usuário: me lembre de ligar para o médico\nAssistente:\n"
output = generator(prompt, max_length=100, do_sample=True)
print(output[0]["generated_text"])
```

---

### 🙋 Sobre Mim

Este projeto faz parte da minha exploração prática em:

* Customização de modelos LLM
* Engenharia de prompts
* Curadoria de dados para tarefas reais

Se procura alguém que una **proeficiência em deep learning** com **visão de produto**, entre em contato!

</details>

---

## 🇺🇸 Fine-tune-GPT-2 (English Version)

> *This project uses **Flask** — a lightweight Python web framework, commonly used for APIs & microservices — to create a local API that makes calls and retrieves responses from a locally trained model based on the provided prompt.*

<details>
<summary><strong>Click to expand the English version</strong></summary>

---

### 🧠 Smart Task Generator (Fine-Tuned GPT-2 Model)

A fine-tuned version of the GPT-2 language model designed to understand natural language prompts and generate structured task descriptions — complete with task names and appropriate execution times — ideal for productivity tools, virtual assistants, and smart reminders.

---

### 🛠️ Using

```bash
# Install if first time
python3 -m venv ai-backend-env
pip install flask transformers torch
source ai-backend-env/bin/activate

# If not, just activate:
source ai-backend-env/bin/activate

# Call local API
curl -X POST http://localhost:5000/generate \
     -H "Content-Type: application/json" \
     -d '{"prompt": "Create a task for me to go to the dentist"}'
```

Expected response:

```json
"response": "Dentist appointment task added.\n[TASK: Dentist appointment | TIME: 10:00]"
```

---

### 📌 Project Description

This project showcases a hands-on implementation of **fine-tuning GPT-2** for a **natural language task management assistant**. Given a user prompt (e.g., *"remind me to call the doctor"*), the model returns a structured response such as:

```
Assistant:
Reminder set to call the doctor.
[TASK: Call doctor | TIME: 10:30]
```

---

### ✅ Key Features

* 💬 Understands natural language task commands
* 📋 Generates structured tasks with `[TASK: ... | TIME: ...]` format
* ⏰ Learns appropriate timing (e.g., workouts in the morning, meetings in the afternoon)
* 🤖 Fully fine-tuned on **custom curated dataset**
* 🧪 Ready-to-use with `transformers` pipeline for inference

---

### 📂 Dataset

```json
{
  "text": "User: remind me to water the plants\nAssistant:\nReminder set to water the plants.\n[TASK: Water plants | TIME: 09:00]"
}
```

---

### 🛠️ Tech Stack

* Python 3.x
* 🤗 Transformers (`GPT2LMHeadModel`)
* HuggingFace Datasets
* PyTorch
* Google Colab + CUDA acceleration

---

### 🚀 How It Works

1. Load and tokenize the custom dataset
2. Fine-tune GPT-2 using `Trainer` from Hugging Face
3. Export and use the model locally or in a pipeline
4. Input: `"User: create a task to finish the report"`
5. Output:

```
Assistant:
Report task added.
[TASK: Finish report | TIME: 16:00]
```

---

### 🧠 Value Proposition

This project demonstrates the ability to **customize LLMs for real-world tasks**, transforming general-purpose language models into **domain-specific assistants**. Ideal for:

* Smart calendar or productivity tools
* Virtual assistant backends
* Conversational UI systems
* User-centric time management apps

---

### 📈 Results

* Understands user intent
* Produces clear and clean outputs
* Generates meaningful time allocations with task descriptions

---

### 📥 Installation & Inference

```python
from transformers import pipeline

generator = pipeline("text-generation", model="./gpt2-tasker", tokenizer="./gpt2-tasker")

prompt = "User: remind me to call the doctor\nAssistant:\n"
output = generator(prompt, max_length=100, do_sample=True)
print(output[0]["generated_text"])
```

---

### 🙋 About Me

This project is part of my practical exploration into:

* LLM fine-tuning
* Prompt engineering
* Data curation for real-world NLP applications

If you're looking for someone who blends **deep learning proficiency** with **product vision**, feel free to reach out!

</details>

