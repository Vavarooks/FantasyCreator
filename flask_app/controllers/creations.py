from flask import Flask, render_template, redirect, request, session, flash
from flask_app.models.creation import Sheet
from flask_app.models.user import Users
from flask_bcrypt import Bcrypt
from werkzeug.utils import secure_filename
import base64
from flask_app import app
bcrypt = Bcrypt(app)

ALLOWED_EXTENSIONS = {'txt', 'pdf', 'png', 'jpg', 'jpeg', 'gif'}

def allowed_file(filename):
    return '.' in filename and \
        filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

@app.route("/")
def index():
    return render_template("login.html")

@app.route('/home')
def home():
    all_characters = Sheet.get_all()
    operator = {
        "id": session["logged_id"]
    }
    this_user = Users.find_one_by_id(operator)
    return render_template("index.html",all_characters=all_characters,this_user=this_user)

@app.route('/auction')
def auction():
    return render_template('auction.html')

@app.route('/adventure')
def adventure():
    return render_template('adventure.html')

@app.route('/guild')
def guild():
    return render_template('guildhall.html')

@app.route('/created/<int:id>')
def creates(id):
    data ={
        "id": id
    }
    operator = {
        "id": session["logged_id"]
    }
    this_user = Users.find_one_by_id(operator)
    one_character = Sheet.get_one(data)
    return render_template('created.html',one_character=one_character,this_user=this_user)

@app.route('/edit/<int:id>')
def edit(id):
    data ={
        "id": id
    }
    operator = {
        "id": session["logged_id"]
    }
    this_user = Users.find_one_by_id(operator)
    one_character = Sheet.get_one(data)
    return render_template('edit.html',one_character=one_character,this_user=this_user)

@app.route('/delete/<int:id>')
def delete(id):
    data = {
        "id":id
    }
    Sheet.delete(data)
    return redirect('/home')

@app.route('/creation/post',methods=["POST"])
def created():

    if request.method == 'POST':
        # check if the post request has the file part
        if 'img_data' not in request.files:
            flash("No Image! Please Put one!")
            print('No file part')
            return redirect("/")
        file = request.files['img_data']
        # If the user does not select a file, the browser submits an
        # empty file without a filename.
        if file.filename == '':
            print('No selected file')
            return redirect(request.url)
        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)
            # file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
            print("hey we can process it now!")
            image = request.files["img_data"]
            # to encode
            image_string = base64.b64encode(image.read())
            #when you pull the data from the database, you can put it in this variable like so
            #make sure image_string before this line is the data for just the image from the table
            image_string = image_string.decode("utf-8")

    data ={
        "img_data": image_string,
        "character_dis": request.form["character_dis"],
        "height": request.form["height"],
        "weight": request.form["weight"],
        "name": request.form["name"],
        "race": request.form["race"],
        "gender": request.form["gender"],
        "job": request.form["job"],
        "character_bio": request.form["character_bio"],
        "strength": request.form["strength"],
        "dexterity": request.form["dexterity"],
        "wisdom": request.form["wisdom"],
        "constatution": request.form["constatution"],
        "intelegence": request.form["intelegence"],
        "charisma": request.form["charisma"],
        "users_id": session["logged_id"]
    }
    if not Sheet.validate(data):
        print("not valid")
        return redirect("/home")
    new_id = Sheet.save(data)
    print(f'{new_id}')
    # session["logged_id"] == Sheet.save(data)
    print("Made Character")
    return redirect("/home")
    # return redirect('/created/'+ str(image.string))

@app.route('/result/<int:id>')
def result(id):
    data = {
        "id" : id,
    }
    if "logged_id" not in session:
        flash("Log in to veiw!")
        return redirect("/")
    one_character = Sheet.get_one(data)
    # print(one_character)
    operator = {
        "id": session["logged_id"]
    }
    this_user = Users.find_one_by_id(operator)
    print('Submitted Form')
    return render_template('owned.html', one_character=one_character, this_user = this_user)

@app.route('/edited/<int:id>/post',methods=["POST"])
def edited(id):

    if request.method == 'POST':
        # check if the post request has the file part
        if 'img_data' not in request.files:
            print('No file part')
            return redirect("/")
        file = request.files['img_data']
        # If the user does not select a file, the browser submits an
        # empty file without a filename.
        if file.filename == '':
            print('No selected file')
            return redirect(request.url)
        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)
            # file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
            print("hey we can process it now!")
            image = request.files["img_data"]
            # to encode
            image_string = base64.b64encode(image.read())
            #when you pull the data from the database, you can put it in this variable like so
            #make sure image_string before this line is the data for just the image from the table
            image_string = image_string.decode("utf-8")

    data ={
        "id": id,
        "img_data": image_string,
        "character_dis": request.form["character_dis"],
        "height": request.form["height"],
        "weight": request.form["weight"],
        "name": request.form["name"],
        "race": request.form["race"],
        "gender": request.form["gender"],
        "job": request.form["job"],
        "character_bio": request.form["character_bio"],
        "strength": request.form["strength"],
        "dexterity": request.form["dexterity"],
        "wisdom": request.form["wisdom"],
        "constatution": request.form["constatution"],
        "intelegence": request.form["intelegence"],
        "charisma": request.form["charisma"],
        "users_id": session["logged_id"]
    }
    if not Sheet.validate(data):
        print("not valid")
        return redirect("/home")
    Sheet.edit(data)
    print("Made Character")
    return redirect('/home')

@app.route("/success")
def success():
    if "logged_id" not in session:
        
        return redirect("/")

    # user_id = Users.veiw_one({"id": session["logged_id"]})
    return redirect("/home")

@app.route("/register", methods=["post"])
def register_user():
    print("trying to register here")
    

    data = {
        "first_name": request.form["first_name"],
        "last_name": request.form["last_name"],
        "email": request.form["email"],
        "password": request.form["password"],
        "password_confirm": request.form["password_confirm"],
        "email_confirm": request.form["email_confirm"],
    }
    if not Users.validate(data):
        print("not valid")
        return redirect('/')

    pw_hash = bcrypt.generate_password_hash(request.form['password'])
    data["password"] = pw_hash
    print(f"password:{request.form['password']}")
    
    user_id = Users.save(data)
    session["logged_id"] = user_id
    return redirect('/success')


@app.route("/logout")
def logout():
    session.clear()
    return redirect("/")

@app.route("/login", methods=["post"])
def login():

    data = {
        "email" : request.form["email"]
    }

    this_user = Users.find_one_by_email(data)

    if not this_user:
        flash("Invalid Email or Password")
        return redirect("/")
    if not bcrypt.check_password_hash(this_user.password, request.form['password']):
        flash("Invalid Email or Password")
        return redirect("/")

    session["logged_id"] = this_user.id
    
    print("Successful Login!")


    return redirect("/success")