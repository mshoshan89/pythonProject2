
import telnetlib

Device_IP = input("Pls enter Device IP: ")
Username = input("Pls enter your username: ")
Password = input("Pls enter your password: ")

connection = telnetlib.Telnet(host=Device_IP)

connection.read_until(b"Username: ")
connection.write(Username.encode("ascii") + b"\n")

connection.read_until(b"Password: ")
connection.write(Password.encode("ascii") + b"\n")

# connection.read_until(b">")
# connection.write("enable".encode("ascii") + b"\n")

connection.read_until(b"#")
connection.write(b"terminal length 0" + b"\n")

connection.read_until(b"#")

print("")
print("Login Successfully to host: ", Device_IP)
print("")

while True:
	command = input("Pls enter your command: ")
	connection.write(command.encode("ascii") + b"\n")

	output = connection.read_until(b"#")
	print(output.decode("ascii"))

	if command == "exit" or command == "Exit" or command == "EXIT":
		break
