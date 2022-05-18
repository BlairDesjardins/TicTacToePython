Feature: Website lets you log in

  Scenario: Log in works
    Given The user is on the log in page
    When The user inputs their username
    And The user inputs their password
    And The user presses log in
    Then The user should be on the main game page

  Scenario: Log in fails
    Given The user is on the log in page
    When The user inputs their username incorrectly
    And The user inputs their password incorrectly
    And The user presses log in
    Then The user should be on the log in page