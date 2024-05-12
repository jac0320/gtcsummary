import os

OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")

GTCSUMMARY_SEARCH_API_KEY = os.getenv("GTCSUMMARY_SEARCH_API_KEY")
GTCSUMMARY_SEARCH_ENGINE_ID = os.getenv("GTCSUMMARY_SEARCH_ENGINE_ID")

KEYNOTE_PERSIST_DIR = ".keynote_storage"
PERSONAL_NOTE_PERSIST_DIR = ".personal_notes_storage"
NOTES_PERSIST_DIR = ".notes_storage"
NOTES_DAT_DIR = "summarized_notes"
