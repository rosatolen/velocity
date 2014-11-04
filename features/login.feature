Feature: Basic login functionality

  Background:
    Given I reset my user

  Scenario: Accessing the home page
    When I try to access the home page
    Then I should be asked to login

  Scenario: Registration
    Given I register as the user "Galatea"
    When I try to login as "Galatea"
    Then I should be able to see my home page
    When I logout
    Then I should be asked to login

  Scenario: Login as an unknown user
    When I try to login as "Jessica"
    Then I should get an upper level error message that says "Invalid Username or Password"
    Then I should be able to register

  Scenario: Login as an known user with a bad password
    Given I register as the user "Jessica"
    When I try to login as "Jessica" with a bad password
    Then I should get an upper level error message that says "Invalid Username or Password"

  Scenario: Bad username to login form
    When I leave the username on the login form blank
    Then I should get an input error message that says "Required"

  Scenario: Bad password to login form
    When I leave the password on the login form blank
    Then I should get an input error message that says "Required"

  Scenario: Blank input to registration form
    Given I navigate to the registration page
    When I register with a blank username
    Then I should get an input error message that says "Required"

  Scenario: Registration Passwords are not the same
    Given I navigate to the registration page
    When I register with mismatching passwords
    Then I should get an upper level error message that says "Passwords do not match"

  Scenario: Link each user with their own data
    Given I register as the user "Galatea"
    Given I register as the user "Sannidhi"
    When I try to login as "Galatea"
    When I save a reward called "A kiss from my girlfriend" with a cost of 100 Bad Ass Points
    Then I should be able to view all rewards
    When I logout
    When I try to login as "Sannidhi"
    Then I should not see the reward "A kiss from my girlfriend" with a cost 100 listed
    When I save a reward called "Trip to London" with a cost of 300 Bad Ass Points
    When I logout
    When I try to login as "Galatea"
    Then I should only see one reward called "A kiss from my girlfriend" with a cost of 100

  #Scenario: Check login is threadsafe on another browser
  #Scenario: Should not be able to register a second user with the same username as an existing one
