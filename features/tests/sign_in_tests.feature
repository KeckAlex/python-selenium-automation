Feature: Tests for sign in page

  Scenario: User can open and close Terms and Conditions from sign in page
   Given Open sign in page
   And Store original window
   When Click Target terms and conditions link
   And Switch to new window
   Then Verify Terms and Conditions page opened
   And Close current page
   And Return to original window