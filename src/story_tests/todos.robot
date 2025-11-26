*** Settings ***
Resource  resource.robot
Suite Setup      Open And Configure Browser
Suite Teardown   Close Browser
Test Setup       Reset Todos

*** Test Cases ***
At start there are no citations
    Go To  ${HOME_URL}
    Title Should Be  Citation app
    Page Should Contain  No citations added

After adding a citation, there is one
    Go To  ${HOME_URL}
    Click Link  Lisää artikkeli
    Input Text  title  science
    Input Text  author  jerry
    Input Number  year  1999
    Click Button  Save
    Page Should Contain  article: science 1999, jerry

After adding two todos and marking one done, there is one unfinished
    Go To  ${HOME_URL}
    Click Link  Create new todo
    Input Text  content  Buy milk
    Click Button  Create
    Click Link  Create new todo
    Input Text  content  Clean house
    Click Button  Create
    Click Button  //li[div[contains(text(), 'Buy milk')]]/form/button
    Page Should Contain  things still unfinished: 1
    Page Should Contain  Buy milk, done

