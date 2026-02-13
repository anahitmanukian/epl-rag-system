### main.py
from src.rag.pipeline import RAGPipeline

def main():
    # Change in main.py or pipeline.py
    rag = RAGPipeline()  # Much smaller
    query = input("Enter your query: ")
    result = rag.query(query, top_k=10)
    print("\nSummary:\n", result)

if __name__ == "__main__":
    main()


