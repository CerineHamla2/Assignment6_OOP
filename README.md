# Assignment6_OOP
# # Animal Class Assignment

# **Purpose of the first part:**

The first part of the assignment creates an `Animal` class to store information about animals at an animal shelter. Each animal has attributes such as name, age, sex, size, weight, type, image, location, food type, amount of food, and last feeding time.

The program validates some of the inputs before assigning them to the attributes.

- **Size:** The size must be Small, Medium, or Large.
- **Last Fed:** The last feeding time must be Breakfast, Lunch, or Dinner.
- **Sex:** The sex must be Male or Female.
- **Age:** The age must be a non-negative integer. If the input is invalid, an exception is raised.

**Updating information:** The `Animal` class includes methods to update the amount of food, location, image, and last feeding time. 
The `update_last_fed()` method checks that the new value is valid before updating the attribute.

**#Example 1:**

The program creates three animal objects: Scooby Doo, Garfield, and Woodstock.

```python
Woods = Animal('Woodstock', 'Male', 60, 'Small', '<1 oz',
               'Bird', 'Photo', 'Cage', 'Dry Food',
               '0.5 oz', 'Breakfast')
```
To test my Update_last_fed() I printed the original feeding time,then updates it from Breakfast to Dinner using the `update_last_fed()` method.
**Output:**

```text
Woodstock was Last Fed: Breakfast
Updated Woodstock last fed to: Dinner
```


The program also updates Scooby Doo's image using the `update_image()` method.

**#Purpose of the second part:**

The second part creates two subclasses, `Dog` and `Cat`, that inherit from the `Animal` parent class. The subclasses use `super().__init__()` to initialize the inherited attributes and add specific rules for dogs and cats.

**Dog class:**

- Adds a `Breed` attribute to store the dog's breed.
- Sets the animal type to Dog.
- Sets the location to Kennel and the food type to Kibble.
- Sets the amount of food based on the dog's size: 8 oz for Small, 16 oz for Medium, and 24 oz for Large.

**Cat class:**

- Sets the animal type to Cat.
- Sets the location to Kennel.
- Checks that the food type is either Wet Food or Dry Food.
- Sets the amount of food to 6 oz.

**#Example 2:**

The program creates a Dog object for Scooby Doo and a Cat object for Garfield.

```python
scooby2 = Dog("Scooby Doo", "Male", 57, "Large",
              "200 pounds", "Dog", "image1", "Kennel",
              "Dry Food", "6 oz", "Dinner", "Great Dane")
```

The output shows Scooby Doo's updated food amount, food type, location, and breed based on the rules defined in the `Dog` subclass.

**#Instructions:**

**First part (Animal class):**

1. Create an animal object by calling `Animal()` and entering the animal's information in the following order: name, sex, age, size, weight, type, image, location, food type, amount of food, and last feeding time.

2. Enter a valid sex (`Male` or `Female`), size (`Small`, `Medium`, or `Large`), and last feeding time (`Breakfast`, `Lunch`, or `Dinner`). If an invalid value is entered, an exception is raised.

3. Use the `update_amount()`, `update_location()`, `update_image()`, or `update_last_fed()` methods to update an animal's information. Enter the new value as the argument of the method.

**Second part (Dog and Cat subclasses):**

1. Create a `Dog` object by entering the animal's information, followed by the dog's breed.

2. The program automatically sets the dog's type to Dog, location to Kennel, and food type to Kibble. The amount of food is determined by the dog's size: 8 oz for Small, 16 oz for Medium, and 24 oz for Large.

3. Create a `Cat` object by entering the animal's information. Enter either `Wet Food` or `Dry Food` as the food type. The program automatically sets the cat's type to Cat, location to Kennel, and amount of food to 6 oz.

4. Run the program to see the output for the example animals. To test the validation, modify the values passed to the constructors and check whether invalid values raise the appropriate exceptions.

**Running the program:** Save the code in a Python file and run it using `python animal.py` in the terminal. Modify the example values directly in the code to test different animals and updates.

**#Sources:**

- Lecture slides and YouTube videos explaining how to write initializers and methods.

- AI assistance was used to understand how to call the parent class initializer in a subclass using super().__init__(), and to organize the Read.me document.

**#Contributors:**
 Cerine 
