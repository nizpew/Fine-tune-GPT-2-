# Fine-tune-GPT-2-
This project showcases a hands-on implementation of fine-tuning GPT-2 for a natural language task management assistant. Given a user prompt (e.g., "remind me to call the doctor"), the model returns a structured response such as:


# 🧠 Smart Task Generator (Fine-Tuned GPT-2 Model)

A fine-tuned version of the GPT-2 language model designed to understand natural language prompts and generate structured task descriptions — complete with task names and appropriate execution times — ideal for productivity tools, virtual assistants, and smart reminders.




## using
```
#install if first time
python3 -m venv ai-backend-env
pip install flask transformers torch
source ai-backend-env/bin/activate



#if not just 
source ai-backend-env/bin/activate

curl -X POST http://localhost:5000/generate \
     -H "Content-Type: application/json" \
     -d '{"prompt": "Create a task for me to go to the dentist"}'

#"response": "Dentist appointment task added.\n[TASK: Dentist appointment | TIME: 10:00]"
```



---

## 📌 Project Description

This project showcases a hands-on implementation of **fine-tuning GPT-2** for a **natural language task management assistant**. Given a user prompt (e.g., *"remind me to call the doctor"*), the model returns a structured response such as:

```
Assistant:
Reminder set to call the doctor.
[TASK: Call doctor | TIME: 10:30]
```

Unlike traditional text generation, this model was trained to output **structured responses with actionable elements**, including contextual task timing — simulating realistic daily routines.

---

## ✅ Key Features

* 💬 Understands natural language task commands
* 📋 Generates structured tasks with `[TASK: ... | TIME: ...]` format
* ⏰ Learns appropriate timing (e.g., workouts in the morning, meetings in the afternoon)
* 🤖 Fully fine-tuned on **custom curated dataset**
* 🧪 Ready-to-use with `transformers` pipeline for inference

---

## 📂 Dataset

The dataset contains over 50 custom instructions paired with assistant responses, carefully crafted to reflect real-world usage:

```json
{
  "text": "User: remind me to water the plants\nAssistant:\nReminder set to water the plants.\n[TASK: Water plants | TIME: 09:00]"
}
```

Each sample simulates user-assistant interaction in a productivity assistant context, combining **NLP understanding** with **schedule reasoning**.

---

## 🛠️ Tech Stack

* Python 3.x
* 🤗 Transformers (`GPT2LMHeadModel`)
* HuggingFace Datasets
* PyTorch
* Google Colab + CUDA acceleration

---

## 🚀 How It Works

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

## 🧠 Value Proposition

This project demonstrates the ability to **customize LLMs for real-world tasks**, transforming general-purpose language models into **domain-specific assistants**. Ideal for:

* Smart calendar or productivity tools
* Virtual assistant backends
* Conversational UI systems
* User-centric time management apps

---

## 📈 Results

The fine-tuned model consistently generates well-structured tasks. While timing predictions can still improve, the model:

* Understands user intent
* Produces clear and clean outputs
* Generates meaningful time allocations with task descriptions

---

## 📥 Installation & Inference

```python
from transformers import pipeline

generator = pipeline("text-generation", model="./gpt2-tasker", tokenizer="./gpt2-tasker")

prompt = "User: remind me to call the doctor\nAssistant:\n"
output = generator(prompt, max_length=100, do_sample=True)
print(output[0]["generated_text"])
```

---

## 🙋 About Me

This project is part of my practical exploration into **LLM fine-tuning and prompt engineering**. It reflects my skills in:

* Model customization
* Data curation
* LLM integration in product use cases

If you're looking for someone who blends **deep learning proficiency** with **product vision**, feel free to reach out!

