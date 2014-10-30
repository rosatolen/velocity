Feature: Bad Ass Points

  Scenario: When a task is completed, you can see the Bad Ass Points increase
    Given I create a quail task called "Finish the book DNS and BIND"
    When I complete the quail task called "Finish the book DNS and BIND"
    Then I should see my bad ass points increase to 8
