from .log_match_registry import LogMatchRegistry

class SearchSequence:
    def __init__(self, target_filepath="", input_list=[], case_sensitivity=True, successive_log_lines=False):
        self.target_filepath = target_filepath
        self.type = type
        self.input_list = input_list
        self.case_sensitivity = case_sensitivity
        self.successive_log_lines = successive_log_lines
        
    def execute(self):
        extracted_log_lines = self.__extract_log_from_file()

        if not extracted_log_lines:
            return False
        
        log_match_registry = self.create_log_match_registry(log_lines=extracted_log_lines)

        if not isinstance(log_match_registry, LogMatchRegistry):
            return False
        
        has_empty_matched_logs = log_match_registry.check_empty_matched_log_list()

        if has_empty_matched_logs:
            return False
        
        is_equalized = log_match_registry.equalize_log_lists()

        if not is_equalized:
            return False
        
        return self.__establish_sequence(log_match_registry)

    def __establish_sequence(self, log_match_registry):
        result_list = []

        for log_index in range(log_match_registry.get_minimum_log_list_length()):
            log_sequence_instance = []

            is_sequence_disjointed = False
            for log_list_index in range(log_match_registry.count_log_lists()):
                current_sequence_log = log_match_registry.get_log(log_list_index=log_list_index, log_index=log_index)

                if self.successive_log_lines is True:
                    if log_list_index > 0:
                        previous_sequence_log = log_match_registry.get_log(log_list_index=log_list_index-1, log_index=log_index)

                        if previous_sequence_log["log_line"] > current_sequence_log["log_line"]:
                             is_sequence_disjointed = True
                             break

                log_sequence_instance.append(current_sequence_log)

            if is_sequence_disjointed is False:
                result_list.append(log_sequence_instance)
        
        return result_list
    
    def __extract_log_from_file(self):    
        try:
            with open(self.target_filepath, "r", encoding="utf-8") as file:
                return file.readlines()
         
        except Exception as e:
            # print("An error occurred: {}".format(e))
            return False

    def create_log_match_registry(self, log_lines):
        pass