Feature: Target main page tests

  Scenario: Verify that user can navigate to Sign In
    Given Open target main page
    When Click Sign In
    When From right side navigation menu click Sign In
    Then Verify Sign In form opened


 Scenario: Benefit cells on the Target Circle page
    Given Open target circle page
    Then Verify target circle page has 14 benefit cells
