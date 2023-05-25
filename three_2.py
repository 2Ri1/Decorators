# Применить написанный логгер к приложению из любого предыдущего д/з.

from two import logger

list_of_lists_1 = [
        ['a', 'b', 'c'],
        ['d', 'e', 'f', 'h', False],
        [1, 2, None]
    ]

class FlatIterator:
	
	def __init__(self, list_of_list):
		
		self.main_list = list_of_list
	
	def __iter__(self):
		self.main_list_cursor = 0  # курсор основного списка
		self.nested_list_cursor = -1  # курсор списка вложенного в основной список
		return self
	
	def __next__(self):
		
		self.nested_list_cursor += 1    # увеличиваем nested_list_cursor
		if self.nested_list_cursor >= len(self.main_list[self.main_list_cursor]):  # если во вложенном списке элементы закончились,
			
			self.main_list_cursor += 1       # то переходи на следующий список увеличив main_list_cursor
			self.nested_list_cursor = 0     # и обнуляем main_list_cursor

		if self.main_list_cursor  >= len(self.main_list):
			raise StopIteration
			
		return self.main_list[self.main_list_cursor][self.nested_list_cursor]
	
path = 'fun.log'
@logger(path)
def test_4():

    list_of_lists_1 = [
        ['a', 'b', 'c'],
        ['d', 'e', 'f', 'h', False],
        [1, 2, None]
    ]

    for flat_iterator_item, check_item in zip(
            FlatIterator(list_of_lists_1),
            ['a', 'b', 'c', 'd', 'e', 'f', 'h', False, 1, 2, None]
    ):

        assert flat_iterator_item == check_item

    assert list(FlatIterator(list_of_lists_1)) == ['a', 'b', 'c', 'd', 'e', 'f', 'h', False, 1, 2, None]