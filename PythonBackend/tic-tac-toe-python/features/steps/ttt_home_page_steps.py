
# Scenario 1
@given('The user is on the log in page')
def user_gets_to_login_page(context):

@when('The user inputs their username')
def user_logs_in():

@then('The user should be on the main game page')
def log_in_successful():

# -------------------------------------------------------------------------------------------------------

# Scenario 2
# @given('The user is on the log in page')
# def user_gets_to_login_page():

@when('The user inputs their username incorrectly')
def user_does_not_log_in():

@then('The user should be on the log in page')
def log_in_fails():