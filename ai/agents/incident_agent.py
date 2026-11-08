
from pathlib import Path

from ai.llm.client import LLMClient
from ai.rag.retrieve import KnowledgeRetriever


class IncidentAssistant:

    def __init__(self):
        self.llm = LLMClient()
        self.retriever = KnowledgeRetriever()

        self.prompt_template = Path(
            "ai/prompts/incident_analysis.txt"
        ).read_text(encoding="utf-8")

    async def analyze(self, incident: str) -> dict:

        documents = self.retriever.search(incident)

        context = "\n\n".join(
            item["content"]
            for item in documents
        )

        prompt = self.prompt_template.format(
            incident=incident,
            context=context or "No relevant documents found.",
        )

        response = await self.llm.generate(prompt)

        return {
            "incident": incident,
            "analysis": response,
            "sources": [
                item["source"]
                for item in documents
            ],
        }
