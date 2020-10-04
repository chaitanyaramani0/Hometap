# Septic-Check
Hometap-septic-check is web app that checks the whether property has Septic system or not based on the property address.
To validate septic system of each property Hometap-septic-check uses api which is based on the Postman mock server.

## Installation


```bash
pip install virtualenv
```
```bash
virtualenv env 
```
## For window
```bash
\env\Scripts\activate
```
## For mac or linux
```bash
Source env/bin/activate
```

### Naviagte to Hometap/
```bash
pip install -r requirments.txt
```

### (**Optional Migrations)
```bash
pyhton manage.py makemigrations
python manage.py migrate
```
### Run the command
```bash
pyhton manage.py runserver 
```
### go to the localhost:8000 or http://127.0.0.1:8000/
webpage will ask the addresh and zipcode both are mendetory.
api will give you result based on zipcode. basically api gets the zipcode and pass as one of the parameter to api.

to get excet result below are some example of zipcode.
```bash
32145 - septic
98243 - septic
42223- municipal
32145 - municiaple
51023 -strorm 
```
## Expansion 
you can pass any zipcode but to get precise result choose one of above any other zipcode will match 
mock api data base on matching algorithms and give you closed result whoever match the above zipcode closest.

# Using Django REST framework
septic check also use django rest framework this is basically another way to check the setic system.

## route to below endpoint you pass any zipcode as query param 
### for eg ?zipcode=98243
```bash
http://localhost:8000/api/v1?zipcode=111111 
```
### or 
```bash
http://127.0.0.1:8000/api/v1?zipcode=111111
```
 
