Feature: Target search tests
#
#  Scenario: User can search for a product on Target
#    Given Open Target main page
#    When Search for coffee
#    Then Verify search results shown for coffee
#    And Verify search results URL opens for coffee
#
# Scenario Outline: User can search for a product on Target
#    Given Open Target main page
#    When Search for <product>
#    Then Verify search results shown for <expected_results>
#    And Verify search results URL opens for <expected_results>
#    Examples:
#      |product     |expected_results     |
#      |coffee      |coffee               |
#      |iphone      |iphone               |
#      |mug         |mug                  |


 Scenario: User can add a product to cart
    Given Open Target main page
    When Search for persil
    And Click on Add to Cart button
    And Store product name
    And Confirm Add to Cart button from side navigation
    And Open cart page
    Then Verify that cart has 1 item(s)
    And Verify cart has correct product

