# tweet-emotion-classifier

This classifier with full unicode support takes two sets of training data in the form of tab delimited files containing tweets mined using the Twitter API. 

The SVM_perf implementation of the Support Vector Machine (SVM) is then used to create a binary classifier. 

For example, the first training set can be composed of tweets mined using happy emoticons as a query. The second would then be composed of tweets mined using sad emoticons as a query.
Running the authormator.sh shell script would clean the tweets, stripping them of superfluous data and characters. 

The training data is then used to create a dictionary of features; an index of unique words in the dataset. The tweets are randomized and then divided into training, development, and testing sets that are then output as series of ‘feature:value’ pairs based on the features in each tweet found in the feature dictionary. Each of these lines was preceded by a class identifier, -1 for ‘sad’ and 1 for ’happy’ tweets.  
This vectorised data was then used to train an SVM classifier using svm_pref_learn with a C value of 20 for the hashtag based classifier and 220 for the emoticon based classifier. 

The resulting classifier, if it performs well, can then be used to classify further tweets.
