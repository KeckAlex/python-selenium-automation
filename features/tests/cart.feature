Feature: Tests for cart functionality

  Scenario: Verify “Your cart is empty” message is shown
    Given Open target main page
    When Click on Cart icon
    Then Verify “Your cart is empty” message is shown