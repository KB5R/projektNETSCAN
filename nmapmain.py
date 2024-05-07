import nmap3
import json
import subprocess






# TCP SYN Scan (-sS)
#def syn_scan(host):
#    nmap = nmap3.Nmap()
#    scan_results = nmap.nmap_os_detection(host)
#   print(json.dumps(scan_results, indent=2))

#host = input('Введите IP адрес или DNS имя для SYN cканирования: ')
#syn_scan(host)

# TCP connect() scan (-sT)

def tcp_scan(host):
    nmap = nmap3.NmapScanTechniques()
    scan_results = nmap.nmap_tcp_scan(host)
    ports = [(f"port: {port['portid']}\n"
              f"state: {port['state']}\n"
              f"name: {port['service']['name']}\n"
              f"protocol: {port['protocol']}\n")
        for port in scan_results[host]['ports']
    ]
    return ports


host = '10.255.250.56'
ports = tcp_scan(host)
print("\n".join(ports))


# FIN Scan (-sF)

def fin_scan(host):
    nmap = nmap3.NmapScanTechniques()
    scan_results = nmap.nmap_fin_scan(host)
    print(json.dumps(scan_results, indent=2))
#host = input('Введите IP адрес или DNS имя для FIN cканирования: ')
#fin_scan(host)

def syn_scan(host):
    nmap = nmap3.Nmap()
    scan_results = nmap.nmap_os_detection(host)
    if "error" in scan_results.keys():
        print(scan_results["msg"])
        return
    oss = [item['name'] for item in scan_results[host]['osmatch']]
    return oss
#host = input('Введите IP адрес или DNS имя для SYN cканирования: ')
#names = syn_scan(host)
#print(names)




# Пинг-сканирование (-sP)

def ping_scan(host):
    nmap = nmap3.NmapScanTechniques()
    scan_results = nmap.nmap_ping_scan(host)
    print(json.dumps(scan_results, indent=2))

#host = input('Введите IP адрес для ping сканирования\n'
#           'Пример:192.168.1.1/24: Такой формат ввода сканирует всю подсеть\n'
#            'Пример:192.168.1.10:Такой формат ввода сканирует конкретную машину\n '
#            'Введите адрес: ')
#ping_scan(host)










#nmap = nmap3.Nmap()
#results = nmap.scan_top_ports("10.255.250.52")
#print(results)

#input()

def trace_route(ip_address):
    result = subprocess.run(['tracert', ip_address], capture_output=True, text=True)

    if result.returncode == 0:
        print(result.stdout)
    else:
        print("Error executing tracert:", result.stderr)


#tracertIP = input('Введите адрес для трассировким')
#trace_route(tracertIP)



