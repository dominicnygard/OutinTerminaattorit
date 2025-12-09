*** Settings ***
Resource  resource.robot
Suite Setup      Open And Configure Browser
Suite Teardown   Close Browser
Test Setup       Reset Citations

*** Test Cases ***
At start there are no citations
    Go To  ${HOME_URL}
    Title Should Be  Citation App
    Page Should Contain  No citations added

After adding a reference, there is one
    Go To  ${HOME_URL}
    Click Link  xpath=//a[contains(., 'Add New Citation')]
    Click Button  Continue
    Input Text  title  Test article
    Input Text  author  Testi Testinen
    Input Text  year  2025
    Input Text  journal  science
    Click Button  Save reference
    Page Should Contain  articles

After adding two different types of citations there are two different types
    Go To  ${HOME_URL}
    Click Link  xpath=//a[contains(., 'Add New Citation')]
    Click Button  Continue
    Input Text  title  Test title
    Input Text  author  Testi Testinen
    Input Text  year  2025
    Input Text  journal  science
    Click Button  Save reference
    Click Link  xpath=//a[contains(., 'Add New Citation')]
    Select Radio Button  reference_type  books
    Click Button  Continue
    Input Text  title  Test title
    Input Text  author  Testi Testinen
    Input Text  year  2025
    Input Text  publisher  pub
    Input Text  address  add
    Click Button  Save reference
    Page Should Contain  articles
    Page Should Contain  books



When searching for reference with right title there is a search result
    Go To  ${HOME_URL}
    Click Link  xpath=//a[contains(., 'Add New Citation')]
    Click Button  Continue
    Input Text  title  Test article
    Input Text  author  Testi Testinen
    Input Text  year  2025
    Input Text  journal  science
    Click Button  Save reference
    Input Text  name=query  Test article
    Click Button  Search
    Page Should Contain  Test article

When searching for reference with wrong title there is a message
    Go To  ${HOME_URL}
    Input Text  name=query  wrong query
    Click Button  Search
    Page Should Contain  No results matched the search query


Clicking a citation opens detail view and bibtex
    Go To  ${HOME_URL}
    Click Link  xpath=//a[contains(., 'Add New Citation')]
    Click Button  Continue
    Input Text  title  Article
    Input Text  author  Author
    Input Text  year  2024
    Input Text  journal  Journal
    Click Button  Save reference
    Click Link  xpath=//a[contains(@class,'citation-card-link') and contains(., 'Article')]
    Page Should Contain  Article
    Page Should Contain  Author
    Page Should Contain  Journal
    Page Should Contain  @article{
    Page Should Contain  author = {Author}
    Page Should Contain  journal = {Journal}

Christmas mode can be toggled
    Go To  ${HOME_URL}
    Execute Javascript  window.localStorage.setItem('theme', 'light'); return null;
    Reload Page
    Body Should Have Class  light
    Click Button  id=theme-button
    Wait Until Keyword Succeeds  3x  1s  Body Should Have Class  christmas
    Click Button  id=theme-button
    Wait Until Keyword Succeeds  3x  1s  Body Should Have Class  light

*** Keywords ***
Body Should Have Class
    [Arguments]  ${expected}
    ${classes}=  Get Element Attribute  //body  class
    Should Contain  ${classes}  ${expected}

