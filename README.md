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

![Screen Shot 2021-10-13 at 1 37 10 AM](https://user-images.githubusercontent.com/89488845/137074189-22dfd8b5-0de0-4a3b-a0e0-55cf2fa807e3.png)

... in order to generate the following sentence.
```
['she', 'was', 'not', 'in', 'the', 'habit', 'of', 'seeing', 'much', 'occupation', 'at', 'home', ',', 'and', 'you']
```
