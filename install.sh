
sudo cp gameOfLife.py /usr/bin/gameOfLife

# create the .desktop file
echo "[Desktop Entry]
Type=Application
Encoding=UTF-8
Name=Game of Life
Comment=Made by Jkutkut
Exec=gameOfLife
Icon=/home/jkutkut/github/PY-GameOfLife/gameOfLife.png
Terminal=false" >> gameOfLife.desktop

sudo rm /usr/share/applications/gameOfLife.desktop
sudo mv gameOfLife.desktop /usr/share/applications/