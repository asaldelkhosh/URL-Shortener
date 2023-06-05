class Query(object):
    def createTable(self):
        """create the base table

        Returns:
            str: create table query
        """
        return '''
            create table urls (
                id    INTEGER PRIMARY KEY AUTOINCREMENT,
                url   VARCHAR(1024) NOT NULL,
                short VARCHAR(1024) NOT NULL
            );
        '''
    
    def createURL(self, url, short):
        """create a new url query

        Args:
            url (str): url
            short (str): short url

        Returns:
            str: insert query
        """
        return f'''
            insert into urls values ("{url}", "{short}");
        '''
    
    def getAll(self):
        """get all urls query

        Returns:
            str: get all query
        """
        return '''
            select * from urls;
        '''
    
    def removeURL(self, id):
        """remove a url

        Args:
            id (int): url id

        Returns:
            str: remove query
        """
        return f'''
            delete from urls where id = {id};
        '''
