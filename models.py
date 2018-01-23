from datetime import date

class Comment(object):
    def __init__(self, text, date):
        """Counstructor."""
        super(Comment, self).__init__()
        self.text = text
        self.date = date

    def __repr__(self):
        return "Comment: {} Created: {}".format(self.text, self.date)

    def serialize(self):
        return {
            'comment': self.text, 
            'date': self.date,
        }


COMMENTS = []
COMMENTS.append(Comment("This is so cool", date.today().strftime("%Y-%m-%d")))
COMMENTS.append(Comment("This is great", date.today().strftime("%Y-%m-%d")))
COMMENTS.append(Comment("I like this", date.today().strftime("%Y-%m-%d")))
