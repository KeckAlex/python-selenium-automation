Feature: Tests for sign in page

  @smoke
  Scenario: User can open and close Terms and Conditions from sign in page
   Given Open sign in page
   And Store original window
   When Click Target terms and conditions link
   And Switch to new window
   Then Verify Terms and Conditions page opened
   And Close current page
   And Return to original window


 Scenario: User cannot login with incorrect email and password combination
   Given Open sign in page
   Then Verify sign in form opened
   And Enter email address
   And Enter password
   Then Click login button
   Then Verify “We cannot find your account.” message is shown