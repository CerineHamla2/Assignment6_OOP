
class Animal:
    #defining attributes:
    Name: str
    Age: int
    Sex: str
    Size: str
    Weight: str
    Type: str
    Image: str
    Location:str
    Food_type:str
    Amount:str 
    Last_fed:str 
    #initialize attributes after validations
    def __init__(self, name,sex, age, size,weight,type,image,location, food_type, amount, last_fed):
        #created 2 lists to check if the size and last feeding time are in the lists (if not raise an exception)
        size_list=['Small','Medium','Large']
        last_fed_list=['Breakfast','Lunch','Dinner']

        if size not in size_list: 
            raise ValueError("invalid pet size, the size must be: Small,Medium or Large")
        if last_fed not in last_fed_list:
            raise ValueError("invalid input for Last Fed, it must be : Breakfast,Lunch or Dinner")

        # Check if the sex is Male or Female
        if (sex!='Female' and sex != 'Male'):
            raise ValueError("the sex must be 'female' or 'male' ")
        
        # Convert the age to an integer and handle invalid input
        try:
            age=int(age)
        except:
            raise TypeError("invalid input, the Age must be an number")
        
        if(age<0):  # age must be >0
            raise ValueError("The age must be a positive integer")
        self.Name=name
        self.Age=age
        self.Sex=sex 
        self.Size=size
        self.Weight=weight
        self.Type=type
        self.Image=image
        self.Location=location
        self.Food_type=food_type
        self.Amount=amount
        self.Last_fed=last_fed
    
    def update_amount(self,amount):  # amount is the new values that will be assigned to the object 
        self.Amount=amount
   
    def update_location(self,location):
        self.Location=location

    def update_image(self,pic):
        self.Image=pic

    def update_last_fed(self,last):
        if last not in ['Breakfast','Lunch','Dinner']:
            raise ValueError("invalid last fed value,it must be :Breakfast,Lunch or Dinner")
        self.Last_fed=last   #updating last feeding time after checking that the value is in the list
    
#creating my objects:

Scooby=Animal("Scooby Doo",'Male',57,"Large",'200 pounds','dog','image1','Kennel','Dry Food','6 oz','Dinner')

Garf=Animal('Garfield', 'Male', 48, 'Small', '5.5 pounds', 'Cat', 'Photo', 'Kennel', 'Dry Food', '6 oz', 'Dinner')

Woods=Animal('Woodstock', 'Male', 60, 'Small', '<1 oz', 'Bird', 'Photo', 'Cage', 'Dry Food', '0.5 oz', 'Breakfast')
print("Woodstock was Last Fed:",Woods.Last_fed)   #printing the original last feeding time

Woods.update_last_fed('Dinner')  #updating Woodstock last fed from Breakfast to dinner
print("Updated Woodstock last fed to:",Woods.Last_fed)      #printing the new feeding time to confirm the method works


Scooby.update_image('simple plan photo')   #updating Scooby Doo image to new image 



###### 2nd part###############

class Dog(Animal):
    Breed:str
    # Initialize the dog using the Animal parent class and its breed
    def __init__(self, name,sex, age, size,weight,type,image,location, food_type, amount, last_fed, breed):
        super().__init__(name,sex,age,size,weight,type,image,location,food_type,amount,last_fed)    # Call the parent class initializer to set up the inherited attributes

        self.Breed=breed 

        self.Type="Dog"                 ## Setting the dog's specific type, location, and food
        self.Location="Kennel"
        self.Food_type="Kibble"

        # Setting the amount of food according to the dog's size
        if self.Size=='Small':
            self.Amount='8 oz'
        elif self.Size=='Medium':
            self.Amount='16 oz'
        elif self.Size=='Large':
            self.Amount='24 oz'   
        
       


class Cat(Animal):
    def __init__(self,name,sex,age,size,weight,type,image,location,food_type,amount,last_fed):    
        super().__init__(name,sex,age,size,weight,type,image,location,food_type,amount,last_fed)    #call the initializer of the class Animal(parent)
        # Setting the cat's type and location
        self.Type='Cat'
        self.Location='Kennel'

        if(self.Food_type !='Wet Food' and self.Food_type!='Dry Food'):     ## Checking that the cat's food type is either Wet Food or Dry Food
            raise ValueError("Cats be fed Wet food or Dry Food only")
        
        self.Amount='6 oz'

#updating the affected animals and create Scooby Doo using Dog subclass, and garfield using Cat subclass

scooby2=Dog("Scooby Doo",'Male',57,"Large",'200 pounds','Dog','image1','Kennel','Dry Food','6 oz','Dinner','Great Dane')
print('New scooby Doo(subclass):',scooby2.Amount,scooby2.Food_type,scooby2.Location,scooby2.Breed) #just wanted to check the new attributes' values 


Garf2 = Cat('Garfield', 'Male', 48, 'Small', '5.5 pounds','Cat', 'Photo', 'Kennel', 'Dry Food', '6 oz', 'Dinner')

