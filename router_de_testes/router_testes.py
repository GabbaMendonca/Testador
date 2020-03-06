"""
ssh 10.121.2.8
Login : oi369932
Senha : 1234

ssh cen-ce-ser-a01
"""


#sh ip bg su | i :
def __sh_ip_bg_su__i():
    print("100.127.119.169 4         7738     480     297    14699    0    0 02:14:56     1041")


# sh ver | i power | up
def __sh_ver__i_power__up():
    print("FLA_5983243_FSVASCONCELOS uptime is 1 day, 5 hours, 26 minutes")


# sh ip int br
def __sh_ip_int_br():
    print("""Interface                  IP-Address      OK? Method Status                Protocol
Embedded-Service-Engine0/0 unassigned      YES NVRAM  administratively down down
GigabitEthernet0/0         unassigned      YES NVRAM  up                    up
GigabitEthernet0/0.1201    100.127.119.170 YES NVRAM  up                    up
GigabitEthernet0/1         10.60.80.3      YES NVRAM  up                    up
Serial0/0/0                unassigned      YES NVRAM  administratively down down
Loopback0                  100.127.200.112 YES NVRAM  up                    up""")


#sh int | i Last clearing
def __sh_int__i_Last_clearing():
    print("""  Last clearing of "show interface" counters never
  Last clearing of "show interface" counters never
  Last clearing of "show interface" counters never
  Last clearing of "show interface" counters never
  Last clearing of "show interface" counters never
  Last clearing of "show interface" counters never""")


#sh int | i CRC
def __sh_int__i_CRC():
    print("""     0 input errors, 0 CRC, 0 frame, 0 overrun, 0 ignored
     0 input errors, 0 CRC, 0 frame, 0 overrun, 0 ignored
     0 input errors, 0 CRC, 0 frame, 0 overrun, 0 ignored
     0 input errors, 0 CRC, 0 frame, 0 overrun, 0 ignored, 0 abort
     0 input errors, 0 CRC, 0 frame, 0 overrun, 0 ignored, 0 abort""")


#sh int Serial0/0/0
def __sh_int_Serial0_0_0():
    print("""Serial0/0/0 is administratively down, line protocol is down
  Hardware is WIC MBRD Serial
  MTU 1500 bytes, BW 1544 Kbit/sec, DLY 20000 usec,
     reliability 255/255, txload 1/255, rxload 1/255
  Encapsulation HDLC, loopback not set
  Keepalive set (10 sec)
  Last input never, output never, output hang never
  Last clearing of "show interface" counters never
  Input queue: 0/75/0/0 (size/max/drops/flushes); Total output drops: 0
  Queueing strategy: fifo
  Output queue: 0/40 (size/max)
  5 minute input rate 0 bits/sec, 0 packets/sec
  5 minute output rate 0 bits/sec, 0 packets/sec
     0 packets input, 0 bytes, 0 no buffer
     Received 0 broadcasts (0 IP multicasts)
     0 runts, 0 giants, 0 throttles
     0 input errors, 0 CRC, 0 frame, 0 overrun, 0 ignored, 0 abort
     0 packets output, 0 bytes, 0 underruns
     0 output errors, 0 collisions, 3 interface resets
     0 unknown protocol drops
     0 output buffer failures, 0 output buffers swapped out
     0 carrier transitions
     DCD=down  DSR=down  DTR=down  RTS=down  CTS=down
""")


#sh arp
def __sh_arp():
    print("""Protocol  Address          Age (min)  Hardware Addr   Type   Interface
Internet  10.60.80.3              -   80e0.1dcf.04c1  ARPA   GigabitEthernet0/1
Internet  10.60.80.5              2   943f.c2be.8fa6  ARPA   GigabitEthernet0/1
Internet  10.60.80.10             3   eceb.b8f5.1f60  ARPA   GigabitEthernet0/1
Internet  100.127.119.169       134   e481.8482.b639  ARPA   GigabitEthernet0/0.1201
Internet  100.127.119.170         -   80e0.1dcf.04c0  ARPA   GigabitEthernet0/0.1201""")


#sh int Serial0/0/0 | i counters | CRC
def __sh_int_Serial0_0_0__i_counters__CRC():
    print("""  Last clearing of "show interface" counters 00:03:01
     0 input errors, 0 CRC, 0 frame, 0 overrun, 0 ignored, 0 abort""")


from itertools import count
import time
from random import randint


# ===================================================================
#ping
def __ping(repetir=5, perda=False, passo_perda=2):
    pacotes_enviados = 0
    ger_pacote = count()

    print("""Type escape sequence to abort.
Sending 500, 1500-byte ICMP Echos to 192.168.1.23, timeout is 2 seconds:""")

    for pacote in ger_pacote:

        if perda == True:

            if randint(1,3) == 1:
                print(".", end="")
            else:
                pacotes_enviados += 1
                print("!", end="")

        else:

            pacotes_enviados += 1
            print("!", end="")

        time.sleep(0.5)

        if pacote == (repetir-1):
            break

    porcentagem = round( pacotes_enviados * 100 / repetir )
    print('\nSuccess rate is {0} percent ({1}/{2}), round-trip min/avg/max = 68/70/204 ms'
          .format(porcentagem, pacotes_enviados, repetir))


# ===================================================================
# CPE
def cpe():
    login = input("""
*******************************************************************************
                              OI - Simples Assim!

    Cliente: MAGAZINE LUIZA SA
    Circuito: FLA FLA VM 5983243
    Equipamento: FLA_5983243_FSVASCONCELOS

 Warning! The use of this system is restricted to authorized users.
 All information and communications on this system are subject to review,
 monitoring and recording at any time, without notice or permission.
 Unauthorized access or use shall be subject to prosecution.

 Atencao! A utilizacao desse sistema e limitado a usuarios autorizados.
 Todas as informacoes e comunicacoes sobre este sistema estao sujeitos ao
 monitoramento e gravacao a qualquer momento, sem previo aviso ou autorizacao.
 O Acesso ou uso nao autorizado estara sujeito as medidas legais.

*******************************************************************************


User Access Verification

Username: """)

    senha = input("Password: ")

    if login != "oi369932" or senha != "1234":
        print("% Authentication failed")
        return

    print('\n"NAO ESQUECA SALVAR A CONFIGURACAO DO ROUTER NA NVRAM, APOS CONSOLIDADA(s) A(s) ALTERACAO(OES) !! " \n')

    ena = False
    while True:

        if ena == True:
            entrada = input("FLA_5983243_FSVASCONCELOS#")
        else:
            entrada = input("FLA_5983243_FSVASCONCELOS>")

        if "ena" == entrada:
            senha = input("Password:")
            if senha == "1234":
                ena = True

        if "sh ver | i power | up" == entrada:
            __sh_ver__i_power__up()

        if "sh ip bg su | i :" == entrada:
            __sh_ip_bg_su__i()

        if "sh ip int br" == entrada:
            __sh_ip_int_br()

        if "sh int | i Last clearing" == entrada:
            __sh_int__i_Last_clearing()

        if "sh int | i CRC" == entrada:
            __sh_int__i_CRC()

        if "sh int Serial0/0/0" == entrada:
            __sh_int_Serial0_0_0()

        if "sh arp" == entrada:
            __sh_arp()


        if "ping p" == entrada:
            __ping(perda=True)

        if "ping" == entrada:
            __ping()

        if "ping 192.168.1.23" == entrada:
            __ping()

        if "ping 192.168.1.23 r 10 size 1500" == entrada:
            __ping(repetir=10)


        if "logout" == entrada:
            print("Connection to cen-ce-ser-a01 closed.")
            break


# ===================================================================

def bgp():
    print("""
===============================================================================
 BGP Router ID:200.223.230.168  AS:7738        Local AS:7738
===============================================================================
BGP Admin State         : Up          BGP Oper State              : Up
Total Peer Groups       : 1           Total Peers                 : 1
Total BGP Paths         : 201         Total Path Memory           : 42008
Total IPv4 Remote Rts   : 16          Total IPv4 Rem. Active Rts  : 16
Total McIPv4 Remote Rts : 0           Total McIPv4 Rem. Active Rts: 0
Total McIPv6 Remote Rts : 0           Total McIPv6 Rem. Active Rts: 0
Total IPv6 Remote Rts   : 0           Total IPv6 Rem. Active Rts  : 0
Total IPv4 Backup Rts   : 0           Total IPv6 Backup Rts       : 0

Total Supressed Rts     : 0           Total Hist. Rts             : 0
Total Decay Rts         : 0

Total FlowIpv4 Rem Rts  : 0           Total FlowIpv4 Rem Act Rts  : 0
Total FlowIpv6 Rem Rts  : 0           Total FlowIpv6 Rem Act Rts  : 0

===============================================================================
BGP Summary
===============================================================================
Neighbor
                   AS PktRcvd InQ  Up/Down   State|Rcv/Act/Sent (Addr Family)
                      PktSent OutQ
-------------------------------------------------------------------------------
100.127.43.106
                65000 1142376    0 14h39m13s 16/16/1161 (IPv4)
                         1897    0
-------------------------------------------------------------------------------""")

def localizar_serial():
    print("8/1/11         BLM BLM VM 5625641; COMPANHIA BRASILEIRA DE DISTRIBUICAO; TC VPN")

def localizar_serial_2():
    print("5/2/3.1.4.3.2  PAA PAA VM 5010511; WAL MART BRASIL LTDA;TC VPN VIP")

def show_port_2_associations():
    print("""
============================================================================
Interface Table
============================================================================
Router/ServiceId                Name                            Encap Val
----------------------------------------------------------------------------
Service: 7804                   PAA_5010511                     
----------------------------------------------------------------------------
Interfaces
============================================================================""")

def show_port_2():
    print("""
============================================================================
TDM DS0 Chan Group
============================================================================
Description        : PAA PAA VM 5010511; WAL MART BRASIL LTDA;TC VPN VIP
Interface          : 5/2/3.1.4.3.2           
TimeSlots          : 2-17
Speed              : 64                      CRC                  : 16
Admin Status       : up                      Oper Status          : down
BER SF Link Down   : disabled                 """)

def show_port_2_ppp():
    print("""
============================================================================
PPP Protocols for 5/2/3.1.4.3.2
============================================================================
Protocol  State      Last Change         Restart Count   Last Cleared
----------------------------------------------------------------------------
lcp       ack sent   10/23/2014 07:16:15         29      09/10/2014 03:57:33
ipcp      initial    10/23/2014 04:38:07         28      09/10/2014 03:57:33
mplscp    initial    08/01/2014 02:52:49          0      09/10/2014 03:57:33
bcp       initial    08/01/2014 02:52:49          0      09/10/2014 03:57:33
osicp     initial    08/01/2014 02:52:49          0      09/10/2014 03:57:33
ipv6cp    initial    08/01/2014 02:52:49          0      09/10/2014 03:57:33
============================================================================

============================================================================
PPP Statistics
============================================================================
Local Mac address  : 7c:20:64:59:3d:df  Remote Mac address :                  
Local Magic Number : 0x0                Remote Magic Number: 0x0
Local IPv4 address : 100.126.88.93      Remote IPv4 address: 0.0.0.0 (*****)
Local IPv6 address : ::
Remote IPv6 address: ::
Line Monitor Method: keepalive
Keepalive statistics

Request interval   : 10           Threshold exceeded : 12
Drop Count         : 3            In packets         : 364149
Time to link drop  : 00h00m30s    Out packets        : 364195
Last cleared time  : 09/10/2014 03:57:33

PPP Header Compression
 ACFC              : Disabled     PFC                : Disabled
============================================================================
""")

def show_port():
    print("""
===============================================================================
Ethernet Interface
===============================================================================
Description        : BLM BLM VM 5625641; COMPANHIA BRASILEIRA DE DISTRIBUICAO;
                     TC VPN VIP
Interface          : 8/1/11                     Oper Speed       : 100 mbps
Link-level         : Ethernet                   Config Speed     : 100 mbps
Admin State        : up                         Oper Duplex      : full
Oper State         : up                         Config Duplex    : full
Physical Link      : Yes                        MTU              : 1564
Single Fiber Mode  : No                         Min Frame Length : 64 Bytes
IfIndex            : 270893056                  Hold time up     : 0 seconds
Last State Change  : 07/15/2019 11:54:48        Hold time down   : 0 seconds
Last Cleared Time  : N/A                        DDM Events       : Enabled
Phys State Chng Cnt: 27

Configured Mode    : access                     Encap Type       : 802.1q
Dot1Q Ethertype    : 0x8100                     QinQ Ethertype   : 0x8100
PBB Ethertype      : 0x88e7
Ing. Pool % Rate   : 100                        Egr. Pool % Rate : 100
Ing. Pool Policy   : n/a
Egr. Pool Policy   : n/a
Net. Egr. Queue Pol: default
Egr. Sched. Pol    : n/a
Auto-negotiate     : false                      MDI/MDX          : MDX
Oper Phy-tx-clock  : not-applicable
Accounting Policy  : None                       Collect-stats    : Disabled
Acct Plcy Eth Phys : None                       Collect Eth Phys : Disabled
Egress Rate        : Default                    Ingress Rate     : Default
Load-balance-algo  : Default                    LACP Tunnel      : Disabled

Down-when-looped   : Disabled                   Keep-alive       : 10
Loop Detected      : False                      Retry            : 120
Use Broadcast Addr : False

Sync. Status Msg.  : Disabled                   Rx Quality Level : N/A
Tx DUS/DNU         : Disabled                   Tx Quality Level : N/A
SSM Code Type      : sdh

Down On Int. Error : Disabled

CRC Mon SD Thresh  : Disabled                   CRC Mon Window   : 10 seconds
CRC Mon SF Thresh  : Disabled

Configured Address : a4:7b:2c:e7:cc:99
Hardware Address   : a4:7b:2c:e7:cc:99

Transceiver Data

Transceiver Type   : SFP
Model Number       : 3HE00062AAAA01  ALA  IPUIAEHDAA
TX Laser Wavelength: 0 nm                       Diag Capable     : no
Connector Code     : Unknown                    Vendor OUI       : 00:90:65
Manufacture date   : 2008/07/03                 Media            : Ethernet
Serial Number      : PE13JVJ
Part Number        : FCMJ-8521-3-A5
Optical Compliance : GIGE-T
Link Length support: 100m for copper

===============================================================================
Traffic Statistics
===============================================================================
                                                   Input                 Output
-------------------------------------------------------------------------------
Octets                                     1853775881637          2617787746929
Packets                                       4711706693             3825366911
Errors                                                 0                      0
===============================================================================

===============================================================================
Port Statistics
===============================================================================
                                                   Input                 Output
-------------------------------------------------------------------------------
Unicast Packets                               4670313691             3825349949
Multicast Packets                               41376392                      0
Broadcast Packets                                  16610                  16962
Discards                                               0                      0
Unknown Proto Discards                                 0
===============================================================================

===============================================================================
Ethernet-like Medium Statistics
===============================================================================

Alignment Errors :                   0  Sngl Collisions  :                   0
FCS Errors       :                   0  Mult Collisions  :                   0
SQE Test Errors  :                   0  Late Collisions  :                   0
CSE              :                   0  Excess Collisns  :                   0
Too long Frames  :                   0  Int MAC Tx Errs  :                   0
Symbol Errors    :                   0  Int MAC Rx Errs  :                   0
In Pause Frames  :                   0  Out Pause Frames :                   0
===============================================================================""")

def monitor_port():
    print("""
===============================================================================
Monitor statistics for Port 6/1/2.1.1.1.1
===============================================================================
                                                   Input                 Output
-------------------------------------------------------------------------------
-------------------------------------------------------------------------------
At time t = 0 sec (Base Statistics)
-------------------------------------------------------------------------------
Octets                                             38544                  33070
Packets                                              843                    855
Errors                                                 0                      0

-------------------------------------------------------------------------------
At time t = 3 sec (Mode: Delta)
-------------------------------------------------------------------------------
Octets                                                32                     32
Packets                                                2                      2
Errors                                                 0                      0

-------------------------------------------------------------------------------
At time t = 6 sec (Mode: Delta)
-------------------------------------------------------------------------------
Octets                                                 0                      0
Packets                                                0                      0
Errors                                                 0                      0

-------------------------------------------------------------------------------
At time t = 9 sec (Mode: Delta)
-------------------------------------------------------------------------------
Octets                                                 0                      0
Packets                                                0                      0
Errors                                                 0                      0

-------------------------------------------------------------------------------
At time t = 12 sec (Mode: Delta)
-------------------------------------------------------------------------------
Octets                                                14                     14
Packets                                                1                      1
Errors                                                 0                      0

-------------------------------------------------------------------------------
At time t = 15 sec (Mode: Delta)
-------------------------------------------------------------------------------
Octets                                                18                     18
Packets                                                1                      1
Errors                                                 0                      0

-------------------------------------------------------------------------------
At time t = 18 sec (Mode: Delta)
-------------------------------------------------------------------------------
Octets                                                 0                      0
Packets                                                0                      0
Errors                                                 0                      0

-------------------------------------------------------------------------------
At time t = 21 sec (Mode: Delta)
-------------------------------------------------------------------------------
Octets                                                14                     14
Packets                                                1                      1
Errors                                                 0                      0

-------------------------------------------------------------------------------
At time t = 24 sec (Mode: Delta)
-------------------------------------------------------------------------------
Octets                                                18                     18
Packets                                                1                      1
Errors                                                 0                      0

-------------------------------------------------------------------------------
At time t = 27 sec (Mode: Delta)
-------------------------------------------------------------------------------
Octets                                                 0                      0
Packets                                                0                      0
Errors                                                 0                      0

-------------------------------------------------------------------------------
At time t = 30 sec (Mode: Delta)
-------------------------------------------------------------------------------
Octets                                                14                     14
Packets                                                1                      1
Errors                                                 0                      0

===============================================================================""")

# PE de Borda
def pe_alcatel():
    yes_no = input("""
The authenticity of host 'cen-ce-ser-a01 (200.195.96.17)' can't be established.
RSA key fingerprint is 07:74:ef:10:62:23:15:24:2e:b2:c5:11:9b:f9:b9:2a.
Are you sure you want to continue connecting (yes/no)? """)

    if yes_no == "yes":
        senha = input("""
Warning: Permanently added 'cen-ce-ser-a01,200.195.96.17' (RSA) to the list of known hosts.
******************************************************************************************
**********                             Roteador CEN-CE-SER-A01                  **********
**********  Only authorized person has the right to access to this equipament.  **********
**********               Other are urged to log off IMEDIATELY !!               **********
**********      Somente pessoal autorizado pode acessar este equipamento.       **********
**********  Se ha razao para acessar este equipamento, identifique-se ABAIXO.   **********
******************************************************************************************
oi369932@cen-ce-ser-a01's password: """)

        if senha == "1234":
            while True:
                entrada = input("*A:CEN-CE-SER-A01# ")

                if entrada == "logout":
                    print("Connection to cen-ce-ser-a01 closed.")
                    break
                if entrada == "telnet router 5104 100.127.119.170" or entrada == "n":
                    print("Trying 100.127.119.170 ... ")
                    cpe()
                if entrada == "ena":
                    pass
                if entrada == "ping router 5104 100.127.119.170":
                    __ping()
                if entrada == "show router 5104 bgp summary neighbor 100.127.119.170":
                    bgp()

                if entrada == "show port description | match 5625641":
                    localizar_serial()
                if entrada == "show port 8/1/11":
                    show_port()
                if entrada == "monitor port 8/1/11 interval 3":
                    monitor_port()

                if entrada == "show port description | match 5010511":
                    localizar_serial_2()
                if entrada == "show port 5/2/3.1.4.3.2":
                    show_port_2()
                if entrada == "show port 5/2/3.1.4.3.2 ppp":
                    show_port_2_ppp()
                if entrada == "show port 5/2/3.1.4.3.2 associations":
                    show_port_2_associations()


# ===================================================================
# Maquina Testes
def servidor_de_testes():

    login = input("Login : ")
    senha = input("Senha : ")

    if login != "oi369932" or senha != "1234":
        print("Acesso negado !")
        return

    print("""
-----------------------------------------------------------
-                  _________  ___ ______                  -
-                  | ___ \  \/  |/  ___|                  -
-                  | |_/ / .  . |\ `--.                   -
-                  |    /| |\/| | `--. \                  -
-                  | |\ \| |  | |/\__/ /                  -
-                  \_| \_\_|  |_/\____/                   -
-                                                         -
-                       GATEWAY R1                        -
-                 Oi - Simples assim                      -
-                                                         -
-      USO RESTRITO - Todas as acoes serao logadas        -
-                                                         -
-      Acesso RMS:      PRA 10.121.241.94                 -
-                       PRA 10.121.241.165                -
-                       ARC 10.121.2.8                    -
-                       ARC 10.121.2.61                   -
-                                                         -
-                                                         -
-  Contato: LD-SN3SRAC                                    -
-----------------------------------------------------------
Last login: Thu Oct 17 14:42:11 2019 from 10.11.126.143
Acesso restrito a usuarios autorizados.
    """)

    while True:
        entrada = input("oi369932@ARC-RJ-GWA-01> ")

        if entrada == "exit":
            break
        if entrada == "ssh cen-ce-ser-a01" or entrada == "n":
            pe_alcatel()


# ===================================================================
# Minha maquina
while True:
    entrada = input("minha_maquina> ")

    if entrada == "exit":
        break
    if entrada == "ssh 10.121.2.8" or entrada == "n":
        servidor_de_testes()
    if entrada == "cpe":
        cpe()