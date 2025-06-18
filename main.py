from post import Post
from user import User

user_one = User("email@mail.com", "Rico", 'pwd', "Dev")
user_one.get_user_info()

user_one.change_job_title("test")
user_one.get_user_info()

user_two = User("email2@mail.com", "Math", 'mdp', "Runner")
user_two.get_user_info()

post_one = Post("post one", "me")
post_one.get_post_info()

post_two = Post("post one", user_two.name)
post_two.get_post_info()
