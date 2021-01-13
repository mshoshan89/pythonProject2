from netmiko import ConnectHandler

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

    print("\n-------------------------------------")
    print("Connecting to device:", devices.strip())
    print("---------------------------------------")

    # Establish SSH connection to devices.txt
    net_connect = ConnectHandler(**ios_device)

    # Push command "hostname Swx" in Configuration mode for every device
    output = net_connect.send_config_set("hostname R1")
    print(output)
