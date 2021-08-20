# Leap2Trend: A Temporal Word Embedding Approach for Instant Detection of Emerging Scientific Trends
# Amna Dridi, Mohamed Medhat Gaber, R. Muhammad Atif Azad, Jagdev Bhogal, 2019

## Quick Summary

Unlike previous attempts to detect emerging trends in research papers through bibliography which are known to have problem in timeliness and content analysis, the literature proposed an approach using temporal word embeddings, dubbed as Leap2Trend. Leap2Trend tracks similarities between pairs of keywords overtime which yielded results suggesting the robustness and timeliness characteristics of the method.

## Problem Addressed/Main Contribution

* Citation counting has many limitations: massive delay in updating references & citations, lack of content and context analysis

* Topic modeling's weakness in detecting pair-wise association of keywords

* Using temporal techniques to leverage word embedding, hence addressing fore-mentioned limitations

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

    + Language-based: stop words/common academic vocabulary removal, build bag-of-word of uni-gram and bi-gram using word2phrase

    + Time-based: divide the corpus into smaller time span using 2 different paradigms: incremental windows and sliding windows

* Word Embeddings

    + Skip-gram Model

        - Hyperparameter: Context windows and dimensionality matter

        - Using k-nearest neighbors theory of word vectors to get the most optimal hyper-parameters

    + Temporal Word Embeddings 

        - Incremental Embeddings: 
        
            + Update embeddings incrementally on an annual basis

            + 2 different embeddings: Fresh (retrain) and Update (train continuous)

        - Sliding Embeddings:

            + Fixed period length, retrain embedding every time the window slide and have new vocabulary

* Similarity computation: 

    + Cosine Similarity between embeddings in each time span across all corpora

    + Same keywords (only top-k keywords for efficiency) are used over all time span

* Post Processing

    + Ranking: compare similarities (ambiguous)

    + Rank Ascent Identification: 
    
        - compare the differences in ranking of pairs of keywords between time spans to 0 and a threshold

        - if between 0 and threshold, it is considered as a jump in ranking, if more than threshold, it considered as a leap, both indicating fast emerging keywords 

## Evaluation and Results

* Evaluation: 

    + Gold Standard: 

        - Google Trends hits: compare to the results from query of pair of keywords, for the purpose of verifying ascent captured by Leap2Trend is whether a positive sign which can lead to emerging trend

        - Google Scholar citation: stack the ascents of pairs of keywords extracted by Leap2Trend against the citation count change over time, to find out their correlation 
    
    + Evaluation Metric:

        - Ascent Accuracy and Recall: 
        
            + Accuracy: fraction of ascent turned into positive slope in Google Trend over total ascent detected 

            + Recall: number of ascent in the gold standard that was correctly detected

        - Ascent Precision: percentage of pair of keywords that ended up with positive slopes to total of pair of keywords in vocabulary

* Results:

    + Regarding Incremental Embeddings, fresh retraining proved to be the better option. However, Sliding Embeddings is the best alternative

    + Results showed that Leap2Trend is able to detect emerging keyword in a timeliness manner

    + Experiment limited in time period (only after 2004 due to Google Trends), scenario (only considered rising, not falling in trends), and field of research (only computer science and bioinformatics)

