# Creating classes
class User:
    """User class"""

    def __init__(self, user_id, username):
        # constructor for attributes
        self.id = user_id
        self.username = username
        self.followers = 0
        self.following = 0

    def follow(self, user):
        # Needs to have the self parameter
        """Follow input user"""
        user.followers += 1
        self.following += 1


# instantiating object
user_1 = User("001", "Bob")
user_2 = User("002", "Jill")

user_1.follow(user_2)
print(user_1.followers)
print(user_1.following)
print(user_2.followers)
print(user_2.following)
