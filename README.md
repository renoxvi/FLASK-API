Use the attached description to create a RESTful application that uses JSON as primary Representation Format. Once
a client places a booking via REST he/she can be assured that the order has been
received and accepted by the Hotel The booking details are
confirmed in a response that contains additional information such as the
payment amount, currency, and a timestamp for when the booking was received
Develop the API end-points using PHP, Python, Nodejs or Java. To test the end-points, use Insomnia or Postman.

Create Room, Client and Booking in JSON using POST into
database with 3 related tables [room->roomid, client->clientid,
booking->clientid,roomid]

Search [GET] available rooms based on Boolean status: Booked
=1, Free = 0

Retrieve a list of all rooms, clients and bookings in JSON

POST booking JSON with clientid and roomid as composite PK.
Other details are check-in date, check-out date and time

Retrieve [GET] confirmation of booking total amount depending
on number of rooms booked
