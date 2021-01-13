from netmiko import ConnectHandler
from datetime import datetime
with open('devices.txt') as d:
	devices_list = d.readlines()

with open('command.txt') as c:
	commands_list = c.readlines()

for devices in devices_list:
	ios_device = {
		'device_type': 'cisco_ios',
		'host': devices.strip(),
		'username': 'admin',
		'password': 'cisco',
		'secret': 'cisco'
	}
	print("Connection Established Successfully fo host: ", devices.strip())
	ssh_connect = ConnectHandler(**ios_device)

	for commands in commands_list:
		output = ssh_connect.send_command(commands.strip())
		print(output)

		file = open('Host {} - {}-config.txt'.format(ios_device['host'], datetime.now().date()), 'a')
		file.write("-------------------------\n")
		file.write("Host {}".format(ios_device['host']))
		file.write("\n")
		file.write(output)
		file.close()
