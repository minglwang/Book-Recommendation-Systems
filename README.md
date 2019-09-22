# Book-Recommendation-Systems

<p>Charles Darwin is one of the few universal figures of science. His most renowned work is without a doubt his "<em>On the Origin of Species</em>" published in 1859 which introduced the concept of natural selection. But Darwin wrote many other books on a wide range of topics, including geology, plants or his personal life. In this notebook, we will automatically detect how closely related his books are to each other.</p>
<p>To this purpose, we will develop the bases of <strong>a content-based book recommendation system</strong>, which will determine which books are close to each other based on how similar the discussed topics are. The methods we will use are commonly used in text- or documents-heavy industries such as legal, tech or customer support to perform some common task such as text classification or handling search engine queries.</p>

The steps of buiding the system are as follows:
1. Load the contents of each book into Python
2. Find "On the Origin of Species"
3. Tokenize the corpus
4. Stemming of the tokenized corpus
5. Building a bag-of-words model
6. Find The most common words of a given book
7. Build a tf-idf model
8. Compute distance between texts
9. The book most similar to "On the Origin of Species"
10. Find books have similar content using dendrogram


The similarity Matrix visualization 
<p align = "center">
<img width ="800" height="400", src =https://github.com/minglwang/Book-Recommendation-Systems/blob/master/figures/Similarities.png>
 
 
 
The dendrogram
 
<p align = "center">
<img width ="800" height="300", src =https://github.com/minglwang/Book-Recommendation-Systems/blob/master/figures/recommendation.png>
  
