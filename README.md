# gcal-toggl

#### This is a simple python script that imports all the events on your Google calendar to Toggl in a date range that you specify.

#### What this script can't do (yet):
1. Add toggl tags
2. Filter for specific events, such as events you said 'YES' to. Or filter out events you don't want to track like OOO events etc.
3. gCal returns with RFC3339 timestamps with time zone offset; still not perfect in the script when it comes to pulling in events in the same day.

####  Let's get things going:
#### Step 1: Enable your gCal API & Install Google Client Library

Basically, **step 1** and **step 2** [here](https://developers.google.com/calendar/quickstart/python).

Make sure you have python 3.4 and above.

Create a folder and have the `configurations.json` file in the same working directory as the python script.

#### Step 2: Get your Toggl API token
Hover over to the left sidebar and select **Profile Settings**.

Scroll all the way down for your Toggl API token. Don't forget to save the file.

#### Step 3: Replace the Toggl token with yours in the script.

#### Step 4: Run script.

Navigate to the working working directory where the script and `configurations.json` live.

`cd working_directory`

Run script.

`python toggl_gcal_GH.py`

Enter the start date you want to import to Toggl, as well as the end date.
(Since timestamps stuff is not perfect, I'd go with more than 1 day to avoid duplicate events)

#### Step 5: *Voila!*

Refresh Toggl and you should see the events populated!
