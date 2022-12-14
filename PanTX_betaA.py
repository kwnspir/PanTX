#!/usr/bin/env python3
# -*- coding: utf-8 -*-

#
# SPDX-License-Identifier: GPL-3.0
#
# GNU Radio Python Flow Graph
# Title: Pantransmitter_betaA
# GNU Radio version: 3.8.1.0

from distutils.version import StrictVersion

if __name__ == '__main__':
    import ctypes
    import sys
    if sys.platform.startswith('linux'):
        try:
            x11 = ctypes.cdll.LoadLibrary('libX11.so')
            x11.XInitThreads()
        except:
            print("Warning: failed to XInitThreads()")

from PyQt5 import Qt
from gnuradio import eng_notation
from gnuradio import qtgui
import sip
from gnuradio import analog
from gnuradio import blocks
import numpy
from gnuradio import digital
from gnuradio import gr
from gnuradio.filter import firdes
import sys
import signal
from argparse import ArgumentParser
from gnuradio.eng_arg import eng_float, intx
from gnuradio import gr, digital, analog
from gnuradio import qtgui

class PanTX_betaA(gr.top_block, Qt.QWidget):

    def __init__(self):
        gr.top_block.__init__(self, "Pantransmitter_betaA")
        Qt.QWidget.__init__(self)
        self.setWindowTitle("Pantransmitter_betaA")
        qtgui.util.check_set_qss()
        try:
            self.setWindowIcon(Qt.QIcon.fromTheme('gnuradio-grc'))
        except:
            pass
        self.top_scroll_layout = Qt.QVBoxLayout()
        self.setLayout(self.top_scroll_layout)
        self.top_scroll = Qt.QScrollArea()
        self.top_scroll.setFrameStyle(Qt.QFrame.NoFrame)
        self.top_scroll_layout.addWidget(self.top_scroll)
        self.top_scroll.setWidgetResizable(True)
        self.top_widget = Qt.QWidget()
        self.top_scroll.setWidget(self.top_widget)
        self.top_layout = Qt.QVBoxLayout(self.top_widget)
        self.top_grid_layout = Qt.QGridLayout()
        self.top_layout.addLayout(self.top_grid_layout)

        self.settings = Qt.QSettings("GNU Radio", "PanTX_betaA")

        try:
            if StrictVersion(Qt.qVersion()) < StrictVersion("5.0.0"):
                self.restoreGeometry(self.settings.value("geometry").toByteArray())
            else:
                self.restoreGeometry(self.settings.value("geometry"))
        except:
            pass

        ##################################################
        # Variables
        ##################################################
        self.variable_constellation_0 = variable_constellation_0 = digital.constellation_16qam().base()
        self.txpower = txpower = 0.1
        self.samp_rate = samp_rate = 4e6
        self.qam_samp_per_symb = qam_samp_per_symb = 2
        self.qam_en = qam_en = 1
        self.qam_BW = qam_BW = 350e-3
        self.psk_samp_per_symb = psk_samp_per_symb = 2
        self.psk_num = psk_num = 8
        self.psk_en = psk_en = 0
        self.psk_BW = psk_BW = 350e-3
        self.gmsk_samp = gmsk_samp = 2
        self.gmsk_en = gmsk_en = 0
        self.gmsk_BT = gmsk_BT = 350e-3
        self.gfsk_en = gfsk_en = 0
        self.cpm_spsym = cpm_spsym = 4
        self.cpm_pulse_duration = cpm_pulse_duration = 4
        self.cpm_mod_index = cpm_mod_index = 500e-3
        self.cpm_en = cpm_en = 0
        self.cpm_BT = cpm_BT = 300e-3
        self.bandwidth = bandwidth = 1e6
        self.CenterFreq = CenterFreq = 915e6

        ##################################################
        # Blocks
        ##################################################
        self.tab_id = Qt.QTabWidget()
        self.tab_id_widget_0 = Qt.QWidget()
        self.tab_id_layout_0 = Qt.QBoxLayout(Qt.QBoxLayout.TopToBottom, self.tab_id_widget_0)
        self.tab_id_grid_layout_0 = Qt.QGridLayout()
        self.tab_id_layout_0.addLayout(self.tab_id_grid_layout_0)
        self.tab_id.addTab(self.tab_id_widget_0, 'Info')
        self.tab_id_widget_1 = Qt.QWidget()
        self.tab_id_layout_1 = Qt.QBoxLayout(Qt.QBoxLayout.TopToBottom, self.tab_id_widget_1)
        self.tab_id_grid_layout_1 = Qt.QGridLayout()
        self.tab_id_layout_1.addLayout(self.tab_id_grid_layout_1)
        self.tab_id.addTab(self.tab_id_widget_1, 'GMSK')
        self.tab_id_widget_2 = Qt.QWidget()
        self.tab_id_layout_2 = Qt.QBoxLayout(Qt.QBoxLayout.TopToBottom, self.tab_id_widget_2)
        self.tab_id_grid_layout_2 = Qt.QGridLayout()
        self.tab_id_layout_2.addLayout(self.tab_id_grid_layout_2)
        self.tab_id.addTab(self.tab_id_widget_2, 'GFSK')
        self.tab_id_widget_3 = Qt.QWidget()
        self.tab_id_layout_3 = Qt.QBoxLayout(Qt.QBoxLayout.TopToBottom, self.tab_id_widget_3)
        self.tab_id_grid_layout_3 = Qt.QGridLayout()
        self.tab_id_layout_3.addLayout(self.tab_id_grid_layout_3)
        self.tab_id.addTab(self.tab_id_widget_3, 'PSK')
        self.tab_id_widget_4 = Qt.QWidget()
        self.tab_id_layout_4 = Qt.QBoxLayout(Qt.QBoxLayout.TopToBottom, self.tab_id_widget_4)
        self.tab_id_grid_layout_4 = Qt.QGridLayout()
        self.tab_id_layout_4.addLayout(self.tab_id_grid_layout_4)
        self.tab_id.addTab(self.tab_id_widget_4, 'QAM')
        self.tab_id_widget_5 = Qt.QWidget()
        self.tab_id_layout_5 = Qt.QBoxLayout(Qt.QBoxLayout.TopToBottom, self.tab_id_widget_5)
        self.tab_id_grid_layout_5 = Qt.QGridLayout()
        self.tab_id_layout_5.addLayout(self.tab_id_grid_layout_5)
        self.tab_id.addTab(self.tab_id_widget_5, 'CPM')
        self.top_grid_layout.addWidget(self.tab_id, 6, 0, 1, 5)
        for r in range(6, 7):
            self.top_grid_layout.setRowStretch(r, 1)
        for c in range(0, 5):
            self.top_grid_layout.setColumnStretch(c, 1)
        self._qam_samp_per_symb_tool_bar = Qt.QToolBar(self)
        self._qam_samp_per_symb_tool_bar.addWidget(Qt.QLabel('Samples per Symbol' + ": "))
        self._qam_samp_per_symb_line_edit = Qt.QLineEdit(str(self.qam_samp_per_symb))
        self._qam_samp_per_symb_tool_bar.addWidget(self._qam_samp_per_symb_line_edit)
        self._qam_samp_per_symb_line_edit.returnPressed.connect(
            lambda: self.set_qam_samp_per_symb(int(str(self._qam_samp_per_symb_line_edit.text()))))
        self.tab_id_grid_layout_4.addWidget(self._qam_samp_per_symb_tool_bar, 1, 0, 1, 5)
        for r in range(1, 2):
            self.tab_id_grid_layout_4.setRowStretch(r, 1)
        for c in range(0, 5):
            self.tab_id_grid_layout_4.setColumnStretch(c, 1)
        _qam_en_check_box = Qt.QCheckBox('QAM')
        self._qam_en_choices = {True: 1, False: 0}
        self._qam_en_choices_inv = dict((v,k) for k,v in self._qam_en_choices.items())
        self._qam_en_callback = lambda i: Qt.QMetaObject.invokeMethod(_qam_en_check_box, "setChecked", Qt.Q_ARG("bool", self._qam_en_choices_inv[i]))
        self._qam_en_callback(self.qam_en)
        _qam_en_check_box.stateChanged.connect(lambda i: self.set_qam_en(self._qam_en_choices[bool(i)]))
        self.top_grid_layout.addWidget(_qam_en_check_box, 0, 3, 1, 1)
        for r in range(0, 1):
            self.top_grid_layout.setRowStretch(r, 1)
        for c in range(3, 4):
            self.top_grid_layout.setColumnStretch(c, 1)
        self._qam_BW_tool_bar = Qt.QToolBar(self)
        self._qam_BW_tool_bar.addWidget(Qt.QLabel('Excess BW' + ": "))
        self._qam_BW_line_edit = Qt.QLineEdit(str(self.qam_BW))
        self._qam_BW_tool_bar.addWidget(self._qam_BW_line_edit)
        self._qam_BW_line_edit.returnPressed.connect(
            lambda: self.set_qam_BW(eng_notation.str_to_num(str(self._qam_BW_line_edit.text()))))
        self.tab_id_grid_layout_4.addWidget(self._qam_BW_tool_bar, 2, 0, 1, 5)
        for r in range(2, 3):
            self.tab_id_grid_layout_4.setRowStretch(r, 1)
        for c in range(0, 5):
            self.tab_id_grid_layout_4.setColumnStretch(c, 1)
        self._psk_samp_per_symb_tool_bar = Qt.QToolBar(self)
        self._psk_samp_per_symb_tool_bar.addWidget(Qt.QLabel('Samples per Symbol' + ": "))
        self._psk_samp_per_symb_line_edit = Qt.QLineEdit(str(self.psk_samp_per_symb))
        self._psk_samp_per_symb_tool_bar.addWidget(self._psk_samp_per_symb_line_edit)
        self._psk_samp_per_symb_line_edit.returnPressed.connect(
            lambda: self.set_psk_samp_per_symb(int(str(self._psk_samp_per_symb_line_edit.text()))))
        self.tab_id_grid_layout_3.addWidget(self._psk_samp_per_symb_tool_bar, 2, 0, 1, 5)
        for r in range(2, 3):
            self.tab_id_grid_layout_3.setRowStretch(r, 1)
        for c in range(0, 5):
            self.tab_id_grid_layout_3.setColumnStretch(c, 1)
        self._psk_num_tool_bar = Qt.QToolBar(self)
        self._psk_num_tool_bar.addWidget(Qt.QLabel('Number of points' + ": "))
        self._psk_num_line_edit = Qt.QLineEdit(str(self.psk_num))
        self._psk_num_tool_bar.addWidget(self._psk_num_line_edit)
        self._psk_num_line_edit.returnPressed.connect(
            lambda: self.set_psk_num(int(str(self._psk_num_line_edit.text()))))
        self.tab_id_grid_layout_3.addWidget(self._psk_num_tool_bar, 1, 0, 1, 5)
        for r in range(1, 2):
            self.tab_id_grid_layout_3.setRowStretch(r, 1)
        for c in range(0, 5):
            self.tab_id_grid_layout_3.setColumnStretch(c, 1)
        _psk_en_check_box = Qt.QCheckBox('PSK')
        self._psk_en_choices = {True: 1, False: 0}
        self._psk_en_choices_inv = dict((v,k) for k,v in self._psk_en_choices.items())
        self._psk_en_callback = lambda i: Qt.QMetaObject.invokeMethod(_psk_en_check_box, "setChecked", Qt.Q_ARG("bool", self._psk_en_choices_inv[i]))
        self._psk_en_callback(self.psk_en)
        _psk_en_check_box.stateChanged.connect(lambda i: self.set_psk_en(self._psk_en_choices[bool(i)]))
        self.top_grid_layout.addWidget(_psk_en_check_box, 0, 2, 1, 1)
        for r in range(0, 1):
            self.top_grid_layout.setRowStretch(r, 1)
        for c in range(2, 3):
            self.top_grid_layout.setColumnStretch(c, 1)
        self._psk_BW_tool_bar = Qt.QToolBar(self)
        self._psk_BW_tool_bar.addWidget(Qt.QLabel('Excess BW' + ": "))
        self._psk_BW_line_edit = Qt.QLineEdit(str(self.psk_BW))
        self._psk_BW_tool_bar.addWidget(self._psk_BW_line_edit)
        self._psk_BW_line_edit.returnPressed.connect(
            lambda: self.set_psk_BW(eng_notation.str_to_num(str(self._psk_BW_line_edit.text()))))
        self.tab_id_grid_layout_3.addWidget(self._psk_BW_tool_bar, 3, 0, 1, 5)
        for r in range(3, 4):
            self.tab_id_grid_layout_3.setRowStretch(r, 1)
        for c in range(0, 5):
            self.tab_id_grid_layout_3.setColumnStretch(c, 1)
        self._gmsk_samp_tool_bar = Qt.QToolBar(self)
        self._gmsk_samp_tool_bar.addWidget(Qt.QLabel('Samples Per Symbol' + ": "))
        self._gmsk_samp_line_edit = Qt.QLineEdit(str(self.gmsk_samp))
        self._gmsk_samp_tool_bar.addWidget(self._gmsk_samp_line_edit)
        self._gmsk_samp_line_edit.returnPressed.connect(
            lambda: self.set_gmsk_samp(int(str(self._gmsk_samp_line_edit.text()))))
        self.tab_id_grid_layout_1.addWidget(self._gmsk_samp_tool_bar, 1, 0, 1, 5)
        for r in range(1, 2):
            self.tab_id_grid_layout_1.setRowStretch(r, 1)
        for c in range(0, 5):
            self.tab_id_grid_layout_1.setColumnStretch(c, 1)
        _gmsk_en_check_box = Qt.QCheckBox('GMSK')
        self._gmsk_en_choices = {True: 1, False: 0}
        self._gmsk_en_choices_inv = dict((v,k) for k,v in self._gmsk_en_choices.items())
        self._gmsk_en_callback = lambda i: Qt.QMetaObject.invokeMethod(_gmsk_en_check_box, "setChecked", Qt.Q_ARG("bool", self._gmsk_en_choices_inv[i]))
        self._gmsk_en_callback(self.gmsk_en)
        _gmsk_en_check_box.stateChanged.connect(lambda i: self.set_gmsk_en(self._gmsk_en_choices[bool(i)]))
        self.top_grid_layout.addWidget(_gmsk_en_check_box, 0, 0, 1, 1)
        for r in range(0, 1):
            self.top_grid_layout.setRowStretch(r, 1)
        for c in range(0, 1):
            self.top_grid_layout.setColumnStretch(c, 1)
        self._gmsk_BT_tool_bar = Qt.QToolBar(self)
        self._gmsk_BT_tool_bar.addWidget(Qt.QLabel('BT' + ": "))
        self._gmsk_BT_line_edit = Qt.QLineEdit(str(self.gmsk_BT))
        self._gmsk_BT_tool_bar.addWidget(self._gmsk_BT_line_edit)
        self._gmsk_BT_line_edit.returnPressed.connect(
            lambda: self.set_gmsk_BT(eng_notation.str_to_num(str(self._gmsk_BT_line_edit.text()))))
        self.tab_id_grid_layout_1.addWidget(self._gmsk_BT_tool_bar, 2, 0, 1, 5)
        for r in range(2, 3):
            self.tab_id_grid_layout_1.setRowStretch(r, 1)
        for c in range(0, 5):
            self.tab_id_grid_layout_1.setColumnStretch(c, 1)
        _gfsk_en_check_box = Qt.QCheckBox('GFSK')
        self._gfsk_en_choices = {True: 1, False: 0}
        self._gfsk_en_choices_inv = dict((v,k) for k,v in self._gfsk_en_choices.items())
        self._gfsk_en_callback = lambda i: Qt.QMetaObject.invokeMethod(_gfsk_en_check_box, "setChecked", Qt.Q_ARG("bool", self._gfsk_en_choices_inv[i]))
        self._gfsk_en_callback(self.gfsk_en)
        _gfsk_en_check_box.stateChanged.connect(lambda i: self.set_gfsk_en(self._gfsk_en_choices[bool(i)]))
        self.top_grid_layout.addWidget(_gfsk_en_check_box, 0, 1, 1, 1)
        for r in range(0, 1):
            self.top_grid_layout.setRowStretch(r, 1)
        for c in range(1, 2):
            self.top_grid_layout.setColumnStretch(c, 1)
        self._cpm_spsym_tool_bar = Qt.QToolBar(self)
        self._cpm_spsym_tool_bar.addWidget(Qt.QLabel('Samples Per Symbol' + ": "))
        self._cpm_spsym_line_edit = Qt.QLineEdit(str(self.cpm_spsym))
        self._cpm_spsym_tool_bar.addWidget(self._cpm_spsym_line_edit)
        self._cpm_spsym_line_edit.returnPressed.connect(
            lambda: self.set_cpm_spsym(int(str(self._cpm_spsym_line_edit.text()))))
        self.tab_id_grid_layout_5.addWidget(self._cpm_spsym_tool_bar, 2, 0, 1, 5)
        for r in range(2, 3):
            self.tab_id_grid_layout_5.setRowStretch(r, 1)
        for c in range(0, 5):
            self.tab_id_grid_layout_5.setColumnStretch(c, 1)
        self._cpm_pulse_duration_tool_bar = Qt.QToolBar(self)
        self._cpm_pulse_duration_tool_bar.addWidget(Qt.QLabel('Pulse Duration' + ": "))
        self._cpm_pulse_duration_line_edit = Qt.QLineEdit(str(self.cpm_pulse_duration))
        self._cpm_pulse_duration_tool_bar.addWidget(self._cpm_pulse_duration_line_edit)
        self._cpm_pulse_duration_line_edit.returnPressed.connect(
            lambda: self.set_cpm_pulse_duration(int(str(self._cpm_pulse_duration_line_edit.text()))))
        self.tab_id_grid_layout_5.addWidget(self._cpm_pulse_duration_tool_bar, 3, 0, 1, 5)
        for r in range(3, 4):
            self.tab_id_grid_layout_5.setRowStretch(r, 1)
        for c in range(0, 5):
            self.tab_id_grid_layout_5.setColumnStretch(c, 1)
        self._cpm_mod_index_tool_bar = Qt.QToolBar(self)
        self._cpm_mod_index_tool_bar.addWidget(Qt.QLabel('Modulation Index' + ": "))
        self._cpm_mod_index_line_edit = Qt.QLineEdit(str(self.cpm_mod_index))
        self._cpm_mod_index_tool_bar.addWidget(self._cpm_mod_index_line_edit)
        self._cpm_mod_index_line_edit.returnPressed.connect(
            lambda: self.set_cpm_mod_index(eng_notation.str_to_num(str(self._cpm_mod_index_line_edit.text()))))
        self.tab_id_grid_layout_5.addWidget(self._cpm_mod_index_tool_bar, 1, 0, 1, 5)
        for r in range(1, 2):
            self.tab_id_grid_layout_5.setRowStretch(r, 1)
        for c in range(0, 5):
            self.tab_id_grid_layout_5.setColumnStretch(c, 1)
        _cpm_en_check_box = Qt.QCheckBox('CPM')
        self._cpm_en_choices = {True: 1, False: 0}
        self._cpm_en_choices_inv = dict((v,k) for k,v in self._cpm_en_choices.items())
        self._cpm_en_callback = lambda i: Qt.QMetaObject.invokeMethod(_cpm_en_check_box, "setChecked", Qt.Q_ARG("bool", self._cpm_en_choices_inv[i]))
        self._cpm_en_callback(self.cpm_en)
        _cpm_en_check_box.stateChanged.connect(lambda i: self.set_cpm_en(self._cpm_en_choices[bool(i)]))
        self.top_grid_layout.addWidget(_cpm_en_check_box, 0, 4, 1, 1)
        for r in range(0, 1):
            self.top_grid_layout.setRowStretch(r, 1)
        for c in range(4, 5):
            self.top_grid_layout.setColumnStretch(c, 1)
        self._cpm_BT_tool_bar = Qt.QToolBar(self)
        self._cpm_BT_tool_bar.addWidget(Qt.QLabel('BT' + ": "))
        self._cpm_BT_line_edit = Qt.QLineEdit(str(self.cpm_BT))
        self._cpm_BT_tool_bar.addWidget(self._cpm_BT_line_edit)
        self._cpm_BT_line_edit.returnPressed.connect(
            lambda: self.set_cpm_BT(eng_notation.str_to_num(str(self._cpm_BT_line_edit.text()))))
        self.tab_id_grid_layout_5.addWidget(self._cpm_BT_tool_bar, 4, 0, 1, 5)
        for r in range(4, 5):
            self.tab_id_grid_layout_5.setRowStretch(r, 1)
        for c in range(0, 5):
            self.tab_id_grid_layout_5.setColumnStretch(c, 1)
        self._txpower_tool_bar = Qt.QToolBar(self)
        self._txpower_tool_bar.addWidget(Qt.QLabel('TX Power (0-1)' + ": "))
        self._txpower_line_edit = Qt.QLineEdit(str(self.txpower))
        self._txpower_tool_bar.addWidget(self._txpower_line_edit)
        self._txpower_line_edit.returnPressed.connect(
            lambda: self.set_txpower(eng_notation.str_to_num(str(self._txpower_line_edit.text()))))
        self.top_grid_layout.addWidget(self._txpower_tool_bar, 5, 0, 1, 5)
        for r in range(5, 6):
            self.top_grid_layout.setRowStretch(r, 1)
        for c in range(0, 5):
            self.top_grid_layout.setColumnStretch(c, 1)
        self._samp_rate_tool_bar = Qt.QToolBar(self)
        self._samp_rate_tool_bar.addWidget(Qt.QLabel('Sample Rate (sps)' + ": "))
        self._samp_rate_line_edit = Qt.QLineEdit(str(self.samp_rate))
        self._samp_rate_tool_bar.addWidget(self._samp_rate_line_edit)
        self._samp_rate_line_edit.returnPressed.connect(
            lambda: self.set_samp_rate(eng_notation.str_to_num(str(self._samp_rate_line_edit.text()))))
        self.top_grid_layout.addWidget(self._samp_rate_tool_bar, 1, 0, 1, 5)
        for r in range(1, 2):
            self.top_grid_layout.setRowStretch(r, 1)
        for c in range(0, 5):
            self.top_grid_layout.setColumnStretch(c, 1)
        self.qtgui_const_sink_x_0_0 = qtgui.const_sink_c(
            1024, #size
            "", #name
            1 #number of inputs
        )
        self.qtgui_const_sink_x_0_0.set_update_time(0.10)
        self.qtgui_const_sink_x_0_0.set_y_axis(-2, 2)
        self.qtgui_const_sink_x_0_0.set_x_axis(-2, 2)
        self.qtgui_const_sink_x_0_0.set_trigger_mode(qtgui.TRIG_MODE_FREE, qtgui.TRIG_SLOPE_POS, 0.0, 0, "")
        self.qtgui_const_sink_x_0_0.enable_autoscale(False)
        self.qtgui_const_sink_x_0_0.enable_grid(False)
        self.qtgui_const_sink_x_0_0.enable_axis_labels(True)


        labels = ['', '', '', '', '',
            '', '', '', '', '']
        widths = [1, 1, 1, 1, 1,
            1, 1, 1, 1, 1]
        colors = ["blue", "red", "red", "red", "red",
            "red", "red", "red", "red", "red"]
        styles = [0, 0, 0, 0, 0,
            0, 0, 0, 0, 0]
        markers = [0, 0, 0, 0, 0,
            0, 0, 0, 0, 0]
        alphas = [1.0, 1.0, 1.0, 1.0, 1.0,
            1.0, 1.0, 1.0, 1.0, 1.0]

        for i in range(1):
            if len(labels[i]) == 0:
                self.qtgui_const_sink_x_0_0.set_line_label(i, "Data {0}".format(i))
            else:
                self.qtgui_const_sink_x_0_0.set_line_label(i, labels[i])
            self.qtgui_const_sink_x_0_0.set_line_width(i, widths[i])
            self.qtgui_const_sink_x_0_0.set_line_color(i, colors[i])
            self.qtgui_const_sink_x_0_0.set_line_style(i, styles[i])
            self.qtgui_const_sink_x_0_0.set_line_marker(i, markers[i])
            self.qtgui_const_sink_x_0_0.set_line_alpha(i, alphas[i])

        self._qtgui_const_sink_x_0_0_win = sip.wrapinstance(self.qtgui_const_sink_x_0_0.pyqwidget(), Qt.QWidget)
        self.top_grid_layout.addWidget(self._qtgui_const_sink_x_0_0_win, 7, 0, 3, 3)
        for r in range(7, 10):
            self.top_grid_layout.setRowStretch(r, 1)
        for c in range(0, 3):
            self.top_grid_layout.setColumnStretch(c, 1)
        self.digital_psk_mod_0 = digital.psk.psk_mod(
            constellation_points=psk_num,
            mod_code="none",
            differential=True,
            samples_per_symbol=psk_samp_per_symb,
            excess_bw=psk_BW,
            verbose=False,
            log=False)
        self.digital_gmsk_mod_0 = digital.gmsk_mod(
            samples_per_symbol=gmsk_samp,
            bt=gmsk_BT,
            verbose=False,
            log=False)
        self.digital_gfsk_mod_0 = digital.gfsk_mod(
            samples_per_symbol=2,
            sensitivity=1.0,
            bt=0.35,
            verbose=False,
            log=False)
        self.digital_cpmmod_bc_0 = digital.cpmmod_bc(analog.cpm.LREC, cpm_mod_index, cpm_spsym, cpm_pulse_duration, cpm_BT)
        self.digital_constellation_modulator_0 = digital.generic_mod(
            constellation=variable_constellation_0,
            differential=True,
            samples_per_symbol=qam_samp_per_symb,
            pre_diff_code=True,
            excess_bw=qam_BW,
            verbose=False,
            log=False)
        self.blocks_multiply_xx_0_1 = blocks.multiply_vcc(1)
        self.blocks_multiply_xx_0_0_1 = blocks.multiply_vcc(1)
        self.blocks_multiply_xx_0_0_0_0 = blocks.multiply_vcc(1)
        self.blocks_multiply_xx_0_0_0 = blocks.multiply_vcc(1)
        self.blocks_multiply_xx_0 = blocks.multiply_vcc(1)
        self.blocks_add_xx_0 = blocks.add_vcc(1)
        self._bandwidth_tool_bar = Qt.QToolBar(self)
        self._bandwidth_tool_bar.addWidget(Qt.QLabel('Bandwidth (Hz)' + ": "))
        self._bandwidth_line_edit = Qt.QLineEdit(str(self.bandwidth))
        self._bandwidth_tool_bar.addWidget(self._bandwidth_line_edit)
        self._bandwidth_line_edit.returnPressed.connect(
            lambda: self.set_bandwidth(eng_notation.str_to_num(str(self._bandwidth_line_edit.text()))))
        self.top_grid_layout.addWidget(self._bandwidth_tool_bar, 2, 0, 1, 5)
        for r in range(2, 3):
            self.top_grid_layout.setRowStretch(r, 1)
        for c in range(0, 5):
            self.top_grid_layout.setColumnStretch(c, 1)
        self.analog_random_source_x_0_0_0_0_0_0 = blocks.vector_source_b(list(map(int, numpy.random.randint(0, 255, 1000))), True)
        self.analog_random_source_x_0_0_0_0_0 = blocks.vector_source_b(list(map(int, numpy.random.randint(0, 255, 1000))), True)
        self.analog_random_source_x_0_0_0_0 = blocks.vector_source_b(list(map(int, numpy.random.randint(0, 255, 1000))), True)
        self.analog_random_source_x_0_0_0 = blocks.vector_source_b(list(map(int, numpy.random.randint(0, 255, 1000))), True)
        self.analog_random_source_x_0 = blocks.vector_source_b(list(map(int, numpy.random.randint(0, 255, 1000))), True)
        self.analog_const_source_x_0_0_0_0_0_0_0_0 = analog.sig_source_c(0, analog.GR_CONST_WAVE, 0, 0, cpm_en)
        self.analog_const_source_x_0_0_0_0_0_0_0 = analog.sig_source_c(0, analog.GR_CONST_WAVE, 0, 0, psk_en)
        self.analog_const_source_x_0_0_0_0 = analog.sig_source_c(0, analog.GR_CONST_WAVE, 0, 0, qam_en)
        self.analog_const_source_x_0_0_0 = analog.sig_source_c(0, analog.GR_CONST_WAVE, 0, 0, gfsk_en)
        self.analog_const_source_x_0 = analog.sig_source_c(0, analog.GR_CONST_WAVE, 0, 0, gmsk_en)
        self._CenterFreq_tool_bar = Qt.QToolBar(self)
        self._CenterFreq_tool_bar.addWidget(Qt.QLabel('Center Frequency (Hz)' + ": "))
        self._CenterFreq_line_edit = Qt.QLineEdit(str(self.CenterFreq))
        self._CenterFreq_tool_bar.addWidget(self._CenterFreq_line_edit)
        self._CenterFreq_line_edit.returnPressed.connect(
            lambda: self.set_CenterFreq(eng_notation.str_to_num(str(self._CenterFreq_line_edit.text()))))
        self.top_grid_layout.addWidget(self._CenterFreq_tool_bar, 3, 0, 1, 5)
        for r in range(3, 4):
            self.top_grid_layout.setRowStretch(r, 1)
        for c in range(0, 5):
            self.top_grid_layout.setColumnStretch(c, 1)



        ##################################################
        # Connections
        ##################################################
        self.connect((self.analog_const_source_x_0, 0), (self.blocks_multiply_xx_0, 0))
        self.connect((self.analog_const_source_x_0_0_0, 0), (self.blocks_multiply_xx_0_0_0, 0))
        self.connect((self.analog_const_source_x_0_0_0_0, 0), (self.blocks_multiply_xx_0_1, 0))
        self.connect((self.analog_const_source_x_0_0_0_0_0_0_0, 0), (self.blocks_multiply_xx_0_0_1, 0))
        self.connect((self.analog_const_source_x_0_0_0_0_0_0_0_0, 0), (self.blocks_multiply_xx_0_0_0_0, 0))
        self.connect((self.analog_random_source_x_0, 0), (self.digital_gmsk_mod_0, 0))
        self.connect((self.analog_random_source_x_0_0_0, 0), (self.digital_gfsk_mod_0, 0))
        self.connect((self.analog_random_source_x_0_0_0_0, 0), (self.digital_constellation_modulator_0, 0))
        self.connect((self.analog_random_source_x_0_0_0_0_0, 0), (self.digital_cpmmod_bc_0, 0))
        self.connect((self.analog_random_source_x_0_0_0_0_0_0, 0), (self.digital_psk_mod_0, 0))
        self.connect((self.blocks_add_xx_0, 0), (self.qtgui_const_sink_x_0_0, 0))
        self.connect((self.blocks_multiply_xx_0, 0), (self.blocks_add_xx_0, 0))
        self.connect((self.blocks_multiply_xx_0_0_0, 0), (self.blocks_add_xx_0, 2))
        self.connect((self.blocks_multiply_xx_0_0_0_0, 0), (self.blocks_add_xx_0, 1))
        self.connect((self.blocks_multiply_xx_0_0_1, 0), (self.blocks_add_xx_0, 4))
        self.connect((self.blocks_multiply_xx_0_1, 0), (self.blocks_add_xx_0, 3))
        self.connect((self.digital_constellation_modulator_0, 0), (self.blocks_multiply_xx_0_1, 1))
        self.connect((self.digital_cpmmod_bc_0, 0), (self.blocks_multiply_xx_0_0_0_0, 1))
        self.connect((self.digital_gfsk_mod_0, 0), (self.blocks_multiply_xx_0_0_0, 1))
        self.connect((self.digital_gmsk_mod_0, 0), (self.blocks_multiply_xx_0, 1))
        self.connect((self.digital_psk_mod_0, 0), (self.blocks_multiply_xx_0_0_1, 1))

    def closeEvent(self, event):
        self.settings = Qt.QSettings("GNU Radio", "PanTX_betaA")
        self.settings.setValue("geometry", self.saveGeometry())
        event.accept()

    def get_variable_constellation_0(self):
        return self.variable_constellation_0

    def set_variable_constellation_0(self, variable_constellation_0):
        self.variable_constellation_0 = variable_constellation_0

    def get_txpower(self):
        return self.txpower

    def set_txpower(self, txpower):
        self.txpower = txpower
        Qt.QMetaObject.invokeMethod(self._txpower_line_edit, "setText", Qt.Q_ARG("QString", eng_notation.num_to_str(self.txpower)))

    def get_samp_rate(self):
        return self.samp_rate

    def set_samp_rate(self, samp_rate):
        self.samp_rate = samp_rate
        Qt.QMetaObject.invokeMethod(self._samp_rate_line_edit, "setText", Qt.Q_ARG("QString", eng_notation.num_to_str(self.samp_rate)))

    def get_qam_samp_per_symb(self):
        return self.qam_samp_per_symb

    def set_qam_samp_per_symb(self, qam_samp_per_symb):
        self.qam_samp_per_symb = qam_samp_per_symb
        Qt.QMetaObject.invokeMethod(self._qam_samp_per_symb_line_edit, "setText", Qt.Q_ARG("QString", str(self.qam_samp_per_symb)))

    def get_qam_en(self):
        return self.qam_en

    def set_qam_en(self, qam_en):
        self.qam_en = qam_en
        self._qam_en_callback(self.qam_en)
        self.analog_const_source_x_0_0_0_0.set_offset(self.qam_en)

    def get_qam_BW(self):
        return self.qam_BW

    def set_qam_BW(self, qam_BW):
        self.qam_BW = qam_BW
        Qt.QMetaObject.invokeMethod(self._qam_BW_line_edit, "setText", Qt.Q_ARG("QString", eng_notation.num_to_str(self.qam_BW)))

    def get_psk_samp_per_symb(self):
        return self.psk_samp_per_symb

    def set_psk_samp_per_symb(self, psk_samp_per_symb):
        self.psk_samp_per_symb = psk_samp_per_symb
        Qt.QMetaObject.invokeMethod(self._psk_samp_per_symb_line_edit, "setText", Qt.Q_ARG("QString", str(self.psk_samp_per_symb)))

    def get_psk_num(self):
        return self.psk_num

    def set_psk_num(self, psk_num):
        self.psk_num = psk_num
        Qt.QMetaObject.invokeMethod(self._psk_num_line_edit, "setText", Qt.Q_ARG("QString", str(self.psk_num)))

    def get_psk_en(self):
        return self.psk_en

    def set_psk_en(self, psk_en):
        self.psk_en = psk_en
        self._psk_en_callback(self.psk_en)
        self.analog_const_source_x_0_0_0_0_0_0_0.set_offset(self.psk_en)

    def get_psk_BW(self):
        return self.psk_BW

    def set_psk_BW(self, psk_BW):
        self.psk_BW = psk_BW
        Qt.QMetaObject.invokeMethod(self._psk_BW_line_edit, "setText", Qt.Q_ARG("QString", eng_notation.num_to_str(self.psk_BW)))

    def get_gmsk_samp(self):
        return self.gmsk_samp

    def set_gmsk_samp(self, gmsk_samp):
        self.gmsk_samp = gmsk_samp
        Qt.QMetaObject.invokeMethod(self._gmsk_samp_line_edit, "setText", Qt.Q_ARG("QString", str(self.gmsk_samp)))

    def get_gmsk_en(self):
        return self.gmsk_en

    def set_gmsk_en(self, gmsk_en):
        self.gmsk_en = gmsk_en
        self._gmsk_en_callback(self.gmsk_en)
        self.analog_const_source_x_0.set_offset(self.gmsk_en)

    def get_gmsk_BT(self):
        return self.gmsk_BT

    def set_gmsk_BT(self, gmsk_BT):
        self.gmsk_BT = gmsk_BT
        Qt.QMetaObject.invokeMethod(self._gmsk_BT_line_edit, "setText", Qt.Q_ARG("QString", eng_notation.num_to_str(self.gmsk_BT)))

    def get_gfsk_en(self):
        return self.gfsk_en

    def set_gfsk_en(self, gfsk_en):
        self.gfsk_en = gfsk_en
        self._gfsk_en_callback(self.gfsk_en)
        self.analog_const_source_x_0_0_0.set_offset(self.gfsk_en)

    def get_cpm_spsym(self):
        return self.cpm_spsym

    def set_cpm_spsym(self, cpm_spsym):
        self.cpm_spsym = cpm_spsym
        Qt.QMetaObject.invokeMethod(self._cpm_spsym_line_edit, "setText", Qt.Q_ARG("QString", str(self.cpm_spsym)))

    def get_cpm_pulse_duration(self):
        return self.cpm_pulse_duration

    def set_cpm_pulse_duration(self, cpm_pulse_duration):
        self.cpm_pulse_duration = cpm_pulse_duration
        Qt.QMetaObject.invokeMethod(self._cpm_pulse_duration_line_edit, "setText", Qt.Q_ARG("QString", str(self.cpm_pulse_duration)))

    def get_cpm_mod_index(self):
        return self.cpm_mod_index

    def set_cpm_mod_index(self, cpm_mod_index):
        self.cpm_mod_index = cpm_mod_index
        Qt.QMetaObject.invokeMethod(self._cpm_mod_index_line_edit, "setText", Qt.Q_ARG("QString", eng_notation.num_to_str(self.cpm_mod_index)))

    def get_cpm_en(self):
        return self.cpm_en

    def set_cpm_en(self, cpm_en):
        self.cpm_en = cpm_en
        self._cpm_en_callback(self.cpm_en)
        self.analog_const_source_x_0_0_0_0_0_0_0_0.set_offset(self.cpm_en)

    def get_cpm_BT(self):
        return self.cpm_BT

    def set_cpm_BT(self, cpm_BT):
        self.cpm_BT = cpm_BT
        Qt.QMetaObject.invokeMethod(self._cpm_BT_line_edit, "setText", Qt.Q_ARG("QString", eng_notation.num_to_str(self.cpm_BT)))

    def get_bandwidth(self):
        return self.bandwidth

    def set_bandwidth(self, bandwidth):
        self.bandwidth = bandwidth
        Qt.QMetaObject.invokeMethod(self._bandwidth_line_edit, "setText", Qt.Q_ARG("QString", eng_notation.num_to_str(self.bandwidth)))

    def get_CenterFreq(self):
        return self.CenterFreq

    def set_CenterFreq(self, CenterFreq):
        self.CenterFreq = CenterFreq
        Qt.QMetaObject.invokeMethod(self._CenterFreq_line_edit, "setText", Qt.Q_ARG("QString", eng_notation.num_to_str(self.CenterFreq)))



def main(top_block_cls=PanTX_betaA, options=None):

    if StrictVersion("4.5.0") <= StrictVersion(Qt.qVersion()) < StrictVersion("5.0.0"):
        style = gr.prefs().get_string('qtgui', 'style', 'raster')
        Qt.QApplication.setGraphicsSystem(style)
    qapp = Qt.QApplication(sys.argv)

    tb = top_block_cls()
    tb.start()
    tb.show()

    def sig_handler(sig=None, frame=None):
        Qt.QApplication.quit()

    signal.signal(signal.SIGINT, sig_handler)
    signal.signal(signal.SIGTERM, sig_handler)

    timer = Qt.QTimer()
    timer.start(500)
    timer.timeout.connect(lambda: None)

    def quitting():
        tb.stop()
        tb.wait()
    qapp.aboutToQuit.connect(quitting)
    qapp.exec_()


if __name__ == '__main__':
    main()
