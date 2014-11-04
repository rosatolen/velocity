Feature: Rewards

  Background:
    Given I reset my user
    Given I register as the user "Athena"
    When I try to login as "Athena"

  Scenario: Rewards are remembered by the system
    When I save a reward called "A kiss from my girlfriend" with a cost of 100 Bad Ass Points
    When I save a reward called "Go to London" with a cost of 2000 Bad Ass Points
    Then I should be able to view all rewards

  Scenario: Rewards cannot be entered without a name
    When I save a reward with an empty name
    Then I should get an input error message that says "Required"

  Scenario: New Reward cost can only be entered with a number
    When I add a reward with "blah" as the cost
    Then I should get an input error message that says "Must be an integer"

  Scenario: New rewards with the name of an existing reward cannot be added
    Given I have a reward called "A kiss from my girlfriend" with a cost of 100 Bad Ass Points
    When I save a reward called "A kiss from my girlfriend" with a cost of 100 Bad Ass Points
    Then I should only see one reward called "A kiss from my girlfriend" with a cost of 100
    And I should get an input error message that says "Reward already exists"

  Scenario: You can buy rewards with bad ass points
    Given I create a watermelon task called "Finish the book DNS and BIND"
    When I complete the watermelon task called "Finish the book DNS and BIND"
    Given I have a reward called "A kiss from my girlfriend" with a cost of 10 Bad Ass Points
    When I purchase the reward
    Given I have a reward called "A kiss from my girlfriend" with a cost of 10 Bad Ass Points
    When I purchase the reward
    Then I should not see the reward "A kiss from my girlfriend" with a cost 10 listed
    And I should have 1 Bad Ass Points

  Scenario: You can not buy rewards that you cannot afford
    Given I have a reward called "A kiss from my girlfriend" with a cost of 100 Bad Ass Points
    When I purchase the reward
    Then I should be able to view all rewards
    And I should get an upper level error message that says "Not enough points"
