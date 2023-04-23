# import pyrebase
#
# config = {
#     'apiKey': "AIzaSyA9QC0EMc0lZj4MfSbOWAHUi8jo27K-qj8",
#     'authDomain': "react-minor-demo.firebaseapp.com",
#     'databaseURL': "https://react-minor-demo-default-rtdb.asia-southeast1.firebasedatabase.app",
#     'projectId': "react-minor-demo",
#     'storageBucket': "react-minor-demo.appspot.com",
#     'messagingSenderId': "56042135778",
#     'appId': "1:56042135778:web:5564362569ca2786573ebb"
# }
#
# firebase = pyrebase.initialize_app(config)
# auth = firebase.auth()
#
# # email = "test@gmail.com"
#
# email_list = ["test1@gmail.com", "test2@gmail.com", "test3@gmail.com"]
# password = "123456"
#
# # user = auth.create_user_with_email_and_password(email, password)
#
# for email in email_list:
#     try:
#         user = auth.sign_in_with_email_and_password(email, password)
#         print(f"Successfully authenticated with email: {email}")
#     except:
#         print(f"Failed to authenticate with email: {email}")


# mere testing ke liye hain
# auth.send_email_verification(user['idToken'])
# auth.send_password_reset_email(email)


# import pyrebase
#
# config = {
#     'apiKey': "AIzaSyA9QC0EMc0lZj4MfSbOWAHUi8jo27K-qj8",
#     'authDomain': "react-minor-demo.firebaseapp.com",
#     'databaseURL': "https://react-minor-demo-default-rtdb.asia-southeast1.firebasedatabase.app",
#     'projectId': "react-minor-demo",
#     'storageBucket': "react-minor-demo.appspot.com",
#     'messagingSenderId': "56042135778",
#     'appId': "1:56042135778:web:5564362569ca2786573ebb"
# }
#
# firebase = pyrebase.initialize_app(config)
# auth = firebase.auth()
#
# email_list = ["test@gmail.com", "test1@gmail.com", "test2@gmail.com", "test3@gmail.com", "snigdh27@gmail.com",
#               "harshul147@gmail.com"]
# password = "123456"
#
# for email in email_list:
#     try:
#         user = auth.create_user_with_email_and_password(email, password)
#         print(f"Successfully created user with email: {email}")
#     except:
#         print(f"Failed to create user with email: {email}")


# import pyrebase
#
# config = {
#     'apiKey': "AIzaSyA9QC0EMc0lZj4MfSbOWAHUi8jo27K-qj8",
#     'authDomain': "react-minor-demo.firebaseapp.com",
#     'databaseURL': "https://react-minor-demo-default-rtdb.asia-southeast1.firebasedatabase.app",
#     'projectId': "react-minor-demo",
#     'storageBucket': "react-minor-demo.appspot.com",
#     'messagingSenderId': "56042135778",
#     'appId': "1:56042135778:web:5564362569ca2786573ebb"
# }
#
# firebase = pyrebase.initialize_app(config)
# auth = firebase.auth()
#
# email_list = ["test@gmail.com", "test1@gmail.com", "test2@gmail.com", "test5@gmail.com", "snigdh27@gmail.com"]
# password = "123456"
#
# for email in email_list:
#     try:
#         user = auth.sign_in_with_email_and_password(email, password)
#         print(f"Successfully authenticated with email: {email}")
#     except:
#         print(f"Failed to authenticate with email: {email}")


import pyrebase

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

email_list = ["test@gmail.com", "test1@gmail.com", "test2@gmail.com", "snigdh27@gmail.com"]
password = "123456"

for email in email_list:
    try:
        user = auth.sign_in_with_email_and_password(email, password)
        print(f"Successfully authenticated with email: {email}")
    except Exception as e:
        print(f"Failed to authenticate with email: {email}. Error message: {e}")
