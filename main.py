#!/usr/bin/env python3
import requests

def factCheck():
	#google fact-check api:
	payload = {'query': 'Policia', 'key':'AIzaSyDFZHZGntGonssz3t-Tw0-Q-ZmPoG-aXAU'}
	response = requests.get("https://factchecktools.googleapis.com/v1alpha1/claims:search", params=payload)
	print(response.text)

if __name__ == '__main__':
	factCheck()

