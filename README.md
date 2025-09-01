# WiZ Lights Local Control Automation Test

WiZ is a smart lighting brand under Signify that supports local UDP control within the same network. This project is a Python-based automation suite designed to test core functionalities of WiZ lights.  
> ⚠️ This is a side project for learning and experimentation.

---

## Supported Features

- Power control: ON / OFF
- Color adjustment: R / G / B / CW / WW (range: 0–225)
- Brightness control: 0–100
- Color temperature: 2700–6500K
- Light scenes: `scene_id` 1–28 (possibly more supported)

---

## Project Roadmap

| Phase | Description | Link |
|-------|-------------|------|
| Phase 1 | Basic test script | [basic.py](simple_scripts/basic.py) |
| Phase 2 | Refactored script with cleaner structure and result output | [basic_refactor.py](simple_scripts/basic_refactor.py) |
| Phase 3 | Pytest-based test suite | [pytest/](pytest) |
| Phase 4 | CLI tool implementation<br>🗓️ Updated: July 14, 2025 | [cli.py](cli.py) |
| Phase 5 | Simple frontend for triggering tests<br>🗓️ Updated: July 16, 2025 | [app.py](app.py) |

---

## Overview
```
 wiz-light-local-test-script
｜＿＿ modules/                  # For the use of cli.py and app.py 
｜    ｜＿＿ __init__.py      
｜    ｜＿＿ communication.py    # Build the udp connection, send and receive the udp packet
｜    ｜＿＿ runner.py           # Run the test cases
｜    ｜＿＿ type_data.py        # Test cases based on different device types
｜＿＿ pytest/ 
｜    ｜＿＿ tests/
｜    ｜   ｜＿＿ conftest.py
｜    ｜   ｜＿＿ test_basic.py
｜    ｜＿＿ pytest.ini
｜＿＿ simple_scripts
｜    ｜＿＿ basic_refactor.py
｜    ｜＿＿ basic.py
｜＿＿ cli.py                    # CLI tool
｜＿＿ app.py                    # streamlit
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
