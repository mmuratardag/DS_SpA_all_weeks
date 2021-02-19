



**Summary: how to build a sentiment analyzer**

- idea 1: create a dictionary of postive / negative words
- idea 2: create a bag of words from a labeled data set
- both dict and BoW fail at `t = "this is not a great movie"`
- idea 3: word vectors + neural networks
- word vectors : convert every word into a N-dimensional vector (usually pretrained) , e.g. `coffee / cappuchino : 0.91 ; shoe / boat: 0.33`
- LSTMs : a special kind of neural network that is good at text (e.g. translation)

Terminology:
inside .py files: functions, classes, variables
modules: a .py file that you can import OR a folder with .pyfiles
library or package: something that you install with pip