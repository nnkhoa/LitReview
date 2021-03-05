# Sentence-BERT: Setence Embeddings using Siamese BERT-Networks
# Nils Reimers, Iryna Gurvych, 2019

## Keywords

BERT, siamese network, semantic textual similarity(sts)

## Quick summary

The author present Setence-BERT, a modification of pretrained BERT network using siamese and triplet network structure to calculate semantic textual similirity between setences. This methods is unsupervised and compared other past approaches, performs extremely faster, experimented on common STS and transfer learning task.

## Main purpose/ Problem addressed

Because BERT use cross-encoder which can generate too many possible combinations between two setences thus is time consuming, the method is clearly unsuitable to identify which pair of setences are similar to each other.

Example: Finding in 10000 setences the pairs that has the highest similarity required 499950 computations, which cost ~65 hours depends on the GPU.  

## Dataset

* Training data: 
    
    + SNLI: 570000 setence pair, labeled with contradiction, eintailment and neutral

    + Multi-gerne NLI: 430000 setence pairs, wide coverage of gernes

## Proposed Approach

* After each sentence goes into BERT model, a pooling layer is added to transform them into a fixed sized setence embedding.

* 3-layer siamese network structure: BERT, pooling, and an objective function that depends on the purpose of the task: softmax for classification, cosine-similarity for regression, etc.

* Training detail: fine-tuned with 3-way softmax-classifier function for 1 epoch, batch-size 16, Adam optimizer, learning rate 2e-5, linear learning rate warm-up of 10% of training data, default pooling strat is MEAN

## Experimental Results

* On unsupervised STS datasets, the approach has poor results, consist of Spearman rank's correlation between cosine-similarity of the sentence embedding and the gold label. 

* With supervised dataset, the model proved to be better with certain configuration and certain dataset.

* Computational efficiency: with smart batching, SBERT was 55% faster than Universal Setence Encoder. On CPU, smart batching has 89% improvement in speed, while on GPU, 48%

