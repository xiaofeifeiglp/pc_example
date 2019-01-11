# from contextlib import contextmanager
#
# @contextmanager  # my_open=contextmanager(my_open)
# def my_open(path, mode):
#     f = open(path, mode)
#     print(type(f))
#     yield f
#     f.close()
#
# with my_open('out.txt', 'w') as f:
#     f.write('hello python ---')
#     print('------------')
#
#
#
#


# class ListTransaction:
#     def __init__(self, orig_list):
#         self.orig_list = orig_list
#         self.working = list(orig_list)
#
#     def __enter__(self):
#         return self.working
#
#     def __exit__(self, exc_type, exc_val, exc_tb):
#         self.orig_list[:] = self.working
#
# items_3 = [1, 2, 3]
# with ListTransaction(items_3) as working_3:
#     working_3.append(4)
#     working_3.append(5)
# print(items_3)
