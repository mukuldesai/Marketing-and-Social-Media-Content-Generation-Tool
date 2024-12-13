import pytest
from content_app.utils.chroma_utils import load_documents, split_text

def test_load_documents():
    documents = load_documents()
    assert len(documents) > 0, "No documents found"

def test_split_text():
    documents = load_documents()
    chunks = split_text(documents)
    assert len(chunks) > 0, "No chunks generated from documents"
