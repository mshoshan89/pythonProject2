from netmiko import ConnectHandler

cisco_switches = ["192.168.1.10", "192.168.1.11", "192.168.1.12"]

for ip in cisco_switches:
    connection = {
        "device_type": "cisco_ios",
        "host": ip.strip(),
        "username": "admin",
        "password": "cisco",
        "secret": "cisco"
    }
    net_connect = ConnectHandler(**connection)
    output = net_connect.send_command("show ip int br")
    print(output)