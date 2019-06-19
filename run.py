from Include import app


if __name__ == '__main__':
    app.run(debug=True)


"""
pip install Bcrypt
from flask_bcrypt import Bcrypt
bcrypt = Bcrypt()
bcrypt.generate_password_hash('testing')
bcrypt.generate_password_hash('testing').decode('utf-8')
hash_pw = bcrypt.generate_password_hash('testing').decode('utf-8')

bcrypt.check_password_hash(hash_pw, 'password') # False
bcrypt.check_password_hash(hash_pw, 'testing')  #True
                        
                        DataBase Creation
from Include.models import db
from Include.models import User, Post
db.create_all()
User.query.all()
Post.query.all()
                        DataBase Check after Sign up
from Include import db
from Include.models import User
user = User.query.first()
user
user.password

from Include.models import Post
posts = Post.query.all()

for post in posts:
     print(post)

 posts = Post.query.paginate()
 posts
 dir(posts)
 posts.per_page
 posts.page 
for post in posts.items:
     print(post)

posts = Post.query.paginate(page=2)
for post in posts.items:
     print(post)
     
posts = Post.query.paginate(per_page = 5)
posts.page

posts.total

from itsdangerous import TimedJSONWebSignatureSerializer as Serializer
s = Serializer("secret", 30) # Token expire after 30 second
token = s.dumps({'user_id':1}).decode('utf-8')
token
s.loads(token)
"""
