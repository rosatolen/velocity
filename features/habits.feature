Feature: Habits

  Background:
    Given I register as the user "Athena"
    When I try to login as "Athena"

  Scenario: I am given points for completing positive habits
    Given I create a habit called "Row 5k" with no theme
    When I complete the habit
    Then I should see today's bad ass points increase to 1
    Then I should see my total bad ass points increase to 1
