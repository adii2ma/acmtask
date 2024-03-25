import requests
import subprocess
import time

# Define website to ping and login URL
PING_WEBSITE = "www.google.com"
LOGIN_URL = "https://phc.prontonetworks.com/cgi-bin/authlogin?URI=http://captive.apple.com/hotspot-detect.html"
CONFIG_FILE = "config.txt"

def read_credentials():
    """Reads username and password from config file."""
    with open(CONFIG_FILE, "r") as file:
        user_id = file.readline().strip()
        password = file.readline().strip()
    return user_id, password

def ping_website(website):
    """Checks if the website can be pinged."""
    try:
        subprocess.check_output(['ping', '-q', '-c', '1', website], stderr=subprocess.STDOUT)
        return True
    except subprocess.CalledProcessError:
        return False

def login_to_portal(user_id, password):
    """Logs in to the captive portal."""
    payload = {
        "userId": user_id,
        "password": password,
        "serviceName": "ProntoAuthentication",
        "Submit22": "Login"
    }
    try:
        response = requests.post(LOGIN_URL, data=payload, verify=False)
        response.raise_for_status()
        if response.ok:
            print("Successfully logged in to captive portal.")
        else:
            print("Login failed with status code:", response.status_code)
    except requests.exceptions.RequestException as e:
        print("Error logging in to captive portal:", e)

def main():
    user_id, password = read_credentials()
    while True:
        if ping_website(PING_WEBSITE):
            time.sleep(10)
        else:
            login_to_portal(user_id, password)
            time.sleep(5)

if _name_ == "_main_":
    main()
