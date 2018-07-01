# DJango-example

# Hi Mike!
Open two different tabs. Each tab represents a different user. Each user sends their position and receives positions of all other users.
Each user "asks" the server for the position of other users and sends its own position.

Tab 1:
http://127.0.0.1:8080/user/?user=me&position=999

Tab 2:
http://127.0.0.1:8080/user/?user=you&position=123

Refresh both tabs

Tab 3:
http://127.0.0.1:8080/user/?user=other&position=59595

Refresh all three tabs

Tab 1:
http://127.0.0.1:8080/user/?user=me&position=123

Refresh all three tabs


# There are things here that are REALLY bad. (may be more than what is listed)
1. I am storing the data in a file. This should be a database or something designed better
2. There is no security
3. I am not sure but I don't think DJango scales well at all
4. There is no initial handshake (i.e. there might be some data that should be transfered at the start of a session)
5. Everything uses TCP which may not be fast enough
6. I'm sure there is a bunch of other crap here you shouldn't actually do
