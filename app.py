import os
from flask import Flask, redirect, request, send_file
from storage_f import get_list_of_files, upload_file

bucket_name = "project-1-cloud-native_cloudbuild"
os.makedirs('files', exist_ok = True)

app = Flask(__name__)

@app.route('/')
def index():
    index_html="""
<form method="post" enctype="multipart/form-data" action="/upload" method="post">
  <div>
    <label for="file">Choose file to upload</label>
    <input type="file" id="file" name="form_file" accept="image/jpeg"/>
  </div>
  <div>
    <button>Submit</button>
  </div>
</form>"""    

    for file in get_list_of_files(bucket_name):
        index_html += "<li><img width=""200"" height=""200"" src=""https://storage.cloud.google.com/project-1-cloud-native_cloudbuild/"+file+" /></li><br>"

    return index_html

@app.route('/upload', methods=["POST"])
def upload():
    if 'form_file' not in request.files:
        return "No file uploaded", 400
    file = request.files['form_file']
    filename = file.filename
    if not (filename.lower().endswith(('.jpeg', '.jpg'))):
        return "Invalid file type", 400
    temp_path = os.path.join('files', filename)
    file.save(temp_path)
    upload_file(bucket_name, temp_path, filename)
    os.remove(temp_path)
    return redirect("/")

if __name__ == '__main__':
    app.run(debug=True)