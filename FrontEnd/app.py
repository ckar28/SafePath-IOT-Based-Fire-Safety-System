from flask import Flask, render_template
import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore

# Set up Firebase credentials and initialize Firestore
cred = credentials.Certificate("path/to/serviceAccountKey.json")  # Replace with your service account key file
firebase_admin.initialize_app(cred)
db = firestore.client()

app = Flask(__name__)

# Route to display the safest paths
@app.route('/')
def display_safest_paths():
    safest_paths = get_safest_paths_from_firestore()
    return render_template('safest_paths.html', safest_paths=safest_paths)

# Function to retrieve the safest paths from Firestore
def get_safest_paths_from_firestore():
    doc_ref = db.collection(u'safest_paths').document(u'paths')
    doc = doc_ref.get()
    if doc.exists:
        safest_paths = doc.to_dict()
        return safest_paths
    else:
        return None

if __name__ == '__main__':
    app.run()
