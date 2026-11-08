
from qdrant_client import QdrantClient
from sentence_transformers import SentenceTransformer

COLLECTION = "operations_knowledge"


class KnowledgeRetriever:

    def __init__(
        self,
        qdrant_url: str = "http://localhost:6333",
    ):
        self.client = QdrantClient(url=qdrant_url)

        self.encoder = SentenceTransformer(
            "sentence-transformers/all-MiniLM-L6-v2"
        )

    def search(
        self,
        question: str,
        limit: int = 5,
    ) -> list[dict]:

        embedding = self.encoder.encode(question).tolist()

        results = self.client.query_points(
            collection_name=COLLECTION,
            query=embedding,
            limit=limit,
        ).points

        return [
            {
                "content": result.payload.get("content", ""),
                "source": result.payload.get("source", ""),
                "score": result.score,
            }
            for result in results
        ]
