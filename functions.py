
import io
import re
import skimage
from skimage.util.shape import view_as_blocks
from skimage import io, transform
pieces = 'prbnkqPRBNKQ_'


def process_image(img):
    square_size = int(240/8) 
    img_read = io.imread(img) 
    img_read = transform.resize(img_read, (240, 240), mode = 'constant') 
    squares = view_as_blocks(img_read, block_shape = (square_size, square_size, 3)) 
    squares = squares.squeeze(axis = 2) 
    squares = squares.reshape(64, square_size, square_size, 3) 
    return squares 


def fen_from_matrix(matrixed_fen):
    
    output = ''
    s = []
    q = []
    
    for j in range(64):
        for i in range(12,13):
            if(matrixed_fen[j][i] == 1.):
                output += '1'             
        for i in range(12):
            if(matrixed_fen[j][i] == 1.):
                output += pieces[i]       
        
    output = [output[i:i+8] for i in range(0, len(output), 8)] 
    
    for i in range(len(output)):
        s.append(re.split('(\d+)', output[i])) 
    
    try:
        
        for i in range(len(s)):
            if s[i][-1].endswith(('p', 'r', 'b', 'n', 'k', 'q', 'P', 'R', 'B', 'N', 'K', 'Q')) and s[i+1][0].endswith(('p', 'r', 'b', 'n', 'k', 'q', 'P', 'R', 'B', 'N', 'K', 'Q')):
                s[i].append('')
    
    except IndexError:
        
        pass                     
    
    for i in range(len(s)):
        for j in s[i]:
            try:
                q.append(int(j))
            except:
                q.append(j)       
                
    fen = [len(str(i)) if type(i) == int else i for i in q] 
    
    fen = ['-' if i == '' else i for i in fen] 
    
    fen = [str(i) if type(i) == int else i for i in fen] 
    
    fen = ''.join(fen) 
    
    fen = fen.replace('--', '-') 
    
    if '7r' or '7R' or '7n' or '7N' or '7b' or '7B' or '7q' or '7Q' or '7k' or '7K' or '7p' or '7P' in fen:
        
        fen = fen.replace('7r', '7r-')
        fen = fen.replace('7R', '7R-')
        fen = fen.replace('7n', '7n-')
        fen = fen.replace('7N', '7N-')
        fen = fen.replace('7b', '7b-')
        fen = fen.replace('7B', '7B-')
        fen = fen.replace('7q', '7q-')
        fen = fen.replace('7Q', '7Q-')
        fen = fen.replace('7k', '7k-')
        fen = fen.replace('7K', '7K-')
        fen = fen.replace('7p', '7p-')
        fen = fen.replace('7P', '7P-')
    
    if 'r7' or '7R' or 'n7' or 'N7' or 'b7' or 'B7' or 'q7' or 'Q7' or 'k7' or 'K7' or 'p7' or 'P7' in fen:
        
        fen = fen.replace('r7', '-r7')
        fen = fen.replace('R7', '-R7')
        fen = fen.replace('n7', '-n7')
        fen = fen.replace('N7', '-N7')
        fen = fen.replace('b7', '-b7')
        fen = fen.replace('B7', '-B7')
        fen = fen.replace('q7', '-q7')
        fen = fen.replace('Q7', '-Q7')
        fen = fen.replace('k7', '-k7')
        fen = fen.replace('K7', '-K7')
        fen = fen.replace('p7', '-p7')
        fen = fen.replace('P7', '-P7')
        
    
        
    if fen.startswith('-') == True and fen.endswith('-') == True:
        fen = fen[1:-1]
    elif fen.startswith('-') == True:
        fen = fen[1:]
    elif fen.endswith('-') == True:
        fen = fen[:-1]
    else: fen = fen
    
    
    
    fen = fen.replace('--', '-') 
    
    
    
    fen = fen.replace('--', '-') 
    

    return fen
