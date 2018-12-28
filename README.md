# Simple Django login/signup implementation 

About Project -


A Simple Django Project with cool frontend (Linkedin Clone).


Project is based on function based views [FBV]


It has Features like :


1. Signup - A User can signup using unique username.


2. Signin


3. Email Verification - Using Gmail SMTP, we send verification email
                        to the user by generating token. Activation link when accessed
                        decodes and activates user's account.
                        
4. Form Field Errors - Errors are displayed, if there are errors in Signup/Signin Forms
                       
                      
New developers, who are starting development or advancing through concepts may find this project a good learning material.
                        

For Developers/Contributers:
  To Set up follow these steps -
  
  1. Run on git terminal
  
    `git clone https://github.com/PratibhaShrivastav/Linkedin`
    
  2. Change working directory to /LinkedIn
  
 
  3. make virtualenv 
  
    `virtual env <env-name>`
    
  4. Activate your virtual environment
  
     `source env/bin/activate`
     
  5. Install requirements.txt
  
      `pip install -r requirements.txt`
      
  6. Run migrations :
  
     `python manage.py migrate`
     
  7. Run server :
  
      `python manage.py runserver <port>`
