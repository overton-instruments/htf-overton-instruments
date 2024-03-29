# HTF Extension for Overton Instruments Devices
This extension enables the testing of [Overton Instruments](http://overtoninstruments.com/)' devices with htf (Hilster Testing Framework).
More information about htf can be found on [HILSTER's website](https://www.hilster.io/en/testbench/)
and on [htf's documentation site](https://docs.hilster.io/htf/latest/index.html).
This extension works with our community license.

## PyPi project page
[htf-overton-instruments](https://pypi.org/project/htf-overton-instruments/)

## Installation guide
The htf-overton extension can be installed using pip.

``pip install -i https://pypi.hilster.io htf-overton-instruments``

Naturally it requires the htf package to be installed, which can be done by following [this guide](https://docs.hilster.io/htf/latest/installation.html#installation-of-htf-via-pip)

## Examples

There are two included examples on how to use this extension with htf.

``fixture_example.py`` shows how to use ``htf.fixtures`` to set up the test environment. Furthermore, the ``test_<device>`` functions can be split into multiple functionality tests (whether bits are getting set, etc.), for this each function name must start with ``test`` or be decorated with ``htf.test``.

``testcase_example.py`` showcases htf's functionality more generally. For more information see the [htf documentation](https://docs.hilster.io/htf/latest/writing_tests.html#) on writing tests.

Both examples create a ``testreport.html``, as do all htf test runs, where you can see the results and all outputs in a more accessible manner.

## Device support

Currently, the devices SWITCH-MATE/HP(vI), GSM-MATE4/8(vI), LDM-MATE(vI) r1.0, MUX-MATE(vI), and SFM-MATE(vI) are supported.