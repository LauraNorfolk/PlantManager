import json

class Plant:

	light_loss_per_hour = 1
	water_loss_per_hour = 1

	def __init__(self, name, water_level, light_level, age):
		self.name = name
		self.water_level = water_level
		self.light_level = light_level
		self.age = age


	def water_plant(self, water_amount):
		self.water_level += water_amount 


	def expose_to_sun(self, hours_in_sun):
		self.light_level += hours_in_sun

	
	def passing_time(self, time_elapsed):
		self.water_level -= self.water_loss_per_hour * time_elapsed
		self.light_level -= self.light_loss_per_hour * time_elapsed
		self.age += time_elapsed /24 


	def inspect_plant(self):
		print("Plant is called: {}\nCurrent water level is: {}\nCurrent light level is: {}\nAge of plant is {} days".format(self.name, self.water_level, self.light_level, self.age))


	def to_dict(self):
		return {
			"type": "Plant",
			"name": self.name,
			"light_level": self.light_level,
			"water_level": self.water_level,
			"age": self.age
		}





class Succulent(Plant):

	light_loss_per_hour = 2
	water_loss_per_hour = 0.1

	def __init__(self, name, water_level, light_level, age, sub_plant):
		self.sub_plant = sub_plant
		super().__init__(name, water_level, light_level, age)


	def spawn_plant(self):
		self.sub_plant += 1


	def passing_time(self, time_elapsed):
		super().passing_time(time_elapsed)
		if time_elapsed >= 6:
			self.spawn_plant()


	def inspect_plant(self):
		super().inspect_plant()
		print("There are {} subplants".format(self.sub_plant))


	def to_dict(self):
		dictionary = super().to_dict()
		dictionary["type"] = "Succulent"
		dictionary["sub_plant"] = self.sub_plant
		return dictionary


class House_Plant(Plant):

	def to_dict(self):
		dictionary = super().to_dict()
		dictionary["type"] = "House_Plant"
		return dictionary


class Trailing_Plant(Plant):

	water_loss_per_hour = 2

	def __init__(self, name, water_level, light_level, age, trailing_length):
		self.trailing_length = trailing_length
		super().__init__(name, water_level, light_level, age)


	def grow_length(self):
		self.trailing_length += 1


	def passing_time(self, time_elapsed):
		super().passing_time(time_elapsed)
		if time_elapsed >= 2:
			self.grow_length()


	def inspect_plant(self):
		super().inspect_plant()
		print("The plant is {} foot".format(self.trailing_length))


	def to_dict(self):
		dictionary = super().to_dict()
		dictionary["type"] = "Trailing_Plant"
		dictionary["trailing_length"] = self.trailing_length
		return dictionary


def list_plants(current_plants):
	for i,plant in enumerate(current_plants):
		print("Plant {} is a {} named {}".format(i, type(plant), plant.name))

	return


def view_plant(current_plants):
	input_option = int(input("Enter plant number "))
	selected_plant = current_plants[input_option]
	selected_plant.inspect_plant()
	print()
	print("Select 1 to water plant")
	print("Select 2 to expose plant to light")
	print("Select 3 to do nothing")

	input_option = int(input("Select option number "))

	if input_option == 3:
		return

	change_value = int(input("How much? "))

	if input_option == 1:
		selected_plant.water_plant(change_value)

	elif input_option == 2:
		selected_plant.expose_to_sun(change_value)

	selected_plant.inspect_plant()
	return


def create_succulent():
	name = input("Enter plant name ")
	water_level = 0
	light_level = 0
	age = 0
	sub_plant = 0
	return Succulent(name, water_level, light_level, age, sub_plant)
	

def create_house_plant():
	name = input("Enter plant name ")
	water_level = 0
	light_level = 0
	age = 0
	return House_Plant(name, water_level, light_level, age)


def create_trailing_plant():
	name = input("Enter plant name ")
	water_level = 0
	light_level = 0
	age = 0
	trailing_length = 0
	return Trailing_Plant(name, water_level, light_level, age, trailing_length)


def create_plant(current_plants):
	print("Select 1 to create a succulent")
	print("Select 2 to create a house plant")
	print("Select 3 to create a trailing plant")
	print("Select 4 to cancel")
	input_option = int(input("Select option number "))

	if input_option == 4:
		return

	if input_option == 1:
		current_plants.append(create_succulent())
		return

	elif input_option == 2:
		current_plants.append(create_house_plant())
		return

	elif input_option == 3:
		current_plants.append(create_trailing_plant())
		return


def delete_plant(current_plants):
	print("Which plant do you want to delete? ")
	list_plants(current_plants)
	del_value = int(input("Enter plant number "))
	del current_plants[del_value]


def pass_time(current_plants):
	print("How much time do you want to pass? ")
	input_option = int(input("Enter amount of hours "))
	for plant in current_plants:
		plant.passing_time(input_option)
	return


def load_file():
	with open("plants.json", "r") as f:
		plants_json = f.read()
		plant_dicts = json.loads(plants_json)
	loaded_plants = []
	for plant_dict in plant_dicts:
		if plant_dict["type"] == "Plant":
			new_plant = Plant(plant_dict["name"], plant_dict["water_level"], plant_dict["light_level"], plant_dict["age"])
			loaded_plants.append(new_plant)

		elif plant_dict["type"] == "House_Plant":
			new_plant = House_Plant(plant_dict["name"], plant_dict["water_level"], plant_dict["light_level"], plant_dict["age"])
			loaded_plants.append(new_plant)

		elif plant_dict["type"] == "Succulent":
			new_plant = Succulent(plant_dict["name"], plant_dict["water_level"], plant_dict["light_level"], plant_dict["age"], plant_dict["sub_plant"])
			loaded_plants.append(new_plant)

		elif plant_dict["type"] == "Trailing_Plant":
			new_plant = Trailing_Plant(plant_dict["name"], plant_dict["water_level"], plant_dict["light_level"], plant_dict["age"], plant_dict["trailing_length"])
			loaded_plants.append(new_plant)

	return loaded_plants



def save_plants(current_plants):
	plant_dicts = [plant.to_dict() for plant in current_plants]
	plants_json = json.dumps(plant_dicts)
	with open("plants.json", "w") as f:
		f.write(plants_json)
	return


def main():
	current_plants = []
	while True:
		print("Select 1 to list plants")
		print("Select 2 to view plant")
		print("Select 3 to create a plant")
		print("Select 4 to delete a plant")
		print("Select 5 to pass time")
		print("Select 6 to load from file")
		print("Select 7 to save plants")


		input_option = int(input("Enter selection "))

		if input_option == 1:
			list_plants(current_plants)
			
		elif input_option == 2:
			view_plant(current_plants)
			
		elif input_option == 3:
			create_plant(current_plants)

		elif input_option == 4:
			delete_plant(current_plants)

		elif input_option == 5:
			pass_time(current_plants)

		elif input_option == 6:
			current_plants = load_file()

		elif input_option == 7:
			save_plants(current_plants)



if __name__ == "__main__":

	main()