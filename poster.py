class Post():
    
    def __init__(self, theme, title, contents, link, date):
        self.theme = theme
        self.title = title
        self.contents = contents
        self.link = link
        self.date = date

    def __str__(self):
        return self.title + "-" + self.date

    def __repr__(self):
        return self.title + "-" + self.date
    
    def make_mail_content(self):
        return self.theme + "\n" + self.title + "\n" + self.contents + "\n" + self.link
