# Large-Scale Sentiment Analysis for News and Blogs
# Godbole, 2007

## Keywords/Topics/Fields of Study

Sentiment Analysis, News & Blogs, Named Entity, Natural Language Processing.

## Main Purpose/Problem(s) being adressed

- Sentiment Lexicon Generation without the need of human curation as the richer the lexicon the better the analysis, especially in topic-specified events.

- Lexicon expansion using synonym has the problem of weaker coherence as the synonyms get further away from the seeded word in terms of distance

- Rather than counting the number of positive/negative words based on a pre-existing dictionary to deduce the sentiment of a document, the paper presented a method to calculate score that indicates the sentiment of each word, thus construct a custom sentiment dictionary.

-  Additionally, the target of sentiment analysis in this work was on the named entity mentioned in the document, rather than on the whole document itself, giving a more in-depth analysis of what is presented in a document, instead of the theme of the whole document.

## General Idea

- Custom Sentiment Dictionary: based on a small list of candidate seed lists of positive and negative words, the approach is to expand it to a complete sentiment dictionary via path-based analysis of synonyms and antonyms in WordNet. Hop counts from seeded words will alter the sentiment value, hence modify the polarity strength of candidate terms and remove ambiguous terms.

- Sentiment Index Formulation: Sentiment Term Juxtaposition with Entities and Frequency-weighted interpolation with world happiness level to contruct a statistical index reflect the significance of sentiment juxtaposition

- Evaluation: by using serveral classes of real world events in correlation with sentiment index, statistical evidences were derived to verify and evaluate the resulting sentiment

## Detailed Solution and Method

- Sentiment Lexicon Generation

    * Path-based Analysis:

        + After assigning polarity (postive/negative) to a candidate word, synonyms will inherit such polarity from the parent while antonym will get the opposite polarity. For each candidate word, the further it is to the seeded word (in this case, depth of the graph), the less significant the sentiment of the word will be. The significance score descrease exponentially based on the depth: score (W) = 1/c^d where c is a constant > 1 and d is the depth of the word compared to the seeded word. The final score will be the sum of all scores accross all paths.

        + It is theorized in the paper that paths that alter the polarity of a word between positive and negative (named as flip by the author) are more prone to generate incorrect result. Hence, the algorithm is set to run in 2 iterations: First iteration is executed as described above to calculate the preliminary score for each word, while the second iteration re-enumerate all the path to calculate the number of flips. Less flips means more reliable result. Hence only words that have the number of flips within a pre-determined threshold will be kept.

        + To fetch synonyms and antonyms, the author used WordNet, which rank such words by sense and the more common sense words are at the top. Hence, only the top ranked word were used in order to increase accuracy


