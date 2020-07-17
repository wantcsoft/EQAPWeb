import sqlite3

from Models.DeviceInfoModel import DeviceInfoModel
from Models.ProtocolFieldInfo import ProtocolFieldInfo
from Models.ProtocolInfo import ProtocolInfo
from Models.ProtocolMsgInfo import ProtocolMsgInfo
from Models.SysConfigInfo import SysConfigInfo


class PublicMethods:
    def __init__(self,strDBFilePath):
        self.DBFileName = strDBFilePath

    def GetSystemConfig(self):

        sqlCmdTxt = '''SELECT SaveLog,TerminalID,TimeSequence,RetryTimes,DataKeptDays,LastDataCleanDate FROM BSC_SysConfig'''
        conn = sqlite3.connect(self.DBFileName)
        result = conn.execute(sqlCmdTxt).fetchone()

        if result is None:
            print('None')
            return SysConfigInfo(0, 0, 0, 0, 7, '2000-01-01')
        else:
            return SysConfigInfo(result[0], result[1], result[2], result[3], result[4], result[5])

    def UpdateSysConfig(self,nSaveLog,nTerminalID,nTimeSequence,nRetryTims,nDataKeptDays,dtLastCleanDate):
        sqlCmdTxt = "UPDATE BSC_SysConfig SET SaveLog = {}, TerminalID = {}, TimeSequence = {}, RetryTims = {},DataKeptDays={},LastDataCleanDate='{}'".format(nSaveLog,nTerminalID,nTimeSequence,nRetryTims,nDataKeptDays,dtLastCleanDate)
        conn = sqlite3.connect(self.DBFileName)
        conn.execute(sqlCmdTxt)
        conn.commit()
        conn.close()

    def GetDeviceInfoFromDB(self):
        device = DeviceInfoModel()

        sqlCmdQuery = '''SELECT DeviceID,DeviceName,DeviceSerialNo,DeviceDesc,DeviceLocation,ServerIP,ServerPort,TimeOut FROM BSC_DeviceInfo'''
        try:
            conn = sqlite3.connect(self.DBFileName)
            cursor = conn.cursor()
            cursor.execute(sqlCmdQuery)
            result = cursor.fetchone()

            if result is not None:
                device.InitDeviceInfo(result[0],result[1],result[2],result[3],result[4],result[5],result[6],result[7])
        except BaseException as e:
            print("Get communication data from DB with EXCEPTION:".format(e))
        finally:
            cursor.close()
            conn.close()

        return device

    def UpdateDeviceInfoToDB(self,nDeviceID,strDeviceName,strDeviceSerialNo,strDeviceDesc,strDeviceLocation,strServerIP,nServerPort,fTimeout):
        bRetValue = False
        sqlCmdUpdate = '''UPDATE BSC_DeviceInfo SET DeviceName = '{}', DeviceSerialNo = '{}', DeviceDesc = '{}',DeviceLocation = '{}',ServerIP = '{}',ServerPort = {},TimeOut = '{}' WHERE DeviceID = {} '''.format(strDeviceName,strDeviceSerialNo,strDeviceDesc,strDeviceLocation,strServerIP,nServerPort,fTimeout,nDeviceID)
        try:
            conn = sqlite3.connect(self.DBFileName)
            cursor = conn.cursor()
            cursor.execute(sqlCmdUpdate)
            bRetValue = True
        except BaseException as e:
            self.Logger.error("Get communication data from DB with EXCEPTION:".format(e))
        finally:
            cursor.close()
            conn.commit()
            conn.close()
        return bRetValue

    def GetProtocolList(self):
        sqlCmdProtocolQuery = '''SELECT ProtocolID,ProtocolName,ProtocolType,IsEnabled FROM BSC_ProtocolInfo'''
        lstProtocolModel = []
        try:
            conn = sqlite3.connect(self.DBFileName)
            lstProtocol = conn.execute(sqlCmdProtocolQuery).fetchall()

            for prot in lstProtocol:
                protocol = ProtocolInfo()
                protocol.InitProtocolInfo(prot[0],prot[1],prot[2],prot[3])
                lstProtocolModel.append(protocol.toJson())
        except BaseException as e:
            print("Get Protocol list from DB with EXCEPTION:".format(e))
        finally:
            conn.close()
        return lstProtocolModel

    def UpdateProtocolInfo(self, ProtocolID, ProtocolName, ProtocolType, IsEnabled):
        sqlCmdTxt = "UPDATE BSC_ProtocolInfo SET ProtocolName = '{}', ProtocolType = '{}', IsEnabled = {} where ProtocolID = {}".format(ProtocolName, ProtocolType, IsEnabled, ProtocolID)
        conn = sqlite3.connect(self.DBFileName)
        conn.execute(sqlCmdTxt)
        conn.commit()
        conn.close()

    def SaveProtocolInfo(self, ProtocolName, ProtocolType, IsEnabled):
        sqlCmdTxt = "INSERT INTO BSC_ProtocolInfo(ProtocolName,ProtocolType,IsEnabled)VALUES('{}','{}',{})".format(ProtocolName,ProtocolType,IsEnabled)
        conn = sqlite3.connect(self.DBFileName)
        conn.execute(sqlCmdTxt)
        conn.commit()

    def DeleteProtocolInfo(self, ProtocolID):
        sqlCmdTxt1 = "DELETE FROM BSC_ProtocolInfo WHERE ProtocolID = {}".format(ProtocolID)
        sqlCmdTxt2 = "DELETE FROM BSC_ProtocolMsgInfo WHERE ProtocolID = {}".format(ProtocolID)
        sqlCmdTxt3 = "DELETE FROM BSC_BasicProtocolFieldInfo WHERE ProtocolID = {}".format(ProtocolID)
        conn = sqlite3.connect(self.DBFileName)
        conn.execute(sqlCmdTxt1)
        conn.execute(sqlCmdTxt2)
        conn.execute(sqlCmdTxt3)
        conn.commit()

    def GetMessageList(self, ProtocolID):
        sqlCmdProtocolQuery = '''SELECT MsgID,ProtocolID,ProtocolMsgType,MsgHeader,MsgEndFlag,FieldCount,UploadFormat,ToBeUpload,SampleIDFrom FROM BSC_ProtocolMsgInfo where ProtocolID = {}'''.format(ProtocolID)
        lstProtocolMsg = []
        try:
            conn = sqlite3.connect(self.DBFileName)
            lstProtocol = conn.execute(sqlCmdProtocolQuery).fetchall()

            for prot in lstProtocol:
                protocolMsg = ProtocolMsgInfo(prot[0],prot[1],prot[2],prot[3],prot[4],prot[5],prot[6],prot[7],prot[8])
                lstProtocolMsg.append(protocolMsg.toJson())
        except BaseException as e:
            print("Get ProtocolMessage list from DB with EXCEPTION:".format(e))
        finally:
            conn.close()
        return lstProtocolMsg

    def UpdateMessageInfo(self, ProtocolMsgType, MsgHeader, MsgEndFlag, FieldCount, UploadFormat, ToBeUpload, SampleIDFrom, ProtocolID, MsgID):
        sqlCmdProtocolQuery = '''UPDATE BSC_ProtocolMsgInfo
        SET ProtocolMsgType={},MsgHeader='{}',MsgEndFlag='{}',FieldCount={}, UploadFormat='{}',ToBeUpload={},
        SampleIDFrom='{}' where ProtocolID = {} AND MsgID={}'''\
            .format(ProtocolMsgType, MsgHeader, MsgEndFlag, FieldCount, UploadFormat, ToBeUpload, SampleIDFrom, ProtocolID, MsgID)
        conn = sqlite3.connect(self.DBFileName)
        conn.execute(sqlCmdProtocolQuery)
        conn.commit()
        conn.close()

    def SaveMessageInfo(self, ProtocolMsgType, MsgHeader, MsgEndFlag, FieldCount, UploadFormat,
                        ToBeUpload, SampleIDFrom, ProtocolID):
        sqlCmdTxt = '''INSERT INTO BSC_ProtocolMsgInfo
                    (ProtocolMsgType, MsgHeader, MsgEndFlag, FieldCount, UploadFormat, ToBeUpload,
                    SampleIDFrom, ProtocolID)
                    VALUES({},'{}','{}',{},'{}',{},'{}',{})'''.format(ProtocolMsgType, MsgHeader, MsgEndFlag,
                                                                 FieldCount, UploadFormat, ToBeUpload, SampleIDFrom,
                                                                 ProtocolID)
        conn = sqlite3.connect(self.DBFileName)
        conn.execute(sqlCmdTxt)
        conn.commit()

    def DeleteMessageInfo(self, MsgID):
        sqlCmdTxt1 = "DELETE FROM BSC_ProtocolMsgInfo WHERE MsgID = {}".format(MsgID)
        sqlCmdTxt2 = "DELETE FROM BSC_BasicProtocolFieldInfo WHERE MsgID = {}".format(MsgID)
        conn = sqlite3.connect(self.DBFileName)
        conn.execute(sqlCmdTxt1)
        conn.execute(sqlCmdTxt2)
        conn.commit()

    def GetFieldList(self, ProtocolID, MsgID):
        sqlCmdProtocolFieldListQuery = '''SELECT FieldID, ProtocolID, MsgID, FieldName, FieldType, FieldIndex, 
                 StartPos,FieldLen, ValueRange, ToBeCleared, IsRepeat, IsUpload 
                 FROM BSC_BasicProtocolFieldInfo 
                 where ProtocolID = {} AND MsgID = {}'''.format(ProtocolID, MsgID)
        lstProtocolField = []
        try:
            conn = sqlite3.connect(self.DBFileName)
            lstProtocol = conn.execute(sqlCmdProtocolFieldListQuery).fetchall()
            for prot in lstProtocol:
                protocolField = ProtocolFieldInfo(prot[0], prot[1], prot[2], prot[3], prot[4], prot[5], prot[6],
                                                  prot[7], prot[8], prot[9], prot[10], prot[11])
                lstProtocolField.append(protocolField.tojson())
        except BaseException as e:
            print("Get ProtocolField list from DB with EXCEPTION:".format(e))
        finally:
            conn.close()
        return lstProtocolField

    def UpdateFieldInfo(self, FieldName, FieldType, FieldIndex, StartPos,FieldLen, ValueRange, ToBeCleared,
                        IsRepeat, IsUpload, ProtocolID, MsgID, FieldID):
        sqlCmdProtocolUpdate = '''UPDATE BSC_BasicProtocolFieldInfo
                SET FieldName='{}', FieldType='{}', FieldIndex={}, StartPos={},FieldLen={}, ValueRange='{}', 
                ToBeCleared={}, IsRepeat={}, IsUpload={}
                where ProtocolID = {} AND MsgID={} AND FieldID={}''' .format(FieldName, FieldType, FieldIndex,
                 StartPos,FieldLen, ValueRange, ToBeCleared, IsRepeat, IsUpload, ProtocolID, MsgID, FieldID)
        conn = sqlite3.connect(self.DBFileName)
        conn.execute(sqlCmdProtocolUpdate)
        conn.commit()
        conn.close()

    def SaveFieldInfo(self, FieldName, FieldType, FieldIndex, StartPos,FieldLen, ValueRange, ToBeCleared,
                        IsRepeat, IsUpload, ProtocolID, MsgID):
        sqlCmdProtocolUpdate = '''INSERT INTO BSC_BasicProtocolFieldInfo
                        (FieldName, FieldType, FieldIndex, StartPos,FieldLen, ValueRange, 
                        ToBeCleared, IsRepeat, IsUpload,ProtocolID, MsgID)
                        VALUES ('{}','{}',{},{},{},'{}',{},{},{},{},{})'''.format(FieldName, FieldType, FieldIndex,
                                                                                    StartPos, FieldLen, ValueRange,
                                                                                    ToBeCleared, IsRepeat, IsUpload,
                                                                                    ProtocolID, MsgID)
        conn = sqlite3.connect(self.DBFileName)
        conn.execute(sqlCmdProtocolUpdate)
        conn.commit()

    def DeleteFieldInfo(self, FieldID):
        sqlCmdTxt = "DELETE FROM BSC_BasicProtocolFieldInfo WHERE FieldID = {}".format(FieldID)
        conn = sqlite3.connect(self.DBFileName)
        conn.execute(sqlCmdTxt)
        conn.commit()



