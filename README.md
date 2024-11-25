# Subdomain Enumerator

**Subdomain Enumerator** is a Python tool used for discovering subdomains of a target domain using DNS resolution, brute-forcing common subdomains, and leveraging public APIs. It helps security professionals and penetration testers to map out the infrastructure of a domain and identify potentially vulnerable subdomains.

## Features
- **Brute-Forcing**: Uses a predefined wordlist to brute-force common subdomains like `www`, `api`, `mail`, etc.
- **DNS Resolution**: Resolves subdomains to IP addresses using DNS queries.
- **Public API Integration**: Uses public subdomain enumeration APIs (like Sublist3r) for discovering additional subdomains.
- **Multithreading**: Utilizes multiple threads to speed up subdomain enumeration.
- **Customizable**: Easy to customize with your own wordlist and target domain.

## Requirements
- Python 3.x
- `requests` library
- `dnspython` library (for DNS resolution)

To install the required libraries, run:

```bash
pip install requests dnspython
```
# Usage
### Clone the repository:

```bash
git clone https://github.com/yourusername/subdomain-enumerator.git
```
### Navigate to the repository:

```
cd subdomain-enumerator
```
### Run the tool:

```bash
python subdomain_enumerator.py <target-domain>
```
### Example:

```bash
python subdomain_enumerator.py example.com
```
Replace <target-domain> with the domain you want to enumerate subdomains for. The tool will start brute-forcing and resolving subdomains, and it will also check for additional subdomains using a public API.

Example Output
```bash
[*] Starting subdomain enumeration for example.com...

[+] Found subdomain: www.example.com -> 192.168.1.1
[+] Found subdomain: api.example.com -> 192.168.2.1
[+] Found subdomain: mail.example.com -> 192.168.3.1

[*] Checking for subdomains using public API...

[+] Found subdomain: test.example.com
[+] Found subdomain: blog.example.com
[+] Found subdomain: staging.example.com
```
# Customization
Wordlist: The wordlist is customizable. You can add/remove subdomains to fit your needs.
Target Domain: You can specify any domain you want to enumerate by passing it as an argument when running the script.

# Disclaimer
This tool is intended for educational purposes only. It should only be used to enumerate subdomains on domains for which you have explicit permission to test. Unauthorized use of this tool is illegal.
