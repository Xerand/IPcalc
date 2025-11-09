####################
#      IPcalc      #
####################

viola = "\033[35m"
giallo = "\033[33m"
verde = "\033[32m"
rosso = "\033[31m"
reset = "\033[0m"
errore = f"  {rosso}IP in formato non corretto{reset}\n"


print(f"""┌─{viola}[ I P w i z a r d ]{reset}──────────────────────────────────────┐
│ Network toolkit  •  CIDR / Netmask / Network / Broadcast │
└──────────────────────────────────────────────────────────┘""")

while True:
    IP = input("  Inserisci IP nella forma <>.<>.<>.<>/<>: ")
    
    try:
        parts = IP.split('.')
        IPa, IPb, IPc, IPd_cidr = parts
        IPd, cidr = IPd_cidr.split('/')
    except:
        print(errore) 
        continue

    try:
        IPa = int(IPa)
        IPb = int(IPb)
        IPc = int(IPc)
        IPd = int(IPd)
        cidr = int(cidr)
    except:
        print(errore) 
        continue
    
    if (IPa > 256 or IPb > 256 or IPc > 256 or IPd > 256 or cidr > 32):
        print(errore) 
    else:
        break;

print(f"\n  {giallo}{'Address:':<12}{verde}{'.'.join([str(IPa),str(IPb),str(IPc),str(IPd)]):<16}{reset}{format(IPa, '08b')} {format(IPb, '08b')} {format(IPc, '08b')} {format(IPd, '08b')}")
print(f"  {giallo}{'CIDR:':<12}{verde}{cidr}{reset}")

### Calcolo maschera di rete
Ma = ""
for i in range(1, 9):
    if (i <= cidr):
        Ma = Ma + "1"
    else:
        Ma = Ma + "0"

Mb = ""
for i in range(9, 17):
    if (i <= cidr):
        Mb = Mb + "1"
    else:
        Mb = Mb + "0"

Mc = ""
for i in range(17, 25):
    if (i <= cidr):
        Mc = Mc + "1"
    else:
        Mc = Mc + "0"

Md = ""
for i in range(25, 33):
    if (i <= cidr):
        Md = Md + "1"
    else:
        Md = Md + "0"
        
Ma = int(Ma, 2)
Mb = int(Mb, 2)
Mc = int(Mc, 2)
Md = int(Md, 2)

print(f"  {giallo}{'Netmask:':<12}{verde}{'.'.join([str(Ma),str(Mb),str(Mc),str(Md)]):<16}{reset}{format(Ma, '08b')} {format(Mb, '08b')} {format(Mc, '08b')} {format(Md, '08b')}")

if (cidr == 32):
    exit
else:
    ### Calcolo ID di rete
    IDa = IPa & Ma # & esegue l'AND bit a bit tra le due variabili
    IDb = IPb & Mb
    IDc = IPc & Mc
    IDd = IPd & Md

    print(f"  {giallo}{'Network:':<12}{verde}{'.'.join([str(IDa),str(IDb),str(IDc),str(IDd)]):<16}{reset}{format(IDa, '08b')} {format(IDb, '08b')} {format(IDc, '08b')} {format(IDd, '08b')}")

    ### Calcolo indirizzo di Broadcast
    IMa = ~Ma & 0xFF # Con l'operatore bitwise NOT (~) inverto i bit della subnet mask entro 8bit (& 0xFF)
    IMb = ~Mb & 0xFF
    IMc = ~Mc & 0xFF
    IMd = ~Md & 0xFF

    Ba = IDa | IMa # | esegue l'OR bit a bit tra le due variabili
    Bb = IDb | IMb
    Bc = IDc | IMc
    Bd = IDd | IMd

    print(f"  {giallo}{'Broadcast:':<12}{verde}{'.'.join([str(Ba),str(Bb),str(Bc),str(Bd)]):<16}{reset}{format(Ba, '08b')} {format(Bb, '08b')} {format(Bc, '08b')} {format(Bd, '08b')}")

    if (cidr == 31):
        exit
    else:
        ### Calcolo host
        num_host = (2 ** (32 - cidr)) - 2
        print(f"  {giallo}{'Hosts:':<12}{verde}{num_host}{reset}")

        ### HostMin
        HMin_a = IDa
        HMin_b = IDb
        HMin_c = IDc
        HMin_d = IDd + 1

        print(f"  {giallo}{'HostMin:':<12}{verde}{'.'.join([str(HMin_a),str(HMin_b),str(HMin_c),str(HMin_d)]):<16}{reset}{format(HMin_a, '08b')} {format(HMin_b, '08b')} {format(HMin_c, '08b')} {format(HMin_d, '08b')}")

        ### HostMax
        HMax_a = Ba
        HMax_b = Bb
        HMax_c = Bc
        HMax_d = Bd - 1

        print(f"  {giallo}{'HostMax:':<12}{verde}{'.'.join([str(HMax_a),str(HMax_b),str(HMax_c),str(HMax_d)]):<16}{reset}{format(HMax_a, '08b')} {format(HMax_b, '08b')} {format(HMax_c, '08b')} {format(HMax_d, '08b')}")