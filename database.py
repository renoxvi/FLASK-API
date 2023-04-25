import sqlite3

#Set up a connection
con = sqlite3.connect("hotels.db")

cursor = con.cursor()
cursor.execute("""CREATE TABLE IF NOT EXISTS rooms(

    roomId INTEGER PRIMARY KEY,
    status NUMERIC,
    roomNumber INTEGER
    )
    """)


cursor.execute("""CREATE TABLE IF NOT EXISTS client(
    clientId INTEGER PRIMARY KEY,
    name TEXT
    )
    """)

# Create the 'bookings' table
cursor.execute("""CREATE TABLE IF NOT EXISTS bookings (
    id1 INTEGER,
    id2 INTEGER,
    amount INTEGER,
    currency TEXT,
    check_in_date TEXT,
    check_out_date TEXT,
    FOREIGN KEY(id1) REFERENCES rooms(roomId),
    FOREIGN KEY(id2) REFERENCES client(clientId),
    PRIMARY KEY(id1, id2)
)""")


con.close()