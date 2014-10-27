Feature: Rewards

  Scenario: Rewards are remembered by the system
    When I save a reward called "A kiss from my girlfriend" with a cost of 100 Tokens
    When I save a reward called "Go to London" with a cost of 2000 Tokens
    Then I should be able to view all rewards
