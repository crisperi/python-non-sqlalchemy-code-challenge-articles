class Author:
    def __init__(self, name):
        if not isinstance(name, str):
            raise AttributeError("author name should be a string")
        if len(name) == 0:
            raise ValueError("author name should be longer than 0 characters")
        self._name = name

    @property
    def name(self):
        return self._name

    def articles(self):
        return [article for article in Article.all if article.author == self]

    def magazines(self):
        return list(set(article.magazine for article in self.articles()))

    def add_article(self, magazine, title):
        if not isinstance(magazine, Magazine):
            raise ValueError("Magazine must be a Magazine instance.")
        return Article(self, magazine, title)

    def topic_areas(self):
        return list(set(magazine.category for magazine in self.magazines())) or None


class Magazine:
    def __init__(self, name, category):

        if not (2 <= len(name) <= 16):    
            raise ValueError("Name must be a string between 2 and 16 characters.")
        if  len(category) == 0:
            raise ValueError("Category must be a non-empty string.")
        
        self._name = name
        self._category = category

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, name):
        if not isinstance(name, str):
            raise AttributeError("Magazine name should be a string")
        if not (2 <= len(name) <= 16):
            raise ValueError("Name must be a string between 2 and 16 characters.")
        self._name = name

    @property
    def category(self):
        return self._category

    @category.setter
    def category(self, value):
        if not isinstance(value, str):
            raise AttributeError("Magazine category should be a string")
        if len(value) == 0:
            raise ValueError("Category must be a non-empty string.")
        self._category = value

    def articles(self):
        return [article for article in Article.all if article.magazine == self]

    def contributors(self):
        return list(set(article.author for article in self.articles()))

    def article_titles(self):
        titles = [article.title for article in self.articles()]
        return titles if titles else None

    def contributing_authors(self):
        authors = [article.author for article in self.articles()]
        return [author for author in set(authors) if authors.count(author) > 2] or None


class Article:
    all = []

    def __init__(self, author, magazine, title):
        if not isinstance(author, Author):
            raise ValueError("Author must be an Author instance.")
        if not isinstance(magazine, Magazine):
            raise ValueError("Magazine must be a Magazine instance.")
        if not isinstance(title, str) or not (5 <= len(title) <= 50):
            raise ValueError("Title must be a string between 5 and 50 characters.")

        self._author = author
        self._magazine = magazine
        self._title = title
        Article.all.append(self)

    @property
    def author(self):
        return self._author

    @property
    def magazine(self):
        return self._magazine

    @property
    def title(self):
        return self._title

    @author.setter
    def author(self, value):
        if not isinstance(value, Author):
            raise ValueError("Author must be an Author instance.")
        self._author = value

    @magazine.setter
    def magazine(self, value):
        if not isinstance(value, Magazine):
            raise ValueError("Magazine must be a Magazine instance.")
        self._magazine = value