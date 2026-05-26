import requests

response = requests.get('https://www.ndosiautomation.co.za/API/groups')

print(response)

print('')
print('Response from API')
print(response.json())

print()
print(f'Status code is: {response.status_code}')





