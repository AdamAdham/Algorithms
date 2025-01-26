def format_header(header_number,base_url,directory_array,file_name,extension="py"):
    file_path = ""
    for dir in directory_array:
        file_path+=dir.replace(" ","%20") + "/"
    file_name_conv = file_name.replace(" ","%20") + "." + extension
    path = base_url+file_path + file_name_conv
    header = "#"*header_number
    final = f'{header} [{file_name}]({path})'
    return final

header_number = 3
base_url = "https://github.com/AdamAdham/Algorithms/blob/main/"
dp_easy = ["Dynamic Programming","Easy"]
dp_med = ["Dynamic Programming","Medium"]
dp_hard = ["Dynamic Programming","Hard"]

greedy_easy = ["Greedy","Easy"]
greedy_med = ["Greedy","Medium"]
greedy_hard = ["Greedy","Hard"]

intv_easy = ["Top Interview Questions","Easy"]
intv_med = ["Top Interview Questions","Medium"]
intv_hard = ["Top Interview Questions","Hard"]

print(format_header(header_number,base_url,intv_med,"55. Jump Game"))