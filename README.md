## Instructions

1. Run 
```bash 
pip install -r requirements
```

2. Create your knowledge base
```bash 
python knowledge_base.py
```

3. Create your retrieval system
To run the llm in your local install Ollama (https://ollama.com/)
Otherwise get an OpenAI key an put it in your env as OPENAI_API_KEY
```bash 
python retrieval_system.py
```

4. Test your RAG System
```bash 
python index.py
```
