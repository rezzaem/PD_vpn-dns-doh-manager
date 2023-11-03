# import wmi

# def get_dns_servers():
#     c = wmi.WMI()
#     for interface in c.Win32_NetworkAdapterConfiguration(IPEnabled=True):
#         if interface.DNSServerSearchOrder:
#             return interface.DNSServerSearchOrder

#     return None

# # Get the current DNS servers
# dns_servers = get_dns_servers()
# if dns_servers:
#     if len(dns_servers) >= 2:
#         print(f"The current primary DNS server is: {dns_servers[0]}")
#         print(f"The current secondary DNS server is: {dns_servers[1]}")
#     else:
#         print(f"The current DNS server is: {dns_servers[0]}")
# else:
#     print("No DNS servers found.")

import wmi

def set_dns_servers(primary_dns, secondary_dns=None):
    c = wmi.WMI()
    for interface in c.Win32_NetworkAdapterConfiguration(IPEnabled=True):
        if interface.DNSServerSearchOrder:
            if secondary_dns:
                dns = [primary_dns, secondary_dns]
            else:
                dns = [primary_dns]
            return interface.SetDNSServerSearchOrder(dns)

    return None

# Set the DNS servers
primary_dns_server = "1.1.1.1"  # Change this to your desired primary DNS server
secondary_dns_server = "1.0.0.1"  # Change this to your desired secondary DNS server if applicable

result = set_dns_servers(primary_dns_server, secondary_dns_server)
if result == 0:
    print("DNS servers have been successfully updated.")
else:
    print("Failed to update DNS servers.")

x=input("for test : ")