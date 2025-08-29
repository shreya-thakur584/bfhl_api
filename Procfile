import os
import uvicorn

port = int(os.environ.get("PORT", 8080))  # default to 8080 locally

if __name__ == "__main__":
    uvicorn.run("app:app", host="0.0.0.0", port=port, reload=True)
