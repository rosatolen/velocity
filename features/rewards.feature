Feature: Rewards

  Scenario: Rewards are remembered by the system
    When I save a reward called "A kiss from my girlfriend" with a cost of 100 Bad Ass Points
    When I save a reward called "Go to London" with a cost of 2000 Bad Ass Points
    Then I should be able to view all rewards

  Scenario: Rewards cannot be entered without a name
    When I save a reward with an empty name
    Then I should get an error message that says "Required"

  Scenario: New rewards with the name of an existing reward cannot be added
    Given I have a reward called "A kiss from my girlfriend" with a cost of 100 Bad Ass Points
    When I save a reward called "A kiss from my girlfriend" with a cost of 100 Bad Ass Points
    Then I should only see one reward called "A kiss from my girlfriend"
    And I should get an error message that says "Reward already exists"

  Scenario: You can buy rewards with bad ass points
    Given I have a reward called "A kiss from my girlfriend" with a cost of 100 Bad Ass Points
    And I have 100 Bad Ass Points
    When I purchase the reward
    Then I should not see the reward "A kiss from my girlfriend" listed
    And I should have 0 Bad Ass Points
