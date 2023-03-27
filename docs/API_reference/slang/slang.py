from googleapiclient import discovery
import json
import argparse

API_KEY = ""

def send(args):
  inputText = args.input

  client = discovery.build(
    "comentanalyzer",
    "v1alpha1",
    developerKey=API_KEY,
    discoveryServiceUrl="https://commentanalyzer.googleapis.com/$discovery/rest?version=v1alpha1",
    static_discovery=False,
  )

  analyze_request = {
    'comment': { 'text': inputText },
    'requestedAttributes': {'TOXICITY': {}}
  }

  response = client.comments().analyze(body=analyze_request).execute()
  toxicityValue = response["attributeScores"]["TOXICITY"]["summaryScore"]["value"]
  
  print( "bad" if toxicityValue > 0.8 else "notbad")

def main() :
  argparser = argparse.ArgumentParser(
    description = "<Slang API>"
  )

  argparser.add_argument(
    '--input',
    metavar='I',
    default='',
    help='Put input sentence or word in String type'
  )

  args = argparser.parse_args()
  send(args)

if __name__ == "__main__":
    main()