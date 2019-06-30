from .models import Gist

def getDBQueryAndParams(**kwargs):
    query = 'SELECT * FROM gists '
    filters = ''
    params = {}
    if kwargs:
        if 'github_id' in kwargs or 'created_at' in kwargs:
            filters += 'WHERE'
        if 'github_id' in kwargs:
            filters += ' github_id = :github_id'
            params['github_id'] = kwargs['github_id']
        if 'created_at' in kwargs:
            if filters and not filters == 'WHERE':
                filters += ','
            filters += ' datetime(created_at) == datetime(:created_at)'
            params['created_at'] = kwargs['created_at']
    query += filters
    return query, params

def search_gists(db_connection, **kwargs):
    query, params = getDBQueryAndParams(**kwargs)

    cursor = db_connection.execute(query, params)
    results = []
    for gist in cursor:
        results.append(Gist(gist))
    return results
