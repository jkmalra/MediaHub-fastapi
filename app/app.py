from fastapi import FastAPI, HTTPException

app = FastAPI()

text_posts = {
    1: {
        "title": "Morning Vibes 🌅",
        "content": "Captured the sunrise while sipping coffee. Peaceful start to the day."
    },
    2: {
        "title": "City Lights",
        "content": "Tried some long exposure shots in downtown last night — came out amazing!"
    },
    3: {
        "title": "Coding Marathon 💻",
        "content": "Pulled an all-nighter building my FastAPI backend. Worth every line of code."
    },
    4: {
        "title": "Weekend Chill",
        "content": "Editing some clips from the beach — the sound of waves is therapy."
    },
    5: {
        "title": "Gear Update 🎥",
        "content": "Finally got my new lens! Can’t wait to test it on the next shoot."
    },
    6: {
        "title": "Coffee + Code ☕",
        "content": "Favorite combo for productivity. FastAPI routes flying today!"
    },
    7: {
        "title": "Behind The Scenes",
        "content": "Set up lights and props for a new short video — took forever but nailed the vibe."
    },
    8: {
        "title": "Learning Curve",
        "content": "Messing with async functions in FastAPI. Brain fried but progress made."
    },
    9: {
        "title": "Street Portraits",
        "content": "Experimented with natural light and candid expressions. Loving the results."
    },
    10: {
        "title": "Deploy Done ✅",
        "content": "Pushed my MediaHub FastAPI app live — time to test everything on Render."
    }
}

@app.post("/post")
def post():
    return text_posts

@app.get("/posts/{id")
def get_post(id: int):
    if id not in text_posts:
        raise HTTPException(status_code=404, detail="Post not found")
    return text_posts.get(id)

# LEARN ALL HAVE DONE NOT ONLY SEE BUT DO IT YOURSELF AND READ DOCS AND OTHER RELATED STUFF THAT NEEDED
# AFTER THAT START QUERY PARAMETER