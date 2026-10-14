
import json
import urllib.request
import logging

logging.basicConfig(
    level=logging.INFO,
    format="%(levelname)s - %(message)s"
)

url = "https://api.github.com/repos/python/cpython"

try:
    with urllib.request.urlopen(url, timeout=10) as response:
        print("URL used:", response.url)
        data = json.loads(response.read().decode("utf-8"))

    logging.info("API request successful")

    print("\nJSON Response:")
    print(json.dumps(data, indent=4))

    print("\nExtracted Information:")
    print("Quote:", data["quote"])
    print("Author:", data["author"])

except Exception as error:
    logging.error("API request failed: %s", error)
