from netmiko import ConnectHandler

with open('devices.txt') as d:
	devices_list = d.readline()

for devices in devices_list:
	ios_device = {
		'device_type': 'cisco_ios',
		'host': devices.strip(),
		'username': 'admin',
		'password': 'cisco',
		'secret': 'cisco'
	}

	print("\n------------------------------")
	print("Connecting Successfully To Host", devices.strip())
	sw_name = ConnectHandler(**ios_device)

	output = sw_name.send_command("hostname R1")
	print(output)
