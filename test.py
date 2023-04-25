from flask import Flask, jsonify
import sqlite3

app = Flask(__name__)

@app.route('/data', methods=['GET'])
def get_all_data():
    # Set up a connection
    db = get_db
    cursor = db.cursor

    # Execute SQL queries to retrieve data from all tables
    cursor.execute("SELECT * FROM rooms")
    rooms_rows = cursor.fetchall()

    cursor.execute("SELECT * FROM client")
    clients_rows = cursor.fetchall()

    cursor.execute("SELECT * FROM bookings")
    bookings_rows = cursor.fetchall()

    con.close()

    # Convert retrieved data to dictionaries
    rooms = []
    for row in rooms_rows:
        room = {
            'roomId': row[0],
            'status': row[1],
            'roomNumber': row[2]
        }
        rooms.append(room)

    clients = []
    for row in clients_rows:
        client = {
            'clientId': row[0],
            'name': row[1]
        }
        clients.append(client)

    bookings = []
    for row in bookings_rows:
        booking = {
            'id1': row[0],
            'id2': row[1],
            'amount': row[2],
            'currency': row[3],
            'check_in_date': row[4],
            'check_out_date': row[5]
        }
        bookings.append(booking)

    # Create a dictionary to hold all data
    all_data = {
        'rooms': rooms,
        'clients': clients,
        'bookings': bookings
    }

    # Return the list of all data as a JSON response
    return jsonify(all_data)

if __name__ == '__main__':
    app.run(debug=True)
