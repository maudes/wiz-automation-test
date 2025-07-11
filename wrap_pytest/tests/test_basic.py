import pytest


def test_state(wiz_client):
    # Action
    msg = {
        "method": "getPilot",
        "env": "pro"
    }
    response = wiz_client(msg)
    # Assert
    assert response is not None, "Error message, we lost WiZ."


def test_off(wiz_client):
    # Turn off
    msg = {
        "method": "setPilot",
        "env": "pro",
        "params": {
            "state": False
        }
    }
    response = wiz_client(msg)
    assert response is not None
    assert "result" in response and "success" in response["result"] and response["result"]["success"] is True


def test_white(wiz_client):
    # Turn on with white light
    msg = {
        "method": "setPilot",
        "env": "pro",
        "params": {
            "state": True,
            "temp": 6500,
            "dimming": 30
        }
    }
    response = wiz_client(msg)
    assert response is not None
    assert "result" in response and "success" in response["result"] and response["result"]["success"] is True


def test_lightmode(wiz_client):
    # Change light mode
    msg = {
        "method": "setPilot",
        "env": "pro",
        "params": {
            "state": True,
            "sceneId": 21,
            "dimming": 60,
            "speed": 100,
        }
    }
    response = wiz_client(msg)
    assert response is not None
    assert "result" in response and "success" in response["result"] and response["result"]["success"] is True


def test_rgb(wiz_client):
    # Change RGB
    msg = {
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
    response = wiz_client(msg)
    assert response is not None
    assert "result" in response and "success" in response["result"] and response["result"]["success"] is True
