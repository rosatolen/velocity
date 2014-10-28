Feature: Task

  Scenario: Tasks are remembered by the system
    When I create a snail task called "Do expenses for October"
    Then I should be able to view all tasks

  Scenario: Snail Tasks and Quail Tasks can be completed
    Given I create a snail task called "Do expenses for October"
    Given I create a quail task called "Finish the book DNS and BIND"
    When I complete the snail task called "Do expenses for October"
    Then I should have 1 more bad ass point in my bad ass points purse
    Then the snail task "Do expenses for October" should be deleted
    When I complete the quail task called "Finish the book DNS and BIND"
    Then the quail task "Finish the book DNS and BIND" should be deleted
    And I should have 10 more bad ass points in my bad ass points purse

  Scenario: I should not be able to make tasks with names that already exist
    Given I create a snail task called "Do expenses for October"
    Given I create a snail task called "Do expenses for October"
    Then I should only see one snail task called "Do expenses for October"
    And I should get an error message that says "Task already exists"
