Feature: Logout Functionality

  @validCredentials
  Scenario Outline: Validate logout functionality using test data from Excel
    Given the user from row <row_index> is logged in
    When the user clicks the logout button
    Then the user should be redirected to the login page

    Examples:
      |row_index|
      |    0    |
      |    1    |