import requests
import dns.resolver
import sys
import threading
from queue import Queue

# Wordlist for subdomain brute-forcing
wordlist = ["www", "mail", "api", "dev", "ftp", "staging", "blog", "test", "shop"]

# Target domain
target_domain = "example.com"

# Threading for faster resolution
q = Queue()

# Function to resolve subdomains using DNS
def resolve_subdomain(subdomain):
    try:
        result = dns.resolver.resolve(subdomain + "." + target_domain, "A")
        for ip in result:
            print(f"[+] Found subdomain: {subdomain}.{target_domain} -> {ip}")
    except dns.resolver.NXDOMAIN:
        pass
    except dns.resolver.NoAnswer:
        pass
    except Exception as e:
        print(f"Error resolving {subdomain}.{target_domain}: {e}")

# Brute-force subdomains from wordlist
def brute_force_subdomains():
    while not q.empty():
        subdomain = q.get()
        resolve_subdomain(subdomain)
        q.task_done()

# Main function to start enumeration
def start_enumeration():
    print(f"[*] Starting subdomain enumeration for {target_domain}...\n")
    
    # Queue all the subdomains for brute-forcing
    for subdomain in wordlist:
        q.put(subdomain)
    
    # Create threads for concurrent DNS resolution
    for _ in range(10):
        thread = threading.Thread(target=brute_force_subdomains)
        thread.daemon = True
        thread.start()
    
    q.join()

    # Use public API for subdomain enumeration
    try:
        print("\n[*] Checking for subdomains using public API...\n")
        api_url = f"https://api.sublist3r.com/search.php?domain={target_domain}"
        response = requests.get(api_url)
        if response.status_code == 200:
            data = response.json()
            for subdomain in data.get('subdomains', []):
                print(f"[+] Found subdomain: {subdomain}.{target_domain}")
        else:
            print("[!] Could not fetch subdomains from the API.")
    except requests.RequestException as e:
        print(f"[!] Error with the API request: {e}")

# Entry point
if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("[!] Please provide a target domain.")
        sys.exit(1)
    target_domain = sys.argv[1]
    start_enumeration()
