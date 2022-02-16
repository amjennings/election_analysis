#print("Hello World")

counties = ['Arapahoe', 'Denver', 'Jefferson']
#if counties[1] == 'Denver':
 #   print(counties[1])
#if counties[3] != 'Jefferson':
 #  print(counties[2])

#if "El Paso" in counties:
    # print("El Paso is in the list of counties.")
#else:
    # print("El Paso is not in the list of counties.")

#if "Arapahoe" in counties or "El Paso" in counties:
  #  print("Arapahoe or El Paso are in the list of counties.")
#else:
 #   print("Arapahoe and El Paso are not in the list of counties.")

#if "Arapahoe" in counties and "El Paso" not in counties:
 #  print("Only Arapahoe is in the list of counties.")
#else:
 #   print("Arapahoe is in the list of counties and El Paso is not in the list of counties.")

#for county in counties:
 #   print(county)
counties_dict = {"Arapahoe": 422829, "Denver": 463353, "Jefferson": 432438}
#for county in counties_dict.keys():
 #   print(county)
#using a for loop to use the key, county to reference the value
#for county in counties_dict:
 #   print(counties_dict[county])

#getting the values of a key using the get() method on the dicitonary
#for county in counties_dict:
 #   print(counties_dict.get(county))

#for county, voters in counties_dict.items():
    #print(county + " county has " + str(voters) + " registered voters.") 

#same thing as above but using an f-string
#for county, voters in counties_dict.items():
    #print(f"{county} county has {voters} registered voters.")

voting_data = [{"county":"Arapahoe", "registered_voters": 422829}, {"county":"Denver", "registered_voters": 463353}, {"county":"Jefferson", "registered_voters": 432438}]
for county, registered_voters in voting_data():
    print(f"{county} has {registered_voters} registered voters")
