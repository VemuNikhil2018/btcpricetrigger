The program doesn't need any installation. A simple python IDE suffices.
Please copy-paste the code into a python IDE, online or offline and run it.
An online compiler works better, as the program needs to connect to the internet for almost every operation.
It first outputs the current price of Bitcoin and asks if you'd like to set an alert.
If you say no, skip to point 17.
If you say yes, it asks for:
  your desired price,
  the number of users,
  all their emails one by one.
After every email is entered, it verifies for:
  the regex,
  the existance of the email (using Real Email API), (This could even verify the regex, but I thought regex is easily done offline)
  the absence of the email in the mailing list. (As a user shouldn't be sent multiple emails)
Every email is added in the the mailig list after it passes the above tests.
If not, it perceives a human error and asks for the email again.
After all the emails are added, the program starts monitoring the price of Bitcoin from Coingecko API almost relentlessly.
If anytime the price matches with the initial value, the program starts sending emails to the users.
Contd. from point 5 - If you said no, it asks if you want to view the history of all the requests.
It outputs all the data stored in the ThingSpeak database in the perfect format of value, date, and time, with a new line for every value.
If the first input is invalid, it asks for the input again.
