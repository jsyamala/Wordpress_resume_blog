import requests
import json

# Replace with your WordPress site and credentials
WORDPRESS_URL = "https://syamalajresume.wordpress.com/wp-json/wp/v2"
USERNAME = "jayanthi.syamala@gmail.com"
APP_PASSWORD = "SJ_Writes_15"  # Create this from WordPress user settings

# Load content from JSON
with open("C:\\Users\\jayan\\Desktop\\Wordpress_resume_project\\Blog_content.json", "r", encoding="utf-8") as f:
    content = json.load(f)

# Create posts for each section
for title, body in content.items():
    post_data = {
        "title": title,
        "content": body,
        "status": "publish"
    }

    response = requests.post(
        f"{WORDPRESS_URL}/posts",
        auth=(USERNAME, APP_PASSWORD),
        json=post_data
    )

    if response.status_code == 201:
        print(f"✅ Posted: {title}")
    else:
        print(f"❌ Failed to post: {title} — {response.status_code}")
