*** Settings ***
Resource  resource.robot
Suite Setup      Open And Configure Browser
Suite Teardown   Close Browser
Test Setup       Reset Citations

*** Test Cases ***
At start there are no citations
    Go To  ${HOME_URL}
    Title Should Be  Citation app
    Page Should Contain  No citations added

After adding a reference, there is one
    Go To  ${HOME_URL}
    Click Link  Create new citation
    Click Button  Submit
    Input Text  title  Test article
    Input Text  author  Testi Testinen
    Input Text  year  2025
    Click Button  Save
    Page Should Contain  articles

After adding two different types of citations there are two different types
    Go To  ${HOME_URL}
    Click Link  Create new citation
    Click Button  Submit
    Input Text  title  Test title
    Input Text  author  Testi Testinen
    Input Text  year  2025
    Click Button  Save
    Click Link  Create new citation
    Click Button  books
    Click Button  Submit
    Input Text  title  Test title
    Input Text  author  Testi Testinen
    Input Text  year  2025
    Click Button  Save
    Page Should Contain  articles
    Page Should Contain  books
