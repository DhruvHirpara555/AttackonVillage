import pickle as pkl

# ask file name to be replayed

replay_filename = input("Enter File name")

replay_file = open(replay_filename,'rb')

screens = pkl.load(replay_file)

replay_file.close()

framerate= 60

for i in range(len(screens)
