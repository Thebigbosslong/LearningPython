def reverse_string(string_to_reverse):
    string_reversed = ""
    current_index = len(string_to_reverse) - 1
    while current_index >= 0:
        string_reversed += string_to_reverse[current_index]
        current_index -= 1
    return string_reversed


string_dada_la_vuelta = reverse_string("Mañana no hay clase")
print(string_dada_la_vuelta)