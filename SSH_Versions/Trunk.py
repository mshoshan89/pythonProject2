from netmiko import ConnectHandler

with open('trunk.txt') as t:
	commands_list = t.readlines()

with open('devices.txt') as d:
	devices_list = d.readlines()

for devices in devices_list:
	ios_device = {
		'device_type': 'cisco_ios',
		'host': devices.strip(),
		'username': 'admin',
		'password': 'cisco',
		'secret': 'cisco'
	}

	print("Connection Established Successfully to host:", devices.strip())
	print("------------------------")
	
	net_trunk = ConnectHandler(**ios_device)

	for command in commands_list:
		output = net_trunk.send_config_from_file(config_file="trunk.txt")
		print(output)
