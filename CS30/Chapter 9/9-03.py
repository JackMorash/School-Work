class User():
    """Create user profile class"""

    def __init__(self, first_name, last_name, username, email, location):
        """Initialize the user."""
        self.first_name = first_name.title()
        self.last_name = last_name.title()
        self.username = username
        self.email = email
        self.location = location.title()

    def describe_user(self):
        """Display a summary of the user's information."""
        print(f"\n{self.first_name} {self.last_name}")
        print(f"  Username: {self.username}")
        print(f"  Email: {self.email}")
        print(f"  Location: {self.location}")

    def greet_user(self):
        """Display a personalized greeting to the user."""
        print(f"\nHello {self.username}!")

jack = User('jack', 'morash', 'jackmorash0', 'jackmorash0@gmail.com', 'regina')
jack.describe_user()
jack.greet_user()

ali = User('ali', 'nossier', 'gussc00n', 'ali.nossier@gmail.com', 'regina')
ali.describe_user()
ali.greet_user()