# wiz-light-local-test-script
A python script for testing WiZ light local features

## Features 
- Change status: ON/OFF
- Change color: R, G, B, CW, WW (0 - 225)
- Change dimming: 0 - 100
- Change temperature: 2700 - 6500
- Change light modes: scene_id 1 - 28 (should have more)

## Test Cases should be based on Traits
- "is_dimmable": true
- "is_tunable_white": true
- "is_tunable_color": true
