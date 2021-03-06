from . import opdb

'''
    ############################################################
    functionality to insert/update information into the database
    ############################################################
    '''


def insert_row(url, tablename, **kwargs):
    '''
        Description
        -----------
            Insert information into a table

        Parameters
        ----------
            url       : `string` (e.g., 'postgresql://username:password@hostname:port/dbname')
            tablename : `string`
            dataframe : `pandas.DataFrame`

        Returns
        -------
            None

        Note
        ----
            Column labels of `dataframe` should be exactly the same as those of the table
    '''
    db = opdb.OpDB()
    db.dbinfo = url
    try:
        db.connect()
        db.insert_mappings(tablename, [kwargs])
    finally:
        db.close()
    return 0


def insert(url, tablename, dataframe):
    '''
        Description
        -----------
            Insert information into a table

        Parameters
        ----------
            url       : `string` (e.g., 'postgresql://username:password@hostname:port/dbname')
            tablename : `string`
            dataframe : `pandas.DataFrame`

        Returns
        -------
            None

        Note
        ----
            Column labels of `dataframe` should be exactly the same as those of the table
    '''
    db = opdb.OpDB()
    db.dbinfo = url
    try:
        db.connect()
        db.insert(tablename, dataframe)
    finally:
        db.close()
    return 0


def update(url, tablename, dataframe):
    '''
        Description
        -----------
            Update information of a table

        Parameters
        ----------
            url       : `string` (e.g., 'postgresql://username:password@hostname:port/dbname')
            tablename : `string`
            dataframe : `pandas.DataFrame`

        Returns
        -------
            None

        Note
        ----
            Column labels of `dataframe` should be exactly the same as those of the table
    '''
    db = opdb.OpDB()
    db.dbinfo = url
    try:
        db.connect()
        db.update(tablename, dataframe)
    finally:
        db.close()
    return 0


'''
    ##################################################
    functionality to get information from the database
    ##################################################
'''


def fetch_all(url, tablename):
    '''
        Description
        -----------
            Get all records from a table

        Parameters
        ----------
            url       : `string` (e.g., 'postgresql://username:password@hostname:port/dbname')
            tablename : `string`

        Returns
        -------
            df : `pandas.DataFrame`

        Note
        ----
    '''
    db = opdb.OpDB()
    db.dbinfo = url
    try:
        db.connect()
        df = db.fetch_all(tablename)
    finally:
        db.close()
    return df


def fetch_query(url, query):
    '''
        Description
        -----------
            Get all records from SQL query

        Parameters
        ----------
            url       : `string` (e.g., 'postgresql://username:password@hostname:port/dbname')
            query : `string`

        Returns
        -------
            df : `pandas.DataFrame`

        Note
        ----
    '''
    db = opdb.OpDB()
    db.dbinfo = url
    try:
        db.connect()
        df = db.fetch_query(query)
    finally:
        db.close()
    return df


def fetch_by_id(url, tablename, **kwargs):
    '''
        Description
        -----------
            Get records from a table where the keyword identifier is matched

        Parameters
        ----------
            url       : `string` (e.g., 'postgresql://username:password@hostname:port/dbname')
            tablename : `string`
            **kwargs  :          (e.g., pfs_visit_id=12345)

        Returns
        -------
            df : `pandas.DataFrame`

        Note
        ----
    '''
    db = opdb.OpDB()
    db.dbinfo = url
    try:
        db.connect()
        df = db.fetch_by_id(tablename, **kwargs)
    finally:
        db.close()
    return df


def fetch_sps_exposures(url, pfs_visit_id):
    '''
        Description
        -----------
            Get SpS exposure information for a given `pfs_visit_id`

        Parameters
        ----------
            url          : `string` (e.g., 'postgresql://username:password@hostname:port/dbname')
            pfs_visit_id : `int`

        Returns
        -------
            df : `pandas.DataFrame`

        Note
        ----
    '''
    db = opdb.OpDB()
    db.dbinfo = url
    try:
        db.connect()
        df = db.fetch_sps_exposures(pfs_visit_id=pfs_visit_id)
    finally:
        db.close()
    return df
