import os

def custom_head(file_to_read, n_lines, file_to_write=None):
    if not os.path.exists(file_to_read):
        print(f"Error: The file '{file_to_read}' does not exist.")
        return
    input_file = open(file_to_read, 'r')
    output_content = ""
    for i in range(n_lines):
        line = input_file.readline()
        if not line:
            break
        output_content += line
    input_file.close()
    if file_to_write is None:
        print(output_content, end="")
    else:
        output_file = open(file_to_write, 'w')
        output_file.write(output_content)
        output_file.close()

# custom_head('my_file.txt', 10)

