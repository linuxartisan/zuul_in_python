from project import processCommand, createRooms, checkWinningCondition, goRoom
import project
from Command import Command
from Item import Item
from Parser import Parser
import pytest

def test_createRooms():
    # initial phase
    assert project.currentRoom is None
    assert project.finalRoom is None

    # initialise rooms
    createRooms()
    assert project.currentRoom is not None
    assert project.finalRoom is not None

    # test starting and final room
    assert project.currentRoom.description == 'outside the hospital'
    assert project.finalRoom.description == 'in the ICU'

    # test no winning items present in final room at start
    assert project.finalRoom.getItem('Ventilator') is None
    assert project.finalRoom.getItem('Insulin_ump') is None

    # test rooms have exit(s)
    assert len(project.currentRoom.getAllExitDirections()) > 0
    assert len(project.finalRoom.getAllExitDirections()) > 0

    # test item (key) present inside starting room
    assert project.currentRoom.getItem('Key1') is not None

def test_processCommand(capfd):
    # setup
    createRooms()
    parser = Parser()

    # test for no command
    command = None
    assert processCommand(command) is False

    # test for unknown command
    command = parser.getCommand('gibberish')
    assert processCommand(command) is False

    ## test go command ##
    # test no direction provided
    out, err = capfd.readouterr()
    command = parser.getCommand('go')
    processCommand(command)
    out, err = capfd.readouterr()
    assert out == 'Go where?\n'

    # test locked exit
    command = parser.getCommand('go north')
    processCommand(command)
    out, err = capfd.readouterr()
    assert project.currentRoom.isExitLocked('north')
    assert out == 'The door is locked. Need to open it with a key.\n'
    # test non-existant exit
    with pytest.raises(ValueError):
        project.currentRoom.isExitLocked('south') # no exit south

    # test unlocking exit
    command = parser.getCommand('take key1')
    processCommand(command)
    command = parser.getCommand('use key1')
    processCommand(command)
    assert not project.currentRoom.isExitLocked('north')
    # test unlocking non-existant exit
    with pytest.raises(ValueError):
        project.currentRoom.unlockExit('south') # no exit south

    # test changing rooms
    command = parser.getCommand('go north')
    processCommand(command)
    assert project.currentRoom.description == 'in the waiting area'


def test_checkWinningCondition():
    # setup
    createRooms()

    # game just started, so not yet won
    assert not checkWinningCondition()

    # quit the game
    cmd = Command("quit", None)
    processCommand(cmd)
    assert not checkWinningCondition()

    # simulate winning
    insulinPump = Item("Insulin_Pump", "required for diabetic patients")
    ventilator = Item("Ventilator", "used for patients with weak lungs")
    project.finalRoom.addItem(insulinPump)
    project.finalRoom.addItem(ventilator)
    assert checkWinningCondition()
