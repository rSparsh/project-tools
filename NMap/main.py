import nmap as nm
import input

p = input.port
scanner = nm.PortScanner()

def synack_scan():
    scanner.scan(p, '1-1024', '-v -sS')
    print(scanner.scaninfo())
    print("Ip Status: ", scanner[p].state())
    print("protocols:", scanner[p].all_protocols())
    print("Open Ports: ", scanner[p]['tcp'].keys())

def udp_scan():
    print("Nmap Version: ", scanner.nmap_version())
    scanner.scan(p, '1-1024', '-v -sU')
    print(scanner.scaninfo())
    print("Ip Status: ", scanner[p].state())
    print("protocols:", scanner[p].all_protocols())
    print("Open Ports: ", scanner[p]['udp'].keys())

def comp_scan():
    print("Nmap Version: ", scanner.nmap_version())
    scanner.scan(p, '1-1024', '-v -sS -sV -sC -A -O')
    print(scanner.scaninfo())
    print("Ip Status: ", scanner[p].state())
    print(scanner[p].all_protocols())
    print("Open Ports: ", scanner[p]['tcp'].keys())

def reg_scan():
    scanner.scan(p)
    print(scanner.scaninfo())
    print("Ip Status: ", scanner[p].state())
    print(scanner[p].all_protocols())
    print("Open Ports: ", scanner[p]['tcp'].keys())



def ping_scan():
    scanner.scan(hosts=p, arguments='-n -sP -PE -PA21,23,80,3389')
    hosts_list = [(x, scanner[x]['status']['state']) for x in scanner.all_hosts()]
    counter = 0
    for host, status in hosts_list:
        print('{0}:{1}'.format(host, status))
        counter += 1
    if counter == 0:
        print("Either the host is down or the system is private")


