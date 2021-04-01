class Move:
    
    def __init__(self, piece, s_col, s_row, t_col, t_row, taken_piece):
        self.piece = piece
        self.start_pos = (s_row, s_col)
        self.end_pos = (t_row, t_col)
        self.taken_piece = taken_piece