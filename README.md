# TextGenerator
NLP project to use N-Grams and Markov Chains to generate text on a per-word basis. Implements Stupid Backoff, where if no n-gram of a given size is found, it will recurse to the (n-1)-gram until we reach a unigram. 

## Visualize how it works
If we use the same NTLK corpus as in our test case
```
corpus = nltk.corpus.gutenberg.raw('austen-sense.txt')
corpus = nltk.word_tokenize(corpus.lower())
```

... and called the function as so (because stocastic word generation is more fun 😉 )
```
finish_sentence(["she", "was", "not", "in"], 4, corpus, deterministic=False)
```

... we can observe how the function works (with a few additional print statements)

![Screen Shot 2021-10-13 at 12 04 00 PM](https://user-images.githubusercontent.com/89488845/137171277-f30845c4-fa84-4206-9659-420957235829.png)

... in order to generate the following sentence, detokenized by to our trusty `TreebankWordDetokenizer` function from the `nltk.tokenize.treebank` package ❤️
```
she was not in the neighbourhood to which you will not allow me to prove
```

## Stupid Backoff implementation
If we called the function with a word that does not exist in the corpus and/or with n-gram that is too long
```
finish_sentence(["ThisWordDoesNotExist", "unlike"], 4, corpus, deterministic=False)
```

... we can observe how the Backoff works

![Screen Shot 2021-10-13 at 12 33 57 PM](https://user-images.githubusercontent.com/89488845/137176264-f4238906-2e4f-49ed-a1ec-4a9b5d9cf5a3.png)

... in order to generate a sentence regardless

```
ThisWordDoesNotExist unlike yourself must be happy.
```


**Now, try it out yourself!**
