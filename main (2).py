def checkYear(year):

  import calendar
  return (calendar.isleap(year))


print("\t\tParthi Black Program")
print("\t\t********************")
year = 2025
if (checkYear(year)):
  print("Leap Year")
else:
  print("Not a Leap Year")
