import time
import htf
from tests.receiver import Receiver
from htf_overton_instruments import device
from htf.core import Thread


def run_receiver():
    receiver = Receiver(print_messages=True)
    receiver.get_message()


def test_simulated_responses_switch_mate(assertions, step, expected):
    receiver_thread = Thread(target=run_receiver)
    receiver_thread.start()
    time.sleep(1)
    switch_mate = device.SwitchMateV1("COM4")
    switch_mate.open_port()

    with step("Checking if Switch Mate is ready"):
        switch_mate.is_device_ready
        assertions.assert_equal(switch_mate.reply, expected['ready'])

    with step("Checking Switch Mate baud rate"):
        switch_mate.baudrate
        assertions.assert_equal(switch_mate.reply, 3)

    with step("Checking Switch Mate module ID"):
        switch_mate.module_id
        assertions.assert_equal(switch_mate.reply, expected['switch']['module_id'])

    with step("Setting relays to 01010101"):
        for i in range(1, 9):
            if i % 2 == 0:
                switch_mate.relay = i, 0
            else:
                switch_mate.relay = i, 1

    with step("Checking relays"):
        switch_mate.relay
        assertions.assert_equal(switch_mate.reply, expected['switch']['relay'])

    with step("Saving relay configuration"):
        switch_mate.save_relay_config = 1
        assertions.assert_true(switch_mate.reply)

    with step("Clearing relays"):
        switch_mate.clear_relays
        assertions.assert_true(switch_mate.reply)

    with step("Checking saved configuration"):
        switch_mate.read_relay_config = 1
        assertions.assert_equal(switch_mate.reply, expected['switch']['read_relay_config'])

    with step("Setting settling time"):
        switch_mate.settling_time = 120
        assertions.assert_true(switch_mate.reply)

    with step("Checking settling time"):
        switch_mate.settling_time
        assertions.assert_equal(switch_mate.reply, expected['switch']['settling_time'])

    with step("Closing all relays"):
        switch_mate.close_relays

    with step("Checking relays"):
        switch_mate.relay
        assertions.assert_equal(switch_mate.reply, expected['switch']['closed'])

    with step("Clearing all relays"):
        switch_mate.clear_relays

    with step("Checking relays"):
        switch_mate.relay
        assertions.assert_equal(switch_mate.reply, expected['switch']['cleared'])

    switch_mate._serial.reset_input_buffer()
    switch_mate.close_port()
    receiver_thread.stop()


def test_simulated_responses_opto_mate(opto_mate, assertions, expected):
    receiver_thread = Thread(target=run_receiver)
    receiver_thread.start()
    opto_mate.open_port()

    opto_mate.is_device_ready
    assertions.assert_equal(opto_mate.reply, expected['ready'])

    opto_mate.output_bit
    assertions.assert_list_equal(opto_mate.reply, expected['opto']['output_bits'])

    opto_mate.baudrate = 1
    opto_mate.baudrate
    assertions.assert_equal(opto_mate.reply, expected['opto']['baudrate'])

    opto_mate.set_output_bit = 5, 1
    opto_mate.port_number = 0
    opto_mate.output_bit = 1
    assertions.assert_equal(opto_mate.reply, expected['opto']['port_zero_bit_one'])

    opto_mate.port_format
    assertions.assert_true(opto_mate.reply)

    opto_mate.port_format = 1
    assertions.assert_true(opto_mate.reply)

    opto_mate.port_number = 1
    opto_mate.port_data
    assertions.assert_equal(opto_mate.reply, expected['opto']['port_one_data'])
    opto_mate.port_number = 0
    opto_mate.port_data
    assertions.assert_equal(opto_mate.reply, expected['opto']['port_zero_data'])

    opto_mate.port_data = 10001001
    assertions.assert_true(opto_mate.reply)
    opto_mate.port_number = 1
    opto_mate.port_number
    assertions.assert_equal(opto_mate.reply, expected['opto']['port_number'])
    receiver_thread.stop()


def test_simulated_responses_gsm_mate(assertions, expected, step):
    receiver_thread = Thread(target=run_receiver)
    receiver_thread.start()
    gsm_mate = device.GSMMate("COM4")
    gsm_mate.open_port()

    with step("Checking if GSM Mate is ready"):
        gsm_mate.is_device_ready
        assertions.assert_equal(gsm_mate.reply, expected['ready'])

    with step("Checking GSM baudrate"):
        gsm_mate.baudrate
        assertions.assert_equal(gsm_mate.reply, 3)

    with step("Checking GSM module ID"):
        gsm_mate.module_id
        assertions.assert_equal(gsm_mate.reply, expected['gsm']['module_id'])

    with step("Setting and checking GSM relay"):
        gsm_mate.relay = 1, 1
        assertions.assert_true(gsm_mate.reply)

        gsm_mate.relay
        assertions.assert_equal(gsm_mate.reply, expected['gsm']['relay'])

    with step("Set and check GSM settling time"):
        gsm_mate.settling_time = 120
        assertions.assert_true(gsm_mate.reply)

        gsm_mate.settling_time
        assertions.assert_equal(gsm_mate.reply, expected['gsm']['settling_time'])

    with step("Master reset"):
        gsm_mate.master_reset
        assertions.assert_true(gsm_mate.reply)

    gsm_mate.close_port()
    receiver_thread.stop()


def test_simulated_responses_ldm_mate(assertions, expected, step):
    receiver_thread = Thread(target=run_receiver)
    receiver_thread.start()
    ldm_mate = device.LDMMate("COM4")
    ldm_mate.open_port()

    with step("Checking if LDM Mate is ready"):
        ldm_mate.is_device_ready
        assertions.assert_equal(ldm_mate.reply, expected['ready'])

    with step("Checking LDM Mate's output bits"):
        ldm_mate.output_bit
        assertions.assert_list_equal(ldm_mate.reply, expected['ldm']['output_bits'])

    with step("Checking LDM Mate's baudrate"):
        ldm_mate.baudrate
        assertions.assert_equal(ldm_mate.reply, expected['ldm']['baudrate'])

    # shows how to write to the device and test for it, could not be confirmed as working on our device
    with step("Setting output bit 5 to 1"):
        ldm_mate.set_output_bit = 5, 1

    with step("Checking output bit 5"):
        ldm_mate.output_bit = 5
        assertions.assert_equal(ldm_mate.reply, expected['ldm']['port_zero_bit_five'])

    with step("Writing port data"):
        ldm_mate.port_data = 0x0F

    with step("Setting LDM Mate's port format"):
        ldm_mate.port_format = 0
        assertions.assert_true(ldm_mate.reply)

    with step("Checking LDM Mate's port data"):
        ldm_mate.port_data
        assertions.assert_equal(ldm_mate.reply, expected['ldm']['binary_data'])

    with step("Setting LDM Mate's port format"):
        ldm_mate.port_format = 1
        assertions.assert_true(ldm_mate.reply)

    with step("Checking LDM Mate's port format"):
        ldm_mate.port_format
        assertions.assert_equal(ldm_mate.reply, expected['ldm']['port_format'])

    with step("Checking LDM Mate's port data"):
        ldm_mate.port_data
        assertions.assert_equal(ldm_mate.reply, expected['ldm']['hex_data'])

    receiver_thread.stop()


def test_simulated_responses_mux_mate(assertions, expected, step):
    receiver_thread = Thread(target=run_receiver)
    receiver_thread.start()
    mux_mate = device.MUXMate("COM4")
    mux_mate.open_port()

    with step("Checking if MUX Mate is ready"):
        mux_mate.is_device_ready
        assertions.assert_equal(mux_mate.reply, expected['ready'])

    with step("Checking MUX Mate's baud rate"):
        mux_mate.baudrate
        assertions.assert_equal(mux_mate.reply, 3)

    with step("Checking MUX Mate's Module ID"):
        mux_mate.module_id
        assertions.assert_equal(mux_mate.reply, expected['mux']['module_id'])

    with step("Turning relay 1 on"):
        mux_mate.relay = 1, 1
        assertions.assert_true(mux_mate.reply)

    with step("Checking all relays"):
        mux_mate.relay
        assertions.assert_equal(mux_mate.reply, expected['mux']['relay'])

    with step("Setting MUX Mate's settling time"):
        mux_mate.settling_time = 120
        assertions.assert_true(mux_mate.reply)

    with step("Checking MUX Mate's settling time"):
        mux_mate.settling_time
        assertions.assert_equal(mux_mate.reply, expected['mux']['settling_time'])

    with step("Checking MUX Mate's mode"):
        mux_mate.mux_mode
        assertions.assert_equal(mux_mate.reply, 0)

    with step("Closing all relays"):
        mux_mate.close_relays
        assertions.assert_true(mux_mate.reply)

    with step("Checking if all relays are closed"):
        mux_mate.relay
        assertions.assert_equal(mux_mate.reply, expected['mux']['closed'])

    with step("Clearing all relays"):
        mux_mate.clear_relays
        assertions.assert_true(mux_mate.reply)

    with step("Checking if all relays are cleared"):
        mux_mate.relay
        assertions.assert_equal(mux_mate.reply, expected['mux']['cleared'])

    mux_mate.close_port()
    receiver_thread.stop()


def test_simulated_responses_sfm_mate(assertions, expected, step):
    receiver_thread = Thread(target=run_receiver)
    receiver_thread.start()
    sfm_mate = device.SFMMate("COM4")
    sfm_mate.open_port()

    with step("Checking if SFM Mate is ready"):
        sfm_mate.is_device_ready
        assertions.assert_equal(sfm_mate.reply, expected['ready'])

    with step("Checking SFM Mate's module ID"):
        sfm_mate.module_id
        assertions.assert_equal(sfm_mate.reply, expected['sfm']['module_id'])

    with step("Checking short status"):
        sfm_mate.short_status
        assertions.assert_equal(sfm_mate.reply, expected['sfm']['short_status'])

    with step("Setting SFM Mate's settling time"):
        sfm_mate.settling_time = 120
        assertions.assert_true(sfm_mate.reply)

    with step("Checking SFM Mate's settling time"):
        sfm_mate.settling_time
        assertions.assert_equal(sfm_mate.reply, expected['sfm']['settling_time'])

    sfm_mate.close_port()
    receiver_thread.stop()


if __name__ == '__main__':
    htf.main(tests=["fixtures"] + [test_simulated_responses_sfm_mate])

