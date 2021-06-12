Feature: Flipkart dashboard and filters
  Testing multiple scenarios related to flipkart.

  Scenario: Search for any item within flipkart website
    Given User navigates to flipkart homepage
    When User is in home page
    And User searches for Women's Shoes
    Then User verifies all the items related to the search is displayed as result

  Scenario: Applying filters on search results
    Given User navigates to flipkart homepage
    When User is in home page
    And User searches for Men's Shoes
    Then User verifies all the items related to the search is displayed as result
    And User applies filter to sort out the result
    Then User verifies all the items related to the filter is displayed as result

  Scenario: To verify user is able to choose size and buy the product
    Given User navigates to flipkart homepage
    When User is in home page
    And User searches for Shoes
    Then User verifies all the items related to the search is displayed as result
    And User select any item and choose any available size
    Then User clicks on buy now option and is navigated to login page
