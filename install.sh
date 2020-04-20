

sudo cp gameOfLife.png /usr/share/icons/

sudo cp gameOfLife.py /usr/bin/gameOfLife
sudo chmod 755 /usr/bin/gameOfLife

# create the .desktop file
echo "[Desktop Entry]
Type=Application
Encoding=UTF-8
Name=Game of Life
Comment=Made by Jkutkut
Exec=gameOfLife
Icon=/usr/share/icons/gameOfLife.png
Terminal=false" >> gameOfLife.desktop

sudo mv gameOfLife.desktop /usr/share/applications/
echo "GameOfLife installed"
