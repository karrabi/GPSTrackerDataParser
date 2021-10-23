from crc_itu import crc16

ProtocolDescription = {
    '0x01': 'Login Information'
    , '0x22': 'Positioning Data(UTC)'
    , '0x12': 'Positioning Data'
    , '0x13': 'Heartbeat Packet'
    , '0x21': 'Online Command Response of Terminal'
    , '0x15': 'Online Command Response of Terminal'
    , '0x26': 'Alarm Data(UTC)'
    , '0x19': 'LBS Alarm'
    , '0x27': 'Alarm Data (UTC) apply to HVT001'
    , '0x80': 'Online Command'
    , '0x8a': 'Time Check Packet'
    , '0x2c': 'WiFi Communicatin Protocol'
    , '0x94': 'Information Transmission Packet'
    , '0x9b': 'External device transfer Packet(apply X3)'
    , '0x9c': 'External module transm'
}

AlarmDescription = {
    '0x00': 'Normal'
    , '0x01': 'SOS'
    , '0x02': 'Power Cut Alarm'
    , '0x03': 'Vibration Alarm'
    , '0x04': 'Enter Fence Alarm'
    , '0x05': 'Exit Fence Alarm'
    , '0x06': 'Over Speed Alarm'
    , '0x09': 'Moving Alarm'
    , '0x0a': 'Enter GPS Dead Zone Alarm'
    , '0x0b': 'Exit GPS Dead Zone Alarm'
    , '0x0c': 'Power On Alarm'
    , '0x0d': 'GPS First Fix Notice'
    , '0x0e': 'External Low Battery Alarm'
    , '0x0f': 'External Low Battery Protection Alarm'
    , '0x10': 'SIM Change Notice'
    , '0x11': 'Power Off Alarm'
    , '0x12': 'AirPlane Mode Alarm'
    , '0x13': 'Disassemble Alarm'
    , '0x14': 'Door Alarm'
    , '0x15': 'Shutdown Alarm due to Low Power'
    , '0x16': 'Sound Alarm'
    , '0x17': 'Pseudo base-station Alarm'
    , '0x18': 'Open Cover Alarm'
    , '0x19': 'Internal Low Battery Alarm'
    , '0x20': 'Sleep Mode Alarm'
    , '0x21': 'Reserve'
    , '0x22': 'Reserve'
    , '0x23': 'Fall Alarm'
    , '0x24': 'Insert Charger Alarm'
    , '0x29': 'Harsh Acceleration Alarm'
    , '0x30': 'Harsh Breaking Alarm'
    , '0x2a': 'Sharp Left Turn Alarm'
    , '0x2b': 'Sharp Right Turn Alarm'
    , '0x2c': 'Sharp  Crash Alarm'
    , '0x2d': 'Vehicle Rolling Alarm'
    , '0x4b': 'Tilting Alarm'
    , '0x4c': 'Sharp Turn Alarm'
    , '0x4d': 'Abrupt lane switching Alarm'
    , '0x4e': 'Vehicle Stability'
    , '0x4f': 'Vehicle Angle Abnormality'
    , '0x32': 'Pull Alarm'
    , '0x3e': 'Press the Button To Upload Alarm'
    , '0xfe': 'ACC ON Alarm'
    , '0xff': 'ACC OFF Alarm'
}

LanguageDescription = {
    '0x01': 'Chinese'
    , '0x02': 'English'
    , '0x00': 'No Need To Reply'
}

Built_inBatteryVoltageLevelDescription = {
    '0x00': 'No Power'
    , '0x01': 'Extremely Low Battery'
    , '0x02': 'Very Low Battery'
    , '0x03': 'Low Battery'
    , '0x04': 'Medium'
    , '0x05': 'High'
    , '0x06': 'Full'
}

GSMSignalStrengthDescription = {
    '0x00': 'NO Signal'
    , '0x01': 'Extremely Low Signal'
    , '0x02': 'Weak Signal'
    , '0x03': 'Good Signal'
    , '0x04': 'Strong Signal'
}

ACCDescription = {
    '0x00': 'ACC Low'
    , '0x01': 'ACC High'
}

DataUploadModeDescription = {
    '0x00': 'Upload By Time Interval'
    , '0x01': 'Upload By Distance Interval'
    , '0x02': 'Inflection Point Upload'
    , '0x03': 'ACC Status Upload'
    , '0x04': 'Re-Upload the Last GPS point when back to Static'
    , '0x05': 'Upload the last effective point when network recovers'
    , '0x06': 'Update ephemeris and upload GPS data compulsorily'
    , '0x07': 'Upload location when side key triggered'
    , '0x08': 'Upload location after power on'
    , '0x09': 'Unused'
    , '0x0a': 'Upload the last longitude and latitude when device is static; time updated'
    , '0x0d': 'Upload the last longitude and latitude when device is static'
    , '0x0e': 'Gpsdup upload (Upload regularly in a static state.)'
}

GPSRealTimeReUploadDescription = {
    '0x00': 'Real-Time Upload'
    , '0x01': 'Re-Upload'
}


def GenerateCRC(string):
    CRC = hex(crc16(bytes.fromhex(string)))
    return str(CRC[2:].zfill(4))


def hex_to_string_int(hex):
    return str(int(hex[2:].replace(' 0x', ''), 16))


def hex_to_string(hex):
    return str(hex[2:].replace(' 0x', ''))


def hex_to_bin(h):
    return bin(int(h, 16))[2:].zfill(len(h) * 4)


def Process_QuantityOfGPSSatellites(quantity_of_gps_satellites):
    GPSInformationLength = quantity_of_gps_satellites[2]
    PositioningSatellitesNumber = int(quantity_of_gps_satellites[3], 16)
    return GPSInformationLength, str(PositioningSatellitesNumber)


def Process_DateTime(date_time):
    pure_date_time = hex_to_string(hex=date_time)
    year = int(pure_date_time[0:2], 16)
    month = int(pure_date_time[2:4], 16)
    day = int(pure_date_time[4:6], 16)
    hour = int(pure_date_time[6:8], 16)
    minute = int(pure_date_time[8:10], 16)
    second = int(pure_date_time[10:12], 16)
    concated = str(year) + '/' + str(month) + '/' + str(day) + ' - ' + str(hour) + ':' + str(minute) + ':' + str(second)
    return concated


def Process_LatitudeOrLongitude(latitude_or_longitude):
    pure_hex_latitude_or_longitude = hex_to_string(hex=latitude_or_longitude)
    int_latitude_or_longitude = int(pure_hex_latitude_or_longitude, 16) / 1800000
    return str(int_latitude_or_longitude)


def Process_CourseAndStatus(course_and_status):
    pure_hex_course_and_status = hex_to_string(hex=course_and_status)
    bin_course_and_status = hex_to_bin(h=pure_hex_course_and_status)
    GPSPositioningMode = 'Differential' if bin_course_and_status[5] else 'RealTime'
    GPSPositioningStatus = 'Positioned' if bin_course_and_status[4] else 'NOT Positioned'
    LongitudeDirection = 'West' if bin_course_and_status[3] else 'East'
    LatitudeDirection = 'North' if bin_course_and_status[2] else 'South'
    bin_Course = bin_course_and_status[8:15] + bin_course_and_status[0:1]
    return GPSPositioningMode, GPSPositioningStatus, LongitudeDirection, LatitudeDirection, str(int(bin_Course, 2))


def Process_TerminalInformation(terminal_information):
    DecodedTerminalInformation = {}
    pure_hex_terminal_information = hex_to_string(hex=terminal_information)
    bin_terminal_information = hex_to_bin(h=pure_hex_terminal_information)
    Defence = 'Activated' if bin_terminal_information[0] else 'Deactivated'
    ACC = 'High' if bin_terminal_information[1] else 'Low'
    ChargeStatus = 'Charging' if bin_terminal_information[2] else 'NOT Charging'
    CriticalAlarmPart = int(bin_terminal_information[3:6], 2)
    if CriticalAlarmPart == 0:
        CriticalAlarm = 'Normal'
    elif CriticalAlarmPart == 1:
        CriticalAlarm = 'Vibration Alarm'
    elif CriticalAlarmPart == 2:
        CriticalAlarm = 'Power Cut Alarm'
    elif CriticalAlarmPart == 3:
        CriticalAlarm = 'Low Battery Alarm'
    elif CriticalAlarmPart == 4:
        CriticalAlarm = 'SOS Alarm'
    else:
        CriticalAlarm = 'ERROR'
    GPSTracking = 'ON' if bin_terminal_information[6] else 'OFF'
    OilAndElectricity = 'Differential' if bin_terminal_information[7] else 'RealTime'

    DecodedTerminalInformation['TerminalInformation_Defence'] = Defence
    DecodedTerminalInformation['TerminalInformation_ACC'] = ACC
    DecodedTerminalInformation['TerminalInformation_ChargeStatus'] = ChargeStatus
    DecodedTerminalInformation['TerminalInformation_CriticalAlarm'] = CriticalAlarm
    DecodedTerminalInformation['TerminalInformation_GPSTracking'] = GPSTracking
    DecodedTerminalInformation['TerminalInformation_OilAndElectricity'] = OilAndElectricity
    return DecodedTerminalInformation


def Process_Alarm_Language(alarm_language):
    DecodedAlarm_Language = {}
    alarm_language_byte1 = alarm_language[0:4]
    alarm_language_byte2 = alarm_language[5:9]
    DecodedAlarm_Language['Alarm_Language_Alarm Description'] = AlarmDescription[alarm_language_byte1]
    DecodedAlarm_Language['Alarm_Language_Language'] = LanguageDescription[alarm_language_byte2]
    return DecodedAlarm_Language


def SplitData(data, bytes, from_start=True):
    splittedData = ''

    if from_start:
        for byte in range(bytes):
            splittedData = splittedData + '0x' + data[byte * 2:(byte * 2) + 2] + ' '
        remainData = data[bytes * 2:]
    else:
        for byte in range(bytes):
            splittedData = '0x' + data[len(data) - (byte * 2) - 2:len(data) - (byte * 2)] + ' ' + splittedData
        remainData = data[:len(data) - (bytes * 2)]

    return splittedData.strip(), remainData


def process_InformationContent(data, protocol_number):
    Response = 'NOTHING'
    DecodedInformationContent = {}
    if protocol_number == '0x01':  # Login Packet

        TerminalID, remainedData = SplitData(data=data, bytes=8)
        ModelIdentificationCode, remainedData = SplitData(data=remainedData, bytes=2)
        TimeZoneLanguage, remainedData = SplitData(data=remainedData, bytes=2)
        DecodedInformationContent['InformationContent_TerminalID'] = TerminalID
        DecodedInformationContent['InformationContent_ModelIdentificationCode'] = ModelIdentificationCode
        DecodedInformationContent['InformationContent_TimeZoneLanguage'] = TimeZoneLanguage

        ErrorCheck, remainedData = SplitData(data=remainedData, bytes=2, from_start=False)
        InformationSerialNumber, remainedData = SplitData(data=remainedData, bytes=2, from_start=False)
        packetLength = '0x05'

        CRCResponseString = packetLength + ' ' + protocol_number + ' ' + InformationSerialNumber
        CRCString = hex_to_string(CRCResponseString)
        CRC = GenerateCRC(CRCString)
        Response = '7878' + CRCString + CRC + '0d0a'
    elif protocol_number == '0x22' or protocol_number == '0x12':  # Positioning Data Packet

        DateTime, remainedData = SplitData(data=data, bytes=6)
        QuantityOfGPSSatellites, remainedData = SplitData(data=remainedData, bytes=1)
        Latitude, remainedData = SplitData(data=remainedData, bytes=4)
        Longitude, remainedData = SplitData(data=remainedData, bytes=4)
        Speed, remainedData = SplitData(data=remainedData, bytes=1)
        Course_Status, remainedData = SplitData(data=remainedData, bytes=2)
        MCC, remainedData = SplitData(data=remainedData, bytes=2)
        MNC, remainedData = SplitData(data=remainedData, bytes=1)
        LAC, remainedData = SplitData(data=remainedData, bytes=2)
        CellID, remainedData = SplitData(data=remainedData, bytes=3)
        ACC, remainedData = SplitData(data=remainedData, bytes=1)
        DataUploadMode, remainedData = SplitData(data=remainedData, bytes=1)
        GPSRealTimeReUpload, remainedData = SplitData(data=remainedData, bytes=1)
        Mileage, remainedData = SplitData(data=remainedData, bytes=4)

        DecodedInformationContent['DateTime'] = DateTime
        DecodedInformationContent['UTC DateTime'] = Process_DateTime(DateTime)
        DecodedInformationContent['QuantityOfGPSSatellites'] = QuantityOfGPSSatellites
        GPSInformationLength, PositioningSatellitesNumber = Process_QuantityOfGPSSatellites(
            quantity_of_gps_satellites=QuantityOfGPSSatellites)
        DecodedInformationContent['QuantityOfGPSSatellites_GPSInformationLength'] = GPSInformationLength
        DecodedInformationContent['QuantityOfGPSSatellites_PositioningSatellitesNumber'] = PositioningSatellitesNumber
        DecodedInformationContent['Latitude'] = Process_LatitudeOrLongitude(latitude_or_longitude=Latitude)
        DecodedInformationContent['Longitude'] = Process_LatitudeOrLongitude(latitude_or_longitude=Longitude)
        DecodedInformationContent['Speed'] = hex_to_string_int(Speed)
        DecodedInformationContent['Course_Status'] = Course_Status
        GPSPositioningMode, GPSPositioningStatus, LongitudeDirection, LatitudeDirection, Course = \
            Process_CourseAndStatus(course_and_status=Course_Status)
        DecodedInformationContent['Course_Status_GPSPositioningMode'] = GPSPositioningMode
        DecodedInformationContent['Course_Status_GPSPositioningStatus'] = GPSPositioningStatus
        DecodedInformationContent['Course_Status_LongitudeDirection'] = LongitudeDirection
        DecodedInformationContent['Course_Status_LatitudeDirection'] = LatitudeDirection
        DecodedInformationContent['Course_Status_Course'] = Course
        DecodedInformationContent['MCC'] = hex_to_string_int(MCC)
        DecodedInformationContent['MNC'] = hex_to_string_int(MNC)
        DecodedInformationContent['LAC'] = hex_to_string_int(LAC)
        DecodedInformationContent['CellID'] = hex_to_string_int(CellID)
        DecodedInformationContent['ACC'] = ACC
        DecodedInformationContent['ACCDescription'] = ACCDescription[ACC]
        DecodedInformationContent['DataUploadMode'] = DataUploadMode
        DecodedInformationContent['DataUploadModeDescription'] = DataUploadModeDescription[DataUploadMode]
        DecodedInformationContent['GPSRealTimeReUpload'] = GPSRealTimeReUpload
        DecodedInformationContent['GPSRealTimeReUploadDescription'] = GPSRealTimeReUploadDescription[
            GPSRealTimeReUpload]
        if len(Mileage.replace('0x', '').strip()) > 0:
            DecodedInformationContent['Mileage'] = hex_to_string_int(Mileage)

    elif protocol_number == '0x13':  # Heartbeat Packet

        TerminalInformationContent, remainedData = SplitData(data=data, bytes=1)
        Built_inBatteryVoltageLevel, remainedData = SplitData(data=remainedData, bytes=1)
        GSMSignalStrength, remainedData = SplitData(data=remainedData, bytes=1)
        Language_ExtendedPort_Status, remainedData = SplitData(data=remainedData, bytes=2)
        DecodedInformationContent['TerminalInformationContent'] = TerminalInformationContent
        DecodedInformationContent['Built_inBatteryVoltageLevel'] = Built_inBatteryVoltageLevel
        DecodedInformationContent['GSMSignalStrength'] = GSMSignalStrength
        DecodedInformationContent['Language_ExtendedPort_Status'] = Language_ExtendedPort_Status

        ErrorCheck, remainedData = SplitData(data=remainedData, bytes=2, from_start=False)
        InformationSerialNumber, remainedData = SplitData(data=remainedData, bytes=2, from_start=False)
        packetLength = '0x05'
        CRCResponseString = packetLength + ' ' + protocol_number + ' ' + InformationSerialNumber
        CRCString = hex_to_string(CRCResponseString)
        CRC = GenerateCRC(CRCString)
        Response = '7878' + CRCString + CRC + '0d0a'

    elif protocol_number == '0x21':  # Online Command Response from Terminal
        return True
    elif protocol_number == '0x15':  # Online Command Response from Terminal
        return True
    elif protocol_number == '0x26':  # Alarm Data UTC

        DateTime, remainedData = SplitData(data=data, bytes=6)
        QuantityOfGPSSatellites, remainedData = SplitData(data=remainedData, bytes=1)
        Latitude, remainedData = SplitData(data=remainedData, bytes=4)
        Longitude, remainedData = SplitData(data=remainedData, bytes=4)
        Speed, remainedData = SplitData(data=remainedData, bytes=1)
        Course_Status, remainedData = SplitData(data=remainedData, bytes=2)
        LBSLength, remainedData = SplitData(data=remainedData, bytes=1)
        MCC, remainedData = SplitData(data=remainedData, bytes=2)
        MNC, remainedData = SplitData(data=remainedData, bytes=1)
        LAC, remainedData = SplitData(data=remainedData, bytes=2)
        CellID, remainedData = SplitData(data=remainedData, bytes=3)
        TerminalInformation, remainedData = SplitData(data=remainedData, bytes=1)
        Built_inBatteryVoltageLevel, remainedData = SplitData(data=remainedData, bytes=1)
        GSMSignalStrength, remainedData = SplitData(data=remainedData, bytes=1)
        Alarm_Language, remainedData = SplitData(data=remainedData, bytes=4)

        DecodedInformationContent['DateTime'] = DateTime
        DecodedInformationContent['UTC DateTime'] = Process_DateTime(DateTime)
        DecodedInformationContent['QuantityOfGPSSatellites'] = QuantityOfGPSSatellites
        GPSInformationLength, PositioningSatellitesNumber = Process_QuantityOfGPSSatellites(
            quantity_of_gps_satellites=QuantityOfGPSSatellites)
        DecodedInformationContent['QuantityOfGPSSatellites_GPSInformationLength'] = GPSInformationLength
        DecodedInformationContent['QuantityOfGPSSatellites_PositioningSatellitesNumber'] = PositioningSatellitesNumber
        DecodedInformationContent['Latitude'] = Process_LatitudeOrLongitude(latitude_or_longitude=Latitude)
        DecodedInformationContent['Longitude'] = Process_LatitudeOrLongitude(latitude_or_longitude=Longitude)
        DecodedInformationContent['Speed'] = hex_to_string_int(Speed)
        DecodedInformationContent['Course_Status'] = Course_Status
        GPSPositioningMode, GPSPositioningStatus, LongitudeDirection, LatitudeDirection, Course = \
            Process_CourseAndStatus(course_and_status=Course_Status)
        DecodedInformationContent['Course_Status_GPSPositioningMode'] = GPSPositioningMode
        DecodedInformationContent['Course_Status_GPSPositioningStatus'] = GPSPositioningStatus
        DecodedInformationContent['Course_Status_LongitudeDirection'] = LongitudeDirection
        DecodedInformationContent['Course_Status_LatitudeDirection'] = LatitudeDirection
        DecodedInformationContent['Course_Status_Course'] = Course
        DecodedInformationContent['LBSLength'] = LBSLength

        DecodedInformationContent['MCC'] = hex_to_string_int(MCC)
        DecodedInformationContent['MNC'] = hex_to_string_int(MNC)
        DecodedInformationContent['LAC'] = hex_to_string_int(LAC)
        DecodedInformationContent['CellID'] = hex_to_string_int(CellID)

        DecodedInformationContent['TerminalInformation'] = TerminalInformation
        DecodedTerminalInformation = Process_TerminalInformation(TerminalInformation)
        DecodedInformationContent['DecodedTerminalInformation'] = DecodedTerminalInformation
        DecodedInformationContent['Built_inBatteryVoltageLevel'] = Built_inBatteryVoltageLevel
        DecodedInformationContent['Built_inBatteryVoltageLevelDescription'] = \
            Built_inBatteryVoltageLevelDescription[Built_inBatteryVoltageLevel]
        DecodedInformationContent['GSMSignalStrength'] = GSMSignalStrength
        DecodedInformationContent['GSMSignalStrengthDescription'] = GSMSignalStrengthDescription[GSMSignalStrength]
        DecodedInformationContent['Alarm_Language'] = Alarm_Language
        DecodedAlarm_Language = Process_Alarm_Language(Alarm_Language)
        DecodedInformationContent['DecodedAlarm_Language'] = DecodedAlarm_Language

        ErrorCheck, remainedData = SplitData(data=remainedData, bytes=2, from_start=False)
        InformationSerialNumber, remainedData = SplitData(data=remainedData, bytes=2, from_start=False)
        packetLength = '0x05'
        CRCResponseString = packetLength + ' ' + protocol_number + ' ' + InformationSerialNumber
        CRCString = hex_to_string(CRCResponseString)
        CRC = GenerateCRC(CRCString)
        Response = '7878' + CRCString + CRC + '0d0a'
        
    elif protocol_number == '0x19':
        return True
    elif protocol_number == '0x27':
        return True
    elif protocol_number == '0x80':
        return True
    elif protocol_number == '0x8a':
        return True
    elif protocol_number == '0x2c':
        return True
    elif protocol_number == '0x94':
        return True
    elif protocol_number == '0x9b':
        return True
    elif protocol_number == '0x9c':
        return True
    else:
        return True
    return DecodedInformationContent, Response


def DecodeGT08Data(data):
    DecodedPacket = {}

    StartBit, remainedData = SplitData(data=data, bytes=2)
    DecodedPacket['Start Bit'] = StartBit
    if StartBit == '0x78 0x78':
        PacketLengthBytes = 1
    elif StartBit == '0x79 0x79':
        PacketLengthBytes = 2
    else:
        print("(" + StartBit + ")")
        return False

    PacketLength, remainedData = SplitData(data=remainedData, bytes=PacketLengthBytes)
    DecodedPacket['PacketLength'] = PacketLength
    DecodedPacket['Converted PacketLength'] = hex_to_string_int(PacketLength)
    ProtocolNumber, remainedData = SplitData(data=remainedData, bytes=1)
    DecodedPacket['ProtocolNumber'] = ProtocolNumber
    DecodedPacket['Protocol Description'] = ProtocolDescription[ProtocolNumber]

    # StopBit, remainedData = SplitData(data=remainedData, bytes=2, from_start=False)

    DecodedPacket['Raw Information Content'] = remainedData

    DecodedInformationContent, Response = process_InformationContent(data=remainedData, protocol_number=ProtocolNumber)
    DecodedPacket['DecodedInformationContent'] = DecodedInformationContent
    # DecodedPacket['InformationSerialNumber'] = InformationSerialNumber
    # DecodedPacket['ErrorCheck'] = ErrorCheck
    # DecodedPacket['StopBit'] = StopBit

    return DecodedPacket, Response


def DecodeData(data, server_time, type):
    DecodedPackets = []
    Response = ''
    packets = data.split('0d0a')
    i = 0
    for packet in packets:
        i += 1
        if len(str(packet).strip()) > 0:
            decodedPacket = {}
            # print(packet)
            decoded_Packet, Response = DecodeGT08Data(packet)
            decodedPacket['Server Time'] = server_time
            decodedPacket['Type'] = type
            decodedPacket['Offset'] = '{} of {}'.format(i, len(packets) - 1)
            decodedPacket['Decoded'] = decoded_Packet
            decodedPacket['RawPacket'] = packet + '0d0a'
            DecodedPackets.append(decodedPacket)
    return DecodedPackets, Response

