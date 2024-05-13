import re
from .util import SearchSequence, LogMatchRegistry

class RegexSearchSequence(SearchSequence):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def create_log_match_registry(self, log_lines):
        try:
            if not log_lines:
                return False
            
            log_match_registry = LogMatchRegistry()
            
            input_id_list = []
            for input in self.input_list:
                input_id = log_match_registry.create_input_key(input)
                input_id_list.append(input_id)

            for log_line, log_statement in enumerate(log_lines, start=1):
                target_log_statement = log_statement

                if self.case_sensitivity is False:
                    target_log_statement = target_log_statement.lower()

                for input_id in input_id_list:
                    input = log_match_registry.get_input_by_id(input_id)

                    if self.case_sensitivity is False:
                        input = input.lower()

                    if re.search(input, target_log_statement):
                        log_match_registry.insert_log_value(input_id=input_id, log_line=log_line, log_statement=log_statement)

            return log_match_registry

        except Exception as e:
            # print("An error occurred: {}".format(e))
            return False