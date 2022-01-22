from flask import *

bp=Blueprint('views',__name__,url_prefix="/")
usernames=[]
NAME_KEY="name"
@bp.route("/",methods=["GET", "POST"])
def login():
    if request.method =="POST":
        username=request.form.get('username')
        session[NAME_KEY]=username
        usernames.append(username)
        print(session[NAME_KEY])
        return render_template('chat.html',**{"session":session})
    return render_template('login.html')
@bp.route("/chat")
def chat():
    if NAME_KEY not  in session:
        return redirect(url_for("views.login"))
    return render_template('chat.html',**{"session":session})