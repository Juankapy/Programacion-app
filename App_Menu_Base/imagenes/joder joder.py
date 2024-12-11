def setupUi(self, MainWindow):
    MainWindow.setObjectName("MainWindow")
    MainWindow.resize(756, 461)
    MainWindow.setMinimumSize(QtCore.QSize(400, 0))
    MainWindow.setStyleSheet("")
    self.centralwidget = QtWidgets.QWidget(MainWindow)
    self.centralwidget.setObjectName("centralwidget")
    self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
    self.verticalLayout.setContentsMargins(0, 0, 0, 0)
    self.verticalLayout.setSpacing(0)
    self.verticalLayout.setObjectName("verticalLayout")
    # Frame superior
    self.frame_superior = QtWidgets.QFrame(self.centralwidget)
    self.frame_superior.setMinimumSize(QtCore.QSize(0, 35))
    self.frame_superior.setMaximumSize(QtCore.QSize(16777215, 50))
    self.frame_superior.setStyleSheet(
        "QFrame{"
        "border-top-left-radius: 20px;"
        "border-bottom-left-radius: 20px;"
        "background-color: rgb(170, 0, 255);"
        "}"
    )
    self.frame_superior.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
    self.frame_superior.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
    self.frame_superior.setObjectName("frame_superior")
    self.horizontalLayout_8 = QtWidgets.QHBoxLayout(self.frame_superior)
    self.horizontalLayout_8.setContentsMargins(2, 0, 2, 0)
    self.horizontalLayout_8.setSpacing(0)
    self.horizontalLayout_8.setObjectName("horizontalLayout_8")
    # Botón Menú
    self.bt_menu = QtWidgets.QPushButton(self.frame_superior)
    self.bt_menu.setMinimumSize(QtCore.QSize(200, 0))
    self.bt_menu.setMaximumSize(QtCore.QSize(200, 16777215))
    self.bt_menu.setStyleSheet(
        "QPushButton{"
        "background-color: #aa00ff;"
        "font: 87 12pt 'Arial Black';"
        "border-radius:0px;"
        "}"
        "QPushButton:hover{"
        "background-color: white;"
        "font: 87 12pt 'Arial Black';"
        "}"
    )
    icon = QtGui.QIcon()
    icon.addPixmap(QtGui.QPixmap("imagenes/hamburger.png"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
    self.bt_menu.setIcon(icon)
    self.bt_menu.setIconSize(QtCore.QSize(32, 32))
    self.bt_menu.setAutoDefault(False)
    self.bt_menu.setDefault(False)
    self.bt_menu.setFlat(False)
    self.bt_menu.setObjectName("bt_menu")
    self.horizontalLayout_8.addWidget(self.bt_menu, 0, QtCore.Qt.AlignmentFlag.AlignLeft)
    # Espaciador
    spacerItem = QtWidgets.QSpacerItem(
        265, 20, QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Minimum
    )
    self.horizontalLayout_8.addItem(spacerItem)
    # Botón Minimizar
    self.bt_minimizar = QtWidgets.QPushButton(self.frame_superior)
    self.bt_minimizar.setMinimumSize(QtCore.QSize(35, 35))
    self.bt_minimizar.setStyleSheet(
        "QPushButton{border:0px;}"
        "QPushButton:hover{border:5px solid #aa00ff;background-color:#ffff00;}"
    )
    self.bt_minimizar.setText("")
    icon1 = QtGui.QIcon()
    icon1.addPixmap(QtGui.QPixmap("imagenes/minimize.png"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
    self.bt_minimizar.setIcon(icon1)
    self.bt_minimizar.setIconSize(QtCore.QSize(32, 32))
    self.bt_minimizar.setFlat(False)
    self.bt_minimizar.setObjectName("bt_minimizar")
    self.horizontalLayout_8.addWidget(self.bt_minimizar, 0, QtCore.Qt.AlignmentFlag.AlignRight)
    # Otros botones (Maximizar, Restaurar, Cerrar) siguen una lógica similar...
    self.verticalLayout.addWidget(self.frame_superior)
    # Frame inferior (similar ajuste)
    # ...
    MainWindow.setCentralWidget(self.centralwidget)
    self.retranslateUi(MainWindow)
    QtCore.QMetaObject.connectSlotsByName(MainWindow)


def retranslateUi(self, MainWindow):
    _translate = QtCore.QCoreApplication.translate
    MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
