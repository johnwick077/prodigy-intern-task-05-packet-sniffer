from scapy.all import sniff

# Function to display packet details
def packet_callback(packet):
    print(f"Packet Captured: {packet.summary()}")
    
    # Extract and display IP information if the packet is IP
    if packet.haslayer('IP'):
        ip_src = packet['IP'].src
        ip_dst = packet['IP'].dst
        print(f"Source IP: {ip_src}")
        print(f"Destination IP: {ip_dst}")
    
    # Display protocol type
    if packet.haslayer('TCP'):
        print(f"Protocol: TCP")
    elif packet.haslayer('UDP'):
        print(f"Protocol: UDP")
    else:
        print(f"Protocol: {packet.proto}")
    
    # Display payload data if available
    if packet.haslayer('Raw'):
        payload_data = packet['Raw'].load
        print(f"Payload Data: {payload_data}\n")

# Start sniffing network packets
def start_sniffing():
    print("Starting packet capture...")
    sniff(prn=packet_callback, store=0)

if __name__ == "__main__":
    start_sniffing()
