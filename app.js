var app=require('express')(); var http=require('http').Server(app);
var io = require('socket.io')(http);
var username;
let ejs = require('ejs')
let fs = require('fs')
var users=[]

const port=process.env.PORT || 3000;
app.get('/', (req, res) => {
    console.log(username)
  res.sendFile(__dirname + '/index.html')});

  io.on("connection",function(socket){
      console.log("user connected")

      socket.on("message",function(data){
        console.log(data["message"])
        if (data['type']=="connect"){
            console.log('connect')
            msg={
                "username":data['username'],
                "message":"connected"
            }
            fs.appendFile("messages.txt",`${data['username']}: connected\n`,function(err){
                if(err) throw err;
                console.log("its been saved")
            })
            users.push(data['username'])
            io.emit("usersupdate",users)
            console.log("users:",users)
            io.emit("message",msg)
        }
        if (data['type']=="message"){
            msg={
                "username":data['username'],
                "message":data["message"]
            }
            fs.appendFile("messages.txt",`${data['username']}: ${data['message']}\n`,function(err){
                if(err) throw err;
                console.log("its been saved")
            })
            console.log(data['message'])
            io.emit("message",msg)
        }
        if (data['type']=="disconnect"){
            msg={
                "username":data['username'],
                "message":"disconnect"
            }
            fs.appendFile("messages.txt",`${data['username']}: disconnected\n`,function(err){
                if(err) throw err;
                console.log("its been saved")
            })
            const index = users.indexOf(data["username"]);
            users.splice(index,1);
            console.log("user disconnected:",data['username'])
            io.emit("usersupdate",users)
            console.log("users:",users)
            io.emit("message",msg)
        }
      })
      socket.on("whotyped",function(data){
          msg={
              "username":data['username']
          }
          io.emit("whotyped",msg)
      })
  });



http.listen(port, () => {
  console.log('listening on *:5000');
});