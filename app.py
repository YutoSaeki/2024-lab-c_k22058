from flask import Flask, request, jsonify, render_template, flash, redirect, url_for
from flask_sqlalchemy import SQLAlchemy # Flask上でデータベースとのやり取りを行うためのライブラリ（確認用）
from werkzeug.security import generate_password_hash, check_password_hash

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///users.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

app.secret_key = 'secret_key'

db = SQLAlchemy(app)

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    password_hash = db.Column(db.String(128), nullable=False)

    def set_password(self, password):
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password_hash, password)
    
# ログイン画面
@app.route('/')
def index():
    return render_template('addGroup.html')

# ユーザ登録の処理
# @app.route('/register', methods=['POST'])
# def register():
#     data = request.form
#     username = data.get('new_username')
#     password = data.get('new_password')

#     if not username or not password:
#         return jsonify({'message': 'ユーザー名またはパスワードがありません'}), 400

#     if User.query.filter_by(username=username).first():
#         return jsonify({'message': 'このユーザーは既に存在します'}), 400

#     user = User(username=username)
#     user.set_password(password)
#     db.session.add(user)
#     db.session.commit()

#     return jsonify({'message': 'ユーザ登録が完了しました'}), 201

# ログインの処理
# @app.route('/login', methods=['POST'])
# def login():
#     data = request.form
#     username = data.get('username')
#     password = data.get('password')

#     if not username or not password:
#         return jsonify({'message': 'ユーザー名またはパスワードがありません'}), 400
#         #flash('ユーザー名またはパスワードがありません')
#         #return redirect(url_for('login'))

#     user = User.query.filter_by(username=username).first()
#     if user and user.check_password(password):
#         return jsonify({'message': 'ログインしました'}), 200
#         #flash('ログインしました')
#         #return redirect(url_for('login'))

#     return jsonify({'message': 'ユーザー名かパスワードが無効です'}), 400
#     #flash('ユーザー名かパスワードが無効です')

#     #return redirect(url_for('login'))



if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(debug=True, port=5001)
