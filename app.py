from flask import Flask, request, jsonify, g
import sqlite3
app = Flask(__name__)
DATABASE = 'hotels.db'

def get_db():
    db = getattr(g, '_database', None)
    if db is None:
        db = g._database = sqlite3.connect(DATABASE)
    return db


@app.teardown_appcontext
def close_connection(exception):
    db = getattr(g, '_database', None)
    if db is not None:
        db.close()


@app.route('/')
def home_page():
    return "<html><h3>Welcome to this hotel</h3></html>"

@app.route('/rooms', methods=['POST'])
def create_rooms():
    db = get_db()
    cursor = db.cursor()

    # Get list of room data from JSON request
    rooms_data = request.get_json()

    # Loop through the list and insert each room data into 'rooms' table
    for room_data in rooms_data:
        status = room_data['status']
        room_number = room_data['roomNumber']
        cursor.execute("INSERT INTO rooms (status, roomNumber) VALUES (?, ?)", (status, room_number,))
        db.commit()

    return jsonify({'message': 'Rooms created successfully'}), 201

#Ceaate and post a booking
@app.route('/booking', methods=['POST'])
def create_booking():
    db = get_db()
    cursor = db.cursor()

    # Get booking data from JSON request
    booking_data = request.get_json()
    checkin_date = booking_data['checkin_date']
    checkout_date = booking_data['checkout_date']
    amount  = booking_data['amount']
    currency = booking_data['currency']
    # Insert booking data into 'bookings' table
    cursor.execute("INSERT INTO bookings (check_in_date, check_out_date, amount, currency) VALUES (?, ?, ?, ?)",
                   (checkin_date, checkout_date, amount, currency))
    db.commit()

    booking_id = cursor.lastrowid  # Get the auto-incremented booking_id
    return jsonify({'message': 'Booking created successfully', 'booking_id': booking_id}), 201


@app.route('/clients', methods=['POST'])
def create_client():
    
        # Get client name from request body
        name = request.json['name']
        
        # Insert client into databas
        conn = get_db()
        cursor = conn.cursor()
        cursor.execute("INSERT INTO client (name) VALUES (?)", (name,))
        conn.commit()
        conn.close()
        
        return jsonify({'message': 'Client created successfully'}), 201
 
@app.route('/available_rooms', methods=['GET'])
def get_available_rooms():

    db = get_db()
    cursor = db.cursor()
    # Execute SQL query to retrieve rooms with status 1
    cursor.execute("SELECT * FROM rooms WHERE status = 1")
    rows = cursor.fetchall()

    # Convert retrieved data to a list of dictionaries
    rooms = []
    for row in rows:
        room = {
            'roomId': row[0],
            'status': row[1],
            'roomNumber': row[2]
        }
        rooms.append(room)

    cursor.close()
    return jsonify(rooms)

      
@app.route('/all_data', methods=['GET'])
def get_all_data():
    # Set up a connection
    db = get_db()
    cursor = db.cursor()

    # Execute SQL queries to retrieve data from all tables
    cursor.execute("SELECT * FROM rooms")
    rooms_rows = cursor.fetchall()

    cursor.execute("SELECT * FROM client")
    clients_rows = cursor.fetchall()

    cursor.execute("SELECT * FROM bookings")
    bookings_rows = cursor.fetchall()

    cursor.close()

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
   
@app.route('/all_bookings', methods = ['GET'])
def bookings():
    db = get_db()
    cursor = db.cursor()
    #Retrieve all bookings data
    cursor.execute("SELECT * FROM bookings")
    bookings_rows = cursor.fetchall()

    cursor.close()

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

    all_bookings = {
        'bookings': bookings
    }
    return jsonify(all_bookings)