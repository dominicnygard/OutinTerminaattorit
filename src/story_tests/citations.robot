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
    Input Text  journal  science
    Click Button  Save
    Page Should Contain  articles

After adding two different types of citations there are two different types
    Go To  ${HOME_URL}
    Click Link  Create new citation
    Click Button  Submit
    Input Text  title  Test title
    Input Text  author  Testi Testinen
    Input Text  year  2025
    Input Text  journal  science
    Click Button  Save
    Click Link  Create new citation
    Select Radio Button  reference_type  books
    Click Button  Submit
    Input Text  title  Test title
    Input Text  author  Testi Testinen
    Input Text  year  2025
    Input Text  publisher  pub
    Input Text  address  add
    Click Button  Save
    Page Should Contain  articles
    Page Should Contain  books

When searching for reference with right title there is a search result
    Go To  ${HOME_URL}
    Click Link  Create new citation
    Click Button  Submit
    Input Text  title  Test article
    Input Text  author  Testi Testinen
    Input Text  year  2025
    Input Text  journal  science
    Click Button  Save
    Click Link  Search
    Input Text  query  Test article
    Click Button  Search
    Page Should Contain  Test article

When searching for reference with wrong title there is a message
    Go To  ${HOME_URL}
    Click Link  Search
    Input Text  query  wrong query
    Click Button  Search
    Page Should Contain  No results matched the search query

Downloading BibTeX file contains reference data
    Go To  ${HOME_URL}
    Click Link  Create new citation
    Click Button  Submit
    Input Text  title  BibTeX Article
    Input Text  author  Testi Testinen
    Input Text  year  1999
    Input Text  journal  Nature
    Click Button  Save
    Run Keyword And Ignore Error  Remove File  ${DOWNLOAD_DIR}/references.bib
    Empty Directory  ${DOWNLOAD_DIR}
    Click Button  Download references
    ${downloaded_file}=  Wait Until Keyword Succeeds  10x  1s  Wait For Downloaded File
    Move File  ${downloaded_file}  ${DOWNLOAD_DIR}/references.bib
    ${file_content}=  Get File  ${DOWNLOAD_DIR}/references.bib
    Should Contain  ${file_content}  @article
    Should Contain  ${file_content}  title = {BibTeX Article}
    Should Contain  ${file_content}  author = {Testi Testinen}
    Should Contain  ${file_content}  year = {1999}
    Should Contain  ${file_content}  journal = {Nature}

