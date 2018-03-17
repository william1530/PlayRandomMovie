import os, random,subprocess, sys, platform

#get the file name
file_name = __file__

#get path from file_name
dir_path = os.path.dirname(os.path.realpath(file_name))

#change current working directory to where the file lies
os.chdir(dir_path)

#get current working directory
cwd = os.getcwd()

#set message text for the user
msg_text = 'A movie has been chosen for you: \n'

platform_name=sys.platform
  
#get python version
version = int(sys.version[0:1])

while True: 
  #select movie to play
  movie_choice = random.choice(os.listdir(cwd+'/movies'))
  play_this = os.path.join(dir_path,'movies',movie_choice)
  
  #print result
  print(msg_text +'  '+ movie_choice )
  
 
  #Debug
  #print(dir_path)
  #print (os.path.exists(dir_path + '/movies/' + movie_choice))
  #print(version)
  #print(sys.platform)
  #print(platform.system)
  #print(platform.release)
  #print(platform.version)
  #print(os.name)
  #print(os.path.join(dir_path,'movies',movie_choice))
  
  play_yn = 'n'
  
  if version >= 3:
    play_yn = input('Do you want to play that movie now? (j/n)')
  else:
    play_yn = raw_input('Do you want to play that movie now? (j/n)')
  
  
  if play_yn.lower() == "j":
    #open movie in vlc
    if "win" in platform_name:
      P = subprocess.Popen(["C:\\Program Files (x86)\\VideoLan\\VLC\\vlc.exe",play_this])
    else:
      P = subprocess.Popen(['vlc','-vvv',play_this])

    break
  
  else: 
    print('Ok. Getting new Choice.')
  