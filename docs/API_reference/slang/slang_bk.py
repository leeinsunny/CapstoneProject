from googleapiclient import discovery
import json

API_KEY = ""

client = discovery.build(
  "commentanalyzer",
  "v1alpha1",
  developerKey=API_KEY,
  discoveryServiceUrl="https://commentanalyzer.googleapis.com/$discovery/rest?version=v1alpha1",
  static_discovery=False,
)

# Sample Input
analyze_request = {
  'comment': { 'text': 'bull shit' },
  'requestedAttributes': {'TOXICITY': {}}
}

response = client.comments().analyze(body=analyze_request).execute()
print(json.dumps(response, indent=2))

"""
Sample Output:
{
  "attributeScores": {
    "TOXICITY": {
      "spanScores": [
        {
          "begin": 0,
          "end": 30,
          "score": {
            "value": 0.02543884,
            "type": "PROBABILITY"
          }
        }
      ],
      "summaryScore": {
        "value": 0.02543884,
        "type": "PROBABILITY"
      }
    }
  },
  "languages": [
    "en"
  ],
  "detectedLanguages": [
    "en"
  ]
}
"""