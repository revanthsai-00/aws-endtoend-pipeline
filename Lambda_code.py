import json
import requests
import boto3
def lambda_handler(event, context):
    # TODO implement
    bucket_name='cov-buket'
    url = "https://covid-193.p.rapidapi.com/countries"

    headers = {
	"X-RapidAPI-Key": "9f8b7b3e63mshfe78bf3a15878d9p1d872bjsnab35d24624fe",
	"X-RapidAPI-Host": "covid-193.p.rapidapi.com"
    }

    data = requests.request("GET", url, headers=headers)
    cd=data.json()
    covid_data=[]
    for i in cd['response']:
        covid_data.append(i)
    print(covid_data)
    s3 = boto3.resource('s3')
    s3object = s3.Object(bucket_name,'covid_data.json')
    s3object.put(
        Body=(bytes(json.dumps(covid_data).encode('UTF-8')))
    )
    return {
        'statusCode': 200,
        'body': json.dumps('Hello from Lambda!')
    }



