import nltk
from markov_text_generator import finish_sentence


def test_generator():
    """Test Markov text generator."""
    corpus = nltk.corpus.gutenberg.raw("austen-sense.txt")
    corpus = nltk.word_tokenize(corpus.lower())

    words = finish_sentence(["she", "was", "not"], 3, corpus, deterministic=True,)
    assert words == ["she", "was", "not", "in", "the", "world", "."]

