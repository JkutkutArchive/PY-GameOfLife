# Game of Life:

If you have an executable python prog, for example one made from pyinstaller or the likes, you can skip the previous steps and just mv the executable instead in the next steps.

At this point you could simply save this file wherever you want and execute it directly in the terminal with # /path/to/file. BUT, that's not how apps are typically installed... The proper way IMO is as follows:

move the file to the /usr/bin/ directory. This is where much of the executable code goes for other apps installed with apt or other methods. Use this command to do so: $ mv app.py /usr/bin/app. After that you can execute the app at any time from any directory in the terminal by simply running: # app. Notice I dropped the ".py" from the file when moving it... this is optional, whatever you name the file when moving it becomes the command to run it...

Many people might stop here... But I prefer this last step for my apps. Create a desktop file touch app.desktop. A simple desktop file contains the following:

[Desktop Entry]
Type=Application
Encoding=UTF-8
Name=App
Comment=My custom app
Exec=app
Icon=/path/to/some/optional/icon.png
Terminal=false

Exec should be set to whatever you named the file in the previous step when moving to the usr/bin/ driectory. the Icon field is optional. If you need to see the terminal to use the app set Terminal to true.

Save this file to the /usr/share/applications/ directory with $ mv app.desktop /usr/share/applications/

At this point, you should be able to hit the super(windows) key and start typing the name (the one you listed in the .desktop file) and see your application pop-up as an option... hitting enter or clicking it with your mouse should launch it. You can right click on the option and add to favorites if you'd like.