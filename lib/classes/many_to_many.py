class Article:
    all = []
    def __init__(self, author, magazine, title):
        if not isinstance(title, str):
            raise ValueError("Title must be a string.")
        
        if not  5<=len(title)<=50:
            raise ValueError("Title must be between 5 and 50 characters.")

        self.author = author
        self.magazine = magazine
        self._title = title
        Article.all.append(self)
        
    @property
    def title(self):
        return self._title
    
 
        
        
        
        
class Author:
    def __init__(self, name):
        if not isinstance(name, str):
            raise ValueError("Name must be a string.")

        if len(name) == 0:
            raise ValueError("name cannot be empty")
        self._name = name
        self._articles = []
        
        
     
    @property
    def name(self):
        return self._name 
    
    
    def articles(self):
        return self._articles


    def magazines(self):
        return [article.magazine for article in self._articles]


    def add_article(self, magazine, title):
        article = Article(self, magazine, title)
        self._articles.append(article)
        return article


    def topic_areas(self):
        return list(set(magazine.category for magazine in self.magazines()))


class Magazine:
    def __init__(self, name, category):
        self.name = name
        self.category = category
    
    @property
    def name(self):
        return self._name
    
    
    @name.setter
    def name(self, name):
        if not 2<=len(name)<=16:
            raise ValueError("Name must be between 2 and 16 characters.")
        if not isinstance(name, str):
            raise ValueError("name must be between 2 and 16 characters")
        self._name = name
        
    
    def articles(self):
        return self._articles
    

    def contributors(self):
        pass

    def article_titles(self):
        pass

    def contributing_authors(self):
        pass
