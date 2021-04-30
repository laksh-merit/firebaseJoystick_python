import firebase_admin
from firebase_admin import credentials
from firebase_admin import db

# Fetch the service account key JSON file contents
cred = credentials.Certificate('File from your firebase DB')

# Initialize the app with a service account, granting admin privileges
firebase_admin.initialize_app(cred, {
    'databaseURL': 'link of your firebase DB'
})

values = db.reference('firebaseJoystick')
print(values.get())

condition = db.reference('firebaseJoystick/Condition')
print(condition.get())

control = db.reference('firebaseJoystick/Car')
print(control.get())

pos = db.reference('firebaseJoystick/Car-pos')
print(pos.get())

while True:
    print(control.get(), condition.get(), pos.get())
