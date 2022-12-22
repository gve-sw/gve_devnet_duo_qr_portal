# Copyright (c) 2022 Cisco and/or its affiliates.
#
# This software is licensed to you under the terms of the Cisco Sample
# Code License, Version 1.1 (the "License"). You may obtain a copy of the
# License at
#
#                https://developer.cisco.com/docs/licenses
#
# All use of the material herein must be in accordance with the terms of
# the License. All rights not expressly granted by the License are
# reserved. Unless required by applicable law or agreed to separately in
# writing, software distributed under the License is distributed on an "AS
# IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express
# or implied.


from flask import Flask, render_template, request, url_for, redirect
import duo_client
import json

app = Flask(__name__)

# DUO Related Variables - AUTH VARIABLES REQUIRED - FROM DUO PORTAL GO TO APPLICATIONS - AUTH API
duo_integration_key = ""
duo_secret_key = ""
duo_api_host = ""

# Initialize the duo API client
# admin_api = duo_client.Admin(ikey=duo_integration_key, skey=duo_secret_key, host=duo_api_host)
auth_api = duo_client.Auth(ikey=duo_integration_key, skey=duo_secret_key, host=duo_api_host)
if auth_api is not None:
    print(auth_api)
    print('Valid Authentication with DUO')
else:
    print('Not authenticated with DUO, verify credentials')

@app.route('/', methods=["GET", "POST"])
def registration_form():  # put application's code here
    if request.method == "POST":
        print('Enters POST')
        # Values obtained from the WEB Form
        name = request.form['name']
        user_name = request.form['username']
        print('Getting Values from the form')
        print(name)
        print(user_name)

        # Request the DUO API Enroll
        print('Sending POST request to DUO - enroll new user')
        enroll_new_user_request = auth_api.api_call(method='POST', path='/auth/v2/enroll',params={'username': f'{user_name}'})
        enroll_new_user = json.loads(enroll_new_user_request[1])

        # Enters new IF for returned successful/unsuccessful api call
        if enroll_new_user['stat'] == 'OK':
            # print(enroll_new_user['response'])
            print(enroll_new_user['response']['activation_barcode'])
            print(enroll_new_user['response']['activation_code'])
            print(enroll_new_user['response']['activation_url'])
            print(enroll_new_user['response']['expiration'])
            print(enroll_new_user['response']['user_id'])
            print(enroll_new_user['response']['username'])
            activation_barcode = enroll_new_user['response']['activation_barcode']
            activation_code = enroll_new_user['response']['activation_code']
            activation_url = enroll_new_user['response']['activation_url']
            expiration = enroll_new_user['response']['expiration']
            user_id = enroll_new_user['response']['user_id']
            username = enroll_new_user['response']['username']
            return render_template('successful.html', name=name, url=activation_barcode, username = username)
        else:
            # Unsuccessful Response
            # Code 40002 - username already exists
            # Code 40102 - Invalid integration key in request credentials - integration key
            # Code 40103 - Invalid signature in request credentials - secret key
            print(enroll_new_user['code'])  # 40002 - username already exists
            print(enroll_new_user['message'])
            print(enroll_new_user['message_detail'])
            code = enroll_new_user['code']
            if code == 40002:
                print('username already exists')
            elif code == 40102:
                print('Invalid integration key in request credentials - integration key')
            elif code == 40103:
                print('Invalid signature in request credentials - secret key')
            else:
                print('Error not determined, verify credentials')
            message = enroll_new_user['message']
            message_detail = enroll_new_user['message_detail']
            return render_template('unsuccessful.html', code=str(code), message=message, message_detail=message_detail)

    else:
        print('Enters GET')
        return render_template('form.html')


if __name__ == '__main__':
    app.run(port=8080)
