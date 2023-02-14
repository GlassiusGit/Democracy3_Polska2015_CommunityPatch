def switch_coding(filepath, direction):
    if direction not in ["ANSI2D3", "D32ANSI"]:
        return

    # ANSI, D3
    mapping = [
        [0xBF, 0xEE],
        [0xF3, 0xFF],
        [0xB3, 0xF9],
        [0xE6, 0xF6],
        [0xEA, 0xFC],
        [0x9C, 0xEA],
        [0xB9, 0xE4],
        [0x9F, 0xEB],
        [0xF1, 0xFB],
        [0xAF, 0xCE],
        [0xD3, 0x9F],
        [0xA3, 0xD9],
        [0xC6, 0xD6],
        [0xCA, 0xDC],
        [0x8C, 0xCA],
        [0xA5, 0xC4],
        [0x8F, 0xCB],
        [0xD1, 0xDB]
    ]
    
    with open(filepath, "rb") as myFile:
        text = myFile.read()
    text = list(text)

    for i, myByte in enumerate(text):
        for pair in mapping:
            if direction ==  "ANSI2D3":
                if myByte == pair[0]:
                    text[i] = pair[1]
            elif direction ==  "D32ANSI":
                if myByte == pair[1]:
                    text[i] = pair[0]

    text = bytes(text)
    with open(filepath, "wb") as myFile:
        myFile.write(text)
