from . import api,app,Resource
from .utils import predict
from werkzeug.utils import secure_filename
from flask import request
import os

class ImageClassfier(Resource):
    def post(self):
        img  =  request.files['image']
        if img.filename == '':
            return "filename is required"
        filename= secure_filename(img.filename)
        path = os.path.join('app/img',filename)
        img.save(path)
        hasil = predict(path=path)
        if hasil :
            os.remove(path=path)
        return {"msg":"success predict",'return':str(hasil)},200
        

api.add_resource(ImageClassfier,'/api/images')

