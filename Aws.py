import boto3
import json
from pprint import pprint
from summa import summarizer
from summa.summarizer import summarize

class Aws(object):

    def __init__(self,s3,transcribe):
        self.s3 = boto3.resource('s3',
        aws_access_key_id="AKIAIQL2TXLPRNX5BR6A",
        aws_secret_access_key= "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")
        self.s3_client = boto3.client('s3')
        self.transcribe_client = boto3.client('transcribe')
        self.bucketName = 'reinventorsbucket'


    def getTextFromSpeech(self, speechFile):
        s3URL = addToBucket(speechFile)
        response = translateToText(speechFile.name, s3URL)
        newFileName = speechFile.name + '.json'
        self.s3.meta.client.download_file(self.bucket.name, newFileName, './'+newFileName)
        with open(newFileName) as jsonResponse:
            data = json.load(jsonResponse)
        text = data["results"]["transcripts"][0]["transcript"]
        return(text)


    def addToBucket(self,file_name):
        self.bucket = self.s3.Bucket(self.bucketName)
        object_url = "https://s3.amazonaws.com/{0}/{1}".format(self.bucket.name,file_name)
        return object_url


    def translateToText(self,newFileName,s3URL):
        return transcribe_client.start_transcription_job(
        TranscriptionJobName=newFileName,
        LanguageCode='en-US',
        MediaFormat='mp3',
        Media={
            'MediaFileUri': s3URL
        },
        OutputBucketName=self.bucketName,
        Settings={
            'ShowSpeakerLabels': True
            'MaxSpeakerLabels': 3,
            'ChannelIdentification': False
        }
        )




#
#
# summary = summarizer.summarize(text)
# print(summary)
#
# summ = summarize(text, ratio=0.4)
# print(summ)
#
# with open("Summarized.txt", "w") as text_file:
#     text_file.write(summ)
