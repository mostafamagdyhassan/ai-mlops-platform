
import argparse
from pathlib import Path
import uuid

from qdrant_client import QdrantClient, models
from sentence_transformers import SentenceTransformer


COLLECTION = "operations_knowledge"


def ingest_documents(
    documents_dir: str,
    qdrant_url: str,
):
    encoder = SentenceTransformer(
        "sentence-transformers/all-MiniLM-L6-v2"
    )

    client = QdrantClient(url=qdrant_url)

    dimension = encoder.get_sentence_embedding_dimension()

    client.create_collection(
        collection_name=COLLECTION,
        vectors_config=models.VectorParams(
            size=dimension,
            distance=models.Distance.COSINE,
        ),
        timeout=30,
    ) if not client.collection_exists(COLLECTION) else None

    points = []

    for path in Path(documents_dir).rglob("*.txt"):
        content = path.read_text(encoding="utf-8")

        chunks = [
            content[index:index + 800]
            for index in range(0, len(content), 650)
        ]

        embeddings = encoder.encode(chunks)

        for chunk, embedding in zip(chunks, embeddings):
            points.append(
                models.PointStruct(
                    id=str(uuid.uuid4()),
                    vector=embedding.tolist(),
                    payload={
                        "source": path.name,
                        "content": chunk,
                    },
                )
            )

    if points:
        client.upsert(
            collection_name=COLLECTION,
            points=points,
        )

    print(f"Indexed {len(points)} document chunks.")


if __name__ == "__main__":
    parser = argparse.ArgumentParser()

    parser.add_argument(
        "--documents",
        default="ai/knowledge",
    )
    parser.add_argument(
        "--qdrant-url",
        default="http://localhost:6333",
    )

    args = parser.parse_args()

    ingest_documents(
        args.documents,
        args.qdrant_url,
    )
