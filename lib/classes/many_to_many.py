class Article:
    def __init__(self, author, magazine, title):
        if not isinstance(title, str):
            raise ValueError("Title must be a string.")
        
        if not  5<=len(title)<=50:
            raise ValueError("Title must be between 5 and 50 characters.")

        self.author = author
        self.magazine = magazine
        self._title = title
    
    @property
    def title(self):
        return self._title
    
 
        
        
        
        
class Author:
    def __init__(self, name):
        self.name = name
        
     
    @property
    def name(self):
        return self._name 
    
    @name.setter
    def name(self, name):
        if hasattr(self, '_name'):
            raise ValueError("Name already set.")
       
        if not isinstance(name, str):
            raise ValueError("Name must be a string.")

        if len(name) == 0:
            raise ValueError("name cannot be empty")

        self._name = name
    


    def articles(self):
        pass

    def magazines(self):
        pass

    def add_article(self, magazine, title):
        pass

    def topic_areas(self):
        pass

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
        pass

    def contributors(self):
        pass

    def article_titles(self):
        pass

    def contributing_authors(self):
        pass
