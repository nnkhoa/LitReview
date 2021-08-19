# Leap2Treand: A Temporal Word Embedding Approach for Instant Detection of Emerging Scientific Trends
# Amna Dridi, Mohamed Medhat Gaber, R. Muhammad Atif Azad, Jagdev Bhogal, 2019

## Quick Sumnmary

Unlike previous attempts to detect emerging trends in research papers through biblography which are known to have problem in timeliness and content analysis, the literature proposed an approach using temporal word embeddings, dubbed as Leap2Trend. Leap2Trend tracks similarities between pairs of keywords overtime which yielded results suggesting the robustness and timeliness characteristics of the method.

## Problem Addressed/Main Contribution

* Citation counting has many limitations: massive delay in updating references & citations, lack of content and context analysis

* Topic modeling's weakness in detecting pair-wise association of keywords

* Using temporal techniques to leverage word embedding, hence addressing forementioned limitations

## Dataset

* NIPS dataset

    + Neural Information Processing Systems conference papers

    + 7241 entries in 30 years (1987-2017), publicly available on Kaggle

    + meta-data: id, title, event-type, pdf, name, abstract, content

* MICCAI dataset

    + Medical Image and Computer Assisted Intervention conference papers

    + 3844 entries in 15 years (2004-2018)

## Proposed Approach

* Preprocessing

    + Language-based: stop words/common academic vocabulary removal, build bag-of-word of unigram and bigram using word2phrase

    + Time-based: divide the corpus into smaller timespan using 2 different paradigms: incremental windows and sliding windows

* Word Embeddings

    + Skip-gram Model

        - Hyperparameter: Context windows and dimensionality matter

        - Using k-nearest neighbors theory of word vectors to get the most optimal hyperparameters

    + Temporal Word Embeddings 

        - Incremental Embeddings: 
        
            + Update embeddings incrementally on an annual basis

            + 2 different embeddings: Fresh (retrain) and Update (train continuous)

        - Sliding Embeddings:

            + Fixed period length, retrain embedding everytime the window slide and have new vocabulary

* Similarity computation: 

    + Cosine Similarity between embeddings in each timespan across all corpora

    + Same keywords (only top-k keywords for efficiency) are used over all timespan

* Post Processing

    + Ranking: compare similarities 

    + Rank Ascent Identification

## Evaluation and Results


