from website import create_app
from flask_socketio import *

from website.views import *
users=[]
app=create_app()
socketio = SocketIO(app)



@socketio.on("message")
def handle_message(message):
    username=message["username"]
    msg=message["message"]
    new_message=f"{username}: {msg}"
    print(f"{username}: {msg}")
    type=message["type"]
    if type=="message":
        socketio.emit("message",new_message,broadcast=True)
    if type=="connect":
        users.append(username)
        print(f"users: {users}")
        socketio.emit("message",new_message,broadcast=True)
        socketio.emit("update_users",users,broadcast=True)
    if type=="disconnect":
        users.remove(username)
        print(f"users: {users}")
        socketio.emit("message",new_message,broadcast=True)
        socketio.emit("update_users",users,broadcast=True)
@socketio.on("is_typing")
def is_typing(data):
    print("shit")
    socketio.emit("is_typing",data,broadcast=True)

if __name__ == '__main__':
    socketio.run(app,debug=True)