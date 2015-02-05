from flask import Flask
from flask import request
import os
import applescript
import json

app = Flask(__name__)

#Define a song to play for each team member, this could be improved. 

teammember_script = """tell application "iTunes"
	play track "Dont Stop Believing" of playlist "Done"
end tell
"""

teammember2_script = """tell application "iTunes"
	play track "Yelling Into The Wind" of playlist "Done"
end tell
"""

teammember3_script = """tell application "iTunes"
	play track "Good Times" of playlist "Done"
end tell
"""

# All script is to handle any team members who don't have an individual song defined
all_script = """tell application "iTunes"
	play track "NewTown" of playlist "Done"
end tell
"""

# All script is to handle any team members who don't have an individual song defined
bug_script = """tell application "iTunes"
	play track "NewTown" of playlist "Done"
end tell
"""


@app.route('/play/', methods = ['GET', 'POST', 'PATCH'])
@app.route('/play', methods = ['GET', 'POST', 'PATCH'])
def play():
	if request.method == 'POST':
		
		jsondata = request.data
		
		data = json.loads(jsondata)
		
		#Load the new status of the ticket from the JSON payload
		new_status = data['changelog']['items'][0]['toString']

		if (new_status == 'Done'):

				# if user_id is passed in as URL param
				if (request.values.get('user_id', None)):
					u = request.values.get('user_id', None)	
				#checks to see which team member it is. This could be improved.
				if (u == 'user.name'):						
					try:
						applescript.launch_script(teammember_script)
						return "playing first teammember's song"
					except applescript.AppleScriptError:
						return "Something has gone wrong with Applescript"
				
				elif (u == 'user.name'):						
					try:
						applescript.launch_script(teammember2_script)
						return "playing teammember2's song"
					except applescript.AppleScriptError:
						return "Something has gone wrong with Applescript"
				
				elif (u == 'user.name'):						
					try:
						applescript.launch_script(teammember3_script)
						return "playing teammember3's song"
					except applescript.AppleScriptError:
						return "Something has gone wrong with Applescript"
				
				elif u in other_team_members:
					try:
						applescript.launch_script(all_script)
						return "playing the default song"
					except applescript.AppleScriptError:
						return "Something has gone wrong with Applescript"

				#check to see if user_id is empty
				elif u is None:
					return "there was no user specified when this ticket was updated"
		else:
			return "Status not Done, do nothing"

#Create a webhook that only looks at bug type tickets in your project. Then point the webhook to this route.
@app.route('/bug/', methods = ['GET', 'POST', 'PATCH'])
@app.route('/bug', methods = ['GET', 'POST', 'PATCH'])
def bug():
	try:
		applescript.launch_script(bug_script)
		return "playing the bug creation song"
	except applescript.AppleScriptError:
		return "Something has gone wrong with Applescript"

if __name__ == '__main__':
	app.debug = True
	app.run()