### src.retriever.search.py

import faiss
import json
import numpy as np
from sentence_transformers import SentenceTransformer
from src.utils import config, logger

log = logger.get_logger("Retriever")

class MatchRetriever:
    def __init__(self):
        log.info("Loading FAISS index...")
        self.index = faiss.read_index(str(config.INDEX_FILE))

        log.info("Loading match metadata...")
        with open(config.META_FILE, "r", encoding="utf-8") as f:
            self.matches = json.load(f)

        log.info(f"Loading embedding model: {config.EMBEDDING_MODEL}")
        self.model = SentenceTransformer(config.EMBEDDING_MODEL)

    def search(self, query: str, top_k: int = None):
        top_k = top_k or config.TOP_K
        log.info(f"Searching top {top_k} matches for query: '{query}'")
        vec = self.model.encode([query]).astype("float32")
        distances, indices = self.index.search(vec, k=top_k)
        results = [self.matches[i] for i in indices[0]]
        log.info(f"Found {len(results)} matches")
        return results
