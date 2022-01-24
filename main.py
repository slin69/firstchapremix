from website import create_app
from flask_socketio import *

from website.views import *
users=[]
app=create_app()
socketio = SocketIO(app,cors_allowed_origins="*")



@socketio.on("message")
def handle_message(message):
    username=message["username"]
    msg=message["message"]
    new_message=f"{username}: {msg}"

    type=message["type"]
    if type=="message":
        socketio.emit("message",new_message,broadcast=True)
    if type=="connect":
        users.append(username)

        socketio.emit("message",new_message,broadcast=True)
        socketio.emit("update_users",users,broadcast=True)
    if type=="disconnect":
        users.remove(username)

        socketio.emit("message",new_message,broadcast=True)
        socketio.emit("update_users",users,broadcast=True)
@socketio.on("is_typing")
def is_typing(data):

    socketio.emit("is_typing",data,broadcast=True)

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(debug=True)
    #socketio.run(app,host='0.0.0.0', port=5004)
    #socketio.run(app,debug=True)