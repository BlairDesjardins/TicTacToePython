Feature: User can play the game

  Scenario: The user starts game
    Given The user is on the main game page
    When The user presses new game
    And The user inputs the username of another player
    And The user presses send invite
    Then The invite was sent

  Scenario: The user joins a game after being invited
    Given The user is on the main game page
    And The user has been invited to a game
    When The user presses accept
    Then The game starts

  Scenario: The user can place a shape when it's their turn
    Given The user is on the main game page
    And The user is playing a game
    And It is the user's turn to make a move
    When The user selects an empty cell
    Then The shape is placed and their turn ends

  Scenario: The user wins the game
    Given The user is on the main game page
    And The user is playing a game
    When The user makes 3 in a row
    Then The user wins the game

  Scenario: The user loses the game
    Given The user is on the main game page
    And The user is playing a game
    When The opponent makes 3 in a row
    Then The user loses the game

  Scenario: The user draws the game
    Given The user is on the main game page
    And The user is playing a game
    When Neither player makes 3 in a row and every cell is occupied
    Then The user draws the game

  Scenario: The user can request a rematch
    Given The user is on the main game page
    And The game has finished
    When The user presses rematch
    Then The invite was sent

  Scenario: The user can forfeit a match
    Given The user is on the main game page
    And The user is playing a game
    When The user press forfeit
    Then The user loses the game