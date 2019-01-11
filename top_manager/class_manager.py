class Fire():

    def __init__(self, filename, mode):
        self.filename = filename
        self.mode = mode

    def __enter__(self):
        print("__enter")
        self.f = open(self.filename, self.mode)
        return self.f

    def __exit__(self, exc_type, exc_val, exc_tb):
        print('will exit')
        self.f.close()

with Fire('out.txt', 'w') as f:
    print('writting')
    f.write('hello  python')


# from contextlib import contextmanager
#
#
# @contextmanager
# def list_transaction(orig_list):
#     working = list(orig_list)
#     yield working
#     orig_list[:] = working
#
# items_2 = [1, 2, 3]
# try:
#     with list_transaction(items_2) as working_2:
#         working_2.append(4)
#         working_2.append(5)
#         raise RuntimeError('oops')
# except Exception as ex:
#     print(ex)
# finally:
#     print(items_2)

