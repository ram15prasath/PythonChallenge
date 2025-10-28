def filter_by_range(data_list, min_val, max_val):
    result = []
    for number in data_list:
        if min_val < number < max_val:
            result.append(number)
    return result

# --- Alternative (Using List Comprehension) ---

def filter_by_range_comprehension(data_list, min_val, max_val):
    return [number for number in data_list if min_val < number < max_val]