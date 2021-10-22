# Define a variable "country" and assign the country name
country = "India"

# Define a variable "age" and assign an appropriate age value
age = 18

# Check for the eligibility to vote in India
# If "age" is less than 18, print "Not eligible to vote"
if age < 18:
    print("Not eligible to vote")

# If "country" is not India, print "Not eligible to vote in India"  
if country != "India":
    print("Not eligible to vote in India")

# If "country" is India and "age" is greater or equal to 18, print "Eligible to vote in India"    
if country == "India":
    if age >= 18:
        print("Eligible to vote in India")
