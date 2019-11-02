#!/usr/bin/python3

import skrf as rf
rf.stylely()

# load touchstone files
network_open = rf.Network('../Measurements/fixture/Fixture_Open.s1p')
network_short = rf.Network('../Measurements/fixture/Fixture_Shorted.s1p')
network_dut = rf.Network('../Measurements/original/DUT.s1p')

# create dummy files for deembedding (correct number of freqs, ...)
network_deembed_open = rf.Network('../Measurements/original/DUT.s1p')
network_deembed_short = rf.Network('../Measurements/original/DUT.s1p')
network_deembed_open_short = rf.Network('../Measurements/original/DUT.s1p')

# deembed with open and short
network_deembed_open.y = network_dut.y - network_open.y
network_deembed_short.z = network_dut.z - network_short.z
network_deembed_open_short.z = network_deembed_open.z - network_short.z

# plot results
network_dut.plot_s_smith()
network_deembed_open_short.plot_s_smith()

# write touchstone files
network_deembed_open.write_touchstone('../Measurements/deembed-oc/DUT_deembedded_open_python.s1p')
network_deembed_short.write_touchstone('../Measurements/deembed-sc/DUT_deembedded_shorted.s1p')
network_deembed_open_short.write_touchstone('../Measurements/deembed-both/DUT_deembedded_open-short.s1p')

# wait for user, otherwise plot figures get closed
input()
