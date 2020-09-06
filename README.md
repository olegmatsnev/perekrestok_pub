This script is meant to be executed from the command line. 

It checks perekrestok.ru, an online supermarket, for available delivery slots. If such slots are available, it prints when's the next one to the command line, 
otherwise tells you so.

Before using the script, one has to create an account at perekrestok.ru.

The script uses Python keyring library (https://pypi.org/project/keyring/) to securely store credentials, so you'll need to add you login-password pair to the keyring 
and replace "email@address" with the address used to sign up to perekrestok.ru.
