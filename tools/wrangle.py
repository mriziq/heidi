import pandas as pd

# Converting the Case Study data into a dataframe using the
# pandas library, and setting the Student column as the
# primary key.

df = pd.read_csv("194A_data.csv", index_col="Student")

#converting categorical data into binary numeral data
#yes = 1, no = 0
#male = 3, female = 4

df.replace(['Yes', 'No'], [1, 0], inplace=True)
df.replace(['Male', 'Female'], [3,4], inplace=True)

#saving file
df.to_csv("194A_data.csv", index=True)
