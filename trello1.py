import requests

api_key = 'e6c06524fe32ab3fc3f2ec6ecd4cf8e3'
token = 'de0b144514cb058a3ed78be142d5c5bae46cdd8bc5c4ad16924981e0bc44ef26'
board_name = 'pswanth2'
List_name='Book Train tickets'

class Trello:

#Function to create a board
    def create_board(self,api_key,token,board_name):
        url = "https://api.trello.com/1/boards/"
        querystring = {"name":board_name,"defaultLabels":"true","defaultLists":"true","keepFromSource":"none","prefs_permissionLevel":"private","prefs_voting":"disabled","prefs_comments":"members","prefs_invitations":"members","prefs_selfJoin":"true","prefs_cardCovers":"true","prefs_background":"blue","prefs_cardAging":"regular","key":api_key,"token":token}
        response = requests.request("POST", url, params=querystring,verify=False)
        
#Function to get the BoardID
    def get_boardID(self,api_key,token,board_name):
        url = "https://api.trello.com/1/members/me/boards"
        querystring = {"key": api_key, "token":token}
        response = requests.request("GET", url, params=querystring, verify=False)
        r = response.json()
        dict1 = {}
        for i in r:
            dict1.update({i['name']: i['id']})
        return dict1[board_name]
    
#Function to add a list to board
    def add_list(self,board_ID,List_name,api_key,token):
        url = "https://api.trello.com/1/lists"
        querystring = {"name": List_name, "idBoard": board_ID, "key": api_key, "token": token}
        response = requests.request("POST", url, verify=False, params=querystring)

#Function to update the board with emailID and make the user as admin
    def update_board(self,boardID,api_key,token):
        url = "https://api.trello.com/1/boards/"+boardID+"/members"
        querystring = {"email": "prswanth@gmail.com", "type": "admin", "key": api_key, "token": token}
        headers = {'content-type': 'application/json'}
        response = requests.request("PUT", url, headers=headers, verify=False, params=querystring)

#Function to delete the board using boardID
    def delete_board(self,api_key,token,board_ID):
        url = "https://api.trello.com/1/boards/"+board_ID
        querystring = {"key": api_key, "token": token}
        response = requests.request("DELETE", url,verify=False, params=querystring)

# Create an object of class Trello
trel_Obj = Trello()

#Create a new board
trel_Obj.create_board(api_key,token,board_name)

#Get the BoardID using board_name
boardID=trel_Obj.get_boardID(api_key,token,board_name)

# add a list to the board

trel_Obj.add_list(boardID,List_name,api_key,token)

#update the board with emailID and make the user as admin

trel_Obj.update_board(boardID,api_key,token)

#Delete the board

trel_Obj.delete_board(api_key,token,boardID)
