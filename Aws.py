import boto3
import json
from pprint import pprint
from summa import summarizer
from summa.summarizer import summarize

class Aws(object):
    def __init__(self,s3,transcribe):
        self.s3 = s3
        self.transcribe = transcribe

    def s3Obj(self):
        self.s3 = boto3.resource('s3',
        aws_access_key_id="AKIAIQL2TXLPRNX5BR6A",
        aws_secret_access_key= "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")
        s3_client = boto3.client('s3')

    def addToBucket(self,file_name):
        self.bucket = self.s3.Bucket('reinventorsbucket')
        object_url = "https://s3.amazonaws.com/{0}/{1}".format(self.bucket.name,file_name)
        return object_url

    def transcribeObj(self):
        transcribe_client = boto3.client('transcribe')
        response = transcribe_client.start_transcription_job(
        TranscriptionJobName='audioinput',
        LanguageCode='en-US',
        MediaFormat='mp4',
        Media={
            'MediaFileUri': object_url
        },
        OutputBucketName='reinventorsbucket',
        Settings={
            'ShowSpeakerLabels': True
            'MaxSpeakerLabels': 3,
            'ChannelIdentification': False
        }
        )


s3.meta.client.download_file(bucket.name, 'audioinput.json', './audioinput.json')

with open('audioinput.json') as f:
    data = json.load(f)

pprint(data)

text = data["results"]["transcripts"][0]["transcript"]
print(text)

summary = summarizer.summarize(text)
print(summary)

summ = summarize(text, ratio=0.4)
print(summ)

with open("Summarized.txt", "w") as text_file:
    text_file.write(summ)
