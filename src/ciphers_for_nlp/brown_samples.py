import string
import textwrap

import hmmlearn.hmm
import numpy as np
from nltk.corpus import brown

from ciphers_for_nlp import vigenere


def samples():
    for sent in brown.sents():
        yield "".join(c for c in "".join(sent).lower() if c in string.ascii_lowercase)


def samples_for_hmmlearn():
    """
    format text for HMM.
    :return:
    """
    xs = []
    lengths = []
    for sent in samples():
        Xs.append([string.ascii_lowercase.index(c) for c in sent])
        lengths.append(len(xs[-1]))
    return np.concatenate(xs).reshape(-1,1).astype(int),np.array(lengths)


if __name__ == "__main__":
   X,lengths = samples_for_hmmlearn()
   model = hmmlearn.hmm.CategoricalHMM(n_components=2)
   model.fit(X,lengths)
   print(model)
