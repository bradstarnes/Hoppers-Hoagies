########################################################################
##
## CS 101
## Program #
## Brad Starnes
## jbs5pz@mail.umkc.edu
##
## PROBLEM : Describe the problem
##
## ALGORITHM :
##      1. Write out the algorithm
##
## ERROR HANDLING:
##      Any Special Error handling to be noted.  Wager not less than 0. etc
##
## OTHER COMMENTS:
##      Any special comments
##
########################################################################
print('Hi Welcome to Hoppers Hoagies. What did you order?')

#Ask Amount of Small Italians Sold and calcualte the ingredients
smallItalianSold = int(input('How many small Italians were sold? :\n'))
smallItalLoaf =     0.5 * smallItalianSold
smallItalSalam =    0.3 * smallItalianSold
smallItalVeg =      0.2 * smallItalianSold
smallItalCheese =   4.0 * smallItalianSold

#Ask Amount of Large Italians Sold and calcualte the ingredients
largeItalianSold = int(input('How many large Italians were sold? :\n'))
LargeItalLoaf =     1.0 * largeItalianSold
LargeItalSalam =    0.5 * largeItalianSold
LargeItalVeg =      0.5 * largeItalianSold
LargeItalCheese =   8.0 * largeItalianSold

#Ask Amount of Small Vegetarians Sold and calcualte the ingredients
smalVegSold = int(input('How many small Vegetarians were sold? :\n'))
smallVegLoaf =     0.5 * smalVegSold
smallVegVeg =      0.5 * smalVegSold
smallVegCheese =   5.0 * smalVegSold

#Ask Amount of Large Vegetarians Sold and calcualte the ingredients
largeVegSold = int(input('How many large Vegetarians were sold? :\n'))
LargeVegLoaf =     1.0 * largeVegSold
LargeVegVeg =      1.2 * largeVegSold
LargeVegCheese =   11.0 * largeVegSold

#Ask Amount of Small TBirds Sold and calcualte the ingredients
smallTbirdSold = int(input('How many small TBirds were sold? :\n'))
smallTbirdLoaf =     0.5 * smallTbirdSold
smallTbirdTurkey =   0.4 * smallTbirdSold
smallTbirdCheese =   3.0 * smallTbirdSold

#Ask Amount of Large Tbirds Sold and calcualte the ingredients
largeTbirdSold = int(input('How many large TBirds were sold? :\n'))
LargeTbirdLoaf =     1.0 * largeTbirdSold
LargeTbirdTurkey =   0.9 * largeTbirdSold
LargeTbirdCheese =   8.0 * largeTbirdSold

totalBread = smallItalLoaf + LargeItalLoaf + smallVegLoaf + LargeVegLoaf + smallTbirdLoaf + LargeTbirdLoaf
totalSalami = smallItalSalam + LargeItalSalam
totalVeges = LargeVegVeg + smallVegVeg + LargeItalVeg + smallItalVeg
totalCheese = smallItalCheese + LargeItalCheese + smallVegCheese + LargeVegCheese + smallTbirdCheese + LargeTbirdCheese
totalTurkey = round(smallTbirdTurkey + LargeTbirdTurkey, 2)


print('You have used...')
print(totalBread, 'loaves of bread')
print(totalSalami, 'lbs of Salami')
print(totalVeges, 'lbs of Veges')
print(totalCheese, 'slices of Cheese')
print(totalTurkey, 'lbs of Turkey')
print('Thanks for using Hopper Hoagie Calculator')