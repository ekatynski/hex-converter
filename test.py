import to_hex

if __name__ == "__main__":
    i = 0
    while True:
        sample = input("Enter sample text: ")
        answer = to_hex.to_c_array(to_hex.convert_to_hex(sample), i)
        print(answer + "\n")
        i += 1