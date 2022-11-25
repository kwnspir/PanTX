#!/usr/bin/env python3
# -*- coding: utf-8 -*-

#
# SPDX-License-Identifier: GPL-3.0
#
# GNU Radio Python Flow Graph
# Title: PanTX_betaE
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
from gnuradio import blocks
import numpy
from gnuradio import digital
from gnuradio import gr
from gnuradio.filter import firdes
import sys
import signal
from argparse import ArgumentParser
from gnuradio.eng_arg import eng_float, intx
from gnuradio import qtgui

class PanTX_betaE(gr.top_block, Qt.QWidget):

    def __init__(self):
        gr.top_block.__init__(self, "PanTX_betaE")
        Qt.QWidget.__init__(self)
        self.setWindowTitle("PanTX_betaE")
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

        self.settings = Qt.QSettings("GNU Radio", "PanTX_betaE")

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
        self.txpower = txpower = 0.1
        self.samp_rate = samp_rate = 4e6
        self.plt_smbl = plt_smbl = ((-1,1,-1,1),)
        self.plt_carr = plt_carr = ((-6,-5,5,6),)
        self.packet_len = packet_len = 100
        self.occ_carr = occ_carr = ((-4,-3,-2,-1,1,2,3,4),)
        self.fft_len = fft_len = 8
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
        self.tab_id.addTab(self.tab_id_widget_1, 'OFDM')
        self.top_grid_layout.addWidget(self.tab_id, 6, 0, 1, 5)
        for r in range(6, 7):
            self.top_grid_layout.setRowStretch(r, 1)
        for c in range(0, 5):
            self.top_grid_layout.setColumnStretch(c, 1)
        self._plt_smbl_tool_bar = Qt.QToolBar(self)
        self._plt_smbl_tool_bar.addWidget(Qt.QLabel('Pilot symbols' + ": "))
        self._plt_smbl_line_edit = Qt.QLineEdit(str(self.plt_smbl))
        self._plt_smbl_tool_bar.addWidget(self._plt_smbl_line_edit)
        self._plt_smbl_line_edit.returnPressed.connect(
            lambda: self.set_plt_smbl(eval(str(self._plt_smbl_line_edit.text()))))
        self.tab_id_grid_layout_1.addWidget(self._plt_smbl_tool_bar, 5, 0, 1, 5)
        for r in range(5, 6):
            self.tab_id_grid_layout_1.setRowStretch(r, 1)
        for c in range(0, 5):
            self.tab_id_grid_layout_1.setColumnStretch(c, 1)
        self._plt_carr_tool_bar = Qt.QToolBar(self)
        self._plt_carr_tool_bar.addWidget(Qt.QLabel('Pilot carriers' + ": "))
        self._plt_carr_line_edit = Qt.QLineEdit(str(self.plt_carr))
        self._plt_carr_tool_bar.addWidget(self._plt_carr_line_edit)
        self._plt_carr_line_edit.returnPressed.connect(
            lambda: self.set_plt_carr(eval(str(self._plt_carr_line_edit.text()))))
        self.tab_id_grid_layout_1.addWidget(self._plt_carr_tool_bar, 4, 0, 1, 5)
        for r in range(4, 5):
            self.tab_id_grid_layout_1.setRowStretch(r, 1)
        for c in range(0, 5):
            self.tab_id_grid_layout_1.setColumnStretch(c, 1)
        self._packet_len_tool_bar = Qt.QToolBar(self)
        self._packet_len_tool_bar.addWidget(Qt.QLabel('Packet Length' + ": "))
        self._packet_len_line_edit = Qt.QLineEdit(str(self.packet_len))
        self._packet_len_tool_bar.addWidget(self._packet_len_line_edit)
        self._packet_len_line_edit.returnPressed.connect(
            lambda: self.set_packet_len(int(str(self._packet_len_line_edit.text()))))
        self.tab_id_grid_layout_1.addWidget(self._packet_len_tool_bar, 2, 0, 1, 5)
        for r in range(2, 3):
            self.tab_id_grid_layout_1.setRowStretch(r, 1)
        for c in range(0, 5):
            self.tab_id_grid_layout_1.setColumnStretch(c, 1)
        self._occ_carr_tool_bar = Qt.QToolBar(self)
        self._occ_carr_tool_bar.addWidget(Qt.QLabel('Occupied carriers' + ": "))
        self._occ_carr_line_edit = Qt.QLineEdit(str(self.occ_carr))
        self._occ_carr_tool_bar.addWidget(self._occ_carr_line_edit)
        self._occ_carr_line_edit.returnPressed.connect(
            lambda: self.set_occ_carr(eval(str(self._occ_carr_line_edit.text()))))
        self.tab_id_grid_layout_1.addWidget(self._occ_carr_tool_bar, 3, 0, 1, 5)
        for r in range(3, 4):
            self.tab_id_grid_layout_1.setRowStretch(r, 1)
        for c in range(0, 5):
            self.tab_id_grid_layout_1.setColumnStretch(c, 1)
        self._fft_len_tool_bar = Qt.QToolBar(self)
        self._fft_len_tool_bar.addWidget(Qt.QLabel('FFT' + ": "))
        self._fft_len_line_edit = Qt.QLineEdit(str(self.fft_len))
        self._fft_len_tool_bar.addWidget(self._fft_len_line_edit)
        self._fft_len_line_edit.returnPressed.connect(
            lambda: self.set_fft_len(int(str(self._fft_len_line_edit.text()))))
        self.tab_id_grid_layout_1.addWidget(self._fft_len_tool_bar, 1, 0, 1, 5)
        for r in range(1, 2):
            self.tab_id_grid_layout_1.setRowStretch(r, 1)
        for c in range(0, 5):
            self.tab_id_grid_layout_1.setColumnStretch(c, 1)
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
        self.digital_ofdm_tx_0_0_0 = digital.ofdm_tx(
            fft_len=fft_len,
            cp_len=1,
            packet_length_tag_key='len_tag_key',
            occupied_carriers=occ_carr,
            pilot_carriers=plt_carr,
            pilot_symbols=plt_smbl,
            sync_word1=None,
            sync_word2=None,
            bps_header=2,
            bps_payload=1,
            rolloff=0,
            debug_log=False,
            scramble_bits=False)
        self.blocks_stream_to_tagged_stream_0 = blocks.stream_to_tagged_stream(gr.sizeof_char, 1, packet_len, 'len_tag_key')
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
        self.analog_random_source_x_0_0 = blocks.vector_source_b(list(map(int, numpy.random.randint(0, 255, 1000))), True)
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
        self.connect((self.analog_random_source_x_0_0, 0), (self.blocks_stream_to_tagged_stream_0, 0))
        self.connect((self.blocks_stream_to_tagged_stream_0, 0), (self.digital_ofdm_tx_0_0_0, 0))
        self.connect((self.digital_ofdm_tx_0_0_0, 0), (self.qtgui_const_sink_x_0_0, 0))

    def closeEvent(self, event):
        self.settings = Qt.QSettings("GNU Radio", "PanTX_betaE")
        self.settings.setValue("geometry", self.saveGeometry())
        event.accept()

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

    def get_plt_smbl(self):
        return self.plt_smbl

    def set_plt_smbl(self, plt_smbl):
        self.plt_smbl = plt_smbl
        Qt.QMetaObject.invokeMethod(self._plt_smbl_line_edit, "setText", Qt.Q_ARG("QString", repr(self.plt_smbl)))

    def get_plt_carr(self):
        return self.plt_carr

    def set_plt_carr(self, plt_carr):
        self.plt_carr = plt_carr
        Qt.QMetaObject.invokeMethod(self._plt_carr_line_edit, "setText", Qt.Q_ARG("QString", repr(self.plt_carr)))

    def get_packet_len(self):
        return self.packet_len

    def set_packet_len(self, packet_len):
        self.packet_len = packet_len
        Qt.QMetaObject.invokeMethod(self._packet_len_line_edit, "setText", Qt.Q_ARG("QString", str(self.packet_len)))
        self.blocks_stream_to_tagged_stream_0.set_packet_len(self.packet_len)
        self.blocks_stream_to_tagged_stream_0.set_packet_len_pmt(self.packet_len)

    def get_occ_carr(self):
        return self.occ_carr

    def set_occ_carr(self, occ_carr):
        self.occ_carr = occ_carr
        Qt.QMetaObject.invokeMethod(self._occ_carr_line_edit, "setText", Qt.Q_ARG("QString", repr(self.occ_carr)))

    def get_fft_len(self):
        return self.fft_len

    def set_fft_len(self, fft_len):
        self.fft_len = fft_len
        Qt.QMetaObject.invokeMethod(self._fft_len_line_edit, "setText", Qt.Q_ARG("QString", str(self.fft_len)))

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



def main(top_block_cls=PanTX_betaE, options=None):

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
