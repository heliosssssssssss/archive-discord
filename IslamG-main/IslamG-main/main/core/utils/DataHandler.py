import os, time, pprint, math, json

class DataHandler:

    global analyticsDB
    global errorsDB
    global userstatsDB
    global versioninfoDB

    analyticsDB = r"main/IslamG/main/core/secure/data/analyticsDB.json"
    errorsDB = r"main/IslamG/main/core/secure/data/errorsDB.json"
    userstatsDB = r"main/IslamG/main/core/secure/data/userstatsDB.json"
    versioninfoDB = r"main/IslamG/main/core/secure/data/versioninfoDB.json"

    def __init__(self) -> None:
        print("[utils.Data Handler]: launched successfully")

        
    def DataIntegrityCheck(): # Cgecks all the data files are in proper codition
        print("[utils.Data Handler]: Checking data integrity")

        # [list of active data files]

        IO_analyticsDB = r"main/IslamG/main/core/secure/data/analyticsDB.json"
        IO_errorsDB = r"main/IslamG/main/core/secure/data/errorsDB.json"
        IO_userstatsDB = r"main/IslamG/main/core/secure/data/userstatsDB.json"
        IO_versioninfoDB = r"main/IslamG/main/core/secure/data/versioninfoDB.json"

        CHECK_analyticsDB = os.path.isfile(IO_analyticsDB)
        CHECK_errorsDB = os.path.isfile(IO_errorsDB)
        CHECK_userstatsDB = os.path.isfile(IO_userstatsDB)
        CHECK_versioninfoDB = os.path.isfile(IO_versioninfoDB)

        if CHECK_analyticsDB and CHECK_errorsDB and CHECK_userstatsDB and CHECK_versioninfoDB == True:
            print('[utils.Data Handler]: File Integrity is good')
            return True
        else: 
            print('[utils.Data Handler]: File Integrity is bad')
            return False 
        
    def read_file(file_name=None):
        if file_name == None:
            return
        
        r = open(file_name, 'r')
        return r.read()
    