Feature: Task

Scenario: Tasks are remembered by the system
  When I create a snail task called "Do expenses for October"
  When I create a quail task called "Finish the book DNS and BIND"
  Then I should be able to view all tasks

Scenario: Tasks can be completed
  Given I create a snail task called "Do expenses for October"
  When I complete the snail task called "Do expenses for October"
  Then the snail task "Do expenses for October" should be deleted
