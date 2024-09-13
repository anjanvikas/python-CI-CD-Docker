import requests

def fetch_posts():
  """Fetches a list of posts from the JSONPlaceholder API.

  Returns:
    A list of dictionaries representing the fetched posts.
  """

  url = 'https://jsonplaceholder.typicode.com/posts'
  response = requests.get(url)
  response.raise_for_status()  # Raise an exception for error responses

  # Parse the JSON response
  posts = response.json()

  return posts

if __name__ == '__main__':
  posts = fetch_posts()

  # Print the first 5 posts (optional)
  for post in posts[:5]:
    print(post)