import datetime



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
                created_at TEXT,
                updated_at TEXT
            );
        '''
        
    def getAllView(self):
        """return create view query

        Args:
            limit (int): query param

        Returns:
            str: view query
        """
        return f'''
            CREATE VIEW urls_get_view AS
                SELECT * FROM urls ORDER BY count desc LIMIT 3;
        '''
        
    def removeTrigger(self):
        """trigger for removing unused urls

        Returns:
            str: trigger creation query
        """
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
        return '''
            SELECT * FROM urls ORDER BY created_at desc;
        '''
    
    def getAll(self):
        """get top 3 urls query

        Returns:
            str: get all query
        """
        return f'''
            SELECT * FROM urls_get_view;
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
