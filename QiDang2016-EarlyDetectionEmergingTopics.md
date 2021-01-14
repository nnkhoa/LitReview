# Early detection method for emerging topics based on dynamic bayesian networks in micro-blogging networks
# Qui Dang, Feng Gao, Yadong Zhou, 2016

## Keywords/Topics/Field of Study

Mirco-blogging networks, emerging topics, early detection, DBNs

## Quick Summary

Previous researches are suitable for large-scale detection, however fall short on early detection because of less informative properties in small smaple size. Hence, the author proposed a method based on Dynamic Bayesian Network: 
	
	* analyze topic diffusion process to find 2 main properties of emerging topics: attractiveness and key-node

	* build a DBN-based model based on conditional dependency of features selected from topic diffusion to extract emerging keywords (frequency and specific topology properties)

	* clustered emerging keywords into topics using co-occurences relation

Experiments was done on real data (Sina micro-blogging), in which concluded that the method is effective and capable of detecting emerging topics 1-2 hours earlier than preivous methods

## Main Purpose/Problems being addressed 

	* Because of how importance and spontaneous nature of emerging topics, discovering them ASAP is required to design crisis contral strategies, explore business opportunities, find important information, strongly support real-time intelligent system (real-time recommendation, ad-targeting, marketing strategy)

	* Previous researches, while achieved good results in large scale data, still have the following challenges:

		+ Differences between emerging and non-emerging were ambiguous. Using term-frequency to indicate temporal evolution which represent burst property were less effective in a smaller sample size for early detection

		+ Timeliness was not a factor taken into account since (again) the data was large and had a long period of existence 

## Dataset
	
	* provided by Sina micro-blogging API, containing nearly 14 million tweets, posted by about 69 thousand users from Sep 1st to Oct 31, 2012

	* Attributes included: 

		+ basic user info: user's ID, name, gender, number of follower

		+ textual data: tweet's ID, time created, tweet content, retweet tag(to recognize retweeting relationship between users)

	* No standard dataset, hence manually labeled with the help of search engine, using keywords as indicator wheter a tweet is talking about a topic or not

	* 54 emerging topics (topics will develop into a large scale and last for hours), 50 non-emerging (could not last for a long time since their sudden apprearances)

## Technical approach

	* Problem description: 

		+ The goal is to detect the topic ASAP between 2 time period: when topic starting to burst and when topic is becoming emerging near peak time

		+ Meaning that we need to predict when the emerging topic has a sudden increase in attention (aka the emerging phase) 

		+ Because of how quickly a topic live and die (a few hours), using static features can be difficult to evaluate its emergence. Therefore, 2 characteristics were used in this research: attractiveness (how much do users give it attention and join in discussion), and key-node (influencer that can spread the topics with vast ammount of retweet, and greatly promote the development of the topic)

	* Feature selection: 

		+ Tweeting and retweet count, using Cascading Model to form a network of tweet and retweet. 

		+ Attractiveness is represented by the number of retweeting chain which has direct correlation with total number of distinct users attracted by the topic. 

		+ Key-nodes are nodes in the graph with the maxinum number of node in retweets chain, which usually meann that users have a lot of follower 

	* Dynamic Bayesian Networks 

		+ Key idea is to observe the selected feature via social features (retweet counts, retweet chains, maximun retweet chain, and total number of follower) to decide whether a keyword is emerging over an adjacent time step

		+ Calculate the probability of selected features based on the sequence of said social features

		+ In the training stage of the model, the goal is to find the optimize parameter that represent maximum likelihood over the training data

	* Cluster 

		+ DBSCAN is used to cluster the obtained emerging keywords into emerging topics, utilizing co-occurences of each pair of keywords

## Experimental Result

	* Comparing to Topic Graph, Moving Average Convergence/Divergence, and TF-IDF+NN

		+ The presented method performed better than those previously mentioned in terms on F1-Score (while it's not very impressive, only at 0.59/0.72/0.65 for Precision/Recall/F1 respectively)

		+ This approach has proven itself to be the most timeliness out of every other method, with the second fastest detection method (TF-IDF+NN) lacked behind about 1.24 hours, while the slowest has a delay of 2.27 hours

## Limitation
	
	* If more features are added, the state variables and computational complexity will increase multiply, hence features needed to be chosen carefully
