Feature: Rewards

Scenario: Rewards are remembered by the system
When I save a reward called "A kiss from my girlfriend" with a price of 100 Tokens
Then I should be able to list it
