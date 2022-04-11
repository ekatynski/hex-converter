# INPUT: command line input formatted as a string
# OUTPUT: list of all message characters converted to unicode, then hex
def convert_to_hex(message):
    hex_msg = []
    #convert string message to list of converted values
    for letter in message:
        # each appended value is hex conversion of unicode conversion
        hex_msg.append(hex(ord(letter)))
    return hex_msg

# INPUT: list of hex characters, array name iterator (default: 0)
# OUTPUT: formatted C-style hex array
def to_c_array(hex_msg, id = 0):
    # add array declaration
    message = "uint8_t out" + str(id) + "[" +str(len(hex_msg)) + "] = {"
    # add array values
    message += ", ".join([str(i) for i in hex_msg])
    # close array declaration
    message += "};"
    return message