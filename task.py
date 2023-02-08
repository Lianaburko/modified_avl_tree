import re
import avl_tree

def start():
    txt_data = input()
    pattern = '(([mnk]\s[-]?\d+)\s)*[mnk]\s[-]?\d+'

    match = re.fullmatch(pattern, txt_data) 
    if match:
        res = avl_tree.main(txt_data)
    else: 
        res = 'You have mistake in input. Check syntaxis'
    print(res)


start()
