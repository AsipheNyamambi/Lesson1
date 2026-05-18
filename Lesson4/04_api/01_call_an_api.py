import requests

response = requests.get('https://www.ndosiautomation.co.za/API/groups')

print(response)

print('')
print('Response from API')
print(type(response.json))

print()
print(f'status code: {response.status_code}')
