# Automatic trend detection: Time-biased document clustering
# Sahar Behpour, Mohammadmahdi Mohammadi, Mark V. Albert, Zinat S. Alam, Lingling Wang, Ting Xiao, 2021

## Keywords

Text Mining, Trend Detection, Temporal biased clustering, Machine Learning

## Quick Summary

Introduced a weighted temporal feature to bias a topic clustering toward articles in a similar time frame. Target articles belong to financial sector from 1974 to 2020. LDA is used to parameterize each abstract, followed by SVD to reduce the dimension of features. Silhouette score divided standard deviation of clusters over time is used to identify trending topics. Expert judgement will validate the final results.

## Problem Addressed/Main Contribution

* Automated time-biased clustering model to extract trending topic and terms 

* Calculates quality score to automatically evaluate candidate clusters in each iteration of clustering runs

* Works on abstract of journals and can scale to other field and documents of other form

## Dataset

* From 1974 to 2020, 2858 documents from 1819 unique publishers

* Field collected: Abstract, Author, Year of Publication, Affiliation

* No labeling or target class required

## Proposed Approach

* Pre-processing

    + Tokenization, lowercasing, removing punctuation, number & stopwords, and stemming. Resulted in 12k distinct tokens

* General framework

    + Apply LDA to get the general content of the corpus (there 50 topics determined before-hand)

    + TF-IDF for vector representation of each tokens. SVD and NMF are used for reducing the dimension

    + Standard (k-mean with k=15) vs Time-biased clustering (apply time co-efficient)

    + Trend score metric: silhouette score and standard deviation to evaluate different temporal bias variations as threshold for temporal clustering  

        - Silhouette score (s.s) describes how close [-1,1] each point inside a cluster is to neighbor clusters. Higher means suitably matches the neighboring terms within clusters. Lower means wrongly assigned

        - Standard deviation (s.d) illustrates the distribution of articles throughout different years. Lower means more localized cluster's structure and trending topics

        - trend score = s.s/s.d

        - generated the list of bias ammount for each document and created the bias corpus representation by multiplying the bias with the SVD matrix

## Results 

* Clustering 

    + Standard Clustering: K-mean where k=15

        - Disadvantage: tends to combine more than 1 area of finance into the same cluster which limits identifying timely trends 

    + Time-biased Clustering

        - Fewer key terms were extracted, more even article distribution among clusters, with better grouped topics which were easier to recognize

        - higher level bias = lower number of well-defined cluster, but the good ones are still stable while having clearer begining peak and end, thus become more localize in time
        
