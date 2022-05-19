
# Scenario 1
@given('The user is on the main game page')
def user_gets_to_game_page():

@when('The user presses new game')
def user_invites_opponent():

@then('The invite was sent')
def user_accepts_invite():

# -------------------------------------------------------------------------------------------------------

# Scenario 2
@given('The user is on the main game page')
def user_is_on_game_page():

@when('The user has been invited to a game')
def user_enters_game():

@then('The game starts')
def users_start_game():

# -------------------------------------------------------------------------------------------------------

# Scenario 3
# @given('The user is on the main game page')
# def user_is_on_game_page():

@when('The user is playing a game')
def users_play_game():

@then('The shape is placed and their turn ends')
def users_pick_cells():

# ------------------------------------------------------------------------------------------------------

# Scenario 4
# @given('The user is on the main game page') # A lot of this now?
# def user_is_on_game_page():

@when('The user is playing a game')
def user_gets_three_in_a_row():

@then('The user wins the game')
def user_wins_game():

# ------------------------------------------------------------------------------------------------------

# Scenario 5
# @given('The user is on the main game page')
# def user_is_on_game_page():

@when('The user is playing a game')  # <- Wonder if can combine with above win scenario?
def opponent_gets_three_in_a_row():

@then('The user loses the game')  # Maybe just combine with scenario 4
def user_loses_game():            # seems redundant but oh well

# ------------------------------------------------------------------------------------------------------

# Scenario 6
# @given('The user is on the main game page')
# def user_is_on_game_page():

@when('The user is playing a game')
def neither_user_can_get_three_in_a_row():

@then('The user draws the game')
def game_is_a_draw():

# -------------------------------------------------------------------------------------------------------

# Scenario 7
# @given('The user is on the main game page')
# def user_is_on_game_page():

@when('The game has finished')
def user_wants_a_rematch():

@then('The invite was sent')
def users_choose_to_play_again():

# ------------------------------------------------------------------------------------------------------

# Scenario 8
# @given('The user is on the main game page')
# def user_is_on_game_page():

@when('The user is playing a game')
def user_forfeits_game():

@then('The user loses the game')
def game_ends():

# ------------------------------------------------------------------------------------------------------
