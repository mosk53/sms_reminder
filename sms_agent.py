from twilio.rest import Client
from time import sleep
import smtplib
from pythonping import ping
import pickle
from einst import *
import logging as log
import mysql.connector

log.basicConfig(filename='log.log', level=log.DEBUG, format='%(asctime)s %(message)s', datefmt='%m/%d/%Y %I:%M:%S %p')



class reminder_bot():
    def __init__(self) -> None:
        # Database connection
        log.info("Connecting to database")
        self.db = mysql.connector.connect(
            host=db_host,
            user=db_user,
            password=db_password,
            database=db_name)
        self.cursor = self.db.cursor()
        # Twilio connection
        log.info("Creating Twilio client")
        self.client = Client(tw_account_sid, tw_auth_token)

    def fetch_rows(self):
        # fetch rows from database
        log.info("Executing query")
        self.query = "SELECT * FROM jo348_ausgsms WHERE senddate = CURRENT_DATE AND abfrage = 0;"
        self.cursor.execute(self.query)
        rows = self.cursor.fetchall()
        return rows

    def process_rows(self, rows):
        # get number and message column from rows
        log.info("Processing rows")
        for row in rows:
            # number = row[7] # for testing
            number = tw_to
            message = row[9]
            # send message
            self.send_message(number, message)
            # update row
            self.update_row(row[0])
    
    def send_message(self, number, message):
        # send message
        log.info("Sending message")
        message = self.client.messages.create(
            messaging_service_sid=tw_messaging_service_sid,
            body=str(message),
            to=number
        )

    def update_row(self, id):
        # update row in database to prevent sending message again
        log.info("Updating row")
        query = "UPDATE jo348_ausgsms SET abfrage = 1 WHERE od_id = %s"
        self.cursor.execute(query, (id,))
        self.db.commit()

    def __del__(self):
        # close database connection
        log.info("Closing database connection")
        self.db.close()



if __name__ == "__main__":
    while True:
        try:
            observer = reminder_bot()
            rows = observer.fetch_rows()
            observer.process_rows(rows)
            del observer
            sleep(86400)
        except Exception as e:
            log.error(e)
            log.error("Bot crashed")
            sleep(86400)