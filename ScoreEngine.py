import random
import chess

class ScoreEngine(object):
    
    piece_values = {
        'P': 1,
        'N': 3,
        'B': 3,
        'R': 5,
        'Q': 9,
        'K': 0,
    }

    def __init__(self):
        None

    def play(self, board):
        moves = list(board.legal_moves)
        
        best_move = None
        best_score = -99999  # todo: make this not ugly

        for move in moves:
            # apply the current candidate move
            
            new_board = board.copy()
            new_board.push(move)
            
            # count material in the new position
            
            all_pieces = new_board.piece_map().values()
            
            material_count = 0
            
            for piece in all_pieces:
                value = self.piece_values[piece.symbol().upper()]
                if piece.color == board.turn:
                    material_count += value
                else:
                    material_count -= value
                    
            if material_count > best_score:
                best_move = move
                best_score = material_count
                
        return best_move
