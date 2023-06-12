from django.db import models
from django.utils.timezone import now


# Create your models here.

# <HINT> Create a Car Make model `class CarMake(models.Model)`:
# - Name
# - Description
# - Any other fields you would like to include in car make model
# - __str__ method to print a car make object

class CarMake(models.Model):
    name 				        = models.CharField(max_length=30)
    description 				= models.CharField(max_length=200)
    country   				    = models.CharField(max_length=100)

    def __str__(self):
        return "Name: " + self.name + ", " + \
                "Description" + self.description + ", " + \
                "Country: " + self.country + ", "


# <HINT> Create a Car Model model `class CarModel(models.Model):`:
# - Many-To-One relationship to Car Make model (One Car Make has many Car Models, using ForeignKey field)
# - Name
# - Dealer id, used to refer a dealer created in cloudant database
# - Type (CharField with a choices argument to provide limited choices such as Sedan, SUV, WAGON, etc.)
# - Year (DateField)
# - Any other fields you would like to include in car model
# - __str__ method to print a car make object

class CarModel(models.Model):
    class Type(models.TextChoices):
        SED = "1", "Sedan"
        SUV = "2", "SUV"
        WAG = "3", "Wagon"

    make       = models.ForeignKey(CarMake, null=True, on_delete=models.CASCADE)
    dealer_id  = models.AutoField(primary_key=True)
    name 	   = models.CharField(max_length=30, unique=True)
    type       = models.CharField(max_length=5, choices=Type.choices)
    year       = models.DateField()

    def __str__(self):
        return "Name: " + self.name + ", " + \
                "Make" + self.make + ", " + \
                "Type: " + self.type + ", " + \
                "Year" + self.year + ", " 


# <HINT> Create a plain Python class `CarDealer` to hold dealer data


# <HINT> Create a plain Python class `DealerReview` to hold review data
