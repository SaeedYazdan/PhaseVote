# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'regGr.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets
import numpy as np


class Ui_RegGrDial(object):
    def setupUi(self, RegGrDial, total, normals, precurv, classified):
        self.total = total
        self.normals = normals
        self.mod_curv = classified
        self.curvatures = precurv
        self.plane_normal, self.plane_seed, self.grand_nei = 0, 0, 0

        RegGrDial.setObjectName("RegGrDial")
        RegGrDial.resize(405, 395)

        self.buttonBox = QtWidgets.QDialogButtonBox(RegGrDial)
        self.buttonBox.setGeometry(QtCore.QRect(40, 355, 341, 32))
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")
        self.buttonBox.setDisabled(True)

        self.load_rbtn = QtWidgets.QRadioButton(RegGrDial)
        self.load_rbtn.setGeometry(QtCore.QRect(20, 10, 201, 20))
        self.load_rbtn.setObjectName("load_rbtn")

        self.calc_rbtn = QtWidgets.QRadioButton(RegGrDial)
        self.calc_rbtn.setGeometry(QtCore.QRect(20, 100, 121, 20))
        self.calc_rbtn.setObjectName("calc_rbtn")

        self.load_btn = QtWidgets.QPushButton(RegGrDial)
        self.load_btn.setGeometry(QtCore.QRect(150, 40, 93, 28))
        self.load_btn.setObjectName("Load_btn")
        self.load_btn.setDisabled(True)

        self.load_lb = QtWidgets.QLabel(RegGrDial)
        self.load_lb.setGeometry(QtCore.QRect(120, 70, 151, 21))
        self.load_lb.setAlignment(QtCore.Qt.AlignCenter)
        self.load_lb.setObjectName("Load_lb")
        self.load_lb.setDisabled(True)

        self.nei_spin = QtWidgets.QSpinBox(RegGrDial)
        self.nei_spin.setGeometry(QtCore.QRect(350, 130, 42, 22))
        self.nei_spin.setObjectName("nei_spin")
        self.nei_spin.setDisabled(True)
        self.nei_spin.setMinimum(3)
        self.nei_spin.setMaximum(200)
        self.nei_spin.setValue(15)


        self.label_2 = QtWidgets.QLabel(RegGrDial)
        self.label_2.setGeometry(QtCore.QRect(60, 130, 131, 21))
        self.label_2.setObjectName("label_2")
        self.label_2.setDisabled(True)

        self.label_3 = QtWidgets.QLabel(RegGrDial)
        self.label_3.setGeometry(QtCore.QRect(60, 160, 221, 21))
        self.label_3.setObjectName("label_3")
        self.label_3.setDisabled(True)

        self.angle_spin = QtWidgets.QSpinBox(RegGrDial)
        self.angle_spin.setGeometry(QtCore.QRect(350, 160, 42, 22))
        self.angle_spin.setObjectName("angle_spin")
        self.angle_spin.setDisabled(True)
        self.angle_spin.setMinimum(0)
        self.angle_spin.setMaximum(90)
        self.angle_spin.setValue(10)

        self.label_4 = QtWidgets.QLabel(RegGrDial)
        self.label_4.setGeometry(QtCore.QRect(60, 190, 291, 31))
        self.label_4.setObjectName("label_4")
        self.label_4.setDisabled(True)

        self.min_nei_spin = QtWidgets.QSpinBox(RegGrDial)
        self.min_nei_spin.setGeometry(QtCore.QRect(350, 190, 42, 22))
        self.min_nei_spin.setObjectName("min_nei_spin")
        self.min_nei_spin.setDisabled(True)
        self.min_nei_spin.setMinimum(0)
        self.min_nei_spin.setValue(30)

        self.label_5 = QtWidgets.QLabel(RegGrDial)
        self.label_5.setGeometry(QtCore.QRect(60, 220, 291, 31))
        self.label_5.setObjectName("label_5")
        self.label_5.setDisabled(True)

        self.min_aver_spin = QtWidgets.QSpinBox(RegGrDial)
        self.min_aver_spin.setGeometry(QtCore.QRect(330, 220, 62, 22))
        self.min_aver_spin.setObjectName('min_aver_spin')
        self.min_aver_spin.setDisabled(True)
        self.min_aver_spin.setMinimum(5)
        self.min_aver_spin.setMaximum(10000)
        self.min_aver_spin.setValue(1000)

        self.calc_btn = QtWidgets.QPushButton(RegGrDial)
        self.calc_btn.setGeometry(QtCore.QRect(150, 250, 93, 28))
        self.calc_btn.setObjectName("calc_btn")
        self.calc_btn.setDisabled(True)

        self.save_lb = QtWidgets.QLabel(RegGrDial)
        self.save_lb.setGeometry(QtCore.QRect(110, 320, 151, 21))
        self.save_lb.setAlignment(QtCore.Qt.AlignCenter)
        self.save_lb.setObjectName("save_lb")
        self.save_lb.setDisabled(True)

        self.save_btn = QtWidgets.QPushButton(RegGrDial)
        self.save_btn.setGeometry(QtCore.QRect(150, 290, 93, 28))
        self.save_btn.setObjectName("save_btn")
        self.save_btn.setDisabled(True)

        self.retranslateUi(RegGrDial)
        self.buttonBox.accepted.connect(RegGrDial.accept)
        self.buttonBox.rejected.connect(RegGrDial.reject)
        QtCore.QMetaObject.connectSlotsByName(RegGrDial)

        self.load_rbtn.toggled.connect(self.load_activated)
        self.calc_rbtn.toggled.connect(self.calc_activated)
        self.load_btn.clicked.connect(self.loader)
        self.calc_btn.clicked.connect(self.calcor)
        self.save_btn.clicked.connect(self.savor)


    def retranslateUi(self, RegGrDial):
        _translate = QtCore.QCoreApplication.translate
        RegGrDial.setWindowTitle(_translate("RegGrDial", "Region Growing Dialog"))
        self.load_rbtn.setText(_translate("RegGrDial", "Load from previous sessions"))
        self.calc_rbtn.setText(_translate("RegGrDial", "Calculate it Now"))
        self.load_btn.setText(_translate("RegGrDial", "Load"))
        self.load_lb.setText(_translate("RegGrDial", ""))
        self.label_2.setText(_translate("RegGrDial", "Number of neighbors"))
        self.label_3.setText(_translate("RegGrDial", "Maximum degree of angular distance"))
        self.label_4.setText(_translate("RegGrDial", "Minimum number of points to construct a surface"))
        self.label_5.setText(_translate("RegGrDial", "The threshold for new averaging"))
        self.calc_btn.setText(_translate("RegGrDial", "Calculate"))
        self.save_lb.setText(_translate("RegGrDial", ""))
        self.save_btn.setText(_translate("RegGrDial", "Save"))


    def load_activated(self):
        self.orig()
        self.load_btn.setDisabled(False)
        self.load_lb.setDisabled(False)

    def calc_activated(self):
        self.orig()
        self.calc_btn.setDisabled(False)
        self.label_2.setDisabled(False)
        self.label_3.setDisabled(False)
        self.label_4.setDisabled(False)
        self.label_5.setDisabled(False)
        self.nei_spin.setDisabled(False)
        self.angle_spin.setDisabled(False)
        self.min_nei_spin.setDisabled(False)
        self.min_aver_spin.setDisabled(False)

    def orig(self):
        self.load_btn.setDisabled(True)
        self.load_lb.setDisabled(True)
        self.save_btn.setDisabled(True)
        self.save_lb.setDisabled(True)
        self.buttonBox.setDisabled(True)
        self.calc_btn.setDisabled(True)
        self.label_2.setDisabled(True)
        self.label_3.setDisabled(True)
        self.label_4.setDisabled(True)
        self.label_5.setDisabled(True)
        self.nei_spin.setDisabled(True)
        self.angle_spin.setDisabled(True)
        self.min_nei_spin.setDisabled(True)
        self.min_aver_spin.setDisabled(True)

    def loader(self):
        print('Loading')

        name = QtWidgets.QFileDialog.getOpenFileName(None, "Open File", "/home", "*.out *.txt")

        FName1 = ''
        FName2 = ''
        FName3 = ''

        if name[0]:
            print(name[0])

            FName = name[0].split('.')
            if FName[0][-2:] == 'pn':
                FName1 = name[0]
                FName2 = FName[0][:-2] + 'ps.txt'
                FName3 = FName[0][:-2] + 'gn.txt'
            elif FName[0][-2:] == 'ps':
                FName1 = FName[0][:-2] + 'pn.out'
                FName2 = name[0]
                FName3 = FName[0][:-2] + 'gn.txt'
            elif FName[0][-2:] == 'gn':
                FName1 = FName[0][:-2] + 'pn.out'
                FName2 = FName[0][:-2] + 'ps.txt'
                FName3 = name[0]
            else:
                print('Something is Wrong')

            try:
                self.plane_normal = np.loadtxt(FName1, delimiter=',')

                with open(FName2, 'r') as f:
                    self.plane_seed = f.readlines()

                with open(FName3, 'r') as g:
                    #self.grand_nei = g.readlines()
                    gt = g.read()

                grand_nei = []
                for i in range(len(self.total)):
                    loc1 = gt.find("[")
                    gt = gt[loc1:]
                    # print(gt)
                    loc2 = gt.find("]")
                    row = gt[loc1 + 1:loc2]
                    gt = gt[(loc2 + 2):]
                    grand_nei.append(row)
                    #print(i)
                self.grand_nei = grand_nei



                print(grand_nei)

                #self.plane_seed = np.loadtxt(FName2, delimiter=',')
                #self.grand_nei = np.loadtxt(FName3, delimiter=',')
                self.load_lb.setText(FName1)
                self.buttonBox.setDisabled(False)

                ###################
                #  Here, we should add codes to check whether the loaded file matches the loaded model
                ##################

            except Exception as e:
                print(e)

    def calcor(self):
        print('Calcor')

        from resources.codes import rg_rev

        import math
        deg = math.cos(math.radians(self.angle_spin.value()))

        minNei = int(self.min_nei_spin.value())
        self.plane_normal, self.plane_seed, self.grand_nei = rg_rev.region_growing4(self.normals,
                                                                                    self.total,
                                                                                    self.curvatures,
                                                                                    int(self.nei_spin.value()),
                                                                                    deg,
                                                                                    minNei,
                                                                                    self.min_aver_spin.value())
        self.save_btn.setDisabled(False)
        self.buttonBox.setDisabled(False)

    def savor(self):
        print('Saving')
        name = QtWidgets.QFileDialog.getSaveFileName(None, "Save File", "/home", "*.out")

        if name[0]:
            FName = name[0].split('.')
            np.savetxt(FName[0] + '_pn.out', self.plane_normal, delimiter=',')

            with open(FName[0] + '_ps.txt', 'w') as f:
                for item in self.plane_seed:
                    f.write("%s\n" % item)

            with open(FName[0] + '_gn.txt', 'w') as f:
                for item in self.grand_nei:
                    f.write("%s\n" % item)


            #np.savetxt(FName[0] + '_ps.out', self.plane_seed, delimiter=',')
            #np.savetxt(FName[0] + '_gn.out', self.grand_nei, delimiter=',')
            self.save_lb.setText(FName[0])




if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    RegGrDial = QtWidgets.QDialog()
    ui = Ui_RegGrDial()
    ui.setupUi(RegGrDial, 0, 0, 0, 0)
    RegGrDial.show()
    sys.exit(app.exec_())
