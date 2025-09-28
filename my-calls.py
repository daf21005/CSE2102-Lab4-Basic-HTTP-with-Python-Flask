import httpx
# import json AI told be to include this as an optional import

# url = "https://fluffy-space-barnacle-jj4x59w65rg4h5x9w-5000.app.github.dev/"
url = "http://localhost:5000/"

response = httpx.get(url)
print(response.status_code)
print(response.text)
print(response)


mydata = {
    "text": "Hello Phil!",
    "param2": "Making a POST request",
    "body": "my own value"
}

# A POST request to the API
response = httpx.post(url + "echo", data=mydata)

# Print the response
print(response.status_code)
print(response.text) 


# told AI to make this section more clear
# Test 1: Composite number 12 - Should return [1, 2, 2, 3]
print("\n--- Testing /factors/12 (Composite) ---")
factors_url_12 = url + "factors/12"
response = httpx.get(factors_url_12)
print(f"URL Called: {factors_url_12}")
print(f"Status Code: {response.status_code}")
# The .json() method parses the JSON response into a Python list
print(f"Factors for 12: {response.json()}") 

# Test 2: Prime number 7 - Should return [7]
print("\n--- Testing /factors/7 (Prime) ---")
factors_url_7 = url + "factors/7"
response = httpx.get(factors_url_7)
print(f"URL Called: {factors_url_7}")
print(f"Status Code: {response.status_code}")
print(f"Factors for 7: {response.json()}")

# Test 3: Large number 360 - Should return [1, 2, 2, 2, 3, 3, 5]
print("\n--- Testing /factors/360 ---")
factors_url_360 = url + "factors/360"
response = httpx.get(factors_url_360)
print(f"URL Called: {factors_url_360}")
print(f"Status Code: {response.status_code}")
print(f"Factors for 360: {response.json()}")