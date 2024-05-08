import requests, sys
ip = sys.argv[1]
port_number = sys.argv[2]

# Define the URL of the web service
url = f"http://{ip}:{port_number}/todo"  # Replace with the actual URL

# Optional: Define parameters to send with the request (GET request)
params = {"title": "title4", "completed": "True"}

# Send a GET request
response = requests.post(url, json = params)

# Check for successful response (status code 200)
if response.status_code >= 200 and response.status_code <= 299:
  # Get the response data (usually in JSON format)
  data = response.json()
  print(data)  # Print the data or process it further
else:
  print(f"Error: {response.status_code}")  # Handle unsuccessful response

