from flask import Flask, render_template ,request
import uuid
from werkzeug.utils import secure_filename
import os

UPLOAD_FOLDER = 'user_uploads'
ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg'}

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER


@app.route("/")
def home():
    return render_template("index.html")

@app.route("/create",methods=["GET","POST"])
def create():
    myid=uuid.uuid1()
    if request.method=="POST":
        print(request.files.keys())
        rec_id=(request.form.get("uuid"))
        desc=(request.form.get("text"))
        input_file=[]
        for key,value in request.files.items():
            print(key,value)
            #upload file
            file=request.files[key]
            if file :
                filename = secure_filename(file.filename)
                if(not(os.path.exists(os.path.join(app.config['UPLOAD_FOLDER'],rec_id)))):
                    os.mkdir(os.path.join(app.config['UPLOAD_FOLDER'], rec_id))
                
                file.save(os.path.join(app.config['UPLOAD_FOLDER'], rec_id, filename))
                input_file.append(file.filename)
            #caputer the description and save it to file
            with open(os.path.join(app.config['UPLOAD_FOLDER'], rec_id, "desc.txt"),"w")as f:
              f.write(desc)
        for fl in input_file:
            with open(os.path.join(app.config['UPLOAD_FOLDER'], rec_id, "input.txt"),"a")as f:
                f.write(f"file '{fl}'\nduration 1\n")
    return render_template("create.html",myid=myid)

@app.route("/gallery")
def gallery():
    reels=os.listdir("static/reels")
    print(reels)
    return render_template("gallery.html",reels =reels)

app.run(debug=True)