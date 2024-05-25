def generate_test_input(file_path):
    commands = [
        "1 1715744138011;INTERNAL_SERVER_ERROR;23.72",
        "1 1715744138012;INTERNAL_SERVER_ERROR;10.17",
        "2 INTERNAL_SERVER_ERROR",
        "1 1715744138012;BAD_REQUEST;15.22",
        "1 1715744138013;INTERNAL_SERVER_ERROR;23.72",
        "3 BEFORE 1715744138011",
        "3 AFTER 1715744138010",
        "2 BAD_REQUEST",
        "4 BEFORE INTERNAL_SERVER_ERROR 1715744138011",
        "4 AFTER INTERNAL_SERVER_ERROR 1715744138010"
    ]
    
    with open(file_path, 'w') as file:
        for command in commands:
            file.write(command + '\n')

if __name__ == '__main__':
    generate_test_input('input.txt')
