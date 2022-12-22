# gve_devnet_duo_qr_portal
Python/Flask sample code that enables an admin portal to generate a QR code with the username as input in a web form.

## Contacts
* Max Acquatella

## Solution Components
* DUO
* Python Flask

## Related Sandbox Environment
This sample code assumes that there is an existing DUO organization with the Auth API token enabled.
For a sandbox environment please go to the following link: https://signup.duo.com/

## Prerequisites
NOTE: This code was tested using MacOS.

### Enable DUO APIs
Enable the Admin and Auth API in the Duo portal: 
1. Select Application
2. Protect an Application
3. Select Admin and Auth APIs

See the following:
![/IMAGES/1image.png](/IMAGES/1image.png)

Once the Admin and Auth APIs are enabled, select the Auth API/Details and select the following credentials needed 
for the app.py script:
1. Integration key
2. Secret key
3. API hostname
Auth API - credentials:
![/IMAGES/2image.png](/IMAGES/2image.png)

## Installation/Configuration
1. Clone this repository with `git clone [repository name]`
2. Add the Duo credentials depending on the API section that is being leveraged that you collected in the Prerequisites 
section to the credentials file. The credentials are assigned in the app.py script.

```python
# DUO Related Variables - AUTH VARIABLES REQUIRED - FROM DUO PORTAL GO TO APPLICATIONS - AUTH API
duo_integration_key = ""
duo_secret_key = ""
duo_api_host = ""
```
3. Set up a Python virtual environment. Make sure Python 3 is installed in your environment, and if not, 
you may download Python [here](https://www.python.org/downloads/). 
4. Once Python 3 is installed in your environment, you can activate the virtual environment with the 
instructions found [here](https://docs.python.org/3/tutorial/venv.html).
5. Install the requirements with `pip3 install -r requirements.txt`

## Usage
To run the code, use the command:
```
$ python app.py
```
In your browser, go to the following address: 

http://127.0.0.1:8080

You should land in the following page: 

![/IMAGES/3image.jpg](/IMAGES/3image.jpg)

Input the name and username of the individual that you want to register.
If the credentials are correct, you will land on a second screen which will display the QR code of the newly registered
user. If the credentials are incorrect, you will land on a screen indicating the type of error reported by the API call. 

NOTE:
This tool will not keep track of the registered users. Error 40002 will report a duplicated username, and this is a 
feature of the DUO portal. 

# Screenshots

![/IMAGES/0image.png](/IMAGES/0image.png)

### LICENSE

Provided under Cisco Sample Code License, for details see [LICENSE](LICENSE.md)

### CODE_OF_CONDUCT

Our code of conduct is available [here](CODE_OF_CONDUCT.md)

### CONTRIBUTING

See our contributing guidelines [here](CONTRIBUTING.md)

#### DISCLAIMER:
<b>Please note:</b> This script is meant for demo purposes only. All tools/ scripts in this repo are released for use "AS IS" without any warranties of any kind, including, but not limited to their installation, use, or performance. Any use of these scripts and tools is at your own risk. There is no guarantee that they have been through thorough testing in a comparable environment and we are not responsible for any damage or data loss incurred with their use.
You are responsible for reviewing and testing any scripts you run thoroughly before use in any non-testing environment.