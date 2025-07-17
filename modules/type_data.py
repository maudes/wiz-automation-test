# common features: change RGB, 
# lightmodes: 1 - 5, 7, 8, 19 - 28 (brightness, speed)

# dictionary
color_test_case = {
    "get_state": {
        "method": "getPilot",
        "env": "pro"
        },
    "turn_off": {
        "method": "setPilot",
        "env": "pro",
        "params": {"state": False}
        },
    "turn_on_brightness": {
        "method": "setPilot",
        "env": "pro",
        "params": {
            "state": True,
            "dimming": 38
            }
        },
    "change_temp_warm": {
        "method": "setPilot",
        "env": "pro",
        "params": {
            "state": True,
            "temp": 4200,
            "dimming": 55
            }
        },
    "change_temp_cold": {
        "method": "setPilot",
        "env": "pro",
        "params": {
            "state": True,
            "temp": 5500,
            "dimming": 70
            }
        },
    "scene_relax": {
        "method": "setPilot",
        "env": "pro",
        "params": {
            "state": True,
            "sceneId": 16,
            "dimming": 38
            }
        },
    "scene_ocean": {
        "method": "setPilot",
        "env": "pro",
        "params": {
            "state": True,
            "sceneId": 1,
            "dimming": 45,
            "speed": 100
            }
        },
    "scene_romance": {
        "method": "setPilot",
        "env": "pro",
        "params": {
            "state": True,
            "sceneId": 2,
            "dimming": 50,
            "speed": 100
            }
        },
    "scene_mojito": {
        "method": "setPilot",
        "env": "pro",
        "params": {
            "state": True,
            "sceneId": 25,
            "dimming": 50,
            "speed": 100
            }
        },
    "change_rgb": {
        "method": "setPilot",
        "env": "pro",
        "params": {
            "state": True,
            "r": 100,
            "g": 0,
            "b": 140,
            "cw": 150,
            "ww": 0,
            "dimming": 20,
        }
    }
}


# common features: change temperate 2700 - 6500
# # change temperature lightmodes: 6, 11-16, 18 (brightness, speed)

tuneable_test_case = {
    "get_state": {
        "method": "getPilot",
        "env": "pro"
    },
    "turn_off": {
        "method": "setPilot",
        "env": "pro",
        "params": {
            "state": False
        }
    },
    "turn_on_brightness": {
        "method": "setPilot",
        "env": "pro",
        "params": {
            "state": True,
            "dimming": 38
        }
    },
    "change_temp_warm": {
        "method": "setPilot",
        "env": "pro",
        "params": {
            "state": True,
            "temp": 4200,
            "dimming": 55
        }
    },
    "change_temp_cold": {
        "method": "setPilot",
        "env": "pro",
        "params": {
            "state": True,
            "temp": 5500,
            "dimming": 70
        }
    },
    "scene_daylight": {
        "method": "setPilot",
        "env": "pro",
        "params": {
            "state": True,
            "sceneId": 21,
            "dimming": 38
        }
    }, 
    "scene_relax": {
        "method": "setPilot",
        "env": "pro",
        "params": {
            "state": True,
            "sceneId": 16,
            "dimming": 38
        }
    }
}


# common features: on/off, change brightness
dimmable_test_case = {
    "get_state": {
        "method": "getPilot",
        "env": "pro"
    },
    "turn_off": {
        "method": "setPilot",
        "env": "pro",
        "params": {
            "state": False
        }
    },
    "turn_on_brightness": {
        "method": "setPilot",
        "env": "pro",
        "params": {
            "state": True,
            "dimming": 38
        }
    }
}
