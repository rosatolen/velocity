Feature: Bad Ass Points

  Scenario: When a task is completed, you can see the Bad Ass Points increase
    Given I create a quail task called "Finish the book DNS and BIND"
    When I complete the snail task called "Do expenses for October"
    Then I should see my bad ass points increase to 10