import uuid

class LogMatchRegistry:
    def __init__(self):
        self.__container = {}
        self.__input_mapping = {}

    def create_input_key(self, input):
        input_id = str(uuid.uuid4())

        self.__container[input_id] = []
        self.__input_mapping[input_id] = input

        return input_id

    def insert_log_value(self, input_id, log_line, log_statement):
        if input_id in self.__container:
            self.__container[input_id].append(
                {
                    "log_line": log_line,
                    "log_statement": log_statement
                }
            )

            return True
        
        return False
    
    def get_input_by_id(self, input_id):
        return self.__input_mapping[input_id]
    
    def check_empty_matched_log_list(self):
        return any(len(log_list) == 0 for log_list in self.__container.values())
    
    def get_minimum_log_list_length(self) -> int:
        return min(len(log_list) for log_list in self.__container.values())

    def equalize_log_lists(self):
        if self.check_empty_matched_log_list():
            return False
        
        equalized_length = self.get_minimum_log_list_length()

        for input_id, log_list in self.__container.items():
            self.__container[input_id] = log_list[:equalized_length]

        return True

    def count_log_lists(self):
        return len(self.__container)
    
    def get_log(self, log_list_index, log_index):
        try:
            log = list(self.__container.values())[log_list_index][log_index]

            return log
        
        except Exception as e:
            return None