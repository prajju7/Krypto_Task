# Krypto_Task


## Setup & Installtion

Make sure you have the latest version of Python installed.

```bash
git clone <repo-url>
```

```bash
pip install -r requirements.txt
```

## Running The App

```bash
python app.py
```

## Viewing The App

Go to `http://127.0.0.1:5000`


## MySQL DB 
Script File is included 


## Approach
1. Created a Database for the User data in MySQL 
2. Python is used for both server side scripting and backend for the web page
3. Crypto data is extracted from the url as a JSON Response and the current value of the Cryptocurrency is compares with the user alerted value
4. Email is send to the user if the value crossed the alert value.
5. SMTPlib library is used to send the mail (Could not use the message broker) but I hope that the target requirement is achieved 
6. Have the ability to improvise a lot further and better given the time.

P.S: Good Experience!!!!


