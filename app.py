# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'car.ui'
#
# Created by: PyQt5 UI code generator 5.14.2 And Erfan Saberi (Thanks to Jadi)

from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(998, 722)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.tabWidget = QtWidgets.QTabWidget(self.centralwidget)
        self.tabWidget.setGeometry(QtCore.QRect(420, 10, 571, 401))
        self.tabWidget.setObjectName("tabWidget")
        self.tab = QtWidgets.QWidget()
        self.tab.setObjectName("tab")
        self.output = QtWidgets.QTextBrowser(self.tab)
        self.output.setGeometry(QtCore.QRect(0, 0, 561, 381))
        self.output.setObjectName("output")
        self.tabWidget.addTab(self.tab, "")
        self.tab_2 = QtWidgets.QWidget()
        self.tab_2.setObjectName("tab_2")
        self.tabWidget.addTab(self.tab_2, "")
        self.start = QtWidgets.QPushButton(self.centralwidget)
        self.start.setGeometry(QtCore.QRect(160, 280, 75, 23))
        self.start.setObjectName("start")
        self.Brand = QtWidgets.QComboBox(self.centralwidget)
        self.Brand.setGeometry(QtCore.QRect(110, 140, 69, 22))
        self.Brand.setObjectName("Brand")
        self.Brand.addItem("")
        self.Brand.addItem("")
        self.Brand.addItem("")
        self.Brand.addItem("")
        self.Brand.addItem("")
        self.Model = QtWidgets.QLineEdit(self.centralwidget)
        self.Model.setGeometry(QtCore.QRect(190, 140, 113, 21))
        self.Model.setObjectName("Model")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(130, 120, 151, 16))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(80, 190, 271, 20))
        self.label_2.setObjectName("label_2")
        self.Year = QtWidgets.QLineEdit(self.centralwidget)
        self.Year.setGeometry(QtCore.QRect(80, 220, 113, 20))
        self.Year.setObjectName("Year")
        self.Distance = QtWidgets.QLineEdit(self.centralwidget)
        self.Distance.setGeometry(QtCore.QRect(220, 220, 113, 20))
        self.Distance.setObjectName("Distance")
        self.logs = QtWidgets.QTextBrowser(self.centralwidget)
        self.logs.setGeometry(QtCore.QRect(0, 421, 991, 271))
        self.logs.setObjectName("logs")
        self.Language = QtWidgets.QComboBox(self.centralwidget)
        self.Language.setGeometry(QtCore.QRect(160, 70, 69, 22))
        self.Language.setObjectName("Language")
        self.Language.addItem("")
        self.Language.addItem("")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(130, 50, 131, 16))
        self.label_3.setObjectName("label_3")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 998, 21))
        self.menubar.setObjectName("menubar")
        self.menuCar_Price_Guess = QtWidgets.QMenu(self.menubar)
        self.menuCar_Price_Guess.setObjectName("menuCar_Price_Guess")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.menubar.addAction(self.menuCar_Price_Guess.menuAction())

        self.retranslateUi(MainWindow)
        self.tabWidget.setCurrentIndex(0)
        self.start.clicked.connect(self.startw)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    #this script collect information from bama.ir and help you guess your car price
    #developed by erfan saberi
    #Special Thanks to Jadi :)
    def startw(self):
        try:
            self.logs.clear()
            x , y , data , kar = [], [], [], []
            counter = 0
            lang = str(self.Language.currentText())
            if lang == 'Persian':
                title = 'تخمین قیمت خودرو'
                selectcar = 'از ليست موجود يک ماشين را انتخاب کنيد : '
                selectmodel = 'لطفا از بين مدل هاي موجود انتخاب کنيد : '
                unknowncar = 'ماشين شناخته نشده'
                selectmodelunknown = 'لطفا مدل ماشين مورد نظرتان را وارد کنيد : '
                howmany = 'در صورت تمایل تعداد صفحات مورد نظرتان را برای اعمال محدودیت وارد کنید : '
                inprogress = '        در حال جمع آوري اطلاعات'
                carpr = 'قیمت ماشین شما حدودا  %i تومان است'
                insertkarkard = 'کارکرد ماشین را به کیلومتر وارد کنید'
                insertyear = 'سال توليد ماشين را وارد کنيد'
                donetext = 'برای استفاده مجدد اینتر بزنید ، در غیر اینصورت با تایپ هر چیزی میتوانید از برنامه خارج شوید'
                notenough = 'اطلاعات کافی نیست، در هر حال برنامه به کار خود ادامه میدهد'
                startedstr = 'برنامه شروع به کار کرد'
                loadingbs = 'در حال بارگذاری بیوتیفول سوپ'
                loadingre = 'در حال بارگذاری رجکس'
                loadingreq = 'در حال بارگذاری ریکوئستز'
                loadingsk = 'در حال بارگذاری کتابخانه یادگیری ماشین'
                error = 'به نظر میرسد مشکلی در روند برنامه به وجود آمده است'+'\n'
            elif lang == 'English':
                title = 'Car Price Guess'
                selectcar = 'Please select a car brand from list : '
                selectmodel = 'Please enter your car model from list : '
                unknowncar = 'Unknown car'
                selectmodelunknown = 'Please insert your car model : '
                howmany = '(Optinal) Give me a number to limit web crawler : '
                inprogress = 'Crawling web pages ...'
                carpr = 'Your car price is around %i'
                insertkarkard = 'how many kilometers this car traveled? : '
                insertyear = 'Please insert your car product year : '
                donetext = 'Press enter for another guess or type something to exit'
                notenough = 'there isn\'t enough information about your car. however, programm started'
                startedstr = 'Application Started Working'
                loadingbs = 'Loading BeautifulSoup'
                loadingre = 'Loading RE'
                loadingreq = 'Loading requests'
                loadingsk = 'Loading Sklearn'
                error = 'Its looks there is a problem in program\n'
            self.logs.append(startedstr)
            cartype = str(self.Brand.currentText())
            carmodel = self.Model.text()
            cawork = self.Distance.text()
            pryear = self.Year.text()
            self.logs.append(title)
            #ask user for car brand and model
            a = 100

            self.logs.append('=======================')
            self.logs.append(inprogress)
            self.logs.append('=======================')
            app.processEvents()
            self.logs.append(loadingreq)
            import requests
            self.logs.append(loadingre)
            app.processEvents()
            import re
            self.logs.append(loadingsk)
            app.processEvents()
            from sklearn import tree
            self.logs.append(loadingbs)
            from bs4 import BeautifulSoup
            app.processEvents()
            #Exctracting data from web
            for i in range(1,a+1):
                app.processEvents()
                session = requests.get('https://bama.ir/car/%s/%s/all-trims?hasprice=true&page=%i' % (cartype, carmodel, i))
                app.processEvents()
                if session.url == ('https://bama.ir/car/%s/%s/all-trims?hasprice=true&page=%i' % (cartype, carmodel, i)):
                    soup = BeautifulSoup(session.text, 'html.parser')
                    res = soup.find_all('div', attrs={'class':'listdata'})
                else:
                    break
                for car in res:
                    app.processEvents()
                    name = car.find('h2', attrs={'itemprop':'name'})
                    name = re.sub(r'\s+', ' ', name.text).strip()
                    try:
                        brand = car.find('span', attrs={'class':'hidden-xs mod-date-car-page product-company-name'})
                        brand = (re.sub(r'\s+', ' ', brand.text).strip())
                    except:
                        brand = 'unknown'
                    year = car.find('span', attrs={'itemprop':'releaseDate'})
                    work = car.find('p', attrs={'class':'price hidden-xs'})
                    year,work = re.sub(r'\s+', ' ', year.text), re.sub(r'\s+', ' ', work.text)
                    kar.append(work)
                    if work == ' کارکرد صفر ' or work == 'کارتکس':
                        work = 0
                    elif not work == '-':
                        try:
                            work = re.sub(r'\کارکرد', '', work).strip()
                            work = re.sub(r',', '', work).strip()
                            work = int(work)
                        except:
                            pass
                    else:
                        work = 0
                    year = re.sub(r'، ', '', year)
                    city = car.find('p', attrs={'class':'provice hidden-xs'})
                    city = re.sub(r'\s+', ' ', city.text).strip()
                    cost = car.find('p', attrs={'class':'cost'})
                    cost = re.sub(r'\s+', ' ', cost.text).strip()
                    cost = re.sub(r' تومان', '', cost)
                    cost = re.sub(r',', '', cost)
                    if not cost == 'در توضیحات' and not cost == 'حواله' and not cost == 'توافقی':
                        try:
                            cost = int(cost)
                        except:
                            cost = 'Unknown'
                    if type(cost)==int:
                        self.logs.append('     '+' '+name+' '+str(year)+' '+str(work)+' '+str(cost))
                        data.append(year)
                        data.append(work)
                        y.append(cost)
                        x.append(data)
                        data = []
                        counter += 1
                self.logs.append('page '+str(i)+' done')
                if i > 3 and counter < 10:
                    break
            app.processEvents()
            self.logs.append(str(counter)+' information found')
            self.logs.append('=======================')


            #Start Using ML Library
            def startusingapp():
                app.processEvents()
                
                #Fit extracted data on a Decision Tree Classifier
                clf = tree.DecisionTreeClassifier()
                clf = clf.fit(x, y)

                #price guess
                def carprice(karkard, sal):
                    price = clf.predict([[sal, karkard]])
                    self.output.append(carpr%(price))
                
                #user interface
                def checkcarprice():
                    self.logs.append(title+' '+cartype+' '+carmodel)
                    carprice(cawork, pryear)
                
                checkcarprice()

            #check the informations count
            if counter > 5 :
                startusingapp()
            else :
                self.logs.append(notenough)
                startusingapp()
        except Exception as e:
            self.logs.append(error+str(e))
    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), _translate("MainWindow", "Your Car Price"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), _translate("MainWindow", "Cars like you"))
        self.start.setText(_translate("MainWindow", "Run"))
        self.Brand.setCurrentText(_translate("MainWindow", "peugeot"))
        self.Brand.setItemText(0, _translate("MainWindow", "peugeot"))
        self.Brand.setItemText(1, _translate("MainWindow", "pride"))
        self.Brand.setItemText(2, _translate("MainWindow", "bmw"))
        self.Brand.setItemText(3, _translate("MainWindow", "renault"))
        self.Brand.setItemText(4, _translate("MainWindow", "kia"))
        self.Model.setText(_translate("MainWindow", "Model"))
        self.label.setText(_translate("MainWindow", "Select Car brand and model"))
        self.label_2.setText(_translate("MainWindow", "Enter Your car Production Year and Worked Distance"))
        self.Year.setText(_translate("MainWindow", "Year"))
        self.Distance.setText(_translate("MainWindow", "Distance"))
        self.Language.setCurrentText(_translate("MainWindow", "English"))
        self.Language.setItemText(0, _translate("MainWindow", "Persian"))
        self.Language.setItemText(1, _translate("MainWindow", "English"))
        self.label_3.setText(_translate("MainWindow", "Select Language of output"))
        self.menuCar_Price_Guess.setTitle(_translate("MainWindow", "Car Price Guess"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
