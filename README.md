## done-tunes

**What**

Python flask endpoint app that plays a song via iTunes using applescript whenever someone moves a Jira sprint ticket to Done. The song is customised to whoever completed the ticket. Currently only works on OS X.

**Why**

1. Notify the team when a task is done
2. Attribute completion to an individual through their custom song
3. It's fun

**Dependencies**

* Flask
* Applescript
* ngrok

**How**

1. Setup an ngrok tunnel to point to your flask app on 127.0.0.0:5000 because Jira will only POST webhooks to ports on 80 or 443
2. Edit the script to include the song names and playlist name that you have set up in iTunes
3. Change the script to include the usernames you want to test for
4. Setup a webhook in Jira that points to your ngrok url e.g. xxxxxx.ngrok.com/play
5. Start shipping tickets!

**To-DO**

1. Make song definition more efficient buy only assigning a song name to a user name and just substituting that variable into the applescript variable.
2. Check the need for trailing slash route on the play route
3. Create more routes for potential webhooks like ticket creation, bug creation, ticket re-open. 
4. Define hilarious songs or quotes to go along with these events

**Contribute**

If you think this is a cool idea, but kind of inefficient, please submit a PR and let's make this better.

© 2015, Devin Mancuso · MIT License you know the deal
