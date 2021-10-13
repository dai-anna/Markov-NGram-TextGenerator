# TextGenerator
NLP project to use N-Grams and Markov Chains to generate text on a per-word basis. Implements Stupid Backoff.

## In Action
If we use the same NTLK corpus as in our test case
```
corpus = nltk.corpus.gutenberg.raw('austen-sense.txt')
corpus = nltk.word_tokenize(corpus.lower())
```

... and called the function as so
```
finish_sentence(["she", "was", "not", "in"], 4, corpus, deterministic=True)
```

... we can observe how the function works (with a few additional print statements)

![Screen Shot 2021-10-13 at 1 44 42 AM](https://user-images.githubusercontent.com/89488845/137074693-a1541d89-1e2c-4ec6-8004-2b1309735b23.png)

... in order to generate the following sentence.
```
['she', 'was', 'not', 'in', 'the', 'habit', 'of', 'seeing', 'much', 'occupation', 'at', 'home', ',', 'and', 'you']
```
