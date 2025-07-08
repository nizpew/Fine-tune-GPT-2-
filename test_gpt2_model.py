from transformers import GPT2LMHeadModel, GPT2Tokenizer, pipeline

# Carregar o modelo fine-tunado
model = GPT2LMHeadModel.from_pretrained("./gpt2-tasker")
tokenizer = GPT2Tokenizer.from_pretrained("./gpt2-tasker")

# Criar pipeline de geração
generator = pipeline("text-generation", model=model, tokenizer=tokenizer)

# Prompt de teste
prompt = "User: create a task to buy groceries\nAssistant:\n"

# Gerar a resposta
output = generator(
    prompt,
    max_new_tokens=50,
    temperature=0.7,
    top_p=0.9,
    do_sample=True
)

print(output[0]["generated_text"])

