# Capstone Project: Tensorflow Chessboard Image to FEN 
Finished Web Application [web app](https://share.streamlit.io/dennisstoli/chessboardtofen/main/board_to_fen.py)

## Problem Statement
   
Can we create a machine learning model to read an image of a chess board and convert it to the board's FEN?
We will use Tensorflow Keras to develop our model.
Success will be evaluated on our accuracy of predicting a chess board's FEN from an image of a chess board.
It will be interesting to see how our final model recognizes different board states, colors, and piece variations.

## Executive Summary
    
I downloaded the chess board position images from Kaggle. 
The dataset is described as: 

100000 images of randomly generated chess positions of 5-15 pieces (2 kings and 3-13 pawns/pieces)
Images were generated using 28 styles of chess boards and 32 styles of chess pieces totaling 896 board/piece style combinations.

After proper imports, since the files were named after their FEN position, I extracted the FEN from the file name using a function. This will be used later for training our model. 

We then created a function to convert a FEN into a matrix. The function first takes in a FEN (ex. R3q3-8-5k2-n7-8-3Q2pb-3K1P2-6N1) and converts it to a list of 64 variables (one for each square on a chess board) like so: ['R', '_', '_', '_', 'q', '_', '_', '_', '_', '_', '_', '_', '_', '_', '_', '_', '_', '_', '_', '_', '_', 'k', '_', '_', 'n', '_', '_', '_', '_', '_', '_', '_', '_', '_', '_', '_', '_', '_', '_', '_', '_', '_', '_', 'Q', '_', '_', 'p', 'b', '_', '_', '_', 'K', '_', 'P', '_', '_', '_', '_', '_', '_', '_', '_', 'N', '_']. The function continues and takes this list and converts it into a numpy array to be read by our model in the future.

Now that we have a function to convert a FEN into a Matrix, we need a function to do the opposite.
The process for this was a bit more complex, but the main idea was to transform the matrix into a list first, and then transform that list into a FEN string. Details can be found in the Jupyter Notebook.

Now we required a function to process an image into a Numpy Array, this would be the x input variable in our model. The function converts an image into 64 individual squares (one for each square on a chess board) and returns a numpy array for that image. 

With all the required functions for modeling, we built a train generator that processes an image (x-variable) and extracts the matrix from the corresponding FEN. We then created our Sequential model using Convolution, MaxPooling, and Dense layers. Our final Dense layer having its activation as 'softmax', since we are creating a multi-classification model. We compile the model and are looking for the model's accuracy and loss. Finally, we fit the model with our train generator and save it!

We run predictions on our test image and find that our model has an accuracy of nearly 100%




## Table of Contents


[Code](0_image_to_FEN_CNN.ipynb)

[Neural Network Visual](Images/model_viz.png)

[Streamlit Application](board_to_fen.py)

[Functions for Streamlit](functions.py)

[Streamlit Load Model](load_model.py) 

[Final Model](model.h5) 

[Requirements](requirements.txt)

   
## Data and Data Dictionary

DESCRIPTIVE ABSTRACT: Dataset contains images uploaded to the website https://www.kaggle.com, where individuals can upload datasets for others to use.

SOURCES: 
https://www.kaggle.com/koryakinp/chess-positions

CONTENT:

100000 images of randomly generated chess positions of 5-15 pieces (2 kings and 3-13 pawns/pieces)
Images were generated using 28 styles of chess boards and 32 styles of chess pieces totaling 896 board/piece style combinations.

All images are 400 by 400 pixels.

Training set: 80000 images
Test set: 20000 images
Pieces were generated with the following probability distribution:

30% for Pawn

20% for Bishop

20% for Knight

20% for Rook

10% for Queen

2 Kings are guaranteed to be on the board.

Labels are in a filename in Forsyth–Edwards Notation format, but with dashes instead of slashes.

## Conclusions and Recommendation

We can accurately predict what the FEN of a chess board is with appropriate functions and a Machine Learning Model using Tensorflow Keras. We achieved an accuracy of nearly 100 %.

We successfully converted an image into a matrix, a FEN into a Matrix, and a Matrix into a FEN, to create a Machine Learning Model that can read images and predict a FEN, accurately, from said images.



## Areas for Further Research/Study

After running my created model with different images in my streamlit application, I noticed a few issues.

1.) The chess board needs to be resized into a 400 x 400 jpeg image to achieve best results.

2.) The chess board image cannot have any background outside the 64 squares.

3.) The chess board cannot have pieces that are too 'abstract'.

I was able to fix the first issue by adding a resizing function in my application if required.

The second issue I was able to fix IF the image background outside the 64 squares is uniform, and not too large. I simply created a cropping and resizing function in streamlit to achieve this, but backgrounds that are not so uniform would pose a problem.

I believe I can generate an application that can predict the FEN's of more images if I were to create a function that can crop chess boards exactly to my liking every time. This would require another machine learning model/function that can detect chess squares and crop accordingly.

To fix the third issue, I would have to find more images of chess/boards with 'abstract pieces', although those aren't too widely used as they are often difficult to interpret initially.

In the future, it would be interesting to apply a similar approach to real-life pictures of chess boards. Instead of uploading images of computerized chess boards, I would develop a model that can read physical chess boards and return a computerized one and its position in FEN.
