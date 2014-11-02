Feature: Basic login functionality

  Scenario: Registration
    Given I register as the user "Galatea"
    When I try to login as "Galatea"
    Then I should be able to see my home page
    When I logout
    Then I should be asked to login

  #Scenario: Login
  # Then I should see the error message "This user does not exist"
  #Scneario: bad registration form (see password, retype password must be the same)
  #Scenario: bad login form
  #Scenario: logout should clear data and you must log in again
