# Event Identification in Social Networks
# Fattane Zarinkalam, Ebrahim Bagheri, 2016

## Keywords

Event Detection, Social Network Analysis, Topic Detection and Tracking

## Quick Summary

Social Networks are potential viable sources of information to understand ermerging topics/events due to their nature of enabling discussions and sharing openly recent news, on-going activity, or perspective on different topics. Traditional methods, while often apply to large, formal and structured documents, prove to be less optimal for text with short length, lots of noise or informality that is social posts. The paper describes the state of the art in social network event detection.

## Problem Definition

* Topic Detection and Tracking (TDT): News monitoring from multiple sources for users to update about news and developments

* TDT has been moving from traditional media to Social Network data, mostly Twitter as it is more publicly accessible 

* Media stream 

    * series of posts generated by users in social network, in which each post has text consists of sequence of words/terms, user id and time stamp

    * Time interval of interest and update rate might be provided 

* Output is expected to be emerging topics/events, which refer to specific things that happen at a certain time and place

* Representation of topics can be a cluster of documents or a set of selected important terms/keywords

## Challenges

* Time sensitivity: real-time, user may express opinion, feeling instantly serveral time per day on a daily basis

* Text length is short, hence may provide insufficient context

* Unstructure text with meaningless messages, informal content, irregular terms, grammar/spelling error, improper sentence structure, etc in large amounts. Moreover, content can be ranging from very high to very low quality, hence can negatively affect detection results

* Abundant of information 

## Specified Event Detection

* Identifying already known events, which are partially or fully specified by having their metadatas (location, time, etc.)

* Sasaki\[14\] created a classifier to monitor earthquake and rainbow, using tweets from user with following features: num of words(statistical), keywords, and contextual word. For location, they used a spatiotemporal (?) model. Results shown that statistical was the best, and small improvement when combine all 3.

* \[15\] built a framework for controversial events detection. By ranking controversy score of Twitter snapshot(target entity, given period, and tweets belong in the first two) by considering internal (linguistic, structural, sentiment, controversy) and external (?) features. Conclusion: hashtags are crucial semantic features to discovery the topics. Internal features play a considerable role as well (?)



## Unspecified Event Detection

* Topic Modelling Methods

    * Topic over Time model \[21\] captures term co-occurences and locality of patterns over time to discover event-specific topics

    * Due to sparsity characteristic of social media post, LDA and ToT do not perform well. Research tried to deal with this by concatenate tweets into a single long documents, yet proven less effective due to a small number of users make up a major portion of the content (?).

    * Twitter-LDA considers 1 tweet has only 1 topic, unlike traditional LDA 

    * Biterm topics models (BTM)  learns the topics by directly modeling the generation of word co-occurence patterns. Bursty BTM is an extension that focus on burstiness of topics

    * It is assumed that the number of topics doesn't change when applying these restriction 


* Document Clustering Methods

    * represent textual content as bag of words or n-gram using TF-IDF weighting schema, cosine similarity to compute co-occurrence

    * Disadvantages: cluster fragmentation, similarity is sensitive to noise, hence long/formal documents is better

    * Approach to work around: additional information including social features of social network (timestamp, publisher, location, hashtag)

    * \[35\] considered the multi-relation between tweets. \[34\] take into account temporal, spatial and textual similarity (?)

    * \[31\] proposed a constant time-space approach using locality sensitive hashing. Result shows that user ranking is better than number of tweet ranking. Entropy of the message can help reduce spam (?)

    * \[39\] classifies cluster content into real-world events or non-events by training the classifier using temporal, social, topical, and Twitter-centric features (?)

    * \[37\] proposed TwitterStand, a Twitter news processing system that captures late breaking news, using both textual similarity and temporal proximity. The author utilized a naive Bayes classifier for noise filtering, and an online clustering algorithm to cluster news using weighted term vectors. (?)

    * \[38\] using predefined search queries to sample tweet before grouping to form a news story. Similarity is based on tf-idf value. Usernames, hashtags, proper noun terms are factors that increase weight. Combining with number of followers (reliability), number of retweet (popularity) and time adjustment for freshness, the author can rank each cluster.

* Feature Clustering Methods

    * Extract features of topics from documents then clustering these features based on their senmantic relatedness

    * \[40\] built co-occurrences graph of emerging terms based on frequency and importance to detect emerging topics  (?)

    * \[41\] generate co-occurences graph of topical words, then apply top-down hierarchiacal clustering algorithm to detect events from different time period. Afterward, changes of these events are tracked in consective time period. Event summarization is done by finding the most relevant posts (?)

    * \[42\] experimented with terms co-occurrences graph, whose nodes are clustered using community detection algorithm, connected by edges representing lexical inclusion/similarity (?)

    * \[46\] viewed each topics as a conjunction of several concepts, used graph clustering algorithm to extract temporally related concepts in a give time period. Semantic context was preserved by using inter-concept similarity, which had the co-occurrences customized within a single tweet (?)

* Signal Processing Techniques: use wavelet analysis, discrete fourier transform
