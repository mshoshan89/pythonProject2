from netmiko import ConnectHandler

connection = {

	"device_type": "cisco_ios",
	"host": "192.168.1.10",
	"username": "admin",
	"password": "cisco",
	"secret": "cisco"
}

ssh = ConnectHandler(**connection)

if ssh:
	print("Connection Success !")
	print("\n*****************************************")

output1 = ssh.send_command("sh run | i hostname")
print(output1)
print("\n-----------------------------------------")

output2 = ssh.send_command("sh ip int br")
print(output2)
print("\n-----------------------------------------")

output3 = ssh.send_command("sh clock")
print(output3)

# commands = ["sh ip int br", "sh clock"]
# for command in commands:
#
# 	output = ssh.send_command("commands")
#
# 	print(output)
