
# AI Engineering and LLMOps

This module provides an AI-powered infrastructure incident assistant.

## Components

- Ollama: Local LLM inference.
- LangChain: Future orchestration and agent workflows.
- Sentence Transformers: Text embeddings.
- Qdrant: Vector database.
- RAG: Retrieval-augmented generation.
- AI Evaluation: Response quality checks.

## RAG workflow

1. Load operational documents.
2. Generate text embeddings.
3. Store embeddings in Qdrant.
4. Retrieve relevant documents.
5. Build an incident analysis prompt.
6. Generate an AI response.
7. Evaluate the response.

## Setup

Install dependencies:

```bash
pip install -e ".[ai]"
```

Start Ollama and pull a model:

```bash
ollama pull llama3.2
ollama serve
```

Index documents:

```bash
python ai/rag/ingest.py
```

The initial implementation uses a simple local RAG pipeline. Authentication, tenant isolation, retrieval evaluation, and production prompt safeguards will be added before production deployment.
