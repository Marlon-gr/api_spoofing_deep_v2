
import uvicorn

from api_spoofing_deep_v2 import create_app

# Start App.
app = create_app()


uvicorn.run("__main__:app", host="0.0.0.0", log_level="debug", port=9000)