import pyglet


def handle_first_click(x, y, button, modifiers, board):  # handles a first click on the board
    board.deselect()
    rel_x, rel_y = board.get_rel_xy(x, y)
    board.get_square(rel_x, rel_y).select()


def handle_second_click(x, y, button, modifiers, board, game_state):  # handles a second click on the board
    selected_square = board.get_selected_square()  # previously selected square
    rel_x, rel_y = board.get_rel_xy(x, y)
    clicked_square = board.get_square(rel_x, rel_y)  # newly selected square

    if selected_square.equals(clicked_square):  # clicked on the same square
        pass
    elif game_state.square_is_empty(selected_square):  # clicked on an empty square
        handle_first_click(x, y, button, modifiers, board)
    elif game_state.is_valid_move(clicked_square, selected_square):  # allowed to move
        game_state.move(clicked_square, selected_square)
        piece = board.get_piece(selected_square)
        piece.move_to(rel_x, rel_y)
        board.deselect()
    else:  # selecting a new piece
        handle_first_click(x, y, button, modifiers, board)


def on_board(x, y, board):  # returns true iff the click was on the board
    return board.padding < x < board.size + board.padding and board.padding < y < board.size + board.padding


def on_button(x, y):  # returns true iff the click was on a button
    pass


def handle_button(x, y, button, modifiers):  # handles a click if it was on a button
    pass


def handle_empty_click(x, y, button, modifiers, board):  # handles a click on nothing
    board.deselect()


def handle_cursor_type(x, y, board, window):  # changes the cursor type depending on the location
    if on_board(x, y, board) or on_button(x, y):
        cursor = window.get_system_mouse_cursor(window.CURSOR_HAND)
        window.set_mouse_cursor(cursor)
    else:
        cursor = window.get_system_mouse_cursor(window.CURSOR_DEFAULT)
        window.set_mouse_cursor(cursor)


def handle_button_hover(x, y):  # changes the color of the button when going over it with the cursor
    pass
