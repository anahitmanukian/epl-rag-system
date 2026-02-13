from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent.parent

# Data paths
DATA_DIR = BASE_DIR / "data"
RAW_DIR = DATA_DIR / "raw"
PROCESSED_DIR = DATA_DIR / "processed"

DOC_FILE = PROCESSED_DIR / "epl_documents.txt"
FULL_CSV = PROCESSED_DIR / "epl_all_seasons.csv"

# Embeddings paths
EMBEDDINGS_DIR = BASE_DIR / "embeddings"
INDEX_FILE = EMBEDDINGS_DIR / "football.index.faiss"
META_FILE = EMBEDDINGS_DIR / "metadata.json"

# Models
EMBEDDING_MODEL = "sentence-transformers/all-MiniLM-L6-v2"

# Top-K for retrieval
TOP_K = 5
