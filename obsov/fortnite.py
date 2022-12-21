# import os

# def get_kills():
#     with open(os.path.join(os.getenv('localappdata'), 'FortniteGame\\Saved\\Logs\\FortniteGame.log'), 'r', encoding='utf8') as f:
#         for line in reversed(f.readlines()):
#             if '(KillScore = ' in line:
#                 return line.split('KillScore = ')[1].split(')')[0]

# if __name__ == '__main__':
#     print(get_kills())
