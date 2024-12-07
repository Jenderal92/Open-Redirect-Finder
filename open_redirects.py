#!/usr/bin/env python2
# -*- coding: utf-8 -*-

import requests
import sys
import os
from urlparse import urlparse, urljoin

def print_banner():
    banner = """
=============================================
    Open Redirect Finder | by Python 2.7      
=============================================
"""
    print(banner)

def check_redirect(base_url, payload):
    try:
        test_url = urljoin(base_url, payload)
        response = requests.get(test_url, allow_redirects=False)
        
        if response.status_code in [301, 302]:
            location = response.headers.get('Location', '')
            if urlparse(location).netloc and urlparse(location).netloc != urlparse(base_url).netloc:
                return True, location
        return False, None
    except Exception as e:
        return False, str(e)

def load_custom_payload(file_path):
    payloads = []
    if os.path.exists(file_path):
        with open(file_path, 'r') as f:
            payloads = [line.strip() for line in f.readlines() if line.strip()]
    return payloads

def main():
    print_banner()
    try:
        input_file = raw_input("[*] Enter file name (URL list): ").strip()
        if not os.path.exists(input_file):
            print("[!] File not found.")
            sys.exit(1)
        
        with open(input_file, 'r') as f:
            urls = [line.strip() for line in f.readlines() if line.strip()]
        
        if not urls:
            print("[!] File is empty or does not contain a URL.")
            sys.exit(1)

        print("[*] Select payload options:")
        print("  1. Default Payload")
        print("  2. Custom Payload from file")
        print("  3. Combine Default and Custom Payload")
        payload_option = raw_input("[*] Pilih (1/2/3): ").strip()

        default_payloads = [
            "redirect=http://evil.com",
            "?url=http://evil.com",
            "/?next=http://evil.com",
            "?continue=http://evil.com"
            "?page=http://evil.com"
        ]
        
        custom_payloads = []
        if payload_option in ['2', '3']:
            custom_payload_file = raw_input("[*] Enter a custom payload file name (e.g., custom.txt): ").strip()
            custom_payloads = load_custom_payload(custom_payload_file)
        
        if payload_option == '1':
            payloads = default_payloads
        elif payload_option == '2':
            payloads = custom_payloads
        elif payload_option == '3':
            payloads = default_payloads + custom_payloads
        else:
            print("[!] Invalid option.")
            sys.exit(1)

        print("[*] Starting testing with payload: "+ payloads)
        results = []
        
        for url in urls:
            for payload in payloads:
                is_vulnerable, location = check_redirect(url, payload)
                if is_vulnerable:
                    results.append((url, payload, location))
                    print("[+] Vulnerability detected: {} -> {}".format(url, location))
        
        if results:
            with open("results.txt", "w") as out:
                for url, payload, location in results:
                    out.write("URL: {}\nPayload: {}\nRedirect: {}\n\n".format(url, payload, location))
            print("[*] Results are saved in 'results.txt'")
        else:
            print("[*] No vulnerabilities found.")
    
    except KeyboardInterrupt:
        print("\n[!] Stopped by user.")
        sys.exit(1)

if __name__ == "__main__":
    main()
