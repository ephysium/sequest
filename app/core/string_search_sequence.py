from .__util import SearchSequence

class StringSearchSequence(SearchSequence):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def method(self, log_lines):
        try:
            if not log_lines:
                return False
            
            input_id_list = []
            for input in self.input_list:
                input_id = self.matched_logs.create_input_key(input)
                input_id_list.append(input_id)

            for log_line, log_statement in enumerate(log_lines, start=1):
                target_log_statement = log_statement

                if self.case_sensitivity is False:
                    target_log_statement = target_log_statement.lower()

                for input_id in input_id_list:
                    input = self.matched_logs.get_input_by_id(input_id)

                    if self.case_sensitivity is False:
                        input = input.lower()

                    if input in target_log_statement:
                        self.matched_logs.insert_log_value(input_id=input_id, log_line=log_line, log_statement=log_statement)

            return True

        except Exception as e:
            # print("An error occurred: {}".format(e))
            return False