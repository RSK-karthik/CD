class SymbolTable:
    def _init_(self):
        self.table = {}
    
    def insert(self, id, scope, Type, lineNo):
        if id in self.table:
            return False
        self.table[id] = (scope, Type, lineNo)
        return True
    
    def find(self, id):
        if id in self.table:
            print(f"Identifier's Name: {id}")
            print(f"Type: {self.table[id][1]}")
            print(f"Scope: {self.table[id][0]}")
            print(f"Line Number: {self.table[id][2]}")
            return self.table[id][0]
        return -1
    
    def delete_record(self, id):
        if id in self.table:
            del self.table[id]
            return True
        return False
    
    def modify(self, id, scope, Type, lineNo):
        if id in self.table:
            self.table[id] = (scope, Type, lineNo)
            return True
        return False


if __name__ == '_main_':
    st = SymbolTable()
    print("**** SYMBOL_TABLE ****")
    
    # insert 'if'
    if st.insert("if", "local", "keyword", 4):
        print("if inserted")
    else:
        print("Failed to insert")
    
    # insert 'number'
    if st.insert("number", "global", "variable", 2):
        print("number inserted\n")
    else:
        print("Failed to insert")
    
    # find 'if'
    check = st.find("if")
    if check != -1:
        print("Identifier Is present")
    else:
        print("Identifier Not Present")