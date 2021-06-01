import htf
from htf_overton_instruments import device
import yaml


@htf.fixture('test', name="opto_mate")
def create_opto_mate():
    yield device.OptoMateIII("COM4")


@htf.fixture('test', name="switch_mate")
def create_switch_mate():
    yield device.SwitchMateV1("COM3")


@htf.fixture('test', name="gsm_mate")
def create_gsm_mate():
    yield device.GSMMate("COM3")


@htf.fixture('test', name="ldm_mate")
def create_ldm_mate():
    yield device.LDMMate("COM3")


@htf.fixture('test', name="mux_mate")
def create_mux_mate():
    yield device.MUXMate("COM3")


@htf.fixture('test', name="sfm_mate")
def create_sfm_mate():
    yield device.SFMMate("COM3")


@htf.fixture('test', name="expected")
def load_expected_results():
    with open('expected_results.yml') as f:
        yield yaml.safe_load(f)

