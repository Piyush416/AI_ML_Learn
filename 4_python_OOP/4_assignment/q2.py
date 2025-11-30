''' Create a class Book with the following attributes:
• title
• author
• list of reviews
And add methods to:
• add a new review
• count reviews
• display all reviews '''

class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author
        self.reviews = []
    
    def add_review(self, review):
        self.reviews.append(review)
    
    def total_review(self):
        print(len(self.reviews))
    
    def display_review(self):
        print(self.reviews)

b1 = Book("English", "piyush")
b1.add_review("nice book")
b1.add_review("good book")

b1.total_review()
b1.display_review()


    


