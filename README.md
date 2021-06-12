# **Locus.sh - SDET assignment**
## Web automation on flipkart website using PyTest framework

The Test Automation Framework is created for automating the following test cases - searching for a product, applying filters on search results and buying any one item from the list.

### Scripting Language

Python is used as the scripting language. 
Selenium Webdriver is used to perform browser automation. The front end automation is achieved by implementing pytest test cases using webdriver based automation.

### Folder Structure

The Test Automation Suite is having below folders.

- **Features** : Feature files have been created based on each feature which is under test. The different scenarios and corresponding steps in each test case that is linked to the particular feature have been listed in the same feature file.
- **Source** : Source folder has been used to list the modules used to implement the source files for corresponding feature files steps. Emphasis has been kept to reuse the codes wherever possible using file level methods.
- **Pages** : This folder has been used to save the locators for each page in case of Front End Automation. Each file corresponds to each page in the UI and contains classes which groups the locators in each subsection or action.
- **Drivers** : Folder used to save driver details, used to link selenium to the corresponding browser driver.


### conftest.py file

The conftest file houses all the common functions and common steps which are used inside the source folder. The teardown for the framework is implemented here.

### Creation of a test case

The following steps briefly describe how a new test case can be added to the framework.

1. Create a feature file, if required. Add the scenario and steps in the .feature file in Gherkin format.
2. Map the required page locators to the corresponding page class in the Pages folder. Do create a new page file in .py format if required.
3. Add the test cases scripts in the corresponding file in the Source folder. Do create a new script file if required. The steps and classes which are already implemented may be reused to reduce duplicate scripting.


### Project description

1. Search - open www.flipkart.com (it would show a popup), perform a search for term 'shoes'. 

2. Apply Filters - Choose two filters - eg - price & brand. Ensure the filters are selected. 

3. Product Detail Page - Open the detail page of the first result, select the size of the item & then click 'buy now'.

### Steps to run the project/scenarios

To Run pytest from terminal:

1. $ pytest -m <mark name> 
To run a set of test cases that is tagged with a specific tag eg: @pytest.mark.search

2. $ pytest <testfilename.py>
To run a single test file 

3. $ pytest
To run all the test files/scenarios in the project



