
import requests


# Example 1: Import Requests

print("Python Requests Module")


# Example 2: Send a GET request

url = "https://jsonplaceholder.typicode.com/posts/1"

response = requests.get(url, timeout=10)

print("Status Code:", response.status_code)


# Example 3: Check response

if response.status_code == 200:
    print("Request Successful")
else:
    print("Request Failed")


# Example 4: Display JSON response

if response.status_code == 200:
    data = response.json()

    print("Post ID:", data["id"])
    print("Title:", data["title"])


# Example 5: Display complete response

if response.status_code == 200:
    print(data)


# Example 6: GET request with query parameters

url = "https://jsonplaceholder.typicode.com/posts"

params = {
    "userId": 1
}

response = requests.get(
    url,
    params=params,
    timeout=10
)

if response.status_code == 200:
    posts = response.json()

    print("\nPosts belonging to User 1:")

    for post in posts:
        print(post["id"], post["title"])


# Example 7: Send a POST request

url = "https://jsonplaceholder.typicode.com/posts"

new_post = {
    "title": "Learning Python",
    "body": "Learning API requests",
    "userId": 1
}

response = requests.post(
    url,
    json=new_post,
    timeout=10
)

print("\nPOST Status Code:", response.status_code)
print("POST Response:", response.json())


# Example 8: Handle request errors

try:
    response = requests.get(
        "https://jsonplaceholder.typicode.com/posts/1",
        timeout=10
    )

    response.raise_for_status()

    print("\nAPI Connection Successful")

except requests.exceptions.Timeout:
    print("Request Timed Out")

except requests.exceptions.RequestException as error:
    print("Request Error:", error)


# Example 9: Display response information

print("\nResponse Information")
print("Status:", response.status_code)
print("Content Type:", response.headers.get("Content-Type"))
print("URL:", response.url)


# Example 10: Display API data

if response.status_code == 200:
    api_data = response.json()

    print("\nAPI Data")
    print("User ID:", api_data["userId"])
    print("Post ID:", api_data["id"])
    print("Title:", api_data["title"])
