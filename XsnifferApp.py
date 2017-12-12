import csv
import matplotlib.pyplot as plt
import pyqtgraph as pg

import os
from PySide import QtGui

from gui.FenetrePrincipale import Ui_Form_xsnifferlogparser


class XsnifferApp(Ui_Form_xsnifferlogparser, QtGui.QWidget):
    def __init__(self):
        super(XsnifferApp, self).__init__()

        # init Window
        self.setupUi(self)
        self._update_ui()
        self._setup_raccourcis_clavier()
        self._setup_connections()

        self.show()

    def _update_ui(self):
        self.p2 = self.gwin_histogram.addPlot(title="Light (green) | Temperature (red)")

    def _setup_raccourcis_clavier(self):
        QtGui.QShortcut(QtGui.QKeySequence.Open, self, self._on_btn_browse_clicked)
        QtGui.QShortcut(QtGui.QKeySequence.Refresh, self, self._on_btn_parse_clicked)

    def _on_btn_browse_clicked(self):
        filename, filter = QtGui.QFileDialog.getOpenFileName(parent=self, caption='Open file', dir='.', filter='*.csv')
        if filename:
            print('browsed file {}'.format(filename))
            self.le_browsed_file.setText(filename)
            self.filename = filename
            self.lab_current_file.setText(os.path.basename(self.filename))
            self.btn_parse.setEnabled(True)

    def _on_btn_json_clicked(self):
        json_filename, json_filter = QtGui.QFileDialog.getOpenFileName(parent=self, caption='save to file', dir='.',
                                                                       json_filter='*.json')
        if json_filename:
            pass

    def _on_btn_close_clicked(self):
        self.close()

    def _on_btn_parse_clicked(self):
        print(self.filename)
        if self.filename:
            with open(self.filename) as csvFile:
                print('Reading from {}'.format(self.filename))
                reader = csv.DictReader(csvFile)
                reader = list(reader)

            light_measures = []
            light_nb_errors = 0

            light_current_max = -1
            light_node_max = -1
            light_elapsed_time_max = -1
            light_msec_max = -1

            light_current_min = 256
            light_node_min = 256
            light_elapsed_time_min = 256
            light_msec_min = 256

            temp_measures = []
            temp_nb_errors = 0

            temp_current_max = -1
            temp_node_max = -1
            temp_elapsed_time_max = -1
            temp_msec_max = -1

            temp_current_min = 256
            temp_node_min = 256
            temp_elapsed_time_min = 256
            temp_msec_min = 256

            # parse light
            parse_enumeration = enumerate(reader)
            for light_index, row in parse_enumeration:
                try:
                    light_lsb = int(row['9'])
                    light_msb = int(row['10'])
                    measure = light_lsb + 256 * light_msb
                    light_measures.append(measure)
                    if measure > light_current_max:
                        light_current_max = measure
                        light_node_max = int(row['3'])
                        light_elapsed_time_max = row['ElapsedTime']
                        light_msec_max = int(row['msec'])
                    elif measure < light_current_min:
                        light_current_min = measure
                        light_node_min = int(row['3'])
                        light_elapsed_time_min = row['ElapsedTime']
                        light_msec_min = int(row['msec'])

                except ValueError:
                    print("Error converting: {0} or {1} to an integer at line {2}".format(row['9'], row['10'],
                                                                                          light_index + 1))
                    light_nb_errors += 1

            # parse temp
            parse_enumeration = enumerate(reader)  # to reset the iterator
            for temp_index, temp_row in parse_enumeration:
                try:
                    temp_lsb = int(temp_row['7'])
                    temp_msb = int(temp_row['8'])
                    measure = temp_lsb + 256 * temp_msb
                    temp_measures.append(measure)
                    if measure > temp_current_max:
                        temp_current_max = measure
                        temp_node_max = int(temp_row['3'])
                        temp_elapsed_time_max = temp_row['ElapsedTime']
                        temp_msec_max = int(temp_row['msec'])
                    elif measure < temp_current_min:
                        temp_current_min = measure
                        temp_node_min = int(temp_row['3'])
                        temp_elapsed_time_min = temp_row['ElapsedTime']
                        temp_msec_min = int(temp_row['msec'])

                except ValueError:
                    print(
                        "Error converting: {0} or {1} to an integer at line {2}".format(row['7'], row['8'],
                                                                                        temp_index + 1))
                    temp_nb_errors += 1

            print('...Done reading the file.')

            if light_nb_errors > 0:
                print('Light number of lines skipped: {0} / {1}'.format(light_nb_errors, light_index + 1))
            if temp_nb_errors > 0:
                print('Temp number of lines skipped: {0} / {1}'.format(temp_nb_errors, temp_index + 1))

            print('From file {} with'.format(self.filename))
            print('Light: {0} measures \nmin: {1} @ {2}+{3} on node {4}'.format(
                len(light_measures), light_current_min, light_elapsed_time_min, light_msec_min, light_node_min))
            lavg = sum(light_measures) / len(light_measures)
            print("avg: {0} \nmax: {1} @ {2}+{3} on node {4}".format(lavg, light_current_max, light_elapsed_time_max,
                                                                     light_msec_max, light_node_max))
            self.lab_light_avg.setText(
                'Lavg: ' + str(lavg) + ' (mes=' + str(len(light_measures)) + ', err=' + str(light_nb_errors) + ')')
            self.lab_light_min.setText(
                'Lmin: {0} @ {1}+{2} on n: {3}'.format(str(light_current_min), str(light_elapsed_time_min),
                                                       str(light_msec_min), str(light_node_min)))
            self.lab_light_max.setText(
                'Lmax: {0} @ {1}+{2} on n: {3}'.format(str(light_current_max), str(light_elapsed_time_max),
                                                       str(light_msec_max), str(light_node_max)))

            print('Temp: {0} measures \nmin: {1} @ {2}+{3} on node {4}'.format(
                len(temp_measures), temp_current_min, temp_elapsed_time_min, temp_msec_min, temp_node_min))
            tavg = sum(temp_measures) / len(temp_measures)
            print("avg: {0} \nmax: {1} @ {2}+{3} on node {4}".format(tavg, temp_current_max, temp_elapsed_time_max,
                                                                     temp_msec_max, temp_node_max))
            self.lab_temp_avg.setText(
                'Tavg: ' + str(tavg) + ' (mes=' + str(len(temp_measures)) + ', err=' + str(temp_nb_errors) + ')')
            self.lab_temp_min.setText(
                'Tmin: {0} @ {1}+{2} on n: {3}'.format(str(temp_current_min), str(temp_elapsed_time_min),
                                                       str(temp_msec_min), str(temp_node_min)))
            self.lab_temp_max.setText(
                'Tmax: {0} @ {1}+{2} on n: {3}'.format(str(temp_current_max), str(temp_elapsed_time_max),
                                                       str(temp_msec_max), str(temp_node_max)))

            self.light_measures = light_measures
            self.temp_measures = temp_measures
            if len(light_measures) != 0:
                self.cbox_light.setEnabled(True)
            if len(temp_measures) !=0:
                self.cbox_temperature.setEnabled(True)

    def _on_cbox_light_clicked(self):
        if self.cbox_light.isChecked():
            self.c1 = self.p2.plot(self.light_measures, pen=(0,255,0), name="Light (red)")
        else:
            self.c1.clear()

    def _on_cbox_temperature_clicked(self):
        if self.cbox_temperature.isChecked():
            self.c2 = self.p2.plot(self.temp_measures, pen=(255, 0, 0), name="Temperature (green)")
        else:
            self.c2.clear()


    def _setup_connections(self):
        self.btn_browse.clicked.connect(self._on_btn_browse_clicked)
        self.btn_parse.clicked.connect(self._on_btn_parse_clicked)
        self.btn_json.clicked.connect(self._on_btn_json_clicked)
        self.btn_close.clicked.connect(self._on_btn_close_clicked)
        self.cbox_light.stateChanged.connect(self._on_cbox_light_clicked)
        self.cbox_temperature.stateChanged.connect(self._on_cbox_temperature_clicked)


app = QtGui.QApplication([])
fenetre = XsnifferApp()
app.exec_()
