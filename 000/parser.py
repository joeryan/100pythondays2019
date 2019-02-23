# simple argparse practice
import requests
import argparse
parser = argparse.ArgumentParser()
parser.add_argument("count", help="number of random jokes to get from api", type=int)
parser.add_argument("--verbose", help="increase program output verbosity", action="store_true")
parser.parse_args()
args = parser.parse_args()

jokes_api = "https://geek-jokes.sameerkumar.website/api"
for num in range(1, args.count+1):
  if args.verbose:
    print("Initiating connection to jokes api...")
  joke = requests.get(jokes_api)
  if args.verbose:
    print("result code: {}".format(joke.status_code))
  print("Joke #{0}: {1}".format(num, joke.text)) 
