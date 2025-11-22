class References:
    def __init__(self):
        self._references = {}

    def set_references(self, query):
        self.clear()

        for row in query:
            table = row[0]
            data = {k: v for k, v in dict(row._mapping).items() if v is not None}
            
            if table not in self._registry:
                self._registry[table] = []
            self._registry[table].append(data)

    def get_all(self):
        result = []
        for records in self._registry.values():
            result.extend(records)
        return result
    
    def get_by_table(self, table):
        return self._references.get(table, [])
    
    def clear(self):
        self._references.clear()