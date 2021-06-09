import streamlit as st
import chess
import chess.engine
import chess.pgn
import chess.svg
import base64
from tensorflow.python.keras.saving.save import load_model
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from PIL import Image
from functions import fen_from_matrix, process_image


st.title('Chessboard Image to FEN Generator')

model = load_model('model.h5')


try:
    resize_image = st.file_uploader("If you need to resize and crop the borders of the chess board first, upload it here:", type = "jpeg")
    image = Image.open(resize_image)
    resized_image = image.resize((400,400))
    resized_image = resized_image.crop((14, 14, 386, 386))


    st.image(resized_image) 
    st.header('Right Click, Download New Image and Upload Below')

except:
    pass




try:
    our_image = st.file_uploader("Upload a chess board to Extract the Position in FEN:", type = "jpeg")
    image = Image.open(our_image)
    resized_image = image.resize((400,400))

    st.image(our_image)

    uploaded_fen = fen_from_matrix(np.round(model.predict(process_image(our_image))))
    uploaded_fen = uploaded_fen.replace('-', '/')
    st.header(f'Predicted FEN: {uploaded_fen}')     

except:
    pass


# game = st.text_input('Input a Chess game in FEN:')

# try:
#     board = chess.Board(game)
#     board2 = chess.Board(game)

#     move_list = []
#     eval_list = []

#     engine = chess.engine.SimpleEngine.popen_uci("stockfish")
    
#     while not board2.is_game_over():
#         result = engine.play(board2, chess.engine.Limit(time = 0.2))
#         move_list.append(result.move)

#         info = engine.analyse(board2, chess.engine.Limit(depth=20))
#         eval_list.append(info['score'])
        
#         board2.push(result.move)   
#     engine.quit()

#     eval_list = [str(evals).split(',')[0].replace('PovScore(', '').split(',')[0].split('(') for evals in eval_list]
#     eval_list = [{'type': evals[0], 'value': int(evals[1].replace(')', ''))} for evals in eval_list]

#     if eval_list[0]['value'] > 0:
#         for i in range(len(eval_list)):
#             eval_list[i]['value'] = abs(eval_list[i]['value'])
#     else:
#         for i in range(len(eval_list)):
#             eval_list[i]['value'] = abs(eval_list[i]['value']) * -1

    
#     widget_values = {} #recording widget found in Streamlit Developer Forum
#     def make_recording_widget(f):
#         """Return a function that wraps a streamlit widget and records the
#         widget's values to a global dictionary.
#         """
#         def wrapper(label, *args, **kwargs):
#             widget_value = f(label, *args, **kwargs)
#             widget_values[label] = widget_value
#             return widget_value

#         return wrapper


#     slider = make_recording_widget(st.slider)

#     moves = [str(move) for move in move_list]
#     mv = slider('Move', 0, len(moves), len(moves))

#     for move in moves[0:mv]:
#         board.push(chess.Move.from_uci(move))


#     def render_svg(svg): #this function, also found in Streamlit Forums, renders SVG images, which chessboards in my program are!
#         """Renders the given svg string."""
#         b64 = base64.b64encode(svg.encode('utf-8')).decode("utf-8")
#         html = r'<img src="data:image/svg+xml;base64,%s"/>' % b64
#         st.write(html, unsafe_allow_html=True)
    
#     render_svg(chess.svg.board(board))

    
#     try:
        
#         if eval_list[widget_values['Move']]['type'] == 'Mate' and eval_list[widget_values['Move']]['value'] > 0:
#             st.subheader(f'White mates in {eval_list[widget_values["Move"]]["value"]} moves, best move is {move_list[widget_values["Move"]]}')
#         elif eval_list[widget_values['Move']]['type'] == 'Mate' and eval_list[widget_values['Move']]['value'] < 0:
#             st.subheader(f'Black mates in {eval_list[widget_values["Move"]]["value"] * -1} moves, best move is {move_list[widget_values["Move"]]}')
#         elif eval_list[widget_values['Move']]['type'] == 'Cp' and eval_list[widget_values['Move']]['value'] > 0:
#             st.subheader(f'White is winning, advantage: {eval_list[widget_values["Move"]]["value"]} centipawns, best move is {move_list[widget_values["Move"]]}')
#         elif eval_list[widget_values["Move"]]['type'] == 'Cp' and eval_list[widget_values["Move"]]['value'] < 0:
#             st.subheader(f'Black is winning, advantage: {eval_list[widget_values["Move"]]["value"]} centipawns, best move is {move_list[widget_values["Move"]]}')
    
#     except IndexError:
        
#         if eval_list[widget_values['Move'] - 1]['type'] == 'Mate' and eval_list[widget_values['Move'] - 1]['value'] > 0:
#             st.subheader(f'White Wins, Black is in Checkmate')
#         if eval_list[widget_values['Move'] - 1]['type'] == 'Mate' and eval_list[widget_values['Move'] - 1]['value'] < 0:
#             st.subheader(f'Black Wins, White is in Checkmate')

# except ValueError:
#     st.write('Your input is empty or invalid, input a Valid FEN :ghost:')
#     from PIL import Image
#     image = Image.open('Images/Trollface.png')
#     st.image(image, caption = 'Problem?')
    
