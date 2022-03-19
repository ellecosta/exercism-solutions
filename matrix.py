class Matrix:
    def __init__(self, matrix_string):
        self.matrix_string = matrix_string

    def row(self, index):
        matrix_list = self.matrix_string.split('\n')
        new_row = matrix_list[index-1].split()
        for i in range(0, len(new_row)):
            new_row[i] = int(new_row[i])
        return new_row

    def column(self, index):
        matrix_list = self.matrix_string.split('\n')
        column_list = []
        for item in matrix_list:
            column_list.append(item.split()[index-1])
            
        for i in range(0, len(column_list)):
            column_list[i] = int(column_list[i])
        return column_list