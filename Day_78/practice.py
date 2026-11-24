
import requests
import json


# Challenge 1: Retrieve all posts

url = "https://jsonplaceholder.typicode.com/posts"

response = requests.get(url, timeout=10)
response.raise_for_status()

posts = response.json()

print("All Posts Retrieved Successfully")


# Challenge 2: Display total number of posts

print("\nTotal Posts:", len(posts))


# Challenge 3: Display first five post titles

print("\nFirst Five Post Titles")

for post in posts[:5]:
    print(post["title"])


# Challenge 4: Filter posts belonging to user ID 3

print("\nPosts Belonging to User ID 3")

user_posts = [
    post for post in posts
    if post["userId"] == 3
]

for post in user_posts:
    print(post["id"], post["title"])


# Challenge 5: Search for a post using its ID

search_id = 10

found_post = None

for post in posts:
    if post["id"] == search_id:
        found_post = post
        break

if found_post:
    print("\nPost Found")
    print("ID:", found_post["id"])
    print("Title:", found_post["title"])
else:
    print("\nPost Not Found")


# Challenge 6: Display posts with IDs greater than 50

print("\nPosts with IDs Greater Than 50")

filtered_posts = [
    post for post in posts
    if post["id"] > 50
]

for post in filtered_posts:
    print(post["id"], post["title"])


# Challenge 7: Sort posts by title

sorted_posts = sorted(
    posts,
    key=lambda post: post["title"].lower()
)

print("\nPosts Sorted by Title")

for post in sorted_posts[:10]:
    print(post["title"])


# Challenge 8: Save all posts into posts.json

with open("posts.json", "w", encoding="utf-8") as file:
    json.dump(posts, file, indent=4)

print("\nAll Posts Saved to posts.json")


# Challenge 9: Read posts.json and display first five posts

with open("posts.json", "r", encoding="utf-8") as file:
    saved_posts = json.load(file)

print("\nFirst Five Saved Posts")

for post in saved_posts[:5]:
    print("ID:", post["id"])
    print("Title:", post["title"])


# Challenge 10: Mini API Data Analyzer

def analyze_posts(selected_user_id):

    url = "https://jsonplaceholder.typicode.com/posts"

    try:
        response = requests.get(url, timeout=10)
        response.raise_for_status()

        api_posts = response.json()

        total_posts = len(api_posts)

        unique_user_ids = {
            post["userId"] for post in api_posts
        }

        selected_posts = [
            post for post in api_posts
            if post["userId"] == selected_user_id
        ]

        print("\nPython API Data Analyzer")
        print("Total Posts:", total_posts)
        print("Unique User IDs:", sorted(unique_user_ids))
        print("Selected User ID:", selected_user_id)
        print("Number of Selected User Posts:", len(selected_posts))

        print("\nSelected User Posts")

        for post in selected_posts:
            print(post["id"], post["title"])

    except requests.exceptions.Timeout:
        print("API Request Timed Out")

    except requests.exceptions.RequestException as error:
        print("API Error:", error)


analyze_posts(3)
