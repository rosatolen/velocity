Feature: Bad Ass Points

  Background:
    Given I register as the user "Athena"
    When I try to login as "Athena"

  Scenario: When a task is completed, you can see the Bad Ass Points increase
    Given I create a quail task called "Row 5k"
    When I complete the quail task called "Row 5k"
    Then I should see my total bad ass points increase to 8

  Scenario: I can see how many points I compelted today
    Given I create a quail task called "Row 5k"
    When I complete the quail task called "Row 5k"
    Then I should see today's bad ass points increase to 8
    Then I should see my total bad ass points increase to 8
