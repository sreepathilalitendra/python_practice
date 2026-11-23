
import requests


# Challenge 1: Retrieve post number 5

url = "https://jsonplaceholder.typicode.com/posts/5"

response = requests.get(url, timeout=10)

if response.status_code == 200:
    print("Post Retrieved Successfully")
    print(response.json())


# Challenge 2: Display ID, title and body

if response.status_code == 200:
    post = response.json()

    print("\nPost Details")
    print("ID:", post["id"])
    print("Title:", post["title"])
    print("Body:", post["body"])


# Challenge 3: Retrieve all users

url = "https://jsonplaceholder.typicode.com/users"

response = requests.get(url, timeout=10)

if response.status_code == 200:
    users = response.json()

    print("\nAll Users")
    print("Total Users:", len(users))


# Challenge 4: Display all user names

if response.status_code == 200:
    for user in users:
        print(user["name"])


# Challenge 5: Retrieve posts belonging to user ID 2

url = "https://jsonplaceholder.typicode.com/posts"

params = {
    "userId": 2
}

response = requests.get(
    url,
    params=params,
    timeout=10
)

if response.status_code == 200:
    posts = response.json()

    print("\nUser 2 Posts")

    for post in posts:
        print(post["id"], post["title"])


# Challenge 6: Send a POST request

url = "https://jsonplaceholder.typicode.com/posts"

new_post = {
    "title": "My Python Journey",
    "body": "I am learning Python API requests.",
    "userId": 1
}

response = requests.post(
    url,
    json=new_post,
    timeout=10
)

print("\nPOST Response")
print(response.status_code)
print(response.json())


# Challenge 7: Display POST status code

print("\nPOST Status Code:", response.status_code)

if response.status_code == 201:
    print("New post created successfully")


# Challenge 8: Check API request success

url = "https://jsonplaceholder.typicode.com/posts/1"

response = requests.get(url, timeout=10)

if response.status_code == 200:
    print("\nAPI Request Successful")
else:
    print("\nAPI Request Failed")


# Challenge 9: Display response URL and content type

print("\nResponse Information")
print("URL:", response.url)
print("Content Type:", response.headers.get("Content-Type"))


# Challenge 10: Mini API Data Viewer

def display_posts():
    url = "https://jsonplaceholder.typicode.com/posts"

    try:
        response = requests.get(url, timeout=10)
        response.raise_for_status()

        posts = response.json()

        print("\nPython API Data Viewer")
        print("Total Posts:", len(posts))

        for post in posts[:10]:
            print("\nPost ID:", post["id"])
            print("Title:", post["title"])

    except requests.exceptions.Timeout:
        print("Request timed out")

    except requests.exceptions.RequestException as error:
        print("API Error:", error)


display_posts()
