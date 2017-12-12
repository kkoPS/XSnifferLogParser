# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:\kko\HEIG_VD\ADR\XSnifferLogParser\gui\FenetrePrincipale.ui'
#
# Created: Tue Dec 12 18:10:53 2017
#      by: pyside-uic 0.2.15 running on PySide 1.2.4
#
# WARNING! All changes made in this file will be lost!

from PySide import QtCore, QtGui

class Ui_Form_xsnifferlogparser(object):
    def setupUi(self, Form_xsnifferlogparser):
        Form_xsnifferlogparser.setObjectName("Form_xsnifferlogparser")
        Form_xsnifferlogparser.resize(718, 696)
        self.verticalLayout_4 = QtGui.QVBoxLayout(Form_xsnifferlogparser)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.lab_chose_file = QtGui.QLabel(Form_xsnifferlogparser)
        self.lab_chose_file.setObjectName("lab_chose_file")
        self.verticalLayout_4.addWidget(self.lab_chose_file)
        self.vl_browser = QtGui.QVBoxLayout()
        self.vl_browser.setObjectName("vl_browser")
        self.hl_browse = QtGui.QHBoxLayout()
        self.hl_browse.setObjectName("hl_browse")
        self.le_browsed_file = QtGui.QLineEdit(Form_xsnifferlogparser)
        self.le_browsed_file.setObjectName("le_browsed_file")
        self.hl_browse.addWidget(self.le_browsed_file)
        self.btn_browse = QtGui.QPushButton(Form_xsnifferlogparser)
        self.btn_browse.setObjectName("btn_browse")
        self.hl_browse.addWidget(self.btn_browse)
        self.vl_browser.addLayout(self.hl_browse)
        self.verticalLayout_4.addLayout(self.vl_browser)
        self.hl_parse = QtGui.QHBoxLayout()
        self.hl_parse.setObjectName("hl_parse")
        self.lab_current_file = QtGui.QLabel(Form_xsnifferlogparser)
        self.lab_current_file.setObjectName("lab_current_file")
        self.hl_parse.addWidget(self.lab_current_file)
        self.btn_parse = QtGui.QPushButton(Form_xsnifferlogparser)
        self.btn_parse.setEnabled(False)
        self.btn_parse.setCheckable(False)
        self.btn_parse.setDefault(False)
        self.btn_parse.setFlat(False)
        self.btn_parse.setObjectName("btn_parse")
        self.hl_parse.addWidget(self.btn_parse)
        self.verticalLayout_4.addLayout(self.hl_parse)
        self.hl_sensors = QtGui.QHBoxLayout()
        self.hl_sensors.setObjectName("hl_sensors")
        self.vl_light = QtGui.QVBoxLayout()
        self.vl_light.setObjectName("vl_light")
        self.cbox_light = QtGui.QCheckBox(Form_xsnifferlogparser)
        self.cbox_light.setEnabled(False)
        self.cbox_light.setObjectName("cbox_light")
        self.vl_light.addWidget(self.cbox_light)
        self.lab_light_min = QtGui.QLabel(Form_xsnifferlogparser)
        self.lab_light_min.setObjectName("lab_light_min")
        self.vl_light.addWidget(self.lab_light_min)
        self.lab_light_avg = QtGui.QLabel(Form_xsnifferlogparser)
        self.lab_light_avg.setObjectName("lab_light_avg")
        self.vl_light.addWidget(self.lab_light_avg)
        self.lab_light_max = QtGui.QLabel(Form_xsnifferlogparser)
        self.lab_light_max.setObjectName("lab_light_max")
        self.vl_light.addWidget(self.lab_light_max)
        self.hl_sensors.addLayout(self.vl_light)
        self.vl_temp = QtGui.QVBoxLayout()
        self.vl_temp.setObjectName("vl_temp")
        self.cbox_temperature = QtGui.QCheckBox(Form_xsnifferlogparser)
        self.cbox_temperature.setEnabled(False)
        self.cbox_temperature.setChecked(False)
        self.cbox_temperature.setObjectName("cbox_temperature")
        self.vl_temp.addWidget(self.cbox_temperature)
        self.lab_temp_min = QtGui.QLabel(Form_xsnifferlogparser)
        self.lab_temp_min.setObjectName("lab_temp_min")
        self.vl_temp.addWidget(self.lab_temp_min)
        self.lab_temp_avg = QtGui.QLabel(Form_xsnifferlogparser)
        self.lab_temp_avg.setObjectName("lab_temp_avg")
        self.vl_temp.addWidget(self.lab_temp_avg)
        self.lab_temp_max = QtGui.QLabel(Form_xsnifferlogparser)
        self.lab_temp_max.setObjectName("lab_temp_max")
        self.vl_temp.addWidget(self.lab_temp_max)
        self.hl_sensors.addLayout(self.vl_temp)
        self.verticalLayout_4.addLayout(self.hl_sensors)
        self.gwin_histogram = GraphicsWindow()
        self.gwin_histogram.setObjectName("gwin_histogram")
        self.verticalLayout_4.addWidget(self.gwin_histogram)
        self.hl_bottom_buttons = QtGui.QHBoxLayout()
        self.hl_bottom_buttons.setObjectName("hl_bottom_buttons")
        self.btn_json = QtGui.QPushButton(Form_xsnifferlogparser)
        self.btn_json.setEnabled(False)
        self.btn_json.setObjectName("btn_json")
        self.hl_bottom_buttons.addWidget(self.btn_json)
        self.btn_close = QtGui.QPushButton(Form_xsnifferlogparser)
        self.btn_close.setObjectName("btn_close")
        self.hl_bottom_buttons.addWidget(self.btn_close)
        self.verticalLayout_4.addLayout(self.hl_bottom_buttons)

        self.retranslateUi(Form_xsnifferlogparser)
        QtCore.QMetaObject.connectSlotsByName(Form_xsnifferlogparser)

    def retranslateUi(self, Form_xsnifferlogparser):
        Form_xsnifferlogparser.setWindowTitle(QtGui.QApplication.translate("Form_xsnifferlogparser", "XSniffer Log Parser", None, QtGui.QApplication.UnicodeUTF8))
        self.lab_chose_file.setText(QtGui.QApplication.translate("Form_xsnifferlogparser", "Chose a .csv from XSniffer", None, QtGui.QApplication.UnicodeUTF8))
        self.btn_browse.setText(QtGui.QApplication.translate("Form_xsnifferlogparser", "Browse", None, QtGui.QApplication.UnicodeUTF8))
        self.lab_current_file.setText(QtGui.QApplication.translate("Form_xsnifferlogparser", "chosen file: ", None, QtGui.QApplication.UnicodeUTF8))
        self.btn_parse.setText(QtGui.QApplication.translate("Form_xsnifferlogparser", "parse", None, QtGui.QApplication.UnicodeUTF8))
        self.cbox_light.setText(QtGui.QApplication.translate("Form_xsnifferlogparser", "Light", None, QtGui.QApplication.UnicodeUTF8))
        self.lab_light_min.setText(QtGui.QApplication.translate("Form_xsnifferlogparser", "Lmin: ", None, QtGui.QApplication.UnicodeUTF8))
        self.lab_light_avg.setText(QtGui.QApplication.translate("Form_xsnifferlogparser", "Lavg: ", None, QtGui.QApplication.UnicodeUTF8))
        self.lab_light_max.setText(QtGui.QApplication.translate("Form_xsnifferlogparser", "Lmax: ", None, QtGui.QApplication.UnicodeUTF8))
        self.cbox_temperature.setText(QtGui.QApplication.translate("Form_xsnifferlogparser", "Temperature", None, QtGui.QApplication.UnicodeUTF8))
        self.lab_temp_min.setText(QtGui.QApplication.translate("Form_xsnifferlogparser", "Tmin: ", None, QtGui.QApplication.UnicodeUTF8))
        self.lab_temp_avg.setText(QtGui.QApplication.translate("Form_xsnifferlogparser", "Tavg: ", None, QtGui.QApplication.UnicodeUTF8))
        self.lab_temp_max.setText(QtGui.QApplication.translate("Form_xsnifferlogparser", "Tmax: ", None, QtGui.QApplication.UnicodeUTF8))
        self.btn_json.setText(QtGui.QApplication.translate("Form_xsnifferlogparser", "JSON summary", None, QtGui.QApplication.UnicodeUTF8))
        self.btn_close.setText(QtGui.QApplication.translate("Form_xsnifferlogparser", "exit", None, QtGui.QApplication.UnicodeUTF8))

from pyqtgraph import GraphicsWindow
