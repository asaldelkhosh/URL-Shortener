import time



class Query(object):
    def createTable(self):
        """create the base table

        Returns:
            str: create table query
        """
        return '''
            create table urls (
                id         INTEGER PRIMARY KEY AUTOINCREMENT,
                url        VARCHAR(1024) NOT NULL,
                short      VARCHAR(1024) NOT NULL,
                count      INTEGER,
                updated_at TEXT,
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
            insert into urls (url, short, count, updated_at) values ("{url}", "{short}", 0, "{time.time()}");
        '''
    
    def getAll(self, limit):
        """get top 3 urls query

        Returns:
            str: get all query
        """
        return f'''
            select * from urls order by count desc limit {limit};
        '''
    
    def getURL(self, url):
        """get an specific url

        Args:
            url (str): url

        Returns:
            str: get url query
        """
        return f'''
            select * from urls where url = "{url}"
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
