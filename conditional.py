temperature=int(input("enter the temperature in celcius:"))
if(temperature<=20):
    outfit="jacket"
    print("its a cold weather")
    print("wear a",outfit)
else:
    outfit="t-shirt"
    print("its a sunny weather")
    print("wear a",outfit)

rain=input("is it raining today yes/no:")
if(rain=="yes"):
    thing="umbrella"
    print("its a rainy day today\n take an",thing)

wind=int(input("enter the speed of the wind="))
if(wind>30):
    windbreaker="yes"
    print("its windy day\n wear a windbreaker ")
else:
    print("no need of windbreaker")
    windbreaker="no"

puddles=input("are there puddles on roads yes/no=")
if(puddles=="yes"):
    print("the ground is wet and muddy")
    shoes="boots"
else:
    shoes="sneakers" 
    print("the ground is dry \n you can wear your sneakers")   

print("the outfit checking is done\n\n\n")
print("the outfitis mentioned below⬇️")
print("temperature:",temperature)
print("clothes:",outfit)
print("rain:",rain)
print("thing:",thing)
print("wind=",wind)
print("wind breaker=",windbreaker)
print("puddles=",puddles)
print("shoes=",shoes)



            



