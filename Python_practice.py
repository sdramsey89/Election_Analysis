counties = ["Arapahoe","Denver","Jefferson"]

counties_dict = {"Arapahoe": 422829, "Denver": 463353, "Jefferson": 432438}

#for county in counties_dict.keys():
#    print(county)

#for county in counties_dict.values():
#    print(county)

#for county, voters in counties_dict.items():
#    print(county, voters)

voting_data = [{"county":"Arapahoe", "registered_voters": 422829},
                {"county":"Denver", "registered_voters": 463353}, 
                {"county":"Jefferson", "registered_voters": 432438}]

#retrieve list of dictionaries
print("List of Dictionaries")
for county_dict in voting_data:
    print(county_dict
    
    )

#retrieve list of dictionaries
for i in range(len(voting_data)):
    print(voting_data[i]
      
    )

#retrieve registered voters
for county_dict in voting_data:
    print(county_dict['registered_voters'])

print()
print()
for county, voters in counties_dict.items():
    print(f"{county} county has {voters:,} registered voters.")

print()
print()
for county_dict in voting_data:
print(f"{voting_data['county']} county has {voting_data['registered_voters']:,} registered voters.")