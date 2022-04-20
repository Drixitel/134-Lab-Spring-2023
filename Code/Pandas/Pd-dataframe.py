import pandas as pd

# Create a Data Frame i.e table of values 
# df = data frame 

df = pd.DataFrame(
    {"Last Name, First Name":
        ["Beresford, John", 
        "Pichardo, Michelle", 
        "Reynolds, Ryan", ], 
    "Age": 
        [25,28,35], 
    "Sex":["male", "female", "male"],
    }
)
ages = pd.Series([25,28,35], name = "Ages")
print("\n Data Frame Example:")
print(df)
print("")

# each column is considered a Series e.g Age is a series ]

print("\nNow we select the column 'Age':")
print(df["Age"])

# Create a column a.k.a Series in line

colors = pd.Series(["blue", "white", "pink"], 
                     name = "Favorite Color")

print("\nColomn of added colors:")
print(colors)



# Find max Age 
print("\nThe Max age of the participants is:")
print(df["Age"].max())
print("\nThe Min age is:")
print(ages.min())

#Basics Parameters 

        # Do not forget df is not a command it's the name 
print("\nDescribe some parameters of our DataFram:")
print(df.describe()) 

