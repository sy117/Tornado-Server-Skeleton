import os
import argparse
import json

parser = argparse.ArgumentParser(description="Tornado Server Code Skeleton!!")
parser.add_argument("--prod", type=bool, default=False, help="Input the Runtime Environment")

args = parser.parse_args()

IS_DEVELOPMENT = not args.prod

with open("./configs/{}.json".format("dev" if IS_DEVELOPMENT is True else "prod")) as handle:
    env = json.loads(handle.read())

PORT = os.environ["PORT"] if os.environ.get("PORT") is not None else 8080

PROJECT_NAME = env["project_name"]

SERVICE = env["service"]

API_VERSION = env["api_version"]
