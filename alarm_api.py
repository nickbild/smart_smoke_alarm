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
    # now = str(datetime.now())
    
    # with closing(sqlite3.connect("memory_pill.db")) as connection:
    #     with closing(connection.cursor()) as cursor:
    #         cursor.execute("INSERT INTO medication_administrations (patient_id, medication_id, bottle_opened_at) VALUES ('{0}', '{1}', '{2}')".format(patient_id, medication_id, now))
    #         connection.commit()
    print(location_id)

    return "OK"


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')