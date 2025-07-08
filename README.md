# Local API Test Script for WiZ Lights
WiZ is a smart lighting brand under Signify. They allow UDP control within the same network. In this project, I'd like to compose scripts to test WiZ light's basic features automatically using Python. 
(Note: this is a side-project for learning purpose.)

## Key features of the script
### Basic interface
- Run Python script in CLI (no parameter supported)
### Basic features
1. Run basic feature test as below "Features" section shows
2. Generate a test report as: "Total x paased, and y failed"

### Advanced interface
1. CLI with parameters
2. GUI
### Advanced features
1. Users are allowed to input ip, select device types (which links to differenct test module)
2. Better report format


## Project plan
- **Phase 1:** A straitforward test => **[basic.py](https://github.com/maudes/wiz-light-local-test-script/blob/main/basic.py)**
- **Phase 2:** Wrap-up the code into a more clean and maintanence-friendly format with results output => **[basic_refactor.py](https://github.com/maudes/wiz-light-local-test-script/blob/main/basic_refactor.py)**
- **Phase 3:** Expand the basic test script using Pytest
- **Phase 4:** Create a CLI tool version
- **Phase 5:** Create a simple frontend for users to trigger the auto-testing

## Features 
1. Change status: ON/OFF
2. Change color: R, G, B, CW, WW (0 - 225)
3. Change dimming: 0 - 100
4. Change temperature: 2700 - 6500
5. Change light modes: scene_id 1 - 28 (should have more)

