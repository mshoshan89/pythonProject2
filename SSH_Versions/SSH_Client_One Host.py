from netmiko import ConnectHandler

session = {
	"device_type": "cisco_ios",
	"host": "192.168.1.10",
	"username": "admin",
	"password": "cisco",
	"secret": "cisco"
}

ssh_session = ConnectHandler(**session)

if ssh_session:
	print("Connection successfully !")
	print("\n--------------------------------------")

output = ssh_session.send_command("show ip int br")
print(output)
