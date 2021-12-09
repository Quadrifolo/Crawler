import requests

#Requests Library allows you to send requests 

#url = "mail.google.com"


def request(url):
 try:
   return requests.get("http://" + url)
   #print(get_response)
 except requests.exceptions.ConnectionError:
    pass


target_url = "google.com"

with open("/home/quadri/Downloads/subdomains-wodlist.txt", "r") as wordlist_file:
    for line in wordlist_file:
      word = line.strip()
      test_url = word + "." + target_url
      #print(test_url)
      response = request(test_url)
      if response:
        print("[+] Discovered subdomain --> " + test_url)

