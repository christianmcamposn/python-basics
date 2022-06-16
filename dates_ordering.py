#Python program to sort the dates

#importing datetime module
from datetime import *

# create empty list
group = []

# add today's date
group.append(date.today())

#creating some more dates
d = date(2015, 6, 29)
group.append(d)

d = date(2011, 4, 7 )
group.append(d)

# add 25 days to the date
# and adding it to the list
group.append(d + timedelta(days = 25))

# sort the list
group.sort()

for d in group:
    print(d)




