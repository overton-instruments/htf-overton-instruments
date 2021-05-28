import htf
from htf_overton_instruments import device


class TestOIDevice:

    @htf.tags("opto_mate")
    def test_opto_mate_connection(self):
        device.print_messages = True
        device.is_device_ready
        htf.assert_equal(device.reply, "Ready.")

    @htf.tags("opto_mate")
    def test_opto_mate_output_success(self):
        # Beginning output bits configuration: Port 0 [0, 1, 1, 0, 1, 0, 0, 1], Port 1 [1, 0, 0, 1, 0, 1, 1, 0]
        device.port_number = 1
        device.set_output_bit = 0, 0
        htf.assert_true(device.reply)

        device.port_number = 0
        device.set_output_bit = 5, 1
        htf.assert_true(device.reply)

        device.output_bit
        htf.assert_list_equal(device.reply, [[0, 1, 1, 0, 1, 1, 0, 1], [0, 0, 0, 1, 0, 1, 1, 0]])

    @htf.tags("opto_mate")
    @htf.test
    def opto_mate_output_fail(self):
        device.print_messages = False
        device.port_number = 1
        device.output_bit = 5
        htf.assert_equal(device.reply, 0)

    @htf.tags("opto_mate")
    def test_opto_mate_error(self):
        device.port_number = 2
        htf.assert_equal(device.reply, 1)

    @htf.tags("opto_mate")
    @htf.test
    def opto_mate_skip(self):
        device.print_messages = True
        device.baudrate
        print("Shows up in test report.")
        if device.reply < 2:
            raise htf.SkipTest
        print("Does not show up.")

    @htf.tags("switch_mate")
    def test_switch_mate_connection(self):
        device.print_messages = True
        device.is_device_ready
        htf.assert_equal(device.reply, "Ready.")

    @htf.tags("switch_mate")
    def test_switch_mate_relays(self):
        for i in range(1, 9):
            if i % 2 == 0:
                device.relay = i, 0
            else:
                device.relay = i, 1

        device.relay
        htf.assert_equal(device.reply, "01010101")

    @htf.tags("switch_mate")
    def test_switch_mate_relays_config(self):
        device.save_relay_config = 1
        htf.assert_true(device.reply)

        device.clear_relays
        htf.assert_true(device.reply)

        device.read_relay_config = 1
        htf.assert_equal(device.reply, "01010101")

    @htf.tags("switch_mate")
    def test_switch_mate_settling_time(self):
        device.settling_time = 120
        htf.assert_true(device.reply)

        device.settling_time
        htf.assert_equal(device.reply, "120")

    @htf.tags("switch_mate")
    def test_switch_mate_closed_relays(self):
        device.close_relays

        device.relay
        htf.assert_equal(device.reply, "11111111")

    @htf.tags("switch_mate")
    def test_switch_mate_cleared_relays(self):
        device.clear_relays

        device.relay
        htf.assert_equal(device.reply, "00000000")

    @htf.tags("ldm_mate")
    def test_ldm_mate_ready(self):
        device.is_device_ready

        htf.assert_equal(device.reply, "Ready.")

    @htf.tags("ldm_mate")
    def test_ldm_mate_module_id(self):
        device.module_id

        htf.assert_equal(device.reply, "LDM-MATE(vI) r1.0")

    @htf.tags("ldm_mate")
    def test_ldm_mate_output_bits(self):
        device.output_bit

        device.assert_list_equal(device.reply, [[0, 0, 0, 0, 0, 0, 0, 0], []])

    @htf.tags("ldm_mate")
    def test_ldm_mate_baudrate(self):
        device.baudrate

        htf.assert_equal(device.reply, 3)

    @htf.tags("ldm_mate")
    def test_ldm_mate_port_format(self):
        device.port_format = 1
        htf.assert_true(device.reply)

        device.port_format
        htf.assert_equal(device.reply, 1)

    @htf.tags("ldm_mate")
    def test_ldm_mate_port_data(self):
        device.port_data

        htf.assert_equal(device.reply, "00000000")

    @htf.tags("mux_mate")
    def test_mux_mate_connection(self):
        device.is_device_ready

        htf.assert_equal(device.reply, "Ready.")

    @htf.tags("mux_mate")
    def test_mux_mate_baudrate(self):
        device.baudrate
        htf.assert_equal(device.reply, 3)

    @htf.tags("mux_mate")
    def test_mux_mate_module_id(self):
        device.module_id
        htf.assert_equal(device.reply, "MUX-MATE(vI) r2.1")

    @htf.tags("mux_mate")
    def test_mux_mate_relays(self):
        device.relay = 1, 1
        htf.assert_true(device.reply)

        device.relay
        htf.assert_equal(device.reply, "0000000000000001")

        device.close_relays
        htf.assert_true(device.reply)

        device.relay
        htf.assert_equal(device.reply, "1111111111111111")

        device.clear_relays
        htf.assert_true(device.reply)

        device.relay
        htf.assert_equal(device.reply, "0000000000000000")

    @htf.tags("mux_mate")
    def test_mux_mate_settling_time(self):
        device.settling_time = 120
        htf.assert_true(device.reply)

        device.settling_time
        htf.assert_equal(device.reply, "120")

    @htf.tags("mux_mate")
    def test_mux_mate_mux_mode(self):
        device.mux_mode
        htf.assert_equal(device.reply, 0)


    @htf.tags("sfm_mate")
    def test_sfm_mate_connection(self):
        device.is_device_ready
        htf.assert_equal(device.reply, "Ready.")

    @htf.tags("sfm_mate")
    def test_sfm_mate_module_id(self):
        device.module_id
        htf.assert_equal(device.reply, "SFM-MATE(vI) r2.0")

    @htf.tags("sfm_mate")
    def test_sfm_mate_short_status(self):
        device.short_status
        htf.assert_equal(device.reply, "00000000")

    @htf.tags("sfm_mate")
    def test_sfm_mate_settling_time(self):
        device.settling_time = 120
        htf.assert_true(device.reply)

        device.settling_time
        htf.assert_equal(device.reply, "120")


if __name__ == '__main__':
    # device = oi_device.OptoMateIII("COM3")
    # device = oi_device.SwitchMateV1("COM3")
    # device = oi_device.LDMMate("COM3")
    # device = oi_device.MUXMate("COM3")
    device = device.SFMMate("COM3")

    device.open_port()

    # htf.main(tags="opto_mate")
    # htf.main(tags="switch_mate")
    # htf.main(tags="ldm_mate")
    # htf.main(tags="mux_mate")
    htf.main(tags="sfm_mate")
