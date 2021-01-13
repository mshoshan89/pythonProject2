from netmiko import ConnectHandler

cisco_switches = ["192.168.1.10", "192.168.1.11", "192.168.1.12", "192.168.1.13"]

for ip in cisco_switches:
    ssh_info = {
        "device_type": "cisco_ios",
        "host": ip.strip(),
        "username": "admin",
        "password": "cisco",
        "secret": "cisco"
    }
    net_connect = ConnectHandler(**ssh_info)

    print("Logging successfully")
    output = net_connect.send_command("show runn | i hostname")
    print(output)
