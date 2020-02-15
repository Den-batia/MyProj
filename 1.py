class Na:

    def __enter__(self):
        self.a = open('d:/1.txt', 'a')
        return self.a

    def __exit__(self, exc_type, exc_val, exc_tb):
        if exc_type is None:
            self.a.close()
        else:
            print(exc_type)
            self.a.close()
            return True


with Na() as f:
    raise Exception
    f.write('sssssssss')
print('end')
