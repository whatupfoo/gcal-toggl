# gcal-toggl

#### This is a simple python script that imports all the events from your Google calendar to Toggl in the date range that you specified.

![overview](https://github.com/rwnfoo/gcal-toggl/blob/master/images/Screen%20Shot%202019-08-26%20at%2011.png)

## Let's get to it!

## Step 1: Enable your gCal API & Install Google Client Library.

Basically, **step 1** and **step 2** [here](https://developers.google.com/calendar/quickstart/python).

Make sure you have python 3.4 and above.

Create a folder and have the `configurations.json` file in the same working directory as the python script.

## Step 2: Get your Toggl API token.

![profile_settings_toggl](https://github.com/rwnfoo/gcal-toggl/blob/master/images/Screen%20Shot%202019-08-26%20at%209.01.00%20PM.png)

Hover over to the left sidebar and select **Profile Settings**.

![toggl_api_token](https://github.com/rwnfoo/gcal-toggl/blob/master/images/Screen%20Shot%202019-08-26%20at%209.02.11%20PM.png)

Scroll all the way down for your Toggl API token. 

## Step 3: Paste your Toggl token in the script.

![Replace_token](https://github.com/rwnfoo/gcal-toggl/blob/master/images/Screen%20Shot%202019-08-26%20at%209.04.54%20PM.png)

Replace `API_TOKEN` with your Toggl token and save file.

## Step 4: Run script.

Navigate to the working working directory in your terminal where the script and `configurations.json` live.

```
cd working_directory
```

Run script with the following:

```
python toggl_gcal_GH.py
```

## Step 5: Authenticate and enter date range.

Enter the start date you want to import to Toggl, as well as the end date.
(Since timestamps stuff is not perfect, I'd go with more than 1 day to avoid duplicated events)

Your browser will pop up and prompt you to authenticate your Google account.

## Step 6: *Voila!*

A healthy response looks something like this, but with multiple JSON objects since the script makes batch API calls:
![healthy_response](https://github.com/rwnfoo/gcal-toggl/blob/master/images/Screen%20Shot%202019-08-26%20at%2010.31.25%20PM.png)

Refresh Toggl and you should see the events populated!

## What this script can't do (yet):
1. Add toggl tags, such as "Meetings", "Internal tasks" and "Billable" etc.
2. Filter for specific events, such as events you said 'YES' to. Or filter out events you don't want to track like OOO events etc.
3. gCal API returns with RFC3339 timestamps with time zone offset; still not perfect in the script when it comes to entering the same start and end dates.

## Sources
1. [Toggl API Documentation](https://github.com/toggl/toggl_api_docs/blob/master/toggl_api.md)
2. [API requests to gCal with Python](https://developers.google.com/calendar/quickstart/python)
