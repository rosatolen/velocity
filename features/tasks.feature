Feature: Task

  Background:
    Given I register as the user "Athena"
    When I try to login as "Athena"

    @wip
  Scenario: Tasks are remembered by the system
    When I create a "Finances" themed snail task called "Do expenses for October"
    Then I should be able to view all tasks with their themes

  Scenario: Snail Tasks and Quail Tasks can be completed
    Given I create a snail task called "Do expenses for October"
    Given I create a quail task called "Row 5k"
    When I complete the snail task called "Do expenses for October"
    Then I should have 1 more bad ass points in my bad ass points purse
    Then the snail task "Do expenses for October" should be deleted
    When I complete the quail task called "Row 5k"
    Then the quail task "Row 5k" should be deleted
    And I should have 9 more bad ass points in my bad ass points purse

  Scenario: I should not be able to make a snail task with names that already exist
    Given I create a snail task called "Do expenses for October"
    Given I create a snail task called "Do expenses for October"
    Then I should only see one snail task called "Do expenses for October"
    And I should get an input error message that says "Task already exists"

  Scenario: I should not be able to make a quail task with names that already exist
    Given I create a quail task called "Row 5k"
    Given I create a quail task called "Row 5k"
    Then I should only see one quail task called "Row 5k"
    And I should get an input error message that says "Task already exists"

  Scenario: I should not be able to make a task with names that already exist
    Given I create a quail task called "Row 5k"
    Given I create a snail task called "Row 5k"
    Then I should only see one quail task called "Row 5k"
    And I should get an input error message that says "Task already exists"

  Scenario: I should not be able to add multiple Watermelon tasks
    Given I create a watermelon task called "Finish the book DNS and BIND"
    Given I create a watermelon task called "Finish the book DNS and BIND"
    Then I should only see one watermelon task called "Finish the book DNS and BIND"
    And I should get an input error message that says "Task already exists"

  Scenario: Watermelon tasks
    Given I create a watermelon task called "Finish the book DNS and BIND"
    When I complete the watermelon task called "Finish the book DNS and BIND"
    Then I should see my total bad ass points increase to 55

  Scenario: You can delete a task
    Given I create a watermelon task called "Finish the book DNS and BIND"
    When I delete the task
    Given I create a quail task called "Row 5k"
    When I delete the task
    Then I should not see any tasks
