Feature: Login to Cura Healthcare Service

  @validCredentials
  Scenario Outline: Login with test data from Excel
    Given the user is on login page
    When the user enters credentials from row <row_index>
    And clicks the login button
    Then the user should see the result from row <row_index>

    Examples:
      |row_index|
      |    0    |
      |    1    |

  @invalidCredentials
  Scenario Outline: Login with test data from Excel
    Given the user is on login page
    When the user enters credentials from row <row_index>
    And clicks the login button
    Then the user should see the result from row <row_index>

    Examples:
      |row_index|
      |    2    |
      |    3    |