import json
import requests as re
import logging

# set up logging
logging.basicConfig(
    handlers=[
        logging.FileHandler("logfile.txt"),
        logging.StreamHandler()
        ],
    level=logging.INFO,
    format="%(asctime)s:%(levelname)s:%(message)s"
    )

# load configuration
try:
    with open('config.json', 'r') as f:
        config = json.load(f)
    url = config["url"]
except:
    logging.error("Invalid URL configuration")
    exit(1)

# Configure request, including headers for CORS policy
headers = {
    "Content-Type": "application/json",
    "Access-Control-Allow-Origin": "*"
    }

# retrieve new data from API
try:
    res = re.get(url, headers=headers)
    assert res.status_code == 200
    assert res.headers["Content-Type"].startswith('application/json')
except:
    # save error as html if request fails
    if res.headers['Content-Type'].startswith('text/html'):
        with open('response.html', 'w') as f:
            f.write(res.content)
    logging.error(f"Invalid response: {res.status_code}, {res.headers['Content-Type']}")
    exit(1)

# load content
try:
    content = json.loads(res.content)
except:
    logging.error("Could not load json")
    exit(1)

# test validity of content
try:
    assert len(content) > 0
except:
    logging.error("Content did not pass assertions")
    exit(1)

with open('response.json', 'w') as f:
    json.dump(content, f)

logging.info("Updated response successfully")
