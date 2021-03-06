from scapy.all import Dot11, sniff

iface = "wlan0mon"
ap_list = []


def packetHandler(packet):
    if packet.haslayer(Dot11):
        if packet.type == 0 and packet.subtype == 8:
            if packet.addr2 not in ap_list:
                ap_list.append(packet.addr2)
                print("Access Point MAC: {} with SSID: {}".format(
                    packet.addr2, packet.info))


sniff(iface=iface, prn=packetHandler)
