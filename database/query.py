class Query(object):
    def createTable(self):
        """create the base table

        Returns:
            str: create table query
        """
        with open('database/sql/createTable.sql', 'r') as file:
            return file.read()
        
    def getAllView(self):
        """return create view query

        Args:
            limit (int): query param

        Returns:
            str: view query
        """
        with open('database/sql/urlsView.sql', 'r') as file:
            return file.read()
        
    def removeTrigger(self):
        """trigger for removing unused urls

        Returns:
            str: trigger creation query
        """
        with open('database/sql/urlsTrigger.sql', 'r') as file:
            return file.read()
    
    def createURL(self, url, short):
        """create a new url query

        Args:
            url (str): url
            short (str): short url

        Returns:
            str: insert query
        """
        with open('database/sql/createURL.sql', 'r') as file:
            return file.read()
        
    def updateURL(self):
        """update count value of an url

        Args:
            id (int): url id

        Returns:
            str: update url query
        """
        with open('database/sql/updateURL.sql', 'r') as file:
            return file.read()
    
    def getAllByDate(self):
        """get all urls by created day

        Returns:
            str: get all query
        """
        with open('database/sql/getAll.sql', 'r') as file:
            return file.read()
    
    def getAll(self):
        """get top 3 urls query

        Returns:
            str: get all query
        """
        with open('database/sql/getTop3.sql', 'r') as file:
            return file.read()
    
    def getURL(self):
        """get an specific url

        Args:
            url (str): url

        Returns:
            str: get url query
        """
        with open('database/sql/getURL.sql', 'r') as file:
            return file.read()
    
    def removeURL(self):
        """remove a url

        Args:
            id (int): url id

        Returns:
            str: remove query
        """
        with open('database/sql/deleteURL.sql', 'r') as file:
            return file.read()
