# Local Control Test Script for WiZ Lights
WiZ is a smart lighting brand under Signify. They allow UDP control within the same network. In this project, I'd like to compose scripts to test WiZ light's basic features automatically using Python. 
(Note: this is a side-project for learning purpose.)

### WiZ Lights Local Control Features 
1. Change status: ON/OFF
2. Change color: R, G, B, CW, WW (0 - 225)
3. Change dimming: 0 - 100
4. Change temperature: 2700 - 6500
5. Change light modes: scene_id 1 - 28 (should have more)

## Key features of the script
### Basic interface
- Run Python script in CLI (no parameter supported)
### Basic features
1. Run basic feature test 
2. Generate a test report as: "Total x paased, and y failed"


## Project plan
- **Phase 1:** A straitforward test => **[basic.py](https://github.com/maudes/wiz-light-local-test-script/blob/main/basic.py)**
- **Phase 2:** Wrap-up the code into a more clean and maintanence-friendly format with results output => **[basic_refactor.py](https://github.com/maudes/wiz-light-local-test-script/blob/main/basic_refactor.py)**
- **Phase 3:** Expand the basic test script using Pytest => **[wrap_pytest](https://github.com/maudes/wiz-light-local-test-script/tree/main/wrap_pytest)**
- **Phase 4:** Create a CLI tool version
- **Phase 5:** Create a simple frontend for users to trigger the auto-testing

## How to use basic_refactor.py?
First, download the script file

```Bash
git clone https://github.com/maudes/wiz-light-local-test-script.git
cd wiz-light-local-test-script
```

>***Don't forget to update the `wiz_ip` field to your own WiZ testing device.***<br>
>**HOW TO?** Install the device to WiZ app and check the device info
   
Second, run the script

```Bash
python3 basic_refactor.py
```

Last, check your result. In the best scenario, it shall shows as below:

    WiZ response:  {'method': 'getPilot', 'env': 'pro', 'result': {'mac': 'd8a011ca9f47', 'rssi': -77, 'state': True, 'sceneId': 0, 'r': 100, 'g': 0, 'b': 140, 'c': 0, 'w': 0, 'dimming': 74}}
    WiZ response:  {'method': 'setPilot', 'env': 'pro', 'result': {'success': True}}
    WiZ response:  {'method': 'setPilot', 'env': 'pro', 'result': {'success': True}}
    WiZ response:  {'method': 'setPilot', 'env': 'pro', 'result': {'success': True}}
    WiZ response:  {'method': 'setPilot', 'env': 'pro', 'result': {'success': True}}
    Total 5 tests passed, and 0 tests failed.

## How to use wrap_pytest?

First, go into the wrap_pytest file
```Bash
cd wrap_pytest
```

Then, run the pytest in tests file
```Bash
python3 -m pytest tests
```

And, you should see the test results shown as

```Bash
.....                                                                                              [100%]
5 passed in 0.30s
```

Plus, you can generate a HTML report (don't foreget to download pytest-html first!)
```Bash
python3 -m pytest tests --html=report.html
```


