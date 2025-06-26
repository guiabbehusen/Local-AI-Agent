from langchain_ollama.llms import OllamaLLM
from langchain_core.prompts import ChatPromptTemplate

model = OllamaLLM(model="llama3.2")

template = """
You are an expert in answering wuestions about a pizza restaurante

Here are some reviews: {reviews}

Here is the question to anser: {question}
"""
prompt = ChatPromptTemplate.from_template(template)

chain = prompt | model
while True:
    print("-")*60
    question = input("question:")
    if question == "q":
        break
    result = chain.invoke({"reviews": [], "question": "hat is the best pizza in the town?"})

    print(result)