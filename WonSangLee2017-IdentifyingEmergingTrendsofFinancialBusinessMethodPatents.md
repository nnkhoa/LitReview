# Identifying Emerging Trends of Financial Business Method Patents
# Won Sang Lee, So Young Sohn, 2017

## Keywords

Financial business method patent, emerging topics, topic model, text mining, PWP-GT

## Quick Summary

Using financial business method patents, the research aims to identify emerging technology trend by applying LDA with a exponentially weighted moving average of LDA probability which affect whether a topic is "hot" or "cold". Survival analysis is utilized within the gap of time where a topic emerge from "cold" to "hot" status.

## Problem addressed/Main contribution

* Business Model (BM) patents signify sustainable development in financial industry. Hence, it is needed to figure out which opportunities and crucial factors exist

* Analyze the rise and fall of emerging topics by applying topic modeling - LDA and survival analysis

## Dataset

* 3866 abstracts from BM patents in the period of 1983-2012

* Preprocessing: stopwords removal (presumably), stemming

## Proposed Method

* LDA for topic modeling

    + used perplexity score over 10-fold cross validation (the decreasing function of log-likelihood of topic model give the estimated parameters) to determine the optimal number of topics

    + top 20 highest probability words make up a topic 

    + Topics relationship is evaluated through build topics graph of co-occurrence terms. Topics are considered to be related if they share more than 3 co-occurrence terms

* Survival analysis

    + based on the probability of the topics derived from LDA, exponentially weighted moving average - EWMA is calculated to observe the topic overtime 

    + a threshold is apply to classify whether a topic is "hot" or "cold". In this paper, the threshold value is 0.6
