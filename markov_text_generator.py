import random as rm


def next_word(sentence:list[str], ngram:int, corpus:list[str], deterministic=False):
    """generates next word according to Markov/N-Gram model"""
    search_key = sentence[-(ngram-1):]
    matched = {}
    for idx in range(len(corpus)-ngram+1):
        if search_key == corpus[idx:idx+ngram-1]:
            new_match = corpus[idx+ngram-1]
            if new_match in matched.keys():
                matched[new_match] += 1
            else:
                matched[new_match] = 1
    if len(matched) == 0:
        return next_word(sentence, ngram-1, corpus, deterministic)
    if deterministic == True:
        the_chosen_one = max(matched, key=matched.get)
    else:
        the_chosen_one = rm.choices(
            list(matched.keys()), weights=list(matched.values()))[0]
    return the_chosen_one


def finish_sentence(sentence:list[str], n:int, corpus:list[str], deterministic=False):
    """completes the sentence by leveraging the next_word function"""
    final_sentence = sentence
    while final_sentence[-1] not in {".", "?", "!"} and len(final_sentence) < 15:
        final_sentence.append(next_word(sentence, n, corpus, deterministic))
    return final_sentence
