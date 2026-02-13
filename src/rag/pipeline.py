# src/rag/pipeline.py
from src.retriever.search import MatchRetriever
from src.utils import logger

log = logger.get_logger("RAG_Pipeline")

class RAGPipeline:
    def __init__(self):
        log.info("Initializing RAG pipeline...")
        self.retriever = MatchRetriever()
        log.info("RAG pipeline ready!")

    def query(self, text_query: str, top_k: int = 5):
        log.info(f"Searching for: {text_query}")
        matches = self.retriever.search(text_query, top_k=top_k)
        
        log.info("Generating summary...")
        summary = self._create_summary(matches)
        
        # Add this if you want summary in logs:
        log.info(f"Summary generated:\n{summary}")
        
        return summary
        
    # def _create_summary(self, matches):
    #     summary_parts = [f"Found {len(matches)} relevant matches:\n"]
        
    #     for i, match in enumerate(matches, 1):
    #         lines = match.split('\n')
    #         summary_parts.append(f"\n{i}. {lines[0] if lines else 'Match'}")
    #         # Show more lines (first 10 instead of 6)
    #         for line in lines[1:10]:
    #             if line.strip():
    #                 summary_parts.append(f"   {line.strip()}")
        
    #     return '\n'.join(summary_parts)
    
    def _create_summary(self, matches):
    # Create a detailed summary with key statistics
        if not matches:
            return "No matches found."
        
        summary_parts = [f"Found {len(matches)} relevant matches:\n"]
        
        for i, match in enumerate(matches, 1):
            lines = match.split('\n')
            
            # Extract key info
            match_info = {}
            for line in lines:
                line = line.strip()
                if line.startswith('Match played on'):
                    match_info['date'] = line
                elif line.startswith('Home team:'):
                    match_info['home'] = line.split(':')[1].strip()
                elif line.startswith('Away team:'):
                    match_info['away'] = line.split(':')[1].strip()
                elif line.startswith('Final score:'):
                    match_info['score'] = line.split(':')[1].strip()
                elif 'Home shots:' in line:
                    match_info['shots'] = line
                elif 'Yellow cards:' in line:
                    match_info['yellow'] = line
                elif 'Red cards:' in line:
                    match_info['red'] = line
                elif 'Fouls:' in line:
                    match_info['fouls'] = line
                elif 'Corners:' in line:
                    match_info['corners'] = line
            
            # Format output
            summary_parts.append(f"\n{'='*60}")
            summary_parts.append(f"MATCH {i}:")
            summary_parts.append('='*60)
            summary_parts.append(match_info.get('date', ''))
            summary_parts.append(f"{match_info.get('home', 'N/A')} vs {match_info.get('away', 'N/A')}")
            summary_parts.append(f"Score: {match_info.get('score', 'N/A')}")
            summary_parts.append("")
            summary_parts.append("Statistics:")
            summary_parts.append(f"  {match_info.get('shots', 'Shots: N/A')}")
            summary_parts.append(f"  {match_info.get('fouls', 'Fouls: N/A')}")
            summary_parts.append(f"  {match_info.get('corners', 'Corners: N/A')}")
            summary_parts.append(f"  {match_info.get('yellow', 'Yellow cards: N/A')}")
            summary_parts.append(f"  {match_info.get('red', 'Red cards: N/A')}")
        
        return '\n'.join(summary_parts)