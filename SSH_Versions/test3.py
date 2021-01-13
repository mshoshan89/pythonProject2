from netmiko import ConnectHandler

cisco_device = {
	"device_type": "cisco_ios",
	"host": "192.168.1.50",
	"username": "admin",
	"password": "cisco",
	"secret": "cisco"
}

ssh = ConnectHandler(**cisco_device)
if ssh:
	print("Connection Success !")
	print("\n*********************************")

output = ssh.send_command("sh ip int br")
print(output)
