*** Settings ***
Library     SeleniumLibrary

*** Variables ***
${url}      https://www.amazon.com/ap/signin?openid.pape.max_auth_age=0&openid.return_to=https%3A%2F%2Fwww.amazon.com%2F%3F_encoding%3DUTF8%26ref_%3Dnav_em_hd_re_signin&openid.identity=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0%2Fidentifier_select&openid.assoc_handle=usflex&openid.mode=checkid_setup&openid.claimed_id=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0%2Fidentifier_select&openid.ns=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0&&ref_%3Dnav_em_hd_clc_signin_0_1_1_39
${email_id_field}       id.ap_email
${continue_btn}         //*[@id="continue" and @type="submit" ]
${password_field}       //*[@id="ap_password"]
${sign_in_btn}          //*[@id="signInSubmit"]

*** Keywords ***
Open the Browser and login to Amazon
    Go to       {url}
    Wait Until Element Is Visible       ${email_id_field}       10s
    Input Text      ${email_id_field}       8806427040
    Wait Until Element Is Enabled       ${continue_btn}     10s
    Click Element       ${continue_btn}
    Wait Until Element Is Visible       ${password_field}       10s
    Input Text      {password_field}        Vinod@123
    Wait Until Element Is Enabled    ${sign_in_btn}
    Click Element    ${sign_in_btn}

*** Test Cases ***
Task1
    Open the Browser and login to Amazon
