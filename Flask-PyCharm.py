# from flask import Flask, render_template, request
# from flask_mail import Mail, Message

from flask import * 
from flask_mail import Mail, Message

# mail()
# message()
# sent()

app = Flask(__name__)

# Flask mail configuration
app.config['MAIL_SERVER'] = 'smtp.gmail.com'
app.config['MAIL_PORT'] = 587
app.config['MAIL_USERNAME'] = 'vtu24172@veltech.edu.in'
app.config['MAIL_PASSWORD'] = 'eqjtzodphsheabkl'  # Use the App Password you generated
app.config['MAIL_USE_TLS'] = True


# Instantiate the Mail class
mail = Mail(app)

# Configure the Message class object and send the mail from a URL
@app.route('/', methods=['GET','POST'])
def index():
     msg = Message('subject', sender='vtu24172@veltech.edu.in', recipients=["kingpoovarasan49@gmail.com"])
     msg.body = 'hi, this is the mail sent by using the flask web application'
     mail.send(msg)
     return render_template("index.html")
        
      
  


    
   
    

if __name__ == '__main__':
    app.run(debug=True)


#     @app.route('/', methods=['GET','POST'])
# def index():
#     if request.method == 'POST':
#         name = request.form['data']
#         count=len(name)
#         case=name.upper()
#         return f"Hello, {name}==={count}!==={case} You submitted the form using POST."
#     return render_template('index.html')