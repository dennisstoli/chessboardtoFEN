Capstone Project: Tensorflow Chessboard Image to FEN

0) Problem Statement
   
Can we accurately predict a subreddit from a reddit post's title using classification modeling?
We will use Naive Bayes and Logistic Regression as our clasifiers to develop our models.
Sucess will be evaluated on our accuracy of predicting which post is from which subreddit.
It's interesting to see if there are particular words/phrases that separate one subreddit from another, and if there is any commonality between them as well.

1) Executive Summary
    
I gathered/collected our subreddit data using api requests and pushshift, and built a function to collect data in sets of 100 to then place that data into a dataframe.
I then concatenated the data together from each subreddit into one single dataframe. We were interested in the subreddits r/bitcoin and r/wallstreetbets, two subreddits focused on investing, but fairly different im pther aspects.

After Data collection, we cleaned our data by tokenizing/lemmatizing our titles, engineering some additional features, removing duplicate titles, and removing null values. With our new clean titles, I created some visualizion and conducted proper EDA to better understand the data collected for proper model analysis in the future. We found from the visualizations that the subreddits are fairly evenly distributed in regards to title length, as well as the amount of unique users. We also found the words that appear the most frequently within each subreddit.

I preproccesed our subreddit Data, train-test-split our X and y variables, and created models such as Logistic Regression and Naive Bayes, for scoring and predicting both the Bitcoin and WallStreetBets Subreddits from our clean titles. Created visualizations of our modeled data and predictive variables, created a confusion matrix for analysis, analyzed coeficients and probabilites as well. Found that Naive Bayes gave us the best score, and was able to find the most predictive words for each subreddit, as well as the most predictive titles. 



2) Table of Contents

[Data Collection](code/01_Data_Collection.ipynb)

[Data Cleaning and EDA](code/02_Data_Cleaning_and_EDA.ipynb)

[Preprocessing and Modeling](code/03_Preprocessing_Modeling.ipynb)

[Bitcoin Data](data/btc.csv) 

[WallStreetBets Data](data/wsb.csv) 

[Compiled Subreddit Data](data/compiled_subreddit_data.csv)

[Cleaned/Final Data](data/clean_data.csv)

[Presentation](presentation/Reddit_Presentation.pdf)
   
3) Data and Data Dictionary

DESCRIPTIVE ABSTRACT: Data set contains public information from the website reddit.com, where individuals can anonymously post on any subject.

SOURCES: 
https://reddit.com/r/bitcoin , https://reddit.com/r/wallstreetbets

|Feature|Type|Dataset|Description|
|---|---|---|---|
|**subreddit**|*object*|subreddit_df|The subreddit that the post was created in. (i.e. bitcoin)
|**title**|*object*|subreddit_df|The original title taken from the post. (i.e. GME to the moon!) 
|**author**|*object*|subreddit_df|The author's username who made the post.
|**title_length**|*int*|subreddit_df|The length of the title (in characters, spaces included)
|**title_word_count**|*int*|subreddit_df|The word count of the title.
|**clean_title**|*object*|subreddit_df|The clean titles created from the original titles, removing emojis, capitalization, formatting, spacing, etc.

4) Conclusions and Recommendation

We can accurately predict which subreddit a title is from with an accuracy over 85%, a great achievement.
These subreddits are fairly similar, but with particular individual characteristics we are able to predict accurately.
Through the process of cleaning our titles and predictive modeling, we did quite well.

We notice that r/wallstreetbets has many keywords, such as GME, MVIS, AMC, yolo, ape, etc., these keywords on top of it's meme-y community act as a bit of a separation between r/bitcoin.
r/bitcoin on the other hand is also an investing subreddit, but it's main focus is on bitcoin/btc rather than stocks, but also tends to quite meme-y. 
Another interesting point is that these subreddits frequently refer to eachother and their communities, with many subscribers that are part of both communities. 

r/bitcoin focuses more on investing/studying bitcoin, r/wallstreetbets focuses more on yoloing risky stocks and posting about them for internet points. The things that bring them together are: investing, money, memes, and humor.

If conducting a similar project with different subreddits, I would recommend gathering over 10,000 data entries and to clean the data very thoroughly. Use different modeling techniques as well to get the best accuracy possible.

5) Areas for Further Research/Study

I believe I can generate even more accurate data if I were able to take every post from each subreddit since its inception efficiently. Currently I do not have the knowledge to do that quickly, and that would be very interesting to see the difference between that data and the data I gathered. Also, time periods are interesting as well, currently the stock mvis is a popular keyword in r/wallstreetsbets, but a year from now a different keyword will replace it, dividing the data by time periods and doing separate analysis in that way would be intriguing as well.

In the future I would also recommend to try different types of models, possibly some boosting/KNN/tree to see what types of results those models bring. It would also be interesting to try out some other vectorizers outside of CountVectorizer and TfdifVectorizer.

Exploring different ways to Tokenize/Lemmatize/Clean the data I'm sure would yield different and intersting results as well. (i.e. spacy)



# chessboardtoFEN
