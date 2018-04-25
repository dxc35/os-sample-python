from flask import Flask
application = Flask(__name__)


# -- my_now=datetime.now().strftime('%Y-%m-%d %H:%M:%S')

@application.route("/")
def hello():
#    from datetime import datetime
#    my_message = "Hello World! - My Name is TMR at:" & datetime.now().strftime('%Y-%m-%d %H:%M:%S')
#    return my_message
    return "Hello World! - My Name is TMR "
if __name__ == "__main__":
    application.run()
