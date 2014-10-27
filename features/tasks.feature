Feature: Task

  Scenario: Tasks are remembered by the system
    When I create a snail task called "Do expenses for October"
    Then I should be able to view all tasks

  @wip
  Scenario: Snail Tasks and Quail Tasks can be completed
    Given I create a snail task called "Do expenses for October"
    Given I create a quail task called "Finish the book DNS and BIND"
    When I complete the snail task called "Do expenses for October"
    Then I should have 1 more rapport in my rapport purse
    When I complete the quail task called "Finish the book DNS and BIND"
    Then the snail task "Do expenses for October" should be deleted
    Then the quail task "Finish the book DNS and BIND" should be deleted
    #And I should have 5 more rapport in my rapport purse
