from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MusicApp(object):
    def setupUi(self, MusicApp):
        MusicApp.setObjectName("MusicApp")
        MusicApp.resize(880, 550)
        MusicApp.setMinimumSize(QtCore.QSize(880, 550))
        MusicApp.setMaximumSize(QtCore.QSize(880, 550))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/img/utils/images/app_icon.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        MusicApp.setWindowIcon(icon)
        MusicApp.setStyleSheet("")
        self.centralwidget = QtWidgets.QWidget(MusicApp)
        self.centralwidget.setStyleSheet("")
        self.centralwidget.setObjectName("centralwidget")
        self.background_image = QtWidgets.QLabel(self.centralwidget)
        self.background_image.setGeometry(QtCore.QRect(0, 0, 880, 550))
        self.background_image.setMinimumSize(QtCore.QSize(880, 550))
        self.background_image.setMaximumSize(QtCore.QSize(880, 550))
        self.background_image.setStyleSheet("")
        self.background_image.setText("")
        self.background_image.setPixmap(QtGui.QPixmap("utils/bg_imgs/bg_0002_11.jpg"))
        self.background_image.setScaledContents(True)
        self.background_image.setObjectName("background_image")
        self.bd_overlay = QtWidgets.QLabel(self.centralwidget)
        self.bd_overlay.setGeometry(QtCore.QRect(0, 0, 880, 550))
        self.bd_overlay.setMinimumSize(QtCore.QSize(880, 550))
        self.bd_overlay.setMaximumSize(QtCore.QSize(880, 550))
        self.bd_overlay.setStyleSheet("")
        self.bd_overlay.setText("")
        self.bd_overlay.setPixmap(QtGui.QPixmap("utils/bg_imgs/bg_overlay.png"))
        self.bd_overlay.setScaledContents(True)
        self.bd_overlay.setObjectName("bd_overlay")
        self.title_frame = QtWidgets.QFrame(self.centralwidget)
        self.title_frame.setGeometry(QtCore.QRect(-1, 0, 881, 51))
        self.title_frame.setStyleSheet("border-radius:10px;")
        self.title_frame.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.title_frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.title_frame.setObjectName("title_frame")
        self.close_btn = QtWidgets.QPushButton(self.title_frame)
        self.close_btn.setGeometry(QtCore.QRect(830, 10, 41, 31))
        self.close_btn.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.close_btn.setStyleSheet("QPushButton{\n"
"    background-color: rgba(255, 255, 255, 0);\n"
"    background-repeat:no-repeat;\n"
"    border:none;\n"
"    background-position:center center;\n"
"\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"    background-color: rgba(255, 20, 12, 200);\n"
"}\n"
"\n"
"QPushButton:pressed{\n"
"    background-color: rgba(255, 20, 12, 200);\n"
"    border-color:rgba(255,255,255,30);\n"
"    border-style:inset;\n"
"    color:rgba(0,0,0,100);\n"
"}")
        self.close_btn.setText("")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(":/img/utils/images/quit.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.close_btn.setIcon(icon1)
        self.close_btn.setFlat(True)
        self.close_btn.setObjectName("close_btn")
        self.minimize_btn = QtWidgets.QPushButton(self.title_frame)
        self.minimize_btn.setGeometry(QtCore.QRect(780, 10, 41, 31))
        self.minimize_btn.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.minimize_btn.setStyleSheet("QPushButton{\n"
"    background-color: rgba(255, 255, 255, 0);\n"
"    background-repeat:no-repeat;\n"
"    border:none;\n"
"    background-position:center center;\n"
"\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"    background-color: rgba(255,255,255,130);\n"
"}\n"
"\n"
"QPushButton:pressed{\n"
"    background-color: (255,255,255,130);\n"
"    border-style:inset;\n"
"    color:rgba(0,0,0,100);\n"
"}")
        self.minimize_btn.setText("")
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(":/img/utils/images/min.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.minimize_btn.setIcon(icon2)
        self.minimize_btn.setFlat(True)
        self.minimize_btn.setObjectName("minimize_btn")
        self.label = QtWidgets.QLabel(self.title_frame)
        self.label.setGeometry(QtCore.QRect(50, 10, 111, 31))
        font = QtGui.QFont()
        font.setPointSize(15)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setStyleSheet("color: rgb(79, 208, 178);")
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.title_frame)
        self.label_2.setGeometry(QtCore.QRect(10, 10, 32, 32))
        self.label_2.setText("")
        self.label_2.setPixmap(QtGui.QPixmap(":/img/utils/images/app_icon.png"))
        self.label_2.setScaledContents(True)
        self.label_2.setObjectName("label_2")
        self.frame_2 = QtWidgets.QFrame(self.centralwidget)
        self.frame_2.setGeometry(QtCore.QRect(10, 60, 301, 221))
        self.frame_2.setStyleSheet("background-color: rgba(0, 0, 0, 150);\n"
"border-radius: 15px;")
        self.frame_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_2.setObjectName("frame_2")
        self.label_3 = QtWidgets.QLabel(self.frame_2)
        self.label_3.setGeometry(QtCore.QRect(50, 10, 141, 21))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setUnderline(True)
        font.setWeight(75)
        self.label_3.setFont(font)
        self.label_3.setStyleSheet("background-color: rgba(0, 0, 0,0);\n"
"color: rgb(79, 208, 178);")
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(self.frame_2)
        self.label_4.setGeometry(QtCore.QRect(10, 10, 31, 21))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_4.setFont(font)
        self.label_4.setStyleSheet("background-color: rgba(0, 0, 0,0);\n"
"color: rgb(79, 208, 178);")
        self.label_4.setText("")
        self.label_4.setPixmap(QtGui.QPixmap(":/img/utils/images/current-music.png"))
        self.label_4.setScaledContents(True)
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(self.frame_2)
        self.label_5.setGeometry(QtCore.QRect(10, 40, 141, 21))
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.label_5.setFont(font)
        self.label_5.setStyleSheet("background-color: rgba(0, 0, 0,0);\n"
"color: rgb(79, 208, 178);")
        self.label_5.setObjectName("label_5")
        self.current_song_name = QtWidgets.QLabel(self.frame_2)
        self.current_song_name.setGeometry(QtCore.QRect(10, 60, 281, 21))
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(False)
        font.setWeight(50)
        self.current_song_name.setFont(font)
        self.current_song_name.setStyleSheet("background-color: rgba(0, 0, 0,0);\n"
"color: rgb(255, 255, 255);")
        self.current_song_name.setObjectName("current_song_name")
        self.label_7 = QtWidgets.QLabel(self.frame_2)
        self.label_7.setGeometry(QtCore.QRect(10, 80, 141, 21))
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.label_7.setFont(font)
        self.label_7.setStyleSheet("background-color: rgba(0, 0, 0,0);\n"
"color: rgb(79, 208, 178);")
        self.label_7.setObjectName("label_7")
        self.current_song_path = QtWidgets.QLabel(self.frame_2)
        self.current_song_path.setGeometry(QtCore.QRect(10, 100, 281, 21))
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(False)
        font.setWeight(50)
        self.current_song_path.setFont(font)
        self.current_song_path.setStyleSheet("background-color: rgba(0, 0, 0,0);\n"
"color: rgb(255, 255, 255);")
        self.current_song_path.setObjectName("current_song_path")
        self.add_to_fav_btn = QtWidgets.QPushButton(self.frame_2)
        self.add_to_fav_btn.setGeometry(QtCore.QRect(10, 140, 221, 31))
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.add_to_fav_btn.setFont(font)
        self.add_to_fav_btn.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.add_to_fav_btn.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"color: rgb(255, 140, 64);")
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap(":/img/utils/images/like.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.add_to_fav_btn.setIcon(icon3)
        self.add_to_fav_btn.setIconSize(QtCore.QSize(24, 24))
        self.add_to_fav_btn.setObjectName("add_to_fav_btn")
        self.add_to_playlist_btn = QtWidgets.QPushButton(self.frame_2)
        self.add_to_playlist_btn.setGeometry(QtCore.QRect(10, 180, 221, 31))
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.add_to_playlist_btn.setFont(font)
        self.add_to_playlist_btn.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.add_to_playlist_btn.setStyleSheet("background-color: rgb(255, 140, 64);\n"
"color: rgb(255, 255, 255);")
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap(":/img/utils/images/music_list.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.add_to_playlist_btn.setIcon(icon4)
        self.add_to_playlist_btn.setIconSize(QtCore.QSize(24, 24))
        self.add_to_playlist_btn.setObjectName("add_to_playlist_btn")
        self.volume_dial = QtWidgets.QDial(self.centralwidget)
        self.volume_dial.setGeometry(QtCore.QRect(40, 290, 201, 191))
        self.volume_dial.setCursor(QtGui.QCursor(QtCore.Qt.ClosedHandCursor))
        self.volume_dial.setMaximum(100)
        self.volume_dial.setProperty("value", 50)
        self.volume_dial.setTracking(False)
        self.volume_dial.setWrapping(False)
        self.volume_dial.setNotchesVisible(True)
        self.volume_dial.setObjectName("volume_dial")
        self.frame_3 = QtWidgets.QFrame(self.centralwidget)
        self.frame_3.setGeometry(QtCore.QRect(10, 480, 861, 66))
        self.frame_3.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.frame_3.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_3.setObjectName("frame_3")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.frame_3)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.frame_4 = QtWidgets.QFrame(self.frame_3)
        self.frame_4.setStyleSheet("background-color: rgba(255, 255, 255, 50);\n"
"border-radius:10px;")
        self.frame_4.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.frame_4.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_4.setObjectName("frame_4")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.frame_4)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.play_btn = QtWidgets.QPushButton(self.frame_4)
        self.play_btn.setMinimumSize(QtCore.QSize(30, 30))
        self.play_btn.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.play_btn.setStyleSheet("QPushButton{\n"
"    background-color: rgba(255, 255, 255, 0);\n"
"    background-repeat:no-repeat;\n"
"    border:none;\n"
"    background-position:center center;\n"
"\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"    background-color: rgba(255,255,255,100);\n"
"}\n"
"")
        self.play_btn.setText("")
        icon5 = QtGui.QIcon()
        icon5.addPixmap(QtGui.QPixmap(":/img/utils/images/pase.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.play_btn.setIcon(icon5)
        self.play_btn.setFlat(True)
        self.play_btn.setObjectName("play_btn")
        self.horizontalLayout.addWidget(self.play_btn)
        self.pause_btn = QtWidgets.QPushButton(self.frame_4)
        self.pause_btn.setMinimumSize(QtCore.QSize(30, 30))
        self.pause_btn.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pause_btn.setStyleSheet("QPushButton{\n"
"    background-color: rgba(255, 255, 255, 0);\n"
"    background-repeat:no-repeat;\n"
"    border:none;\n"
"    background-position:center center;\n"
"\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"    background-color: rgba(255,255,255,100);\n"
"}\n"
"")
        self.pause_btn.setText("")
        icon6 = QtGui.QIcon()
        icon6.addPixmap(QtGui.QPixmap(":/img/utils/images/play.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pause_btn.setIcon(icon6)
        self.pause_btn.setFlat(True)
        self.pause_btn.setObjectName("pause_btn")
        self.horizontalLayout.addWidget(self.pause_btn)
        self.stop_btn = QtWidgets.QPushButton(self.frame_4)
        self.stop_btn.setMinimumSize(QtCore.QSize(30, 30))
        self.stop_btn.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.stop_btn.setStyleSheet("QPushButton{\n"
"    background-color: rgba(255, 255, 255, 0);\n"
"    background-repeat:no-repeat;\n"
"    border:none;\n"
"    background-position:center center;\n"
"\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"    background-color: rgba(255,255,255,100);\n"
"}\n"
"")
        self.stop_btn.setText("")
        icon7 = QtGui.QIcon()
        icon7.addPixmap(QtGui.QPixmap(":/img/utils/images/sliderHandle.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.stop_btn.setIcon(icon7)
        self.stop_btn.setFlat(True)
        self.stop_btn.setObjectName("stop_btn")
        self.horizontalLayout.addWidget(self.stop_btn)
        self.previous_btn = QtWidgets.QPushButton(self.frame_4)
        self.previous_btn.setMinimumSize(QtCore.QSize(30, 30))
        self.previous_btn.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.previous_btn.setStyleSheet("QPushButton{\n"
"    background-color: rgba(255, 255, 255, 0);\n"
"    background-repeat:no-repeat;\n"
"    border:none;\n"
"    background-position:center center;\n"
"\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"    background-color: rgba(255,255,255,100);\n"
"}\n"
"")
        self.previous_btn.setText("")
        icon8 = QtGui.QIcon()
        icon8.addPixmap(QtGui.QPixmap(":/img/utils/images/pre.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.previous_btn.setIcon(icon8)
        self.previous_btn.setFlat(True)
        self.previous_btn.setObjectName("previous_btn")
        self.horizontalLayout.addWidget(self.previous_btn)
        self.next_btn = QtWidgets.QPushButton(self.frame_4)
        self.next_btn.setMinimumSize(QtCore.QSize(32, 30))
        self.next_btn.setMaximumSize(QtCore.QSize(25, 16777215))
        self.next_btn.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.next_btn.setStyleSheet("QPushButton{\n"
"    background-color: rgba(255, 255, 255, 0);\n"
"    background-repeat:no-repeat;\n"
"    border:none;\n"
"    background-position:center center;\n"
"\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"    background-color: rgba(255,255,255,100);\n"
"}\n"
"")
        self.next_btn.setText("")
        icon9 = QtGui.QIcon()
        icon9.addPixmap(QtGui.QPixmap(":/img/utils/images/next.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.next_btn.setIcon(icon9)
        self.next_btn.setIconSize(QtCore.QSize(32, 16))
        self.next_btn.setFlat(True)
        self.next_btn.setObjectName("next_btn")
        self.horizontalLayout.addWidget(self.next_btn)
        self.loop_one_btn = QtWidgets.QPushButton(self.frame_4)
        self.loop_one_btn.setMinimumSize(QtCore.QSize(32, 30))
        self.loop_one_btn.setMaximumSize(QtCore.QSize(25, 16777215))
        self.loop_one_btn.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.loop_one_btn.setStyleSheet("QPushButton{\n"
"    background-color: rgba(255, 255, 255, 0);\n"
"    background-repeat:no-repeat;\n"
"    border:none;\n"
"    background-position:center center;\n"
"\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"    background-color: rgba(255,255,255,100);\n"
"}\n"
"\n"
"QPushButton:checked{\n"
"    background-color: rgba(255,255,255,100);\n"
"}\n"
"")
        self.loop_one_btn.setText("")
        icon10 = QtGui.QIcon()
        icon10.addPixmap(QtGui.QPixmap(":/img/utils/images/loop-one.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.loop_one_btn.setIcon(icon10)
        self.loop_one_btn.setIconSize(QtCore.QSize(32, 16))
        self.loop_one_btn.setCheckable(True)
        self.loop_one_btn.setFlat(True)
        self.loop_one_btn.setObjectName("loop_one_btn")
        self.horizontalLayout.addWidget(self.loop_one_btn)
        self.shuffle_songs_btn = QtWidgets.QPushButton(self.frame_4)
        self.shuffle_songs_btn.setMinimumSize(QtCore.QSize(32, 30))
        self.shuffle_songs_btn.setMaximumSize(QtCore.QSize(25, 16777215))
        self.shuffle_songs_btn.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.shuffle_songs_btn.setStyleSheet("QPushButton{\n"
"    background-color: rgba(255, 255, 255, 0);\n"
"    background-repeat:no-repeat;\n"
"    border:none;\n"
"    background-position:center center;\n"
"\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"    background-color: rgba(255,255,255,100);\n"
"}\n"
"\n"
"\n"
"QPushButton:checked{\n"
"    background-color: rgba(255,255,255,100);\n"
"}\n"
"")
        self.shuffle_songs_btn.setText("")
        icon11 = QtGui.QIcon()
        icon11.addPixmap(QtGui.QPixmap(":/img/utils/images/play-random.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.shuffle_songs_btn.setIcon(icon11)
        self.shuffle_songs_btn.setIconSize(QtCore.QSize(32, 16))
        self.shuffle_songs_btn.setCheckable(True)
        self.shuffle_songs_btn.setFlat(True)
        self.shuffle_songs_btn.setObjectName("shuffle_songs_btn")
        self.horizontalLayout.addWidget(self.shuffle_songs_btn)
        self.horizontalLayout_2.addWidget(self.frame_4)
        self.music_slider = QtWidgets.QSlider(self.frame_3)
        self.music_slider.setMinimumSize(QtCore.QSize(0, 50))
        self.music_slider.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.music_slider.setStyleSheet("QSlider::groove:horizontal {\n"
"    border: 1px solid #999999;\n"
"    height: 15px; \n"
"   padding:3px;\n"
"    background: rgba(0, 255, 127, 100);\n"
"    margin: 2px 0;\n"
"    border-radius:11px;\n"
"}\n"
"\n"
"QSlider::handle:horizontal {\n"
"    background:  rgb(255, 200, 50);\n"
"    border: 1px solid #5c5c5c;\n"
"    width: 18px;\n"
"    margin: -2px 0;\n"
"    border-radius: 9px;\n"
"}")
        self.music_slider.setOrientation(QtCore.Qt.Horizontal)
        self.music_slider.setObjectName("music_slider")
        self.horizontalLayout_2.addWidget(self.music_slider)
        self.time_label = QtWidgets.QLabel(self.frame_3)
        self.time_label.setMaximumSize(QtCore.QSize(16777215, 35))
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.time_label.setFont(font)
        self.time_label.setStyleSheet("color: rgb(255, 255, 255);\n"
"padding:2px;\n"
"border-radius:5px")
        self.time_label.setObjectName("time_label")
        self.horizontalLayout_2.addWidget(self.time_label)
        self.stackedWidget = QtWidgets.QStackedWidget(self.centralwidget)
        self.stackedWidget.setGeometry(QtCore.QRect(320, 60, 551, 361))
        self.stackedWidget.setStyleSheet("background-color: rgba(0, 0, 0, 50);\n"
"border-radius:15px;")
        self.stackedWidget.setObjectName("stackedWidget")
        self.song_list_page = QtWidgets.QWidget()
        self.song_list_page.setObjectName("song_list_page")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.song_list_page)
        self.verticalLayout.setObjectName("verticalLayout")
        self.frame_5 = QtWidgets.QFrame(self.song_list_page)
        self.frame_5.setStyleSheet("background-color: rgba(255, 255, 255, 0);")
        self.frame_5.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_5.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_5.setObjectName("frame_5")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout(self.frame_5)
        self.horizontalLayout_4.setContentsMargins(-1, 0, -1, 0)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.label_6 = QtWidgets.QLabel(self.frame_5)
        font = QtGui.QFont()
        font.setPointSize(15)
        font.setBold(True)
        font.setWeight(75)
        self.label_6.setFont(font)
        self.label_6.setStyleSheet("color: rgb(255, 255, 255);")
        self.label_6.setObjectName("label_6")
        self.horizontalLayout_4.addWidget(self.label_6)
        self.frame_6 = QtWidgets.QFrame(self.frame_5)
        self.frame_6.setMaximumSize(QtCore.QSize(130, 16777215))
        self.frame_6.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_6.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_6.setObjectName("frame_6")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.frame_6)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.add_songs_btn = QtWidgets.QPushButton(self.frame_6)
        self.add_songs_btn.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.add_songs_btn.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"border-radius:5px;")
        self.add_songs_btn.setText("")
        icon12 = QtGui.QIcon()
        icon12.addPixmap(QtGui.QPixmap(":/img/utils/images/addFromLocal.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.add_songs_btn.setIcon(icon12)
        self.add_songs_btn.setIconSize(QtCore.QSize(32, 32))
        self.add_songs_btn.setObjectName("add_songs_btn")
        self.horizontalLayout_3.addWidget(self.add_songs_btn)
        self.delete_selected_btn = QtWidgets.QPushButton(self.frame_6)
        self.delete_selected_btn.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.delete_selected_btn.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"border-radius:5px;")
        self.delete_selected_btn.setText("")
        icon13 = QtGui.QIcon()
        icon13.addPixmap(QtGui.QPixmap(":/img/utils/images/clear.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.delete_selected_btn.setIcon(icon13)
        self.delete_selected_btn.setIconSize(QtCore.QSize(32, 32))
        self.delete_selected_btn.setObjectName("delete_selected_btn")
        self.horizontalLayout_3.addWidget(self.delete_selected_btn)
        self.delete_all_songs_btn = QtWidgets.QPushButton(self.frame_6)
        self.delete_all_songs_btn.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.delete_all_songs_btn.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"border-radius:5px;")
        self.delete_all_songs_btn.setText("")
        icon14 = QtGui.QIcon()
        icon14.addPixmap(QtGui.QPixmap(":/img/utils/images/remove.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.delete_all_songs_btn.setIcon(icon14)
        self.delete_all_songs_btn.setIconSize(QtCore.QSize(32, 32))
        self.delete_all_songs_btn.setObjectName("delete_all_songs_btn")
        self.horizontalLayout_3.addWidget(self.delete_all_songs_btn)
        self.horizontalLayout_4.addWidget(self.frame_6)
        self.verticalLayout.addWidget(self.frame_5)
        self.loaded_songs_listWidget = QtWidgets.QListWidget(self.song_list_page)
        font = QtGui.QFont()
        font.setPointSize(13)
        font.setBold(True)
        font.setWeight(75)
        self.loaded_songs_listWidget.setFont(font)
        self.loaded_songs_listWidget.viewport().setProperty("cursor", QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.loaded_songs_listWidget.setStyleSheet("color: rgb(86, 227, 194);\n"
"background-color: rgba(0, 0, 0, 100);\n"
"\n"
"selection-background-color: rgb(255, 140, 64);\n"
"selection-color: rgb(255, 255, 255);\n"
"padding:10px;\n"
"")
        self.loaded_songs_listWidget.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.loaded_songs_listWidget.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.loaded_songs_listWidget.setObjectName("loaded_songs_listWidget")
        self.verticalLayout.addWidget(self.loaded_songs_listWidget)
        self.stackedWidget.addWidget(self.song_list_page)
        self.playlists_page = QtWidgets.QWidget()
        self.playlists_page.setObjectName("playlists_page")
        self.label_9 = QtWidgets.QLabel(self.playlists_page)
        self.label_9.setGeometry(QtCore.QRect(30, 10, 131, 50))
        font = QtGui.QFont()
        font.setPointSize(15)
        font.setBold(True)
        font.setWeight(75)
        self.label_9.setFont(font)
        self.label_9.setStyleSheet("color: rgb(255, 255, 255);\n"
"background-color: rgab(255, 255, 255, 0);")
        self.label_9.setObjectName("label_9")
        self.load_selected_playlist_btn = QtWidgets.QPushButton(self.playlists_page)
        self.load_selected_playlist_btn.setGeometry(QtCore.QRect(390, 20, 141, 31))
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.load_selected_playlist_btn.setFont(font)
        self.load_selected_playlist_btn.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.load_selected_playlist_btn.setStyleSheet("background-color: rgb(0, 255, 127);\n"
"border-radius:15px;")
        self.load_selected_playlist_btn.setObjectName("load_selected_playlist_btn")
        self.playlists_listWidget = QtWidgets.QListWidget(self.playlists_page)
        self.playlists_listWidget.setGeometry(QtCore.QRect(10, 60, 531, 261))
        font = QtGui.QFont()
        font.setPointSize(13)
        font.setBold(True)
        font.setWeight(75)
        self.playlists_listWidget.setFont(font)
        self.playlists_listWidget.viewport().setProperty("cursor", QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.playlists_listWidget.setStyleSheet("color: rgb(86, 227, 194);\n"
"background-color: rgba(0, 0, 0, 100);\n"
"\n"
"selection-background-color: rgb(255, 140, 64);\n"
"selection-color: rgb(255, 255, 255);\n"
"padding:10px;\n"
"")
        self.playlists_listWidget.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.playlists_listWidget.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.playlists_listWidget.setObjectName("playlists_listWidget")
        self.new_playlist_btn = QtWidgets.QPushButton(self.playlists_page)
        self.new_playlist_btn.setGeometry(QtCore.QRect(47, 324, 121, 31))
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.new_playlist_btn.setFont(font)
        self.new_playlist_btn.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.new_playlist_btn.setStyleSheet("QPushButton{\n"
"    background-color: rgb(255, 255, 255);\n"
"    border-radius:15px;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"    color: rgb(0, 85, 0);\n"
"    background-color: rgb(0, 255, 127);\n"
"}")
        self.new_playlist_btn.setObjectName("new_playlist_btn")
        self.remove_selected_playlist_btn = QtWidgets.QPushButton(self.playlists_page)
        self.remove_selected_playlist_btn.setGeometry(QtCore.QRect(180, 324, 151, 31))
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.remove_selected_playlist_btn.setFont(font)
        self.remove_selected_playlist_btn.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.remove_selected_playlist_btn.setStyleSheet("QPushButton{\n"
"    background-color: rgb(255, 255, 255);\n"
"    border-radius:15px;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"    color: rgb(202, 0, 0);\n"
"    background-color: rgb(255, 176, 176);\n"
"}")
        self.remove_selected_playlist_btn.setObjectName("remove_selected_playlist_btn")
        self.remove_all_playlists_btn = QtWidgets.QPushButton(self.playlists_page)
        self.remove_all_playlists_btn.setGeometry(QtCore.QRect(342, 324, 131, 31))
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.remove_all_playlists_btn.setFont(font)
        self.remove_all_playlists_btn.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.remove_all_playlists_btn.setStyleSheet("QPushButton{\n"
"    background-color: rgb(255, 255, 255);\n"
"    border-radius:15px;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"    color: rgb(255, 255, 255);\n"
"    background-color: rgb(255, 44, 44);\n"
"}\n"
"")
        self.remove_all_playlists_btn.setObjectName("remove_all_playlists_btn")
        self.stackedWidget.addWidget(self.playlists_page)
        self.favourites_page = QtWidgets.QWidget()
        self.favourites_page.setObjectName("favourites_page")
        self.label_10 = QtWidgets.QLabel(self.favourites_page)
        self.label_10.setGeometry(QtCore.QRect(30, 10, 131, 50))
        font = QtGui.QFont()
        font.setPointSize(15)
        font.setBold(True)
        font.setWeight(75)
        self.label_10.setFont(font)
        self.label_10.setStyleSheet("color: rgb(255, 255, 255);\n"
"background-color: rgab(255, 255, 255, 0);")
        self.label_10.setObjectName("label_10")
        self.favourites_listWidget = QtWidgets.QListWidget(self.favourites_page)
        self.favourites_listWidget.setGeometry(QtCore.QRect(10, 60, 531, 291))
        font = QtGui.QFont()
        font.setPointSize(13)
        font.setBold(True)
        font.setWeight(75)
        self.favourites_listWidget.setFont(font)
        self.favourites_listWidget.viewport().setProperty("cursor", QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.favourites_listWidget.setStyleSheet("color: rgb(86, 227, 194);\n"
"background-color: rgba(0, 0, 0, 100);\n"
"\n"
"selection-background-color: rgb(255, 140, 64);\n"
"selection-color: rgb(255, 255, 255);\n"
"padding:10px;\n"
"")
        self.favourites_listWidget.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.favourites_listWidget.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.favourites_listWidget.setObjectName("favourites_listWidget")
        self.delete_selected_favourite_btn = QtWidgets.QPushButton(self.favourites_page)
        self.delete_selected_favourite_btn.setGeometry(QtCore.QRect(441, 20, 33, 32))
        self.delete_selected_favourite_btn.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.delete_selected_favourite_btn.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"border-radius:5px;")
        self.delete_selected_favourite_btn.setText("")
        self.delete_selected_favourite_btn.setIcon(icon13)
        self.delete_selected_favourite_btn.setIconSize(QtCore.QSize(32, 32))
        self.delete_selected_favourite_btn.setObjectName("delete_selected_favourite_btn")
        self.delete_all_favourites_btn = QtWidgets.QPushButton(self.favourites_page)
        self.delete_all_favourites_btn.setGeometry(QtCore.QRect(480, 20, 33, 32))
        self.delete_all_favourites_btn.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.delete_all_favourites_btn.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"border-radius:5px;")
        self.delete_all_favourites_btn.setText("")
        self.delete_all_favourites_btn.setIcon(icon14)
        self.delete_all_favourites_btn.setIconSize(QtCore.QSize(32, 32))
        self.delete_all_favourites_btn.setObjectName("delete_all_favourites_btn")
        self.stackedWidget.addWidget(self.favourites_page)
        self.frame_7 = QtWidgets.QFrame(self.centralwidget)
        self.frame_7.setGeometry(QtCore.QRect(340, 430, 501, 51))
        self.frame_7.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.frame_7.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_7.setObjectName("frame_7")
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout(self.frame_7)
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.song_list_btn = QtWidgets.QPushButton(self.frame_7)
        self.song_list_btn.setMinimumSize(QtCore.QSize(0, 35))
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.song_list_btn.setFont(font)
        self.song_list_btn.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.song_list_btn.setStyleSheet("background-color: rgb(255, 255, 127);\n"
"border-radius:15px;")
        self.song_list_btn.setObjectName("song_list_btn")
        self.horizontalLayout_5.addWidget(self.song_list_btn)
        self.playlists_btn = QtWidgets.QPushButton(self.frame_7)
        self.playlists_btn.setMinimumSize(QtCore.QSize(0, 35))
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.playlists_btn.setFont(font)
        self.playlists_btn.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.playlists_btn.setStyleSheet("background-color: rgb(0, 255, 127);\n"
"border-radius:15px;")
        self.playlists_btn.setObjectName("playlists_btn")
        self.horizontalLayout_5.addWidget(self.playlists_btn)
        self.favourites_btn = QtWidgets.QPushButton(self.frame_7)
        self.favourites_btn.setMinimumSize(QtCore.QSize(0, 35))
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.favourites_btn.setFont(font)
        self.favourites_btn.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.favourites_btn.setStyleSheet("background-color: rgb(255, 140, 64);\n"
"border-radius:15px;")
        self.favourites_btn.setObjectName("favourites_btn")
        self.horizontalLayout_5.addWidget(self.favourites_btn)
        self.volume_label = QtWidgets.QLabel(self.centralwidget)
        self.volume_label.setGeometry(QtCore.QRect(120, 380, 41, 21))
        font = QtGui.QFont()
        font.setPointSize(15)
        font.setBold(True)
        font.setWeight(75)
        self.volume_label.setFont(font)
        self.volume_label.setStyleSheet("color: rgb(104, 114, 126);")
        self.volume_label.setObjectName("volume_label")
        self.background_image.raise_()
        self.bd_overlay.raise_()
        self.title_frame.raise_()
        self.frame_2.raise_()
        self.frame_3.raise_()
        self.frame_7.raise_()
        self.stackedWidget.raise_()
        self.volume_dial.raise_()
        self.volume_label.raise_()
        MusicApp.setCentralWidget(self.centralwidget)
        self.actionPlay = QtWidgets.QAction(MusicApp)
        self.actionPlay.setIcon(icon5)
        self.actionPlay.setObjectName("actionPlay")
        self.actionPause_Unpause = QtWidgets.QAction(MusicApp)
        self.actionPause_Unpause.setIcon(icon6)
        self.actionPause_Unpause.setObjectName("actionPause_Unpause")
        self.actionNext = QtWidgets.QAction(MusicApp)
        self.actionNext.setIcon(icon9)
        self.actionNext.setObjectName("actionNext")
        self.actionPrevious = QtWidgets.QAction(MusicApp)
        self.actionPrevious.setIcon(icon8)
        self.actionPrevious.setObjectName("actionPrevious")
        self.actionStop = QtWidgets.QAction(MusicApp)
        self.actionStop.setIcon(icon7)
        self.actionStop.setObjectName("actionStop")
        self.actionAdd_Selected_to_Favourites = QtWidgets.QAction(MusicApp)
        self.actionAdd_Selected_to_Favourites.setIcon(icon3)
        self.actionAdd_Selected_to_Favourites.setObjectName("actionAdd_Selected_to_Favourites")
        self.actionAdd_all_to_Favouries = QtWidgets.QAction(MusicApp)
        self.actionAdd_all_to_Favouries.setIcon(icon3)
        self.actionAdd_all_to_Favouries.setObjectName("actionAdd_all_to_Favouries")
        self.actionLoad_Selected_Playlist = QtWidgets.QAction(MusicApp)
        self.actionLoad_Selected_Playlist.setIcon(icon4)
        self.actionLoad_Selected_Playlist.setObjectName("actionLoad_Selected_Playlist")
        self.actionDelete_Selected_Playlist = QtWidgets.QAction(MusicApp)
        self.actionDelete_Selected_Playlist.setIcon(icon13)
        self.actionDelete_Selected_Playlist.setObjectName("actionDelete_Selected_Playlist")
        self.actionDelete_All_Playlists = QtWidgets.QAction(MusicApp)
        self.actionDelete_All_Playlists.setIcon(icon14)
        self.actionDelete_All_Playlists.setObjectName("actionDelete_All_Playlists")
        self.actionRemove_Selected_Favourite = QtWidgets.QAction(MusicApp)
        self.actionRemove_Selected_Favourite.setIcon(icon13)
        self.actionRemove_Selected_Favourite.setObjectName("actionRemove_Selected_Favourite")
        self.actionRemove_All_Favourites = QtWidgets.QAction(MusicApp)
        self.actionRemove_All_Favourites.setIcon(icon14)
        self.actionRemove_All_Favourites.setObjectName("actionRemove_All_Favourites")
        self.actionSave_Selected_to_a_Playlist = QtWidgets.QAction(MusicApp)
        icon15 = QtGui.QIcon()
        icon15.addPixmap(QtGui.QPixmap(":/img/utils/images/MusicListItem.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionSave_Selected_to_a_Playlist.setIcon(icon15)
        self.actionSave_Selected_to_a_Playlist.setObjectName("actionSave_Selected_to_a_Playlist")
        self.actionSave_all_to_a_playlist = QtWidgets.QAction(MusicApp)
        icon16 = QtGui.QIcon()
        icon16.addPixmap(QtGui.QPixmap(":/img/utils/images/dialog-music.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionSave_all_to_a_playlist.setIcon(icon16)
        self.actionSave_all_to_a_playlist.setObjectName("actionSave_all_to_a_playlist")

        self.retranslateUi(MusicApp)
        self.stackedWidget.setCurrentIndex(0)
        self.minimize_btn.clicked.connect(MusicApp.showMinimized) # type: ignore
        self.close_btn.clicked.connect(MusicApp.close) # type: ignore
        self.volume_dial.sliderMoved['int'].connect(self.volume_label.setNum) # type: ignore
        QtCore.QMetaObject.connectSlotsByName(MusicApp)

    def retranslateUi(self, MusicApp):
        _translate = QtCore.QCoreApplication.translate
        MusicApp.setWindowTitle(_translate("MusicApp", "Modern Music Player"))
        self.label.setText(_translate("MusicApp", "M Beatz"))
        self.label_3.setText(_translate("MusicApp", "Currently Playing"))
        self.label_5.setText(_translate("MusicApp", "Name"))
        self.current_song_name.setText(_translate("MusicApp", "Song name goes here"))
        self.label_7.setText(_translate("MusicApp", "Path"))
        self.current_song_path.setText(_translate("MusicApp", "Song path goes here"))
        self.add_to_fav_btn.setText(_translate("MusicApp", "  Add to Favourites"))
        self.add_to_playlist_btn.setText(_translate("MusicApp", "  Add to Playlist"))
        self.time_label.setText(_translate("MusicApp", "00:00:00 / 00:00:00"))
        self.label_6.setText(_translate("MusicApp", "Song List"))
        self.label_9.setText(_translate("MusicApp", "Playlists"))
        self.load_selected_playlist_btn.setText(_translate("MusicApp", "Load Selected"))
        self.new_playlist_btn.setText(_translate("MusicApp", "Create New"))
        self.remove_selected_playlist_btn.setText(_translate("MusicApp", "Remove Selected"))
        self.remove_all_playlists_btn.setText(_translate("MusicApp", "Remove All"))
        self.label_10.setText(_translate("MusicApp", "Favourites"))
        self.song_list_btn.setText(_translate("MusicApp", "Song List"))
        self.playlists_btn.setText(_translate("MusicApp", "Playlists"))
        self.favourites_btn.setText(_translate("MusicApp", "Favourites"))
        self.volume_label.setText(_translate("MusicApp", "50"))
        self.actionPlay.setText(_translate("MusicApp", "Play"))
        self.actionPause_Unpause.setText(_translate("MusicApp", "Pause/Unpause"))
        self.actionNext.setText(_translate("MusicApp", "Next"))
        self.actionPrevious.setText(_translate("MusicApp", "Previous"))
        self.actionStop.setText(_translate("MusicApp", "Stop"))
        self.actionAdd_Selected_to_Favourites.setText(_translate("MusicApp", "Add Selected to Favourites"))
        self.actionAdd_all_to_Favouries.setText(_translate("MusicApp", "Add all to Favouries"))
        self.actionLoad_Selected_Playlist.setText(_translate("MusicApp", "Load Selected"))
        self.actionDelete_Selected_Playlist.setText(_translate("MusicApp", "Delete Selected"))
        self.actionDelete_All_Playlists.setText(_translate("MusicApp", "Delete All"))
        self.actionRemove_Selected_Favourite.setText(_translate("MusicApp", "Remove Selected"))
        self.actionRemove_All_Favourites.setText(_translate("MusicApp", "Remove All"))
        self.actionSave_Selected_to_a_Playlist.setText(_translate("MusicApp", "Save Selected to a Playlist"))
        self.actionSave_all_to_a_playlist.setText(_translate("MusicApp", "Save all to a playlist"))
import res_rc


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MusicApp = QtWidgets.QMainWindow()
    ui = Ui_MusicApp()
    ui.setupUi(MusicApp)
    MusicApp.show()
    sys.exit(app.exec_())
