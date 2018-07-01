from django.http import HttpResponse
import json

def readData():
	f = open('test.json', 'r')
	jsonData = f.read()
	f.close()
	jsonData = json.loads(jsonData)
	retString = "Users and their positions:<br>"
	for user in jsonData:
		retString += str(user) + ": " + str(jsonData[user]) + "<br>";
	return retString

def writeData(user, position):
	f = open('test.json', 'r')
	jsonData = f.read()
	f.close()
	jsonData = json.loads(jsonData)
	jsonData[user] = position
	f = open('test.json', 'w')
	f.write(json.dumps(jsonData))
	f.close()

def index(request):
	if 'user' not in request.GET:
		return HttpResponse("Please specify a user\n" + readData())
	if 'position' not in request.GET:
		return HttpResponse("Please specify a position\n" + readData())
	print("A user sent their position and is asking for data from others")
	writeData(request.GET['user'], request.GET['position'])

	return HttpResponse(readData())
