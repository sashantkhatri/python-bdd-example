@regression
Feature: Login To Flight Reservation System

  @sanity
  Scenario: Verify user is able to login
    Given User has navigated to login page
    When User enters username as mercury and password as mercury to login
    Then User should be on flight finder page

  Scenario Outline: Verify login with valid and invalid credential
    Given User has navigated to login page
    When User enters username as <username> and password as <password> to login
    Then User should be on flight finder page If entered credentials are <is_valid>

    Examples:
    | username | password | is_valid |
    | mercury | mercury | True |
    | mercury | password | False |
    | username | mercury | True |
