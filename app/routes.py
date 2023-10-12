from flask import render_template,request
from werkzeug.utils import secure_filename
from . import app
from .utils import predict,get_model
import os

@app.route('/',methods=['GET','POST'])
def home():
    if request.method == "POST":
        foto = request.files['foto']
        if foto.filename == '':
            return "filename is required"
        filename= secure_filename(foto.filename)
        path = os.path.join('app/img',filename)
        foto.save(path)
        hasil = predict(path)
        return render_template('dashboard.html',hasil=hasil,fn=filename)
    return render_template('dashboard.html')


@app.route('/clear')
def clear():
    pswd = request.args['pswd']
    if pswd != 'fasisme123':
        return "password anda salah!"
    else:

        img_list = os.listdir(os.path.join('app','img'))
        if len(img_list) == 0:
            return "data sudah kosong !"
        for i in img_list:
            os.remove(os.path.join('app','img',i))
    
        return str(img_list)



