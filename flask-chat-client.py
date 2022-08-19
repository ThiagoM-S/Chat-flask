from socket  import *

socket = id.connect('http://' + document.domain + ':' + location.port)

def function(e):
        e.preventDefault()
        user_name = input(( 'input.username' ))
        user_input = input(( 'input.message' ))
        socket.emit( 'my event', {
        user_name : user_name,
        message : user_input
        } )
        ( 'input.message' ).val( '' ).focus()


def function():
        socket.emit( 'my event', 
          data = 'User Connected'
        )

        form = ( 'form' ).on( 'submit', function( e ))

socket.on('connect',function())

def chat_on(msg):
    socket.on( 'my response', function( msg ))
    print(msg)

      