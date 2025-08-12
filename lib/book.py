#!/usr/bin/env python3

class Book:
     def __init__(self, title=None, page_count=0):
        self.title = title
        self.page_count = page_count

     @property
     def title(self):
        return self._title

     @title.setter
     def title(self, value):
        self._title = value

     @property
     def page_count(self):
        return getattr(self, "_page_count", None)

     @page_count.setter
     def page_count(self, value):
        if isinstance(value, int):
            self._page_count = value
        else:
            # EXACT string, and do NOT raise
            print("page_count must be an integer")
            # (leave _page_count unchanged)
    
     def turn_page(self):
        print("Flipping the page...wow, you read fast!")