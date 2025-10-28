import requests
class Client():
	def __init__(self):
		self.api="smtp.bz/v1/"
		self.headers={"user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/93.0.4577.82 Safari/537.36","x-requested-with": "XMLHttpRequest"}
	def block_list_dns(self,data):
		return requests.get(f"https://dnsbl.{self.api}/Tools/dnsbl/{data}",headers=self.headers).json()
	def check_smtp(self,domain):
		return requests.get(f"https://check.{self.api}/Tools/smtp/{domain}",headers=self.headers).json()
	def status(self):
		return requests.get(f"https://status.{self.api}/services",headers=self.headers).json()
	def uptime_status(self):
		return requests.get(f"https://status.{self.api}/services/uptime",headers=self.headers).json()