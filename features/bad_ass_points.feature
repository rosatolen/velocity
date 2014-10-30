Feature: Bad Ass Points

  Scenario: When a task is completed, you can see the Bad Ass Points increase
    Given I create a quail task called "Row 5k"
    When I complete the quail task called "Row 5k"
    Then I should see my bad ass points increase to 8
