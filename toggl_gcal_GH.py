from __future__ import print_function
import pickle
import os.path
from googleapiclient.discovery import build
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request
import requests
import json
from datetime import datetime

# If modifying these scopes, delete the file token.pickle.
SCOPES = ['https://www.googleapis.com/auth/calendar.readonly']

def gcal_events():
    creds = None
    # The file token.pickle stores the user's access and refresh tokens, and is
    # created automatically when the authorization flow completes for the first
    # time.
    if os.path.exists('token.pickle'):
        with open('token.pickle', 'rb') as token:
            creds = pickle.load(token)
    # If there are no (valid) credentials available, let the user log in.
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file(
                'credentials.json', SCOPES)
            creds = flow.run_local_server(port=0)
        # Save the credentials for the next run
        with open('token.pickle', 'wb') as token:
            pickle.dump(creds, token)

    service = build('calendar', 'v3', credentials=creds)

    # EDIT THE TIMES YOU WANT TO TRACK HERE
    DATETIME_START_LOG = '2019-08-26T00:00:00+00:00'
    DATETIME_END_LOG = '2019-08-27T00:00:00+00:00'

    # Google Calendar API call
    # Parameters you can include: maxResults=3,
    events_result = service.events().list(calendarId='primary', timeMin=DATETIME_START_LOG,
                                        timeMax = DATETIME_END_LOG, singleEvents=True,
                                        orderBy='startTime').execute()
    events = events_result.get('items', [])

    if not events:
        print('No upcoming events found.')
    for event in events:
        event_name = event['summary']
        start = event['start'].get('dateTime', event['start'].get('date'))
        end = event['end'].get('dateTime', event['start'].get('date'))
        start_time = datetime.strptime(start,'%Y-%m-%dT%H:%M:%S%z')
        end_time = datetime.strptime(end,'%Y-%m-%dT%H:%M:%S%z')
        duration = int((end_time - start_time).total_seconds())

        # Toggl API call
        url = "https://www.toggl.com/api/v8/time_entries"

        # EDIT YOUR TOGGL API TOKEN HERE. FIND YOUR TOKEN UNDER YOUR TOGGL PROFILE
        toggl_API_token = 'API_TOKEN'

        payload = {"time_entry":
        {"description":event_name,"stop":end, "duration": duration,"start":start,"created_with":"curl"}
        }
        headers = {
            'Content-Type': "application/json",
            'User-Agent': "PostmanRuntime/7.15.2",
            'Accept': "*/*",
            'Cache-Control': "no-cache",
            'Host': "www.toggl.com",
            'Accept-Encoding': "gzip, deflate",
            'Content-Length': "126",
            'Connection': "keep-alive",
            'cache-control': "no-cache"
            }

        response = requests.request("POST", url, data=json.dumps(payload), headers=headers, auth=(toggl_API_token,'api_token'))

        print(response.text)

gcal_events()
