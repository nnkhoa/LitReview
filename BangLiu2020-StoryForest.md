# Story Forest: Extracting Events and Telling Stories from Breaking News

# Bang Liu, Fred X. Han, Di Niu, LingLong Kong, Kunfeng Lai, Yu Xu, 2020

## Keyword

document clustering, community detection, news articles organization, semi-supervised setting 

## Quick Summary

The paper proposed Story Forest, a system that automatically clusters stream of documents into events and connect relevant events into a storyline that are unfolding. The heart of Story Forest is EventX, a 2-layer, semi-supervised scheme that extract events from enormous news corpora on a finer-grain than past methods. Experiment is done on 3 set of dataset in 2 languages: Chinese and English

## Problem addressed/Main Contribution

* Problem definition

    - An Event is a set of news documents reporting the same content of real-world breaking news 
    
    - A story is a tree of related event that report  

    - 2 articles cover the same event so long as their contents were published during the same time of occurrences as the event, and has the same entities participate in.

    - Relationship between events is only considered via temporal evolution to give a cleaner and more specific, conceptual-wise, representation to the event

    - Topics are usually broader and more abstract than event. However, no event should should fall under multiple topics, which is realistic for breaking news, which, for the sake of timeliness, covers only 1 real-world incident.

    - Each topic can contain many story trees, and each tree can contains multiple events that are connected logically

    - Topics, stories and events do not have to be explicitly defined 

* Contribution

    - Extract events from a large volume of data in a semi-supervised manner, using 2-layered, graph-based document clustering which distinguish topic discovery from finer-grain event extraction

    - Represent a series of events in a tree-based manner, called story tree, which can also dynamically incorporate new events into existing trees

    - Manual label of data for study and evaluation since there are no publically available data in this research area

    - Efficient and scalable, which are important for industry practice

## Dataset

* Chinese News Corpus, containing 60GB of Chinese news from providers such as Tencent, Sina, etc. in the period between 1st Oct 2016 and 31st Dec 2016, that needs to employ human anotators/evaluators to analyze overall performance.

* Chinese News Event - 11,748 articles, a smaller dataset from Tencent, which has been anotated with truth events and stories for event extraction evaluation.

* NewsGroup 20: classic English dataset

## Proposed Method

* Preprocessing

    - Discard very short documents (less than 20 tokens)

    - Tokenization of title and content

    - Keyword (kw) extraction:

        + TF-IDF: cant extract kw with low freq. TextRank: Resources consuming when use with long documents. Rule-based: depends on the rules, less generalization

        + Manual annotation using human judges, resulted in 20k+ positive keywords, 350k+ negative keywords from 10k+ documents

        + Use Binary classifier with the following features: position of appearances (title, content), named entity, TF-IDF, TextRank score, distances between first and last appearances, LDA topic probabilities

        + With LDA, training took 30 hours, with 300k+ documents, picking 1000 topics for modeling.

        + Features are put in Logistic Regression + Gradient Boosting (reduce human bias) or SVM classifier with similar performance

* EventX for Event Extraction

    - Construct keyword co-occurrence graph - 2 keywords are connected if:

        + they co-occur past a certain threshold

        + their conditional probabilities also exceed a pre-defined threshold

    - Topic Clustering based on Keywords Co-occurrences graph

        + Split the graph into communities, based on betweeness centrality score of edges between 2 keywords: the number of shortest paths between all pair of all pair of nodes that pass through

        + Higher betweeness score (HBS) implies edge is between 2 communities and will be remove

        + Use BFS, recalculate HBS after each removal, done recursively on subgraph once not a fully connected graph

        + if subgraph has number of nodes or HBS below a threshold, the process ends 

        +  Documents are then clustered by calculating similarities between keywords community, using TFIDF as representation

    - Event Extraction using Document Relationship Graph

        + each document is considered as a graph node, pairs with the same event should be connected

        + granularity should be adjusted accordingly since events are diversive

        + Semi-supervised SVM to determine if a pair of documents is talking about the same event, based on feature such as TF-IDF, cosine similarity, LDA cosine similarity, etc.

        + After each prediction from the classifier, human judges will determine whether the prediction is correct or not 

* Growing the story trees

    * Identifying related story tree: determined by calculate the similarity between the set of keywords of the stories and events, and if they share a certain ammount of keywords in their titles

    * Update story tree: Merge or Insert/Extend 

## Evaluation Metric

* Homogeneity, Completeness, V-score, Normalize Mutual Information

* Comparing to other methods: KeyGraph, Co-Clustering, Word-to-Doc Clustering, Non-negative Matrix Factorization

## Results 

* Experiment results show that the proposed system outperform past clustering methods significantly
