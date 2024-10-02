from tkinter.font import names


class Encounter:
	def __init__(self, name: str, enc_type: str):
		self.name = name
		self.enc_type = enc_type

	def start_encounter(self):
		"""
		returns a boolean\n
		True if encounter was cleared\n
		False if encounter was failed\n
		:return:
		"""
		print(f"Encountered: {self.name}")

class TechnicalMalfunction(Encounter):
	def __init__(self, name: str):
		super().__init__(name, "technical malfunction")


class ExtremeWeather(Encounter):
	def __init__(sel, name: str):
		super().__init__(name, "extreme_weather")

	def start_encounter(self) -> bool:
		super().start_encounter()
		print("Choose your action ")
		player_input = input("")
		if player_input == "1":
			print("Encounter Cleared")
			return True
		elif player_input == "2":
			print("Encounter Failed")
			return False

		return True

thunder_storm = ExtremeWeather("Thunder Storm")
thunder_storm.start_encounter()