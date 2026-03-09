from k_top_calculator import calculator
from heap import heap_object





class SalesStatisticsSystem:
    def __init__(self):
       self._dataloader = []
       self._products_list = []
       self._top__calculator = calculator(10)
    def execute_top_k_analysis(self):
        for product in self._products_list:
            self._top__calculator.caculate_if_insert_KTOP(product.get_sales())
    def get_Toplist(self):
        return self._top__calculator.get_KTOP
    def load_data(self,data):
        self._dataloader = data
        for item in self._dataloader:
            self._products_list.append(item)