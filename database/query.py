import time



class Query(object):
    def createTable(self):
        """create the base table

        Returns:
            str: create table query
        """
        return '''
            CREATE TABLE urls (
                id         INTEGER PRIMARY KEY AUTOINCREMENT,
                url        VARCHAR(1024) NOT NULL,
                short      VARCHAR(1024) NOT NULL,
                count      INTEGER,
                updated_at TEXT
            );
        '''
        
    def removeTrigger(self):
        return '''
            CREATE TRIGGER remove_unused_urls BEFORE update 
            ON urls
            BEGIN
                DELETE FROM urls WHERE datetime(updated_at) < datetime('now', '-7 day');
            END;
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
            INSERT INTO urls (url, short, count, updated_at) VALUES ("{url}", "{short}", 0, "{time.time()}");
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
    
    def getAll(self, limit):
        """get top 3 urls query

        Returns:
            str: get all query
        """
        return f'''
            SELECT * FROM urls ORDER BY count desc LIMIT {limit};
        '''
    
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
