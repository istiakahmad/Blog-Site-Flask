from datetime import datetime
from itsdangerous import TimedJSONWebSignatureSerializer as Serializer
from Include import db, login_manager, app
from flask_login import UserMixin


"""
****sqlite database creation command****
from Include.models import db  # main file name
db.create_all()
from Include.models import User, Post # User and Post are table
user_1 = User(username='ahmad', email='a@gmail.com', password='password')
db.session.add(user_1)
user_3 = User(username='muhaimeen', email='m@gmail.com', password='password')
db.session.add(user_3)
db.session.commit()
User.query.all()
User.query.first()
User.query.filter_by(username='ahmad').all()
User.query.filter_by(username='ahmad').first()
user1 = User.query.filter_by(username='ahmad').first()
user1.id
user1 = User.query.get(1)
user1.id
user1.posts
post1 = Post(title = 'Blog 1', content='First post', user_id=user1.id)
post3 = Post(title = 'Blog 3', content='Third Post post', user_id=user1.id)
db.session.add(post1)
db.session.add(post3)
db.session.commit()
user1.posts

for post in user1.posts:
    print(post.title)
post = Post.query.first()
post
post.user_id
post.author
db.drop_all()
db.create_all()
User.query.all()
Post.query.all()

"""

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(20), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    image_file = db.Column(db.String(20), nullable=False, default='default.jpg')
    password = db.Column(db.String(60), nullable=False)
    posts = db.relationship('Post', backref='author', lazy=True)

    def get_reset_token(self, expires_sec=1800):
        s = Serializer(app.config['SECRET_KEY'], expires_sec)
        return s.dumps({'user_id': self.id}).decode('utf-8')

    @staticmethod
    def verify_reset_token(token):
        s = Serializer(app.config['SECRET_KEY'])
        try:
            user_id = s.loads(token)['user_id']
        except:
            return None
        return User.query.get(user_id)

    #how object will print description
    def __repr__(self):
        return f"User('{self.username}', '{self.email}', '{self.image_file}')"

class Post(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    date_posted = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    content = db.Column(db.Text, nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)

    #how object will print description
    def __repr__(self):
        return f"Post('{self.title}', '{self.date_posted}')"
