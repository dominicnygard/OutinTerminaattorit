*** Settings ***
Resource  resource.robot
Suite Setup      Open And Configure Browser
Suite Teardown   Close Browser
Test Setup       Reset Citations

*** Test Cases ***
At start there are no citations
    Go To  ${HOME_URL}
    Title Should Be  Reference App
    Page Should Contain  No references added yet

After adding a reference, there is one
    Go To  ${HOME_URL}
    Click Link  xpath=//a[contains(., 'Add New Reference')]
    Click Button  Continue
    Wait Until Element Is Visible  id=title  timeout=5s
    Input Text  id=title  Test article
    Input Text  id=author  Testi Testinen
    Input Text  id=year  2025
    Input Text  id=journal  science
    Click Button  Save reference
    Wait Until Page Contains  articles  timeout=5s

After adding two different types of citations there are two different types
    Go To  ${HOME_URL}
    Click Link  xpath=//a[contains(., 'Add New Reference')]
    Click Button  Continue
    Wait Until Element Is Visible  id=title  timeout=5s
    Input Text  id=title  Test title
    Input Text  id=author  Testi Testinen
    Input Text  id=year  2025
    Input Text  id=journal  science
    Click Button  Save reference
    Wait Until Page Contains  articles  timeout=5s
    Click Link  xpath=//a[contains(., 'Add New Reference')]
    Select Radio Button  reference_type  books
    Click Button  Continue
    Wait Until Element Is Visible  id=title  timeout=5s
    Input Text  id=title  Test title
    Input Text  id=author  Testi Testinen
    Input Text  id=year  2025
    Input Text  id=publisher  pub
    Input Text  id=address  add
    Click Button  Save reference
    Wait Until Page Contains  books  timeout=5s
    Page Should Contain  articles
    Page Should Contain  books

When searching for reference with right title there is a search result
    Go To  ${HOME_URL}
    Click Link  xpath=//a[contains(., 'Add New Reference')]
    Click Button  Continue
    Wait Until Element Is Visible  id=title  timeout=5s
    Input Text  id=title  Test article
    Input Text  id=author  Testi Testinen
    Input Text  id=year  2025
    Input Text  id=journal  science
    Click Button  Save reference
    Wait Until Page Contains  Test article  timeout=5s
    Input Text  id=query  Test article
    Click Button  xpath=//button[contains(., 'Search')]
    Page Should Contain  Test article

When searching for reference with wrong title there is a message
    Go To  ${HOME_URL}
    Input Text  id=query  wrong query
    Click Button  xpath=//button[contains(., 'Search')]
    Page Should Contain  No results matched the search query

Clicking a citation opens detail view and bibtex
    Go To  ${HOME_URL}
    Click Link  xpath=//a[contains(., 'Add New Reference')]
    Click Button  Continue
    Wait Until Element Is Visible  id=title  timeout=5s
    Input Text  id=title  Article
    Input Text  id=author  Author
    Input Text  id=year  2024
    Input Text  id=journal  Journal
    Click Button  Save reference
    Wait Until Element Is Visible  xpath=//a[contains(@class,'citation-card-link')]  timeout=5s
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

