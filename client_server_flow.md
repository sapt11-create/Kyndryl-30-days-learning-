             CLIENT-SERVER FLOW

+------------------+                   +------------------+
|      CLIENT      |                   |      SERVER      |
|                  |                   |                  |
|  Browser / App   |                   |  Python Server   |
+------------------+                   +------------------+
          |                                      |
          |                                      |
          |  1. CONNECTION                       |
          |------------------------------------->|
          |     Establish connection             |
          |                                      |
          |  2. REQUEST                          |
          |------------------------------------->|
          |     GET /student                     |
          |     Ask for student data             |
          |                                      |
          |                          Process request
          |                          Find endpoint
          |                          Prepare response
          |                                      |
          |  3. RESPONSE                         |
          |<-------------------------------------|
          |     HTTP 200 OK                      |
          |     {"id": 1, "name": "Rahul"}       |
          |                                      |
          |                                      |
+------------------+                   +------------------+
| Client receives  |                   | Server completes |
| student data     |                   | the request      |
+------------------+                   +------------------+