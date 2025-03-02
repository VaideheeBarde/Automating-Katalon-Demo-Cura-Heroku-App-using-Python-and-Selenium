Feature: Appointment Booking

  @validCredentials @appointment
  Scenario Outline: Book an appointment with test data from Excel
    Given the user from row <row_index> is logged in
    When the user selects facility from row <row_index>
    And clicks Apply for hospital readmission for condition from row <row_index>
    And chooses healthcare program from row <row_index>
    And selects the visit date from row <row_index>
    And adds a comment from row <row_index>
    And clicks the Book Appointment button
    Then the user should see the appointment confirmation for row <row_index>

    Examples:
      |row_index|
      |    0    |
      |    1    |