# Quantaco_Project

Steps to Start Application :

1. Go to Quantaco_Project\Quantaco 
2. Build the backend Image  (docker build -t 'quantaco-backend' .)
3. Start the container from backend image  (docker run -p 8000:8000 quantaco-backend)

4. Go to Quantaco_Project\frontend 
5. Build the backend Image  (docker build -t 'quantaco-frontend' .)
6. Start the container from frontend image  (docker run -p 5173:5173 quantaco-frontend )

7. http://localhost:5173/quantaco/login

Assumption taken-
All the fields are mandatory to fill
Age has to be between 1 to 150 
Phone number can have +,.,- and spaces in between 
Duplicates not allowed 


Creds for testing:
username-Chandra.mishra
Passsword-Hypex@60


