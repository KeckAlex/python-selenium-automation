Feature: Target shopping card test

  Scenario: Verify “Your cart is empty” message is shown
    Given Open target main page
    When Click on Cart icon
    Then Verify “Your cart is empty” message is shown

  Scenario: Verify that user can navigate to Sign In
    Given Open target main page
    When Click Sign In
    When From right side navigation menu click Sign In
    Then Verify Sign In form opened
