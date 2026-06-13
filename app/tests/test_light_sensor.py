from app.sensors.light_sensor import read_light
import time



def run():
	print("Lendo sensor de luminosidade...")
	while True:
		valor = read_light()

		print(f"Luminosidade: {valor}")

		time.sleep(1)
