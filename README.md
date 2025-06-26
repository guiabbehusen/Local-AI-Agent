# Local AI Agent com RAG para Reviews de Restaurante

Este projeto demonstra como criar um agente de IA local utilizando RAG (Retrieval-Augmented Generation) para responder perguntas com base em avaliações reais de um restaurante. O modelo é executado localmente com a biblioteca Langchain e o Ollama, sem necessidade de chamadas externas à API.

## Tecnologias utilizadas

- Python  
- Langchain  
- Ollama  
- ChromaDB  
- Pandas  

## Funcionalidades

- Geração de respostas utilizando RAG  
- Embeddings locais com `mxbai-embed-large`  
- Vetorização de avaliações reais de restaurante  
- Recuperação de documentos mais relevantes via Chroma  
- Execução local com modelos LLM (ex: `llama3.2`)  
