import argparse
import ipaddress

def parse_cidr_to_addresses(cidr):
    """Convert a CIDR block to a list of addressable IPs."""
    try:
        network = ipaddress.ip_network(cidr, strict=False)
        return [str(ip) for ip in network.hosts()]
    except ValueError as e:
        print(f"Invalid CIDR block: {cidr}. Error: {e}")
        return []

def process_file(filepath):
    """Read CIDR blocks from a file and convert them to addressable IPs."""
    try:
        with open(filepath, 'r') as file:
            lines = file.readlines()
        results = {}
        for line in lines:
            cidr = line.strip()
            results[cidr] = parse_cidr_to_addresses(cidr)
        return results
    except FileNotFoundError:
        print(f"File not found: {filepath}")
        return {}

def main():
    parser = argparse.ArgumentParser(description="Convert CIDR blocks to addressable IP addresses.")
    parser.add_argument("input", type=str, help="A CIDR block or a file containing CIDR blocks.")
    parser.add_argument("-f", "--file", action="store_true", help="Specify if the input is a file.")

    args = parser.parse_args()

    if args.file:
        # Process file containing CIDR blocks
        results = process_file(args.input)
        for cidr, addresses in results.items():
            print(f"{cidr}:")
            for addr in addresses:
                print(f"  {addr}")
    else:
        # Process a single CIDR block
        addresses = parse_cidr_to_addresses(args.input)
        for addr in addresses:
            print(addr)

if __name__ == "__main__":
    main()