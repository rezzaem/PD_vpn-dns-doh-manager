from command_runner.elevate import elevate
from command_runner import command_runner



def main():
    exit_code, output = command_runner('netsh interface ipv4 delete dnsservers "wi-Fi" all')

if __name__ == '__main__':
    elevate(main)