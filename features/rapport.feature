Feature: Rapport

  Scenario: When a task is completed, you can see the Rapport Points increase
    Given I create a quail task called "Finish the book DNS and BIND"
    When I complete the snail task called "Do expenses for October"
    Then I should see my rapport increase to 10