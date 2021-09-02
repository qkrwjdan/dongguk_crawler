from mailer import BaseTemplate

class Post():
    
    def __init__(self, theme, title, content, link, date):
        self.theme = theme
        self.title = title
        self.content = content + "..."
        self.link = link
        self.date = date

    def __str__(self):
        return self.title + "-" + self.date

    def __repr__(self):
        return self.title + "-" + self.date

    def __eq__(self, other):
        return self.title == other.title

    