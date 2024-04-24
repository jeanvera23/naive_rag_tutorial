## Instructions

1. Run 
    ```bash 
    pip install -r requirements
    ```

2. Create your knowledge base

    ```bash 
    python knowledge_base.py
    ```
    Check LangChain documentation for more details (https://python.langchain.com/docs/get_started/introduction/)

3. Create your retrieval system
    To run the llm in your local install Ollama (https://ollama.com/)
    Otherwise get an OpenAI key an put it in your environment variables. Rename ``.env.example`` as ``.env`` and update them with yours.
    ```bash 
    python retrieval_system.py
    ```

4. Test your RAG System
    ```bash 
    python index.py
    ```
