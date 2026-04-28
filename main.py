import requests
from crawler import get_all_forms, get_form_details
from detector import is_vulnerable
from urllib.parse import urljoin


TARGET_URL = "http://localhost:8080/vulnerabilities/sqli/" 

PHPSESSID = "s3ofa6s1dm54n89lotucbg6bs6"

session = requests.Session()
session.cookies.set("PHPSESSID", PHPSESSID)


def run_scanner(url):
    forms = get_all_forms(url, session)
    print(f"[*] Found {len(forms)} forms on {url}")
    
    payload = "'" 
    
    for form in forms:
        details = get_form_details(form)
        print(f"[!] Testing form: {details['action']}")
      
        data = {}
        for input_field in details["inputs"]:
            if input_field["name"]:
                data[input_field["name"]] = payload
        
      
        target_action = urljoin(url, details["action"])
        if details["method"] == "post":
            res = session.post(target_action, data=data)
        else:
            res = session.get(target_action, params=data)
            
      
        if is_vulnerable(res):
            print(f"[!!!] VULNERABILITY DETECTED at {target_action}")
          
            
             
        else:
            print("[+] Form appears safe.")

if __name__ == "__main__":
    run_scanner(TARGET_URL)