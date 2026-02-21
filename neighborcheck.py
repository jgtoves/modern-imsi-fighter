def check_neighbors():
    # Real towers always have neighbors (Cell Towers 'talk' to each other)
    # If Neighboring cells = 0, you are on a 'Stingray Island'
    res = subprocess.check_output(['termux-telephony-cellinfo'])
    cells = json.loads(res)
    
    if len(cells) == 1:
        print("[!] WARNING: No neighboring cells detected. You are on an Isolated Tower.")
