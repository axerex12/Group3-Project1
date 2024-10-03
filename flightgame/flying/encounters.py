import json
import random
import os
from flightgame.db.Database import Database

class Encounter:
	def __init__(self, name: str, enc_type: str, description: str, reaction_options:list):
		self.name = name
		self.enc_type = enc_type
		self.description = description
		self.reaction_options = reaction_options

	def start_encounter(self) -> tuple:
		"""
		returns a boolean\n
		True if encounter was cleared\n
		False if encounter was failed\n
		:return:
		"""
		print(f"Encountered: {self.name}")

		encounter_success = True
		time_add = 0
		encounter_type = "Continue"

		print("Choose your action ")
		opt = 0
		for i in self.reaction_options:
			print(f"{opt}. {i['option']}, {i['outcome']['success_chance']}")
			opt+=1
		while True:
			option = -1
			try:
				option = int(input("> "))
			except Exception as e:
				print("please enter valid input")
				continue

			if int(option) < len(self.reaction_options):
				encounter = self.reaction_options[option]
				print(f"You chose to {self.reaction_options[option]['option']}")
				encounter_type = encounter["type"]
				if encounter_type=="Land":
					print("You landed")
				elif encounter_type=="Wait":
					print("You wait")
				elif encounter_type=="Continue":
					print("You continued")
				else:
					print(f"Type is: {encounter_type}")

				success = random.uniform(0.0,1.0)
				#print(encounter_success)
				#print(encounter["outcome"]["success_chance"])
				encounter_success = success<encounter["outcome"]["success_chance"]
				if encounter_success:
					time_add = encounter["outcome"]["success"]["time_penalty_minutes"]
				else:
					time_add = encounter["outcome"]["failure"]["time_penalty_minutes"]
			else:
				print("Please try correct input")

			return encounter_success,time_add,encounter_type
	def tostring(self):
		print(self.name)

class EncounterClient:
	def __init__(self):
		current_dir = os.path.dirname(__file__)
		enc_path = os.path.join(current_dir, '..', '..', 'encounters.json')
		with open(enc_path) as file:
			encounters = json.load(file)["random_encounters"]
		self.encounters_list = self.load_encounters(encounters=encounters)

	def load_encounters(self, encounters: list) -> list:
		encounters_list = []
		for enc_t in encounters:
			#print(enc_t["type"])
			for enc in enc_t["encounters"]:
				#print(enc["name"])
				#print(enc_t["type"])
				#print(enc["description"])
				#print(enc["reaction_options"])
				encounter = Encounter(enc["name"],enc_t["type"],enc["description"],enc["reaction_options"])
				encounters_list.append(encounter)
		return encounters_list

	def random_encounter(self) -> Encounter:
		return self.encounters_list[random.randint(0,len(self.encounters_list)-1)]

if __name__ == "__main__":
	db = Database()
	encClient = EncounterClient()
	print(encClient.random_encounter().start_encounter())