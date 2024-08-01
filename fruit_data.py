class fruitData:

    def __init__(self,file):

        self.file = file
    
    def iloc_func(self, row_start, row_end, column_start, column_end):

        if column_end == None and row_end == None:
            value = self.file.iloc[row_start:, column_start:]
        elif column_end == None:
            value = self.file.iloc[row_start:row_end, column_start:]
        elif row_end == None:
            value = self.file.iloc[row_start:, column_start:column_end]
        
        return value
