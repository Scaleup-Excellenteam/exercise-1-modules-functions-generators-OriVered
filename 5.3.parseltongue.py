def read_secret_messages(file_path):
    """
    Extracts secret messages from the given file. Secret messages are strings with a length of at least 5
    characters, consisting of lowercase English letters, and ending with an exclamation mark.

    :param file_path: Path to the file containing the secret messages.
    :type file_path: str
    :return: A list of extracted secret messages.
    :rtype: list[str]
    """
    secret_messages = []
    current_message = ''

    with open(file_path, 'rb') as file:
        while True:
            chunk = file.read(1024)
            if not chunk:
                break

            for char in chunk:
                if b'a'[0] <= char <= b'z'[0]:
                    current_message += chr(char)

                elif char == b'!'[0]:
                    if len(current_message) >= 5:
                        secret_messages.append(current_message)
                    current_message = ''
                else:
                    current_message = ''

    return secret_messages


if __name__ == "__main__":
    """
    The main function demonstrates the usage of the read_secret_messages function by extracting secret messages
    from the 'resources/logo.jpg' file and printing the results.
    """
    logo_path = "C:\\Users\\97258\\Notebooks-master\\week05\\resources\\logo.jpg"
    secret_messages = read_secret_messages(logo_path) #outpot - ['python', 'isawesome', 'welldone', 'goodjob']
    print(secret_messages)

