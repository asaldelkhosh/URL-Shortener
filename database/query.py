import datetime



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
        return f'''
            INSERT INTO urls (url, short, count, created_at, updated_at) VALUES ("{url}", "{short}", 1, "{datetime.datetime.now()}", "{datetime.datetime.now()}");
        '''
        
    def updateURL(self, id):
        """update count value of an url

        Args:
            id (int): url id

        Returns:
            str: update url query
        """
        return f'''
            UPDATE urls SET count = count + 1 WHERE id = {id};
        '''
    
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
    
    def getURL(self, url):
        """get an specific url

        Args:
            url (str): url

        Returns:
            str: get url query
        """
        return f'''
            SELECT * FROM urls WHERE url = "{url}";
        '''
    
    def removeURL(self, id):
        """remove a url

        Args:
            id (int): url id

        Returns:
            str: remove query
        """
        return f'''
            DELETE FROM urls WHERE id = {id};
        '''
