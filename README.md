# EPL Match Retrieval System (RAG Pipeline)

A Retrieval-Augmented Generation (RAG) system for searching and analyzing English Premier League match data from 2018-2025 seasons using semantic search powered by FAISS and sentence transformers.

## 🎯 Project Overview

This project implements a RAG pipeline that allows you to query historical EPL match data using natural language. It uses:
- **FAISS** for fast vector similarity search
- **Sentence Transformers** for semantic embeddings
- **Custom document retrieval** for relevant match information

## 📋 Features

- ✅ Semantic search across 7+ seasons of EPL data (2018-2025)
- ✅ Natural language queries (e.g., "Arsenal vs Tottenham", "Liverpool home games")
- ✅ Fast retrieval using FAISS indexing
- ✅ Detailed match statistics (scores, shots, fouls, cards, etc.)
- ✅ Multi-season search capabilities
- ✅ Comprehensive logging system

## 🗂️ Project Structure

```
rag_project/
├── data/
│   ├── raw/                          # Raw CSV files (epl_YYYY.csv)
│   ├── processed/
│   │   ├── epl_all_seasons.csv      # Concatenated data
│   │   └── epl_documents.txt        # Formatted match documents
│   └── embeddings/
│       ├── faiss_index.bin          # FAISS vector index
│       └── match_metadata.json      # Match text metadata
├── src/
│   ├── ingest/
│   │   ├── concat_seasons.py        # Combine season CSVs
│   │   └── build_docs.py            # Format match documents
│   ├── embeddings/
│   │   └── embed.py                 # Create FAISS embeddings
│   ├── retriever/
│   │   └── search.py                # Match retrieval logic
│   ├── rag/
│   │   └── pipeline.py              # Main RAG pipeline
│   └── utils/
│       ├── config.py                # Configuration
│       └── logger.py                # Logging setup
├── main.py                          # Entry point
├── requirements.txt                 # Python dependencies
└── README.md                        # This file
```

## 🚀 Installation

### Prerequisites
- Python 3.8+
- pip

### Setup

1. **Clone or download the project**
```bash
cd C:\Users\Asus\Desktop\rag_project
```

2. **Create virtual environment**
```bash
python -m venv .venv
```

3. **Activate virtual environment**
```bash
# Windows PowerShell
.venv\Scripts\Activate.ps1

# Windows CMD
.venv\Scripts\activate.bat

# Linux/Mac
source .venv/bin/activate
```

4. **Install dependencies**
```bash
pip install -r requirements.txt
```

## 📊 Data Preparation

### Step 1: Prepare Raw Data
Place your EPL season CSV files in `data/raw/`:
```
data/raw/
├── epl_1819.csv
├── epl_1920.csv
├── epl_2021.csv
├── epl_2122.csv
├── epl_2223.csv
├── epl_2324.csv
└── epl_2425.csv
```

### Step 2: Concatenate Seasons
```bash
python -m src.ingest.concat_seasons
```
This creates `data/processed/epl_all_seasons.csv`

### Step 3: Build Documents
```bash
python -m src.ingest.build_docs
```
This creates formatted match documents in `data/processed/epl_documents.txt`

### Step 4: Create Embeddings
```bash
python -m src.embeddings.embed
```
This generates:
- `data/embeddings/faiss_index.bin` (FAISS index)
- `data/embeddings/match_metadata.json` (match texts)

**Note:** First run will download the sentence-transformers model (~80MB) and cache it locally.

## 🎮 Usage

### Basic Usage

```bash
python main.py
```

Then enter your query when prompted:
```
Enter your query: Arsenal vs Tottenham
```

### Example Queries

**Team-specific:**
- `Liverpool matches in 2023 season`
- `Manchester United vs Chelsea`
- `Arsenal home games`
- `Tottenham away performance`

**Head-to-head:**
- `Liverpool vs Manchester City`
- `Arsenal vs Tottenham derbies`
- `Manchester United vs Liverpool`

**Statistical:**
- `High scoring matches`
- `Matches with many yellow cards`
- `Games with red cards`
- `Low scoring draws`

**Season-specific:**
- `2020-21 season matches`
- `Liverpool 2019 season`
- `Manchester City 2023-24 games`

### Sample Output

```
Enter your query: Arsenal vs Tottenham

2026-02-13 21:39:07,540 - INFO - Searching for: Arsenal vs Tottenham
2026-02-13 21:39:07,577 - INFO - Found 5 matches
2026-02-13 21:39:07,577 - INFO - Generating summary...

Summary:
Found 5 relevant matches:

1. 1498
   Match played on 12/05/22 in season-2122 season.
   Home team: Tottenham
   Away team: Arsenal
   Final score: Tottenham 3 - 0 Arsenal
   Full-time result: H
   Half-time score: 2 - 0

2. 2487
   Match played on 15/01/25 in season-2425 (1) season.
   Home team: Arsenal
   Away team: Tottenham
   Final score: Arsenal 2 - 1 Tottenham
   Full-time result: H
   Half-time score: 2 - 1
...
```

## ⚙️ Configuration

Edit `src/utils/config.py` to customize:

```python
# Paths
DATA_DIR = Path("data")
RAW_DIR = DATA_DIR / "raw"
PROCESSED_DIR = DATA_DIR / "processed"
EMBEDDINGS_DIR = DATA_DIR / "embeddings"

# Model settings
EMBEDDING_MODEL = "sentence-transformers/all-MiniLM-L6-v2"
TOP_K = 5  # Number of matches to retrieve

# Files
DOC_FILE = PROCESSED_DIR / "epl_documents.txt"
INDEX_FILE = EMBEDDINGS_DIR / "faiss_index.bin"
META_FILE = EMBEDDINGS_DIR / "match_metadata.json"
```

## 🔧 How It Works

### 1. Document Creation
Each match is formatted as a structured document:
```
Match played on 12/05/22 in season-2122 season.
Home team: Tottenham
Away team: Arsenal
Final score: Tottenham 3 - 0 Arsenal
...
Match statistics:
- Home shots: 15 (on target: 7)
- Away shots: 8 (on target: 3)
...
```

### 2. Embedding Generation
- Uses `sentence-transformers/all-MiniLM-L6-v2`
- Converts each document to a 384-dimensional vector
- Captures semantic meaning of the text

### 3. FAISS Indexing
- Stores vectors in a FAISS index for fast similarity search
- Uses L2 distance for finding nearest neighbors

### 4. Query Processing
- User query → Embedded to vector
- FAISS search → Find top-k most similar matches
- Results → Formatted and displayed

## 📦 Dependencies

```
faiss-cpu==1.9.0
sentence-transformers==3.3.1
pandas==2.2.3
numpy==1.26.4
transformers==4.47.1
torch==2.5.1
```

## 🐛 Troubleshooting

### Issue: "No CSV files found"
**Solution:** Ensure CSV files are in `data/raw/` directory

### Issue: "FAISS index not found"
**Solution:** Run the embedding step: `python -m src.embeddings.embed`

### Issue: Model download is slow
**Solution:** 
- First download takes time (models are cached for future use)
- Set HF_TOKEN for faster downloads from Hugging Face Hub

### Issue: Out of memory
**Solution:** Reduce batch size in embedding generation or use a smaller model

## 🎯 Performance

- **Index size:** ~2000+ matches indexed
- **Search time:** <100ms per query
- **Initialization:** ~3-5 seconds (after models are cached)
- **Embedding model:** 80MB (cached locally)

## 📈 Future Enhancements

- [ ] Add web interface (Streamlit/Gradio)
- [ ] Implement advanced filtering (date range, score range)
- [ ] Add visualization for match statistics
- [ ] Support for other leagues (La Liga, Serie A, etc.)
- [ ] API endpoint for programmatic access
- [ ] Add machine learning-based summarization
- [ ] Player-level statistics integration

## 📝 License

This project is for educational purposes.

## 🙏 Acknowledgments

- **FAISS**: Facebook AI Similarity Search
- **Sentence Transformers**: Hugging Face
- **EPL Data**: Historical match statistics

## 📧 Contact

For questions or suggestions, feel free to open an issue or contribute to the project.

---

**Built with ❤️ for EPL fans and data enthusiasts**