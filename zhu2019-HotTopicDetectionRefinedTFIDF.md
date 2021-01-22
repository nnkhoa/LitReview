# Hot Topic Detection Based on a Refined TF-IDF Algorithm
# Zhiliang Zhu, Jie Liang, Dyang Li, Hai Yu, Guoqi Liu, 2019

## Keywords/Topics/Field of Study

Feature Extraction, Hot Topic Detection, Hot terms, Time sensitive, User attention

## Quick Summary

Because of limitation in the classic algortihm, the research proposed a refined version of TF-IDF to discover hot terms based on time distribution information and user attention. Moreover, generating new and combined terms is also taken into account, using Chinese word segmentation algorithm. To detect hot topics according to hot terms, K-mean clustering algorithm is utilized.
Experimental results indicated that the refined TF-IDF algorithm can discover hot topics in a efficient maner.

## Main Purpose/Addressed Problem(s)

	* classic TF-IDF was not a good text feature to use in hot topic detection due to the fact that in hot topics, new terms appear more frequently in documents, hence lower the IDF weight. As a consequence, the importance of new terms are lowered

	* Existing (Chinese) word segmentation methods cannot recognize new terms/combined terms since they can misinterpret and separate new terms wrongly

## Dataset

Pure text collection crawl from NetEase news from August to November 2017, containing around 2000 articles. Each entry contains title, text content, published time, and number of participants (number of comments, upvote, downvote)
For word segmentation and word frequency statistics, the author use NLPIR system, provided by Chinese Academy of Sciences

## Technical Approach

	* Recognize new terms

		- Based on the segmented words, if the frequency of 2 adjacent words appear together match the frequency of each separated word, the 2 words are joined to create new terms 

	* TA TF-IDF (Refined TF-IDF)

		- By comparing the standard deviation of hot term's IDF weights over 2 different periods of time, 1 includes a particuliar period while the other does not, the method derives an extra weight for IDF value to adjust for hot terms sudden increases in appearance

		- User attention is represented by the average number of comments on news articles that contains the hot terms as an extra weight to adjust the IDF value

		- These 2 adjustment values are normalized to make these figures more meaningful and easier to apply into TF-IDF 

	* Detecting hot topics based on hot terms

		- Based on hot terms, related news will be extracted into a new corpus. Documents will be represented using vector space model

		- As for clustering methods, KMean is used to group documents into hot topics 

## Experimental Results
	
	* Evaluation method: Using Baidu media and search index, which reflects media attention on the keywords and from user's perspective, to decide whether the derived hot word is truly hot or not, which then use them to calculate accuracy

	* Adjusted Value: perform best when combined both attention and time are considered, while generated hot words based on only one aspect cannot outperform in any test. Time factor performed better

	* Hot Topic Detection: Compared to reference methods, the proposed approach has better accuracy, and has better filtering capability
