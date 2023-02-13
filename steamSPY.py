def getTop100in2weeks():
    url = "https://steamspy.com/api.php?request=top100in2weeks"
    response = requests.get(url)
    return response.json()

def getTop100Forever():
    url = "https://steamspy.com/api.php?request=top100forever"
    response = requests.get(url)
    return response.json()