


yes_no = input("Have you have your birthday this year? ").lower()
if yes_no == "yes" or yes_no == "y":
    birthday =+ 2022
else:
    birthday =+ 2021

def num_check(question, low, high):
   error = "Please enter an  number between 1900 and 2022\n"

   valid = False
   while not valid:
       try:
           response = int(input(question))
           if low < response <= high:
               return response


           else:
               print(error)

       except ValueError:
           print(error)


year = num_check("when were you born? ", 1900, 2022)

age = birthday - year
print("Your age is {}".format(age))