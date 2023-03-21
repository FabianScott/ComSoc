import pandas as pd
paper_abstracts = pd.read_csv("paper_abstract_dataset_with_tokens.csv")
#%%
from nltk import *
bigrams_list = [list(bigrams(row)) for row in paper_abstracts["Tokens"]]
#%%
import numpy as np
import scipy
import pickle
p_values = []
for i, bigrams in enumerate(bigrams_list):
    len_bigrams = len(bigrams)
    bigrams1 = np.array([bg[0] for bg in bigrams])
    bigrams2 = np.array([bg[1] for bg in bigrams])
    for bigram in bigrams:
        first_value_true = bigram[0] == bigrams1
        second_value_true = bigram[1] == bigrams2
        contingency_table = np.empty((2,2))
        contingency_table[0,0] = np.sum(np.logical_and(first_value_true, second_value_true))
        contingency_table[1,0] = np.sum(np.logical_and(first_value_true, np.logical_not(second_value_true)))
        contingency_table[0,1] = np.sum(np.logical_and(np.logical_not(first_value_true), second_value_true))
        contingency_table[1,1] = np.sum(np.logical_and(np.logical_not(first_value_true), np.logical_not(second_value_true)))
        p_value = scipy.stats.chi2_contingency(contingency_table)
        p_values.append([i, bigram, p_value[1], len_bigrams])
    if i % 10000 == 0:
        print(i)
        with open('p_values.pickle', 'wb') as handle:
            pickle.dump(p_value, handle, protocol=pickle.HIGHEST_PROTOCOL)
#%%
with open('p_values.pickle', 'wb') as handle:
    pickle.dump(p_value, handle, protocol=pickle.HIGHEST_PROTOCOL)