# Pre-Requisites

logger==1.4, 
selenium==3.141.0, 
pytest==5.0.1, 
chromedriver

# Files/Folders structure of the testing module:
.\
  |-config             # This folder contains all the configurations and path variables
  |----config.py
  |-test_cases     #  This folder is for all the individual test use cases 
  |----test_cases.py
  |-login.py         # This is the entry point
 
 
# To execute the test case, use the following command:  
python -m unittest test_cases/test_cases.py 

