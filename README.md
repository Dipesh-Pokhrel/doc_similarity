"### Document Similarity"
Attempts to use cosine similarity to measure the similarity between two documents

##### cosine similarity
Converts two documents into vectors and calculates their similarity. The inner product space that measures the cosine angle between them is used to calculate similarity.

We define cosine similarity mathematically as the dot product of the vectors divided by their magnitude. For example, if we have two vectors, A and B, the similarity between them is calculated as:

``` math
    similarity(A, B) = cos({/theta}) = A.B / ||A|| ||B||
```