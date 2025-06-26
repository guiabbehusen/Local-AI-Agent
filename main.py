from langchain_ollama.llms import OllamaLLM
from langchain_core.prompts import ChatPromptTemplate
from vector import retriever
model = OllamaLLM(model="llama3.2")

template = """
You are an expert in answering wuestions about a pizza restaurante

Here are some reviews: {reviews}

Here is the question to anser: {question}
"""
prompt = ChatPromptTemplate.from_template(template)

chain = prompt | model
while True:
    print("-----------------")
    question = input("question:")
    if question == "q":
        break
    reviews = retriever.invoke(question)
    result = chain.invoke({"reviews": reviews, "question": "hat is the best pizza in the town?"})

    print(result)