#!/usr/bin/env python
# coding: utf-8

# In[32]:


import nltk
import random2 as random
from nltk.tokenize import word_tokenize
from nltk.tag import pos_tag
from nltk.corpus import wordnet as wn


# In[33]:


def tag(sentence):
 words = word_tokenize(sentence)
 words = pos_tag(words)
 return words

def paraphraseable(tag):
 return tag.startswith('NN') or tag == 'VB' or tag.startswith('JJ')

def pos(tag):
 if tag.startswith('NN'):
  return wn.NOUN
 elif tag.startswith('V'):
  return wn.VERB
 elif tag.startswith('RB'):
  return wn.ADVERB


# In[34]:


def synonyms(word, tag):
    lemma_lists = [ss.lemmas() for ss in wn.synsets(word, pos(tag))]
    lemmas = [lemma.name() for lemma in sum(lemma_lists, [])]
    return set(lemmas)


# In[67]:


def synonymIfExists(sentence):
 for (word, t) in tag(sentence):
   if paraphraseable(t):
    syns = synonyms(word, t)
    if syns:
     if len(syns) > 1:
      List1 = list(syns)
      yield random.choice(List1)
      continue
   yield word


# In[68]:


#def paraphrase(sentence):
 #[x for x in synonymIfExists(sentence)]
# final = ' '.join([str(x) for x in synonymIfExists(sentence)])
# return final

# In[69]:
