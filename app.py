import os
from flask import Flask, flash, request, redirect, url_for,render_template
from werkzeug import secure_filename
import SampleTesting 

app = Flask(__name__)

UPLOAD_FOLDER = './UploadedFiles'
ALLOWED_EXTENSIONS = set(['ODT', 'YAML', 'JPG', 'jpeg'])

app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html') 

@app.route('/upload', methods = ['GET', 'POST'])
def convert_ebook():
    if request.method == 'POST':
        #print('#0001')
        if 'odtfile' not in request.files:
            flash('No file part') 
            #print('#0001  24')
            return redirect(request.url)

    
        odt_file  = request.files['odtfile']
        yaml_file = request.files['yamlfile'] 
        jpg_file = request.files['jpgfile']

        if odt_file.filename == '':    
            flash('No selected file') 
            return redirect(request.url)

        odt_name = secure_filename(odt_file.filename)
        odt_path = os.path.join(app.config['UPLOAD_FOLDER'], odt_name)
        odt_file.save(odt_path)

        yaml_name = secure_filename(yaml_file.filename)
        yaml_path = os.path.join(app.config['UPLOAD_FOLDER'], yaml_name) 
        yaml_file.save(yaml_path) 

        jpg_name = secure_filename(jpg_file.filename) 
        jpg_path = os.path.join(app.config['UPLOAD_FOLDER'], jpg_name) 
        jpg_file.save(jpg_path) 
        
        SampleTesting.testing(ODTFILE=odt_path,CONFIGYAML=yaml_path,COVERJPG=jpg_path) 
       
        return 'file uploaded successfully'


#SampleTesting.testing(ODTFILE='a',CONFIGYAML='b',COVERJPG='c')

if __name__ == '__main__':
    if not os.path.exists(app.config['UPLOAD_FOLDER']):
        os.mkdir(app.config['UPLOAD_FOLDER'])
        print("Creating Directory")
    app.run(debug = True)
