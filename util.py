import chess
import chess.svg


def play_game(board, white_player, black_player, display, last_move=None):
    """
    Plays a game until completion
    """
    
    display(board)
    
    while not board.is_game_over():
        player = white_player if board.turn == chess.WHITE else black_player
        
        move = player.play(board)
        
        board.push(move)
    
        display(board)
    
    return board
    
    
def text_display(board, last_move):
    print("\n- - - - - - -")
    print(board)
    print("- - - - - - -\n")
    

def svg_display(board):
    move = board.peek() if len(board.move_stack) else None
    display(chess.svg.board(board, lastmove=move, size=300))


def position_features(board):
    """
    For now, this will only generate raw features of a position, not knowing anything about moves 
    (castling rights, checks, etc.)
    """
    piece_map = board.piece_map()
    
    turn = board.turn
    
    # todo: encode piece map and turn into vector
