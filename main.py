from fastapi import FastAPI
# All your other code follows below this line
# ...
@app.get("/")
def health_check():
    return {"status": "healthy"}