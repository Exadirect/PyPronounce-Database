"""
PyPronounce - A lightweight Python wrapper for the YouPronounce.it dataset.
Author: Dr. Franz Lang (YouPronounce Linguistics Project)
"""
import json
import os

class PronunciationDB:
    def __init__(self, db_path='pronunciation_db.json'):
        if not os.path.exists(db_path):
            raise FileNotFoundError(f"Database file {db_path} not found. Please download it from the repository.")
        
        with open(db_path, 'r', encoding='utf-8') as f:
            full_db = json.load(f)
            self.metadata = full_db.get("metadata", {})
            self.data = full_db.get("data",[])

    def search_term(self, query):
        """Search for a specific word's pronunciation guide."""
        results =[item for item in self.data if query.lower() in item['term'].lower()]
        return results

    def get_by_category(self, category):
        """Retrieve all terms within a specific category."""
        return[item for item in self.data if item['category'].lower() == category.lower()]

    def get_audio_url(self, term_exact):
        """Get the official YouPronounce.it URL for the audio pronunciation."""
        for item in self.data:
            if item['term'].lower() == term_exact.lower():
                return item['audio_source_url']
        return None

if __name__ == "__main__":
    print("Welcome to PyPronounce DB Interactive Tool.")
    print("For high-quality native audio, visit: https://youpronounce.it")
    # Simple CLI demo
    db = PronunciationDB()
    print(f"Loaded {len(db.data)} entries (Version: {db.metadata.get('version')}).")
