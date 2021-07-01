# HERMEVENT: A News Collection for Emerging-Event Detection
# Cristiano Di Crescenzo, Giulia Gavazzi, Giacomo Legnaro, Elena Troccoli, Ilaria Bordino, Francesco Gullo, 2017

## Quick summary

Introduced a new test collection for event detection called HERMEVENT, including large-scale dump of tweets and news articles from major Italian news in the span of 3 months. Using this dataset, the author aim to construct and extract temporal graph of co-occurred terms with different semantic and temporal granularity. Using 2 state of the art algorithm, the author validated the quality of the data with the help of human judges. The data and results are freely available.

## Problem Addressed/Main Contribution

* Build a new dataset that is freely available for text retrival/data mining task. Consists of tweets and news articles (title, body, date, entities)

* extract from the dataset set of knowledge graph with different granularity in terms of semantic and temporal

* Assessment of the newly built dataset with 2 state of the art algorithms with the help of human jusges for evaluation

## Dataset

* Period: Dec 2016 - March 2017

* Preprocessing: stopword removal, stemming, rare words removal, common words removal

* word-granularity and entity-granularity representation, organize in graph structure

* temporal-graph construction

## Proposed Approach

* BUZZ method: take temporal graph as input and extract emerging terms after 2 phases:

    + anomoly detection using co-occurrences and assigning relative importance score to each term, then compare them to past windows

    + extract k subgraphs from the graph resulted in phase 1, each subgraph has maximum N terms, with the measure of coherence using min-degree-based. Iterate until k is reach or graph is empty

* Raw-Graph Event Detection (RG-ED):

    + build graph based on co-occurrences and extract cohesive subgraphs w/o anomolies nor cohesiveness variance based on a time window

## Evaluation and Results

* Evaluation: human judges to determine the validity of the output

* Result: The dataset appears to be efficient for emerging trends detection, supported by the results of the experiment with BUZZ and RG-ED and the human judges 

* The dataset can be translate easily from Italian (original) to any other languages since the lexicon of the dataset is simple and straight-foward