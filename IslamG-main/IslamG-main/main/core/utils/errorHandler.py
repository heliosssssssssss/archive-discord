import discord
import os, time, pprint, math, json

# [IMPORTS V2]

from discord.ext import commands
from DataHandler import DataHandler


class ErrorHandler:

    global errors_db
    errors_db = 'main\IslamG\main\core\secure\data\errorsDB.json'

    def __init__(self) -> None:
        print("[utils.Error Handler]: launched successfully")

    
    def isErrorValid(error_number): # checks if the error_nunber is a valid error param
        IO_errors_db = json.loads(DataHandler.read_file(errors_db))
        if error_number > IO_errors_db['error_count']:
            return False
        else:
            return True
        
    def getErrorInfo(error_number):
        if ErrorHandler.isErrorValid(error_number) == True:
            IO_errors_db = json.loads(DataHandler.read_file(errors_db))
        else: 
            print("[utils.Error Handler]: uh oh.. :(  // problem with getErrorInfo()")
            return False

ErrorHandler.getErrorInfo(56)
