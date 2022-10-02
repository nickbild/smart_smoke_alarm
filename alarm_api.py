########
# Nick Bild
# nick.bild@gmail.com
#
# Starting the server:
# python3 alarm_api.py
#
# Accessing an endpoint:
# curl http://[SERVER_IP]:5000/[ENDPOINT_NAME]
########

from flask import Flask, request
from datetime import datetime
from contextlib import closing
import sqlite3


app = Flask(__name__)


@app.route("/send_alert")
def send_alert():
    location_id = request.args.get('location_id')
    now = str(datetime.now())
    
    with closing(sqlite3.connect("smart_smoke_alarm.db")) as connection:
        with closing(connection.cursor()) as cursor:
            cursor.execute("INSERT INTO alerts (location_id, time_stamp) VALUES ('{0}', '{1}')".format(location_id, now))
            connection.commit()
    print("Smoke alarm sounding! Person detected in location {0} at {1}.".format(location_id, now))

    return "OK"


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
