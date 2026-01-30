from scapy.all import sniff, IP, TCP, UDP, ICMP

def analyze_packet(packet):
    if IP in packet:
        src_ip = packet[IP].src
        dst_ip = packet[IP].dst
        protocol = "OTHER"

        if TCP in packet:
            protocol = "TCP"
            payload = bytes(packet[TCP].payload)[:50]
        elif UDP in packet:
            protocol = "UDP"
            payload = bytes(packet[UDP].payload)[:50]
        elif ICMP in packet:
            protocol = "ICMP"
            payload = b""

        print("=" * 60)
        print(f"Source IP      : {src_ip}")
        print(f"Destination IP : {dst_ip}")
        print(f"Protocol       : {protocol}")

        if payload:
            try:
                print(f"Payload        : {payload.decode(errors='ignore')}")
            except:
                print("Payload        : <binary data>")
        else:
            print("Payload        : None")

def main():
    print("🚨 Network Packet Analyzer Started")
    print("⚠️ Run ONLY with permission")
    print("Press CTRL+C to stop\n")

    sniff(prn=analyze_packet, store=False)

if __name__ == "__main__":
    main()
