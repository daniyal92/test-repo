# READ ME 
![alt text](littlelemon/static/img/logo.png)
---
This is the documentation for the Little Lemon API built with Django.

Testable endpoints:
---
Static Home Page:
- GET `/api/home/`

Auth (Djoser):
- POST `/auth/users`
- GET `/auth/token/login`

Bookings:
- GET,POST `/api/bookings/`
- GET,PUT,DELETE `/api/bookings/<id>`

MenuItem:
- GET,POST `/api/menu/`
- GET,PUT,DELETE `/api/menu/<id>`
---
Test Directory:
`littlelemon\tests`
