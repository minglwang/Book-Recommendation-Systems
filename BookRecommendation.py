# -*- coding: utf-8 -*-
"""
@author: miwan
"""

# Import library
import glob
import re, os
# %matplotlib inline

os.chdir(r"C:\Users\miwan\Box Sync\Book Recommendations from Charles Darwin\datasets") 
# The books files are contained in this folder
folder = "datasets/"
# List all the.txt files and sort them alphabetically
files = sorted([file for file in glob.glob( "*.txt")])

print(files)


# Initialize the object that will contain the texts and titles
txts = []
titles = []

for n in files:
    # Open each file
    f = open(n, encoding='utf-8-sig')
    # Remove all non-alpha-numeric characters
    data = re.sub('[w_]+','',f.read())
    # Store the texts and titles of the books in two separate lists
    txts.append(data)
    titles.append(os.path.basename(n).replace('.txt',''))

# Print the length, in characters, of each book
[len(t) for t in txts]

# Browse the list containing all the titles
for i in range(len(titles)):
    # Store the index if the title is "OriginofSpecies"
    if titles[i] == "OriginofSpecies":
        ori = i

# Print the stored index
print(ori)


# Define a list of stop words
stoplist = set('for a of the and to in to be which some is at that we i who whom show via may my our might as well'.split())

# Convert the text to lower case 
txts_lower_case = [txt.lower() for txt in txts]

# Transform the text into tokens 
txts_split = [txt.split() for txt in txts_lower_case]

# Remove tokens which are part of the list of stop words
texts = [[word for word in txt if word not in stoplist] for txt in txts_split]

# Print the first 20 tokens for the "On the Origin of Species" book
print(texts[ori][:20])


#import pickle
# Load the Porter stemming function from the nltk package
from nltk.stem import PorterStemmer

# Create an instance of a PorterStemmer object
porter = PorterStemmer()

# For each token of each text, we generated its stem 
texts_stem = [[porter.stem(token) for token in text] for text in texts]
#pickle.dump(texts_stem, open( "texts_stem.p", "wb" ) )
#texts_stem = pickle.load(open("texts_stem.p", "rb"))

# Print the 20 first stemmed tokens from the "On the Origin of Species" book
print(texts_stem[ori][:20])

# Load the functions allowing to create and use dictionaries
from gensim import corpora

# Create a dictionary from the stemmed tokens
dictionary = corpora.Dictionary(texts_stem)

# Create a bag-of-words model for each book, using the previously generated dictionary
bows = [dictionary.doc2bow(texts_stem[i]) for i in range(len(titles))]

# Print the first five elements of the On the Origin of species' BoW model
print(bows[ori][:5])


# Import pandas to create and manipulate DataFrames
import pandas as pd

# Convert the BoW model for "On the Origin of Species" into a DataFrame
df_bow_origin = pd.DataFrame(bows[ori])

# Add the column names to the DataFrame
df_bow_origin.columns = ['index', 'occurrences']

# Add a column containing the token corresponding to the dictionary index
df_bow_origin["token"] = [dictionary[index] for index in df_bow_origin["index"]]

# Sort the DataFrame by descending number of occurrences and print the first 10 values
df_bow_origin.sort_values(by='occurrences', ascending=False)


# Load the gensim functions that will allow us to generate tf-idf models
from gensim.models import TfidfModel

# Generate the tf-idf model
model = TfidfModel(bows)

# Print the model for "On the Origin of Species"
print(model[bows[ori]])



# Convert the tf-idf model for "On the Origin of Species" into a DataFrame
df_tfidf = pd.DataFrame(model[bows[ori]])

# Name the columns of the DataFrame id and score
df_tfidf.columns = ['id','score']

# Add the tokens corresponding to the numerical indices for better readability
df_tfidf["token"] = [dictionary[index] for index in df_tfidf["id"]]


# Sort the DataFrame by descending tf-idf score and print the first 10 rows.
df_tfidf.sort_values(by ='score',ascending = False).head(10)

# Load the library allowing similarity computations
from gensim import similarities

# Compute the similarity matrix (pairwise distance between all texts)
sims = similarities.MatrixSimilarity(model[bows])

# Transform the resulting list into a dataframe
sim_df = pd.DataFrame(list(sims))

# Add the titles of the books as columns and index of the dataframe
sim_df.columns = titles 
sim_df.index = titles 
# Print the resulting matrix
print(sim_df)

# This is needed to display plots in a notebook
#%matplotlib inline

# Import libraries
import matplotlib.pyplot as plt

# Select the column corresponding to "On the Origin of Species" and 
v = sim_df['OriginofSpecies']

# Sort by ascending scores
v_sorted = v.sort_values()
print(v_sorted)
# Plot this data has a horizontal bar plot

v_sorted.plot.barh(y='OriginofSpecies', rot=4).plot()
plt.yticks(fontsize = 15)
# Modify the axes labels and plot title for a better readability
plt.xlabel('Similarity')
plt.ylabel('Books')
plt.title('Similarities of "Origin of Species" and other books ')
plt.show()

# Import libraries
from scipy.cluster import hierarchy

# Compute the clusters from the similarity matrix,
# using the Ward variance minimization algorithm
Z = hierarchy.linkage(sim_df,method = 'ward')

# Display this result as a horizontal dendrogram
plt.figure(figsize = (13,5))
a = hierarchy.dendrogram(Z,leaf_font_size=8,labels=sim_df.index,orientation="left")


