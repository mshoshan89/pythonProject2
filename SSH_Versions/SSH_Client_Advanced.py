# Open commands.txt file and read each command
from netmiko import ConnectHandler

with open('command.txt') as f:
	commands_list = f.readlines()
	# print(commands_list)

# Open devices.txt file and read each device ip
with open('devices.txt') as d:
	devices_list = d.readlines()
	# print(devices_list)

# Loop through each device in "devices.txt" file
for devices in devices_list:
	ios_device = {
		'device_type': 'cisco_ios',
		'host': devices.strip(),
		'username': 'admin',
		'password': 'cisco',
		'secret': 'cisco'
	}

	print("\n-------------------------------------")
	print("Connecting to device:", devices.strip())
	print("-------------------------------------")

	# Establish SSH connection to devices.txt
	net_connect = ConnectHandler(**ios_device)

	# Loop through each command in "commands.txt" file
	for command in commands_list:
		output = net_connect.send_command(command.strip())
		print(output)
