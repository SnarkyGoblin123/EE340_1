#!/usr/bin/env python3
# -*- coding: utf-8 -*-

#
# SPDX-License-Identifier: GPL-3.0
#
# GNU Radio Python Flow Graph
# Title: Not titled yet
# Author: rohannafde
# GNU Radio version: 3.10.1.1

from packaging.version import Version as StrictVersion

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
from gnuradio import qtgui
import sip
from gnuradio import analog
from gnuradio import blocks
import pmt
from gnuradio import digital
from gnuradio import filter
from gnuradio.filter import firdes
from gnuradio import gr
from gnuradio.fft import window
import sys
import signal
from argparse import ArgumentParser
from gnuradio.eng_arg import eng_float, intx
from gnuradio import eng_notation
from gnuradio import zeromq
from gnuradio.qtgui import Range, RangeWidget
from PyQt5 import QtCore



from gnuradio import qtgui

class task6(gr.top_block, Qt.QWidget):

    def __init__(self):
        gr.top_block.__init__(self, "Not titled yet", catch_exceptions=True)
        Qt.QWidget.__init__(self)
        self.setWindowTitle("Not titled yet")
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

        self.settings = Qt.QSettings("GNU Radio", "task6")

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
        self.variable_constellation_0 = variable_constellation_0 = digital.constellation_calcdist([-1.41421, -1+1j, 1.41421*1j, 1+1j, 1.41421, 1-1j, -1.41421*1j, -1-1j], [0, 1, 2, 3, 4, 5, 6, 7],
        4, 1, digital.constellation.AMPLITUDE_NORMALIZATION).base()
        self.samp_rate = samp_rate = 400000
        self.amp = amp = 0
        self.alpha = alpha = 1

        ##################################################
        # Blocks
        ##################################################
        self._amp_range = Range(0, 1, 0.01, 0, 200)
        self._amp_win = RangeWidget(self._amp_range, self.set_amp, "'amp'", "counter_slider", float, QtCore.Qt.Horizontal)
        self.top_layout.addWidget(self._amp_win)
        self._alpha_range = Range(0, 1, 0.01, 1, 200)
        self._alpha_win = RangeWidget(self._alpha_range, self.set_alpha, "'alpha'", "counter_slider", float, QtCore.Qt.Horizontal)
        self.top_layout.addWidget(self._alpha_win)
        self.zeromq_push_sink_0 = zeromq.push_sink(gr.sizeof_gr_complex, 1, 'tcp://127.0.0.1:50001', 100, False, -1)
        self.zeromq_pull_source_0 = zeromq.pull_source(gr.sizeof_gr_complex, 1, 'tcp://127.0.0.1:50001', 100, False, -1)
        self.root_raised_cosine_filter_0_1_1 = filter.fir_filter_fff(
            1,
            firdes.root_raised_cosine(
                3,
                samp_rate,
                50000,
                alpha,
                88))
        self.root_raised_cosine_filter_0_1_0 = filter.fir_filter_fff(
            1,
            firdes.root_raised_cosine(
                3,
                samp_rate,
                50000,
                alpha,
                88))
        self.root_raised_cosine_filter_0_1 = filter.interp_fir_filter_ccf(
            1,
            firdes.root_raised_cosine(
                3,
                samp_rate,
                50000,
                alpha,
                88))
        self.rational_resampler_xxx_0_0_0 = filter.rational_resampler_fff(
                interpolation=1,
                decimation=20,
                taps=[],
                fractional_bw=0)
        self.rational_resampler_xxx_0_0 = filter.rational_resampler_fff(
                interpolation=1,
                decimation=20,
                taps=[],
                fractional_bw=0)
        self.rational_resampler_xxx_0 = filter.rational_resampler_ccf(
                interpolation=20,
                decimation=1,
                taps=[],
                fractional_bw=0)
        self.qtgui_const_sink_x_0 = qtgui.const_sink_c(
            1024, #size
            "", #name
            1, #number of inputs
            None # parent
        )
        self.qtgui_const_sink_x_0.set_update_time(0.10)
        self.qtgui_const_sink_x_0.set_y_axis(-2, 2)
        self.qtgui_const_sink_x_0.set_x_axis(-2, 2)
        self.qtgui_const_sink_x_0.set_trigger_mode(qtgui.TRIG_MODE_FREE, qtgui.TRIG_SLOPE_POS, 0.0, 0, "")
        self.qtgui_const_sink_x_0.enable_autoscale(False)
        self.qtgui_const_sink_x_0.enable_grid(False)
        self.qtgui_const_sink_x_0.enable_axis_labels(True)


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
                self.qtgui_const_sink_x_0.set_line_label(i, "Data {0}".format(i))
            else:
                self.qtgui_const_sink_x_0.set_line_label(i, labels[i])
            self.qtgui_const_sink_x_0.set_line_width(i, widths[i])
            self.qtgui_const_sink_x_0.set_line_color(i, colors[i])
            self.qtgui_const_sink_x_0.set_line_style(i, styles[i])
            self.qtgui_const_sink_x_0.set_line_marker(i, markers[i])
            self.qtgui_const_sink_x_0.set_line_alpha(i, alphas[i])

        self._qtgui_const_sink_x_0_win = sip.wrapinstance(self.qtgui_const_sink_x_0.qwidget(), Qt.QWidget)
        self.top_layout.addWidget(self._qtgui_const_sink_x_0_win)
        self.low_pass_filter_0_0 = filter.interp_fir_filter_fff(
            1,
            firdes.low_pass(
                2,
                samp_rate*20,
                100000,
                1000,
                window.WIN_HAMMING,
                6.76))
        self.low_pass_filter_0 = filter.interp_fir_filter_fff(
            1,
            firdes.low_pass(
                2,
                samp_rate*20,
                100000,
                1000,
                window.WIN_HAMMING,
                6.76))
        self.interp_fir_filter_xxx_0_0 = filter.interp_fir_filter_ccf(8, [1])
        self.interp_fir_filter_xxx_0_0.declare_sample_delay(0)
        self.iir_filter_xxx_1_0 = filter.iir_filter_ffd([1.0001, -1], [-1, 1], True)
        self.iir_filter_xxx_0 = filter.iir_filter_ccf([1e-2], [-1, 0.99], True)
        self.fir_filter_xxx_0_0 = filter.fir_filter_fff(8, [1])
        self.fir_filter_xxx_0_0.declare_sample_delay(0)
        self.fir_filter_xxx_0 = filter.fir_filter_fff(8, [1])
        self.fir_filter_xxx_0.declare_sample_delay(0)
        self.digital_constellation_decoder_cb_0 = digital.constellation_decoder_cb(variable_constellation_0)
        self.digital_chunks_to_symbols_xx_0_0 = digital.chunks_to_symbols_bc([-1.41421, -1+1j, 1.41421*1j, 1+1j, 1.41421, 1-1j, -1.41421*1j, -1-1j], 1)
        self.blocks_vco_c_0_0 = blocks.vco_c(5e4, -5, 2.5)
        self.blocks_vco_c_0 = blocks.vco_c(5e4, -5e4, 1)
        self.blocks_unpack_k_bits_bb_1 = blocks.unpack_k_bits_bb(3)
        self.blocks_unpack_k_bits_bb_0 = blocks.unpack_k_bits_bb(8)
        self.blocks_threshold_ff_0_1 = blocks.threshold_ff(-0.001, 0.001, 0)
        self.blocks_threshold_ff_0_0_0 = blocks.threshold_ff(-0.001, 0.001, 0)
        self.blocks_sub_xx_0 = blocks.sub_ff(1)
        self.blocks_skiphead_0 = blocks.skiphead(gr.sizeof_char*1, 1)
        self.blocks_pack_k_bits_bb_0_0_0 = blocks.pack_k_bits_bb(8)
        self.blocks_pack_k_bits_bb_0_0 = blocks.pack_k_bits_bb(3)
        self.blocks_multiply_xx_2_0 = blocks.multiply_vcc(1)
        self.blocks_multiply_xx_2 = blocks.multiply_vcc(1)
        self.blocks_multiply_xx_0_2 = blocks.multiply_vcc(1)
        self.blocks_multiply_xx_0_1 = blocks.multiply_vff(1)
        self.blocks_multiply_xx_0_0_1 = blocks.multiply_vff(1)
        self.blocks_multiply_xx_0_0_0_0 = blocks.multiply_vff(1)
        self.blocks_multiply_xx_0_0_0 = blocks.multiply_vff(1)
        self.blocks_multiply_xx_0_0 = blocks.multiply_vff(1)
        self.blocks_multiply_xx_0 = blocks.multiply_vff(1)
        self.blocks_multiply_const_vxx_2 = blocks.multiply_const_cc(1)
        self.blocks_multiply_const_vxx_0_1 = blocks.multiply_const_ff(1/8)
        self.blocks_multiply_const_vxx_0_0 = blocks.multiply_const_ff(1.41421)
        self.blocks_multiply_const_vxx_0 = blocks.multiply_const_ff(1.41421)
        self.blocks_multiply_conjugate_cc_0 = blocks.multiply_conjugate_cc(1)
        self.blocks_float_to_complex_0 = blocks.float_to_complex(1)
        self.blocks_file_source_0_0 = blocks.file_source(gr.sizeof_char*1, '/home/joel/Documents/EE340/Lab10/Original_Text.txt', False, 0, 0)
        self.blocks_file_source_0_0.set_begin_tag(pmt.PMT_NIL)
        self.blocks_file_sink_0 = blocks.file_sink(gr.sizeof_char*1, '/home/joel/Documents/EE340/Lab10/task6.txt', False)
        self.blocks_file_sink_0.set_unbuffered(False)
        self.blocks_delay_0_0 = blocks.delay(gr.sizeof_gr_complex*1, 1)
        self.blocks_delay_0 = blocks.delay(gr.sizeof_gr_complex*1, 100)
        self.blocks_complex_to_float_0_0 = blocks.complex_to_float(1)
        self.blocks_complex_to_float_0 = blocks.complex_to_float(1)
        self.blocks_complex_to_arg_0 = blocks.complex_to_arg(1)
        self.blocks_add_xx_0 = blocks.add_vff(1)
        self.blocks_add_const_vxx_0_0 = blocks.add_const_ff(-0.5)
        self.blocks_add_const_vxx_0 = blocks.add_const_ff(-0.5)
        self.analog_sig_source_x_0_1_1 = analog.sig_source_f(samp_rate*20, analog.GR_COS_WAVE, 500000, 1, 0, 0)
        self.analog_sig_source_x_0_1_0_0 = analog.sig_source_f(samp_rate*20, analog.GR_SIN_WAVE, 500000, 1, 0, 0)
        self.analog_sig_source_x_0_1_0 = analog.sig_source_f(samp_rate*20, analog.GR_SIN_WAVE, 500000, 1, 0, 0)
        self.analog_sig_source_x_0_1 = analog.sig_source_f(samp_rate*20, analog.GR_COS_WAVE, 500000, 1, 0, 0)
        self.analog_noise_source_x_0_0 = analog.noise_source_f(analog.GR_GAUSSIAN, amp, 0)


        ##################################################
        # Connections
        ##################################################
        self.connect((self.analog_noise_source_x_0_0, 0), (self.blocks_add_xx_0, 1))
        self.connect((self.analog_sig_source_x_0_1, 0), (self.blocks_multiply_xx_0, 0))
        self.connect((self.analog_sig_source_x_0_1_0, 0), (self.blocks_multiply_xx_0_0, 1))
        self.connect((self.analog_sig_source_x_0_1_0_0, 0), (self.blocks_multiply_xx_0_0_0_0, 1))
        self.connect((self.analog_sig_source_x_0_1_1, 0), (self.blocks_multiply_xx_0_0_0, 0))
        self.connect((self.blocks_add_const_vxx_0, 0), (self.blocks_multiply_const_vxx_0, 0))
        self.connect((self.blocks_add_const_vxx_0_0, 0), (self.blocks_multiply_const_vxx_0_0, 0))
        self.connect((self.blocks_add_xx_0, 0), (self.blocks_multiply_xx_0_0_0, 1))
        self.connect((self.blocks_add_xx_0, 0), (self.blocks_multiply_xx_0_0_0_0, 0))
        self.connect((self.blocks_complex_to_arg_0, 0), (self.blocks_multiply_const_vxx_0_1, 0))
        self.connect((self.blocks_complex_to_float_0, 0), (self.blocks_multiply_xx_0, 1))
        self.connect((self.blocks_complex_to_float_0, 1), (self.blocks_multiply_xx_0_0, 0))
        self.connect((self.blocks_complex_to_float_0_0, 0), (self.blocks_multiply_xx_0_0_1, 1))
        self.connect((self.blocks_complex_to_float_0_0, 1), (self.blocks_multiply_xx_0_1, 1))
        self.connect((self.blocks_complex_to_float_0_0, 1), (self.blocks_threshold_ff_0_0_0, 0))
        self.connect((self.blocks_complex_to_float_0_0, 0), (self.blocks_threshold_ff_0_1, 0))
        self.connect((self.blocks_delay_0, 0), (self.blocks_multiply_xx_0_2, 1))
        self.connect((self.blocks_delay_0_0, 0), (self.blocks_multiply_conjugate_cc_0, 1))
        self.connect((self.blocks_file_source_0_0, 0), (self.blocks_unpack_k_bits_bb_0, 0))
        self.connect((self.blocks_float_to_complex_0, 0), (self.blocks_multiply_xx_0_2, 0))
        self.connect((self.blocks_multiply_conjugate_cc_0, 0), (self.blocks_complex_to_arg_0, 0))
        self.connect((self.blocks_multiply_const_vxx_0, 0), (self.blocks_multiply_xx_0_1, 0))
        self.connect((self.blocks_multiply_const_vxx_0_0, 0), (self.blocks_multiply_xx_0_0_1, 0))
        self.connect((self.blocks_multiply_const_vxx_0_1, 0), (self.blocks_vco_c_0, 0))
        self.connect((self.blocks_multiply_const_vxx_2, 0), (self.blocks_delay_0, 0))
        self.connect((self.blocks_multiply_xx_0, 0), (self.blocks_add_xx_0, 0))
        self.connect((self.blocks_multiply_xx_0_0, 0), (self.blocks_add_xx_0, 2))
        self.connect((self.blocks_multiply_xx_0_0_0, 0), (self.low_pass_filter_0, 0))
        self.connect((self.blocks_multiply_xx_0_0_0_0, 0), (self.low_pass_filter_0_0, 0))
        self.connect((self.blocks_multiply_xx_0_0_1, 0), (self.blocks_sub_xx_0, 1))
        self.connect((self.blocks_multiply_xx_0_1, 0), (self.blocks_sub_xx_0, 0))
        self.connect((self.blocks_multiply_xx_0_2, 0), (self.blocks_multiply_xx_2, 7))
        self.connect((self.blocks_multiply_xx_0_2, 0), (self.blocks_multiply_xx_2, 4))
        self.connect((self.blocks_multiply_xx_0_2, 0), (self.blocks_multiply_xx_2, 6))
        self.connect((self.blocks_multiply_xx_0_2, 0), (self.blocks_multiply_xx_2, 2))
        self.connect((self.blocks_multiply_xx_0_2, 0), (self.blocks_multiply_xx_2, 3))
        self.connect((self.blocks_multiply_xx_0_2, 0), (self.blocks_multiply_xx_2, 5))
        self.connect((self.blocks_multiply_xx_0_2, 0), (self.blocks_multiply_xx_2, 1))
        self.connect((self.blocks_multiply_xx_0_2, 0), (self.blocks_multiply_xx_2, 0))
        self.connect((self.blocks_multiply_xx_0_2, 0), (self.blocks_multiply_xx_2_0, 1))
        self.connect((self.blocks_multiply_xx_0_2, 0), (self.iir_filter_xxx_0, 0))
        self.connect((self.blocks_multiply_xx_2, 0), (self.blocks_delay_0_0, 0))
        self.connect((self.blocks_multiply_xx_2, 0), (self.blocks_multiply_conjugate_cc_0, 0))
        self.connect((self.blocks_multiply_xx_2_0, 0), (self.digital_constellation_decoder_cb_0, 0))
        self.connect((self.blocks_multiply_xx_2_0, 0), (self.qtgui_const_sink_x_0, 0))
        self.connect((self.blocks_pack_k_bits_bb_0_0, 0), (self.digital_chunks_to_symbols_xx_0_0, 0))
        self.connect((self.blocks_pack_k_bits_bb_0_0_0, 0), (self.blocks_file_sink_0, 0))
        self.connect((self.blocks_skiphead_0, 0), (self.blocks_pack_k_bits_bb_0_0_0, 0))
        self.connect((self.blocks_sub_xx_0, 0), (self.iir_filter_xxx_1_0, 0))
        self.connect((self.blocks_threshold_ff_0_0_0, 0), (self.blocks_add_const_vxx_0_0, 0))
        self.connect((self.blocks_threshold_ff_0_1, 0), (self.blocks_add_const_vxx_0, 0))
        self.connect((self.blocks_unpack_k_bits_bb_0, 0), (self.blocks_pack_k_bits_bb_0_0, 0))
        self.connect((self.blocks_unpack_k_bits_bb_1, 0), (self.blocks_skiphead_0, 0))
        self.connect((self.blocks_vco_c_0, 0), (self.blocks_multiply_xx_2_0, 0))
        self.connect((self.blocks_vco_c_0_0, 0), (self.zeromq_push_sink_0, 0))
        self.connect((self.digital_chunks_to_symbols_xx_0_0, 0), (self.interp_fir_filter_xxx_0_0, 0))
        self.connect((self.digital_constellation_decoder_cb_0, 0), (self.blocks_unpack_k_bits_bb_1, 0))
        self.connect((self.fir_filter_xxx_0, 0), (self.blocks_float_to_complex_0, 0))
        self.connect((self.fir_filter_xxx_0_0, 0), (self.blocks_float_to_complex_0, 1))
        self.connect((self.iir_filter_xxx_0, 0), (self.blocks_complex_to_float_0_0, 0))
        self.connect((self.iir_filter_xxx_1_0, 0), (self.blocks_vco_c_0_0, 0))
        self.connect((self.interp_fir_filter_xxx_0_0, 0), (self.root_raised_cosine_filter_0_1, 0))
        self.connect((self.low_pass_filter_0, 0), (self.rational_resampler_xxx_0_0, 0))
        self.connect((self.low_pass_filter_0_0, 0), (self.rational_resampler_xxx_0_0_0, 0))
        self.connect((self.rational_resampler_xxx_0, 0), (self.blocks_complex_to_float_0, 0))
        self.connect((self.rational_resampler_xxx_0_0, 0), (self.root_raised_cosine_filter_0_1_0, 0))
        self.connect((self.rational_resampler_xxx_0_0_0, 0), (self.root_raised_cosine_filter_0_1_1, 0))
        self.connect((self.root_raised_cosine_filter_0_1, 0), (self.rational_resampler_xxx_0, 0))
        self.connect((self.root_raised_cosine_filter_0_1_0, 0), (self.fir_filter_xxx_0, 0))
        self.connect((self.root_raised_cosine_filter_0_1_1, 0), (self.fir_filter_xxx_0_0, 0))
        self.connect((self.zeromq_pull_source_0, 0), (self.blocks_multiply_const_vxx_2, 0))


    def closeEvent(self, event):
        self.settings = Qt.QSettings("GNU Radio", "task6")
        self.settings.setValue("geometry", self.saveGeometry())
        self.stop()
        self.wait()

        event.accept()

    def get_variable_constellation_0(self):
        return self.variable_constellation_0

    def set_variable_constellation_0(self, variable_constellation_0):
        self.variable_constellation_0 = variable_constellation_0

    def get_samp_rate(self):
        return self.samp_rate

    def set_samp_rate(self, samp_rate):
        self.samp_rate = samp_rate
        self.analog_sig_source_x_0_1.set_sampling_freq(self.samp_rate*20)
        self.analog_sig_source_x_0_1_0.set_sampling_freq(self.samp_rate*20)
        self.analog_sig_source_x_0_1_0_0.set_sampling_freq(self.samp_rate*20)
        self.analog_sig_source_x_0_1_1.set_sampling_freq(self.samp_rate*20)
        self.low_pass_filter_0.set_taps(firdes.low_pass(2, self.samp_rate*20, 100000, 1000, window.WIN_HAMMING, 6.76))
        self.low_pass_filter_0_0.set_taps(firdes.low_pass(2, self.samp_rate*20, 100000, 1000, window.WIN_HAMMING, 6.76))
        self.root_raised_cosine_filter_0_1.set_taps(firdes.root_raised_cosine(3, self.samp_rate, 50000, self.alpha, 88))
        self.root_raised_cosine_filter_0_1_0.set_taps(firdes.root_raised_cosine(3, self.samp_rate, 50000, self.alpha, 88))
        self.root_raised_cosine_filter_0_1_1.set_taps(firdes.root_raised_cosine(3, self.samp_rate, 50000, self.alpha, 88))

    def get_amp(self):
        return self.amp

    def set_amp(self, amp):
        self.amp = amp
        self.analog_noise_source_x_0_0.set_amplitude(self.amp)

    def get_alpha(self):
        return self.alpha

    def set_alpha(self, alpha):
        self.alpha = alpha
        self.root_raised_cosine_filter_0_1.set_taps(firdes.root_raised_cosine(3, self.samp_rate, 50000, self.alpha, 88))
        self.root_raised_cosine_filter_0_1_0.set_taps(firdes.root_raised_cosine(3, self.samp_rate, 50000, self.alpha, 88))
        self.root_raised_cosine_filter_0_1_1.set_taps(firdes.root_raised_cosine(3, self.samp_rate, 50000, self.alpha, 88))




def main(top_block_cls=task6, options=None):

    if StrictVersion("4.5.0") <= StrictVersion(Qt.qVersion()) < StrictVersion("5.0.0"):
        style = gr.prefs().get_string('qtgui', 'style', 'raster')
        Qt.QApplication.setGraphicsSystem(style)
    qapp = Qt.QApplication(sys.argv)

    tb = top_block_cls()

    tb.start()

    tb.show()

    def sig_handler(sig=None, frame=None):
        tb.stop()
        tb.wait()

        Qt.QApplication.quit()

    signal.signal(signal.SIGINT, sig_handler)
    signal.signal(signal.SIGTERM, sig_handler)

    timer = Qt.QTimer()
    timer.start(500)
    timer.timeout.connect(lambda: None)

    qapp.exec_()

if __name__ == '__main__':
    main()
