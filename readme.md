# Reminder Bot

The Reminder Bot is a Python script that fetches reminders from a MySQL database, sends them as SMS messages using the Twilio API, and updates the database to indicate that the messages have been sent. This script runs indefinitely and checks the database for reminders once per day.

## Installation

1. Clone or download this repository.

2. Install the required packages by running the following command: 

`pip install -r requirements.txt`

3. Create a `einst.py` file with your Twilio, MySQL, and email credentials.

## Usage

To use the Reminder Bot, run the following command:

`python reminder_bot.py`

The script will run indefinitely, checking the database for reminders once per day. If it encounters an error, it will log the error to a log file and continue running.

## Configuration

The `einst.py` file contains the following configuration parameters:

### Twilio credentials

- `tw_account_sid`: Your Twilio account SID.
- `tw_auth_token`: Your Twilio authentication token.
- `tw_url`: The URL of the Twilio XML file to use for outgoing calls.
- `tw_to`: The phone number to send reminders to.
- `tw_from`: Your Twilio phone number.
- `tw_messaging_service_sid`: The messaging service SID to use for outgoing messages.

### Database credentials

- `db_host`: The host name of your MySQL database.
- `db_user`: The MySQL user name to use.
- `db_password`: The MySQL password to use.
- `db_name`: The name of the MySQL database to use.

### Email credentials

- `e_sender_email`: The email address of the sender.
- `e_receiver_email`: The email address of the recipient.
- `e_password`: The password for the sender's email account.


