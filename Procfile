import os
import uvicorn
from main import main  
port = int(os.environ.get("PORT", 8080))

if __name__ == "__main__":
    uvicorn.run("app:app", host="0.0.0.0", port=port, reload=True)
