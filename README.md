# Local Control Test Script for WiZ Lights
WiZ is a smart lighting brand under Signify. They allow UDP control within the same network. In this project, I'd like to compose scripts to test WiZ light's basic features automatically using Python. 
(Note: this is a side-project for learning purpose.)

### WiZ Lights Local Control Features 
1. Change status: ON/OFF
2. Change color: R, G, B, CW, WW (0 - 225)
3. Change dimming: 0 - 100
4. Change temperature: 2700 - 6500
5. Change light modes: scene_id 1 - 28 (should have more)

## Project plan
- **Phase 1:** A straitforward test => **[basic.py](https://github.com/maudes/wiz-light-local-test-script/blob/main/simple_scripts/basic.py)**
- **Phase 2:** Wrap-up the code into a more clean and maintanence-friendly format with results output => **[basic_refactor.py](https://github.com/maudes/wiz-light-local-test-script/blob/main/simple_scripts/basic_refactor.py)**
- **Phase 3:** Expand the basic test script using Pytest => **[pytest](https://github.com/maudes/wiz-light-local-test-script/tree/main/pytest)**
- **Phase 4:** Create a CLI tool version   *(**7/14/2025:** updated in both `basic_refactor.py` and `wiz_test -> pytest module`)*
- **Phase 5:** Create a simple frontend for users to trigger the auto-testing *(**7/16/2025:** References: `modules`, `app.py`, `cli.py`)*


## Overview
```
 wiz-light-local-test-script
｜＿＿ modules/
｜    ｜＿＿ __init__.py
｜    ｜＿＿ communication.py
｜    ｜＿＿ runner.py
｜    ｜＿＿ type_data.py
｜＿＿ pytest/
｜    ｜＿＿ tests/
｜    ｜   ｜＿＿ conftest.py
｜    ｜   ｜＿＿ test_basic.py
｜    ｜＿＿ pytest.ini
｜＿＿ simple_scripts
｜    ｜＿＿ basic_refactor.py
｜    ｜＿＿ basic.py
｜＿＿ cli.py
｜＿＿ app.py 
｜＿＿ README.md
```

## How to use basic_refactor.py?
First, download the script file

```Bash
git clone https://github.com/maudes/wiz-light-local-test-script.git
cd wiz-light-local-test-script/simple_scripts
```
   
Second, run the script with your test device's ip address

```Bash
python3 basic_refactor.py --ip xxx.xxx.xxx.xxx
```
>**HOW to find the device IP address?** Install the device to WiZ app and check the device info

Last, check your result. In the best scenario, it shall shows as below:

    WiZ response:  {'method': 'getPilot', 'env': 'pro', 'result': {'mac': 'd8a011xxxxxx', 'rssi': -77, 'state': True, 'sceneId': 0, 'r': 100, 'g': 0, 'b': 140, 'c': 0, 'w': 0, 'dimming': 74}}
    WiZ response:  {'method': 'setPilot', 'env': 'pro', 'result': {'success': True}}
    WiZ response:  {'method': 'setPilot', 'env': 'pro', 'result': {'success': True}}
    WiZ response:  {'method': 'setPilot', 'env': 'pro', 'result': {'success': True}}
    WiZ response:  {'method': 'setPilot', 'env': 'pro', 'result': {'success': True}}
    Total 5 tests passed, and 0 tests failed.

## How to use pytest?

First, go into the `pytest` file
```Bash
cd wiz_test
```

Then, run the pytest in tests file
```Bash
python3 -m pytest --ip=xxx.xxx.xxx.xxx
```

And, you should see the test results shown as

```Bash
.....                                                                                              [100%]
5 passed in 0.30s
```

Plus, you can generate a HTML report (don't foreget to download pytest-html first!)
```Bash
python3 -m pytest tests --html={filename}.html
```
## How to use cli.py?
First, execute the file with ip address and device type.
  
```Bash
python3 cli.py --ip xxx.xxx.xxx.xxx --type="Color light/ Tuneable white light/ Dimmable light"
```

You shall receive results like below:

    Total 10 with 10 tests passed and 0 tests failed.
    get_state: {'method': 'getPilot', 'env': 'pro', 'result': {'mac': 'd8a011xxxxxx', 'rssi': -48, 'state': True, 'sceneId': 0, 'r': 100, 'g': 0, 'b': 140, 'c': 0, 'w': 0, 'dimming': 20}}
    turn_off: {'method': 'setPilot', 'env': 'pro', 'result': {'success': True}}
    turn_on_brightness: {'method': 'setPilot', 'env': 'pro', 'result': {'success': True}}
    change_temp_warm: {'method': 'setPilot', 'env': 'pro', 'result': {'success': True}}
    change_temp_cold: {'method': 'setPilot', 'env': 'pro', 'result': {'success': True}}
    scene_relax: {'method': 'setPilot', 'env': 'pro', 'result': {'success': True}}
    scene_ocean: {'method': 'setPilot', 'env': 'pro', 'result': {'success': True}}
    scene_romance: {'method': 'setPilot', 'env': 'pro', 'result': {'success': True}}
    scene_mojito: {'method': 'setPilot', 'env': 'pro', 'result': {'success': True}}
    change_rgb: {'method': 'setPilot', 'env': 'pro', 'result': {'success': True}}

## How to use app.py?

Install streamlit in your local machine, and run in local env (for receiving the UDP packet).
> The default port of streamlit should be: **http://localhost:8501**

```Bash
pip3 install streamlit
streamlit run app.py
```
In terms of the UI, you can have a look [here.](https://wiz-local-test.streamlit.app/)
