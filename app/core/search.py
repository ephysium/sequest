import re

def search(filepath, sequence_list, case_sensitivity=True):
    found_count = {seq_elem: 0 for seq_elem in sequence_list}

    found_logSeq_list = []

    try:
        with open(filepath, "r", encoding="utf-8") as file:
            log_lines = file.readlines()

            for line_number, line_statement in enumerate(log_lines, start=1):
                target_line_statement = line_statement

                if case_sensitivity is False:
                    target_line_statement = target_line_statement.lower()

                for seq_elem in sequence_list:
                    search_elem = seq_elem

                    if case_sensitivity is False:
                        search_elem = search_elem.lower()

                    for _ in re.finditer(re.escape(search_elem), target_line_statement):
                        try:
                            found_logSeq_list[found_count[search_elem]][sequence_list.index(search_elem)] = (line_number, target_line_statement.strip())

                        except IndexError:
                            found_logSeq_list.extend([[("","")] * len(sequence_list)] * (found_count[search_elem] - len(found_logSeq_list) + 1))
                            found_logSeq_list[found_count[search_elem]][sequence_list.index(search_elem)] = (line_number, target_line_statement.strip())

                        except Exception as e:
                            print("An error occurred: {}".format(e))

                        found_count[search_elem] += 1

    except FileNotFoundError:
        print("Error: Log file not found.")

    except PermissionError:
        print("Error: Permission denied. Make sure you have appropriate permissions.")

    except Exception as e:
        print("An error occurred: {}".format(e))

    return found_logSeq_list