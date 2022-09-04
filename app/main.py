import logging
from fastapi import FastAPI
logging.basicConfig(
    level=logging.INFO,
    format="[%(asctime)s] {%(pathname)s:%(lineno)d} %(levelname)s - %(message)s",
)

log = logging.getLogger(__name__)
app = FastAPI(title = "NBA API")

@app.get("/")
def read_root():
	return{"API": "Hello NBA!"}