from flask import Flask, session, render_template, request, redirect
import pyrebase

app = Flask(__name__)
config = {
    'apiKey': "AIzaSyA9QC0EMc0lZj4MfSbOWAHUi8jo27K-qj8",
    'authDomain': "react-minor-demo.firebaseapp.com",
    'databaseURL': "https://react-minor-demo-default-rtdb.asia-southeast1.firebasedatabase.app",
    'projectId': "react-minor-demo",
    'storageBucket': "react-minor-demo.appspot.com",
    'messagingSenderId': "56042135778",
    'appId': "1:56042135778:web:5564362569ca2786573ebb"
}

firebase = pyrebase.initialize_app(config)
auth = firebase.auth()

app.secret_key = 'secret'


@app.route('/', methods=['POST', 'GET'])
def index():
    if ('user' in session):
        return 'Hi, {}'.format(session['user'])
    if request.method == 'POST':
        email = request.form.get('email')
        password = request.form.get('password')
        try:
            user = auth.sign_in_with_email_and_password(email, password)
            session['user'] = email
        except:
            return 'Failed to Login'
    return render_template('home.html')


@app.route('/logout')
def logout():
    session.pop('user')
    return redirect('/')


if __name__ == '__main__':
    app.run(port=1111)
