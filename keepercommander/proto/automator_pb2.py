# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: automator.proto
"""Generated protocol buffer code."""
from google.protobuf.internal import enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from . import ssocloud_pb2 as ssocloud__pb2
from . import enterprise_pb2 as enterprise__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x0f\x61utomator.proto\x12\tAutomator\x1a\x0essocloud.proto\x1a\x10\x65nterprise.proto\"\xbf\x02\n\x15\x41utomatorSettingValue\x12\x11\n\tsettingId\x18\x01 \x01(\x03\x12\x15\n\rsettingTypeId\x18\x02 \x01(\x05\x12\x12\n\nsettingTag\x18\x03 \x01(\t\x12\x13\n\x0bsettingName\x18\x04 \x01(\t\x12\x14\n\x0csettingValue\x18\x05 \x01(\t\x12$\n\x08\x64\x61taType\x18\x06 \x01(\x0e\x32\x12.SsoCloud.DataType\x12\x14\n\x0clastModified\x18\x07 \x01(\t\x12\x10\n\x08\x66romFile\x18\x08 \x01(\x08\x12\x11\n\tencrypted\x18\t \x01(\x08\x12\x0f\n\x07\x65ncoded\x18\n \x01(\x08\x12\x10\n\x08\x65\x64itable\x18\x0b \x01(\x08\x12\x12\n\ntranslated\x18\x0c \x01(\x08\x12\x13\n\x0buserVisible\x18\r \x01(\x08\x12\x10\n\x08required\x18\x0e \x01(\x08\"\xb5\x02\n\x14\x41pproveDeviceRequest\x12\x13\n\x0b\x61utomatorId\x18\x01 \x01(\x03\x12O\n\x1dssoAuthenticationProtocolType\x18\x02 \x01(\x0e\x32(.Automator.SsoAuthenticationProtocolType\x12\x13\n\x0b\x61uthMessage\x18\x03 \x01(\t\x12\r\n\x05\x65mail\x18\x04 \x01(\t\x12\x17\n\x0f\x64\x65vicePublicKey\x18\x05 \x01(\x0c\x12\x1c\n\x14serverEccPublicKeyId\x18\x06 \x01(\x05\x12\x1c\n\x14userEncryptedDataKey\x18\x07 \x01(\x0c\x12>\n\x18userEncryptedDataKeyType\x18\x08 \x01(\x0e\x32\x1c.Enterprise.EncryptedKeyType\"\xc7\x01\n\x0cSetupRequest\x12\x13\n\x0b\x61utomatorId\x18\x01 \x01(\x03\x12\x1c\n\x14serverEccPublicKeyId\x18\x02 \x01(\x05\x12\x31\n\x0e\x61utomatorState\x18\x03 \x01(\x0e\x32\x19.Automator.AutomatorState\x12\'\n\x1f\x65ncryptedEnterprisePrivateEcKey\x18\x04 \x01(\x0c\x12(\n encryptedEnterprisePrivateRsaKey\x18\x05 \x01(\x0c\"B\n\rStatusRequest\x12\x13\n\x0b\x61utomatorId\x18\x01 \x01(\x03\x12\x1c\n\x14serverEccPublicKeyId\x18\x02 \x01(\x05\"\xea\x01\n\x11InitializeRequest\x12\x13\n\x0b\x61utomatorId\x18\x01 \x01(\x03\x12\x13\n\x0bidpMetadata\x18\x02 \x01(\t\x12\x1d\n\x15idpSigningCertificate\x18\x03 \x01(\x0c\x12\x13\n\x0bssoEntityId\x18\x04 \x01(\t\x12\x14\n\x0c\x65mailMapping\x18\x05 \x01(\t\x12\x18\n\x10\x66irstnameMapping\x18\x06 \x01(\t\x12\x17\n\x0flastnameMapping\x18\x07 \x01(\t\x12\x10\n\x08\x64isabled\x18\x08 \x01(\x08\x12\x1c\n\x14serverEccPublicKeyId\x18\t \x01(\x05\"\x96\x02\n\x16NotInitializedResponse\x12 \n\x18\x61utomatorTransmissionKey\x18\x01 \x01(\x0c\x12\x1a\n\x12signingCertificate\x18\x02 \x01(\x0c\x12\"\n\x1asigningCertificateFilename\x18\x03 \x01(\t\x12\"\n\x1asigningCertificatePassword\x18\x04 \x01(\t\x12\x1a\n\x12signingKeyPassword\x18\x05 \x01(\t\x12>\n\x18signingCertificateFormat\x18\x06 \x01(\x0e\x32\x1c.Automator.CertificateFormat\x12\x1a\n\x12\x61utomatorPublicKey\x18\x07 \x01(\x0c\"\xf9\x02\n\x11\x41utomatorResponse\x12\x13\n\x0b\x61utomatorId\x18\x01 \x01(\x03\x12\x0f\n\x07\x65nabled\x18\x02 \x01(\x08\x12\x11\n\ttimestamp\x18\x03 \x01(\x03\x12\x39\n\rapproveDevice\x18\x04 \x01(\x0b\x32 .Automator.ApproveDeviceResponseH\x00\x12+\n\x06status\x18\x05 \x01(\x0b\x32\x19.Automator.StatusResponseH\x00\x12;\n\x0enotInitialized\x18\x06 \x01(\x0b\x32!.Automator.NotInitializedResponseH\x00\x12)\n\x05\x65rror\x18\x07 \x01(\x0b\x32\x18.Automator.ErrorResponseH\x00\x12\x31\n\x0e\x61utomatorState\x18\x08 \x01(\x0e\x32\x19.Automator.AutomatorState\x12\x1c\n\x14\x61utomatorPublicEcKey\x18\t \x01(\x0c\x42\n\n\x08response\"X\n\x15\x41pproveDeviceResponse\x12\x10\n\x08\x61pproved\x18\x01 \x01(\x08\x12\x1c\n\x14\x65ncryptedUserDataKey\x18\x02 \x01(\x0c\x12\x0f\n\x07message\x18\x03 \x01(\t\"\xb4\x02\n\x0eStatusResponse\x12\x13\n\x0binitialized\x18\x01 \x01(\x08\x12\x18\n\x10\x65nabledTimestamp\x18\x02 \x01(\x03\x12\x1c\n\x14initializedTimestamp\x18\x03 \x01(\x03\x12\x18\n\x10updatedTimestamp\x18\x04 \x01(\x03\x12\x1f\n\x17numberOfDevicesApproved\x18\x05 \x01(\x03\x12\x1d\n\x15numberOfDevicesDenied\x18\x06 \x01(\x03\x12\x16\n\x0enumberOfErrors\x18\x07 \x01(\x03\x12 \n\x18sslCertificateExpiration\x18\x08 \x01(\x03\x12\x41\n\x16notInitializedResponse\x18\t \x01(\x0b\x32!.Automator.NotInitializedResponse\" \n\rErrorResponse\x12\x0f\n\x07message\x18\x01 \x01(\t\"X\n\x08LogEntry\x12\x12\n\nserverTime\x18\x01 \x01(\t\x12\x14\n\x0cmessageLevel\x18\x02 \x01(\t\x12\x11\n\tcomponent\x18\x03 \x01(\t\x12\x0f\n\x07message\x18\x04 \x01(\t\"b\n\rAdminResponse\x12\x0f\n\x07success\x18\x01 \x01(\x08\x12\x0f\n\x07message\x18\x02 \x01(\t\x12/\n\rautomatorInfo\x18\x03 \x03(\x0b\x32\x18.Automator.AutomatorInfo\"\xdd\x02\n\rAutomatorInfo\x12\x13\n\x0b\x61utomatorId\x18\x01 \x01(\x03\x12\x0e\n\x06nodeId\x18\x02 \x01(\x03\x12\x0c\n\x04name\x18\x03 \x01(\t\x12\x0f\n\x07\x65nabled\x18\x04 \x01(\x08\x12\x0b\n\x03url\x18\x05 \x01(\t\x12\x32\n\x0f\x61utomatorSkills\x18\x06 \x03(\x0b\x32\x19.Automator.AutomatorSkill\x12@\n\x16\x61utomatorSettingValues\x18\x07 \x03(\x0b\x32 .Automator.AutomatorSettingValue\x12)\n\x06status\x18\x08 \x01(\x0b\x32\x19.Automator.StatusResponse\x12\'\n\nlogEntries\x18\t \x03(\x0b\x32\x13.Automator.LogEntry\x12\x31\n\x0e\x61utomatorState\x18\n \x01(\x0e\x32\x19.Automator.AutomatorState\"e\n\x1b\x41\x64minCreateAutomatorRequest\x12\x0e\n\x06nodeId\x18\x01 \x01(\x03\x12\x0c\n\x04name\x18\x02 \x01(\t\x12(\n\x05skill\x18\x03 \x01(\x0b\x32\x19.Automator.AutomatorSkill\"2\n\x1b\x41\x64minDeleteAutomatorRequest\x12\x13\n\x0b\x61utomatorId\x18\x01 \x01(\x03\"1\n\x1f\x41\x64minGetAutomatorsOnNodeRequest\x12\x0e\n\x06nodeId\x18\x01 \x01(\x03\">\n&AdminGetAutomatorsForEnterpriseRequest\x12\x14\n\x0c\x65nterpriseId\x18\x01 \x01(\x05\"/\n\x18\x41\x64minGetAutomatorRequest\x12\x13\n\x0b\x61utomatorId\x18\x01 \x01(\x03\"C\n\x1b\x41\x64minEnableAutomatorRequest\x12\x13\n\x0b\x61utomatorId\x18\x01 \x01(\x03\x12\x0f\n\x07\x65nabled\x18\x02 \x01(\x08\"\xc8\x01\n\x19\x41\x64minEditAutomatorRequest\x12\x13\n\x0b\x61utomatorId\x18\x01 \x01(\x03\x12\x0c\n\x04name\x18\x02 \x01(\t\x12\x0f\n\x07\x65nabled\x18\x03 \x01(\x08\x12\x0b\n\x03url\x18\x04 \x01(\t\x12(\n\nskillTypes\x18\x05 \x03(\x0e\x32\x14.Automator.SkillType\x12@\n\x16\x61utomatorSettingValues\x18\x06 \x03(\x0b\x32 .Automator.AutomatorSettingValue\"\xb7\x01\n\x1a\x41\x64minSetupAutomatorRequest\x12\x13\n\x0b\x61utomatorId\x18\x01 \x01(\x03\x12\x31\n\x0e\x61utomatorState\x18\x02 \x01(\x0e\x32\x19.Automator.AutomatorState\x12\'\n\x1f\x65ncryptedEcEnterprisePrivateKey\x18\x03 \x01(\x0c\x12(\n encryptedRsaEnterprisePrivateKey\x18\x04 \x01(\x0c\"\xa5\x01\n\x1b\x41\x64minSetupAutomatorResponse\x12\x0f\n\x07success\x18\x01 \x01(\x08\x12\x0f\n\x07message\x18\x02 \x01(\t\x12\x13\n\x0b\x61utomatorId\x18\x03 \x01(\x03\x12\x31\n\x0e\x61utomatorState\x18\x04 \x01(\x0e\x32\x19.Automator.AutomatorState\x12\x1c\n\x14\x61utomatorEcPublicKey\x18\x05 \x01(\x0c\"2\n\x1b\x41\x64minAutomatorSkillsRequest\x12\x13\n\x0b\x61utomatorId\x18\x01 \x01(\x03\"_\n\x0e\x41utomatorSkill\x12\'\n\tskillType\x18\x01 \x01(\x0e\x32\x14.Automator.SkillType\x12\x0c\n\x04name\x18\x02 \x01(\t\x12\x16\n\x0etranslatedName\x18\x03 \x01(\t\"t\n\x1c\x41\x64minAutomatorSkillsResponse\x12\x0f\n\x07success\x18\x01 \x01(\x08\x12\x0f\n\x07message\x18\x02 \x01(\t\x12\x32\n\x0f\x61utomatorSkills\x18\x03 \x03(\x0b\x32\x19.Automator.AutomatorSkill\"1\n\x1a\x41\x64minResetAutomatorRequest\x12\x13\n\x0b\x61utomatorId\x18\x01 \x01(\x03\"6\n\x1f\x41\x64minInitializeAutomatorRequest\x12\x13\n\x0b\x61utomatorId\x18\x01 \x01(\x03\"/\n\x18\x41\x64minAutomatorLogRequest\x12\x13\n\x0b\x61utomatorId\x18\x01 \x01(\x03\"4\n\x1d\x41\x64minAutomatorLogClearRequest\x12\x13\n\x0b\x61utomatorId\x18\x01 \x01(\x03*@\n\x1dSsoAuthenticationProtocolType\x12\x14\n\x10UNKNOWN_PROTOCOL\x10\x00\x12\t\n\x05SAML2\x10\x01*<\n\x11\x43\x65rtificateFormat\x12\x12\n\x0eUNKNOWN_FORMAT\x10\x00\x12\n\n\x06PKCS12\x10\x01\x12\x07\n\x03JKS\x10\x02*K\n\tSkillType\x12\x16\n\x12UNKNOWN_SKILL_TYPE\x10\x00\x12\x13\n\x0f\x44\x45VICE_APPROVAL\x10\x01\x12\x11\n\rTEAM_APPROVAL\x10\x02*\x87\x01\n\x0e\x41utomatorState\x12\x11\n\rUNKNOWN_STATE\x10\x00\x12\x0b\n\x07RUNNING\x10\x01\x12\t\n\x05\x45RROR\x10\x02\x12\x18\n\x14NEEDS_INITIALIZATION\x10\x03\x12\x17\n\x13NEEDS_CRYPTO_STEP_1\x10\x04\x12\x17\n\x13NEEDS_CRYPTO_STEP_2\x10\x05\x42%\n\x18\x63om.keepersecurity.protoB\tAutomatorb\x06proto3')

_SSOAUTHENTICATIONPROTOCOLTYPE = DESCRIPTOR.enum_types_by_name['SsoAuthenticationProtocolType']
SsoAuthenticationProtocolType = enum_type_wrapper.EnumTypeWrapper(_SSOAUTHENTICATIONPROTOCOLTYPE)
_CERTIFICATEFORMAT = DESCRIPTOR.enum_types_by_name['CertificateFormat']
CertificateFormat = enum_type_wrapper.EnumTypeWrapper(_CERTIFICATEFORMAT)
_SKILLTYPE = DESCRIPTOR.enum_types_by_name['SkillType']
SkillType = enum_type_wrapper.EnumTypeWrapper(_SKILLTYPE)
_AUTOMATORSTATE = DESCRIPTOR.enum_types_by_name['AutomatorState']
AutomatorState = enum_type_wrapper.EnumTypeWrapper(_AUTOMATORSTATE)
UNKNOWN_PROTOCOL = 0
SAML2 = 1
UNKNOWN_FORMAT = 0
PKCS12 = 1
JKS = 2
UNKNOWN_SKILL_TYPE = 0
DEVICE_APPROVAL = 1
TEAM_APPROVAL = 2
UNKNOWN_STATE = 0
RUNNING = 1
ERROR = 2
NEEDS_INITIALIZATION = 3
NEEDS_CRYPTO_STEP_1 = 4
NEEDS_CRYPTO_STEP_2 = 5


_AUTOMATORSETTINGVALUE = DESCRIPTOR.message_types_by_name['AutomatorSettingValue']
_APPROVEDEVICEREQUEST = DESCRIPTOR.message_types_by_name['ApproveDeviceRequest']
_SETUPREQUEST = DESCRIPTOR.message_types_by_name['SetupRequest']
_STATUSREQUEST = DESCRIPTOR.message_types_by_name['StatusRequest']
_INITIALIZEREQUEST = DESCRIPTOR.message_types_by_name['InitializeRequest']
_NOTINITIALIZEDRESPONSE = DESCRIPTOR.message_types_by_name['NotInitializedResponse']
_AUTOMATORRESPONSE = DESCRIPTOR.message_types_by_name['AutomatorResponse']
_APPROVEDEVICERESPONSE = DESCRIPTOR.message_types_by_name['ApproveDeviceResponse']
_STATUSRESPONSE = DESCRIPTOR.message_types_by_name['StatusResponse']
_ERRORRESPONSE = DESCRIPTOR.message_types_by_name['ErrorResponse']
_LOGENTRY = DESCRIPTOR.message_types_by_name['LogEntry']
_ADMINRESPONSE = DESCRIPTOR.message_types_by_name['AdminResponse']
_AUTOMATORINFO = DESCRIPTOR.message_types_by_name['AutomatorInfo']
_ADMINCREATEAUTOMATORREQUEST = DESCRIPTOR.message_types_by_name['AdminCreateAutomatorRequest']
_ADMINDELETEAUTOMATORREQUEST = DESCRIPTOR.message_types_by_name['AdminDeleteAutomatorRequest']
_ADMINGETAUTOMATORSONNODEREQUEST = DESCRIPTOR.message_types_by_name['AdminGetAutomatorsOnNodeRequest']
_ADMINGETAUTOMATORSFORENTERPRISEREQUEST = DESCRIPTOR.message_types_by_name['AdminGetAutomatorsForEnterpriseRequest']
_ADMINGETAUTOMATORREQUEST = DESCRIPTOR.message_types_by_name['AdminGetAutomatorRequest']
_ADMINENABLEAUTOMATORREQUEST = DESCRIPTOR.message_types_by_name['AdminEnableAutomatorRequest']
_ADMINEDITAUTOMATORREQUEST = DESCRIPTOR.message_types_by_name['AdminEditAutomatorRequest']
_ADMINSETUPAUTOMATORREQUEST = DESCRIPTOR.message_types_by_name['AdminSetupAutomatorRequest']
_ADMINSETUPAUTOMATORRESPONSE = DESCRIPTOR.message_types_by_name['AdminSetupAutomatorResponse']
_ADMINAUTOMATORSKILLSREQUEST = DESCRIPTOR.message_types_by_name['AdminAutomatorSkillsRequest']
_AUTOMATORSKILL = DESCRIPTOR.message_types_by_name['AutomatorSkill']
_ADMINAUTOMATORSKILLSRESPONSE = DESCRIPTOR.message_types_by_name['AdminAutomatorSkillsResponse']
_ADMINRESETAUTOMATORREQUEST = DESCRIPTOR.message_types_by_name['AdminResetAutomatorRequest']
_ADMININITIALIZEAUTOMATORREQUEST = DESCRIPTOR.message_types_by_name['AdminInitializeAutomatorRequest']
_ADMINAUTOMATORLOGREQUEST = DESCRIPTOR.message_types_by_name['AdminAutomatorLogRequest']
_ADMINAUTOMATORLOGCLEARREQUEST = DESCRIPTOR.message_types_by_name['AdminAutomatorLogClearRequest']
AutomatorSettingValue = _reflection.GeneratedProtocolMessageType('AutomatorSettingValue', (_message.Message,), {
  'DESCRIPTOR' : _AUTOMATORSETTINGVALUE,
  '__module__' : 'automator_pb2'
  # @@protoc_insertion_point(class_scope:Automator.AutomatorSettingValue)
  })
_sym_db.RegisterMessage(AutomatorSettingValue)

ApproveDeviceRequest = _reflection.GeneratedProtocolMessageType('ApproveDeviceRequest', (_message.Message,), {
  'DESCRIPTOR' : _APPROVEDEVICEREQUEST,
  '__module__' : 'automator_pb2'
  # @@protoc_insertion_point(class_scope:Automator.ApproveDeviceRequest)
  })
_sym_db.RegisterMessage(ApproveDeviceRequest)

SetupRequest = _reflection.GeneratedProtocolMessageType('SetupRequest', (_message.Message,), {
  'DESCRIPTOR' : _SETUPREQUEST,
  '__module__' : 'automator_pb2'
  # @@protoc_insertion_point(class_scope:Automator.SetupRequest)
  })
_sym_db.RegisterMessage(SetupRequest)

StatusRequest = _reflection.GeneratedProtocolMessageType('StatusRequest', (_message.Message,), {
  'DESCRIPTOR' : _STATUSREQUEST,
  '__module__' : 'automator_pb2'
  # @@protoc_insertion_point(class_scope:Automator.StatusRequest)
  })
_sym_db.RegisterMessage(StatusRequest)

InitializeRequest = _reflection.GeneratedProtocolMessageType('InitializeRequest', (_message.Message,), {
  'DESCRIPTOR' : _INITIALIZEREQUEST,
  '__module__' : 'automator_pb2'
  # @@protoc_insertion_point(class_scope:Automator.InitializeRequest)
  })
_sym_db.RegisterMessage(InitializeRequest)

NotInitializedResponse = _reflection.GeneratedProtocolMessageType('NotInitializedResponse', (_message.Message,), {
  'DESCRIPTOR' : _NOTINITIALIZEDRESPONSE,
  '__module__' : 'automator_pb2'
  # @@protoc_insertion_point(class_scope:Automator.NotInitializedResponse)
  })
_sym_db.RegisterMessage(NotInitializedResponse)

AutomatorResponse = _reflection.GeneratedProtocolMessageType('AutomatorResponse', (_message.Message,), {
  'DESCRIPTOR' : _AUTOMATORRESPONSE,
  '__module__' : 'automator_pb2'
  # @@protoc_insertion_point(class_scope:Automator.AutomatorResponse)
  })
_sym_db.RegisterMessage(AutomatorResponse)

ApproveDeviceResponse = _reflection.GeneratedProtocolMessageType('ApproveDeviceResponse', (_message.Message,), {
  'DESCRIPTOR' : _APPROVEDEVICERESPONSE,
  '__module__' : 'automator_pb2'
  # @@protoc_insertion_point(class_scope:Automator.ApproveDeviceResponse)
  })
_sym_db.RegisterMessage(ApproveDeviceResponse)

StatusResponse = _reflection.GeneratedProtocolMessageType('StatusResponse', (_message.Message,), {
  'DESCRIPTOR' : _STATUSRESPONSE,
  '__module__' : 'automator_pb2'
  # @@protoc_insertion_point(class_scope:Automator.StatusResponse)
  })
_sym_db.RegisterMessage(StatusResponse)

ErrorResponse = _reflection.GeneratedProtocolMessageType('ErrorResponse', (_message.Message,), {
  'DESCRIPTOR' : _ERRORRESPONSE,
  '__module__' : 'automator_pb2'
  # @@protoc_insertion_point(class_scope:Automator.ErrorResponse)
  })
_sym_db.RegisterMessage(ErrorResponse)

LogEntry = _reflection.GeneratedProtocolMessageType('LogEntry', (_message.Message,), {
  'DESCRIPTOR' : _LOGENTRY,
  '__module__' : 'automator_pb2'
  # @@protoc_insertion_point(class_scope:Automator.LogEntry)
  })
_sym_db.RegisterMessage(LogEntry)

AdminResponse = _reflection.GeneratedProtocolMessageType('AdminResponse', (_message.Message,), {
  'DESCRIPTOR' : _ADMINRESPONSE,
  '__module__' : 'automator_pb2'
  # @@protoc_insertion_point(class_scope:Automator.AdminResponse)
  })
_sym_db.RegisterMessage(AdminResponse)

AutomatorInfo = _reflection.GeneratedProtocolMessageType('AutomatorInfo', (_message.Message,), {
  'DESCRIPTOR' : _AUTOMATORINFO,
  '__module__' : 'automator_pb2'
  # @@protoc_insertion_point(class_scope:Automator.AutomatorInfo)
  })
_sym_db.RegisterMessage(AutomatorInfo)

AdminCreateAutomatorRequest = _reflection.GeneratedProtocolMessageType('AdminCreateAutomatorRequest', (_message.Message,), {
  'DESCRIPTOR' : _ADMINCREATEAUTOMATORREQUEST,
  '__module__' : 'automator_pb2'
  # @@protoc_insertion_point(class_scope:Automator.AdminCreateAutomatorRequest)
  })
_sym_db.RegisterMessage(AdminCreateAutomatorRequest)

AdminDeleteAutomatorRequest = _reflection.GeneratedProtocolMessageType('AdminDeleteAutomatorRequest', (_message.Message,), {
  'DESCRIPTOR' : _ADMINDELETEAUTOMATORREQUEST,
  '__module__' : 'automator_pb2'
  # @@protoc_insertion_point(class_scope:Automator.AdminDeleteAutomatorRequest)
  })
_sym_db.RegisterMessage(AdminDeleteAutomatorRequest)

AdminGetAutomatorsOnNodeRequest = _reflection.GeneratedProtocolMessageType('AdminGetAutomatorsOnNodeRequest', (_message.Message,), {
  'DESCRIPTOR' : _ADMINGETAUTOMATORSONNODEREQUEST,
  '__module__' : 'automator_pb2'
  # @@protoc_insertion_point(class_scope:Automator.AdminGetAutomatorsOnNodeRequest)
  })
_sym_db.RegisterMessage(AdminGetAutomatorsOnNodeRequest)

AdminGetAutomatorsForEnterpriseRequest = _reflection.GeneratedProtocolMessageType('AdminGetAutomatorsForEnterpriseRequest', (_message.Message,), {
  'DESCRIPTOR' : _ADMINGETAUTOMATORSFORENTERPRISEREQUEST,
  '__module__' : 'automator_pb2'
  # @@protoc_insertion_point(class_scope:Automator.AdminGetAutomatorsForEnterpriseRequest)
  })
_sym_db.RegisterMessage(AdminGetAutomatorsForEnterpriseRequest)

AdminGetAutomatorRequest = _reflection.GeneratedProtocolMessageType('AdminGetAutomatorRequest', (_message.Message,), {
  'DESCRIPTOR' : _ADMINGETAUTOMATORREQUEST,
  '__module__' : 'automator_pb2'
  # @@protoc_insertion_point(class_scope:Automator.AdminGetAutomatorRequest)
  })
_sym_db.RegisterMessage(AdminGetAutomatorRequest)

AdminEnableAutomatorRequest = _reflection.GeneratedProtocolMessageType('AdminEnableAutomatorRequest', (_message.Message,), {
  'DESCRIPTOR' : _ADMINENABLEAUTOMATORREQUEST,
  '__module__' : 'automator_pb2'
  # @@protoc_insertion_point(class_scope:Automator.AdminEnableAutomatorRequest)
  })
_sym_db.RegisterMessage(AdminEnableAutomatorRequest)

AdminEditAutomatorRequest = _reflection.GeneratedProtocolMessageType('AdminEditAutomatorRequest', (_message.Message,), {
  'DESCRIPTOR' : _ADMINEDITAUTOMATORREQUEST,
  '__module__' : 'automator_pb2'
  # @@protoc_insertion_point(class_scope:Automator.AdminEditAutomatorRequest)
  })
_sym_db.RegisterMessage(AdminEditAutomatorRequest)

AdminSetupAutomatorRequest = _reflection.GeneratedProtocolMessageType('AdminSetupAutomatorRequest', (_message.Message,), {
  'DESCRIPTOR' : _ADMINSETUPAUTOMATORREQUEST,
  '__module__' : 'automator_pb2'
  # @@protoc_insertion_point(class_scope:Automator.AdminSetupAutomatorRequest)
  })
_sym_db.RegisterMessage(AdminSetupAutomatorRequest)

AdminSetupAutomatorResponse = _reflection.GeneratedProtocolMessageType('AdminSetupAutomatorResponse', (_message.Message,), {
  'DESCRIPTOR' : _ADMINSETUPAUTOMATORRESPONSE,
  '__module__' : 'automator_pb2'
  # @@protoc_insertion_point(class_scope:Automator.AdminSetupAutomatorResponse)
  })
_sym_db.RegisterMessage(AdminSetupAutomatorResponse)

AdminAutomatorSkillsRequest = _reflection.GeneratedProtocolMessageType('AdminAutomatorSkillsRequest', (_message.Message,), {
  'DESCRIPTOR' : _ADMINAUTOMATORSKILLSREQUEST,
  '__module__' : 'automator_pb2'
  # @@protoc_insertion_point(class_scope:Automator.AdminAutomatorSkillsRequest)
  })
_sym_db.RegisterMessage(AdminAutomatorSkillsRequest)

AutomatorSkill = _reflection.GeneratedProtocolMessageType('AutomatorSkill', (_message.Message,), {
  'DESCRIPTOR' : _AUTOMATORSKILL,
  '__module__' : 'automator_pb2'
  # @@protoc_insertion_point(class_scope:Automator.AutomatorSkill)
  })
_sym_db.RegisterMessage(AutomatorSkill)

AdminAutomatorSkillsResponse = _reflection.GeneratedProtocolMessageType('AdminAutomatorSkillsResponse', (_message.Message,), {
  'DESCRIPTOR' : _ADMINAUTOMATORSKILLSRESPONSE,
  '__module__' : 'automator_pb2'
  # @@protoc_insertion_point(class_scope:Automator.AdminAutomatorSkillsResponse)
  })
_sym_db.RegisterMessage(AdminAutomatorSkillsResponse)

AdminResetAutomatorRequest = _reflection.GeneratedProtocolMessageType('AdminResetAutomatorRequest', (_message.Message,), {
  'DESCRIPTOR' : _ADMINRESETAUTOMATORREQUEST,
  '__module__' : 'automator_pb2'
  # @@protoc_insertion_point(class_scope:Automator.AdminResetAutomatorRequest)
  })
_sym_db.RegisterMessage(AdminResetAutomatorRequest)

AdminInitializeAutomatorRequest = _reflection.GeneratedProtocolMessageType('AdminInitializeAutomatorRequest', (_message.Message,), {
  'DESCRIPTOR' : _ADMININITIALIZEAUTOMATORREQUEST,
  '__module__' : 'automator_pb2'
  # @@protoc_insertion_point(class_scope:Automator.AdminInitializeAutomatorRequest)
  })
_sym_db.RegisterMessage(AdminInitializeAutomatorRequest)

AdminAutomatorLogRequest = _reflection.GeneratedProtocolMessageType('AdminAutomatorLogRequest', (_message.Message,), {
  'DESCRIPTOR' : _ADMINAUTOMATORLOGREQUEST,
  '__module__' : 'automator_pb2'
  # @@protoc_insertion_point(class_scope:Automator.AdminAutomatorLogRequest)
  })
_sym_db.RegisterMessage(AdminAutomatorLogRequest)

AdminAutomatorLogClearRequest = _reflection.GeneratedProtocolMessageType('AdminAutomatorLogClearRequest', (_message.Message,), {
  'DESCRIPTOR' : _ADMINAUTOMATORLOGCLEARREQUEST,
  '__module__' : 'automator_pb2'
  # @@protoc_insertion_point(class_scope:Automator.AdminAutomatorLogClearRequest)
  })
_sym_db.RegisterMessage(AdminAutomatorLogClearRequest)

if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  DESCRIPTOR._serialized_options = b'\n\030com.keepersecurity.protoB\tAutomator'
  _SSOAUTHENTICATIONPROTOCOLTYPE._serialized_start=4265
  _SSOAUTHENTICATIONPROTOCOLTYPE._serialized_end=4329
  _CERTIFICATEFORMAT._serialized_start=4331
  _CERTIFICATEFORMAT._serialized_end=4391
  _SKILLTYPE._serialized_start=4393
  _SKILLTYPE._serialized_end=4468
  _AUTOMATORSTATE._serialized_start=4471
  _AUTOMATORSTATE._serialized_end=4606
  _AUTOMATORSETTINGVALUE._serialized_start=65
  _AUTOMATORSETTINGVALUE._serialized_end=384
  _APPROVEDEVICEREQUEST._serialized_start=387
  _APPROVEDEVICEREQUEST._serialized_end=696
  _SETUPREQUEST._serialized_start=699
  _SETUPREQUEST._serialized_end=898
  _STATUSREQUEST._serialized_start=900
  _STATUSREQUEST._serialized_end=966
  _INITIALIZEREQUEST._serialized_start=969
  _INITIALIZEREQUEST._serialized_end=1203
  _NOTINITIALIZEDRESPONSE._serialized_start=1206
  _NOTINITIALIZEDRESPONSE._serialized_end=1484
  _AUTOMATORRESPONSE._serialized_start=1487
  _AUTOMATORRESPONSE._serialized_end=1864
  _APPROVEDEVICERESPONSE._serialized_start=1866
  _APPROVEDEVICERESPONSE._serialized_end=1954
  _STATUSRESPONSE._serialized_start=1957
  _STATUSRESPONSE._serialized_end=2265
  _ERRORRESPONSE._serialized_start=2267
  _ERRORRESPONSE._serialized_end=2299
  _LOGENTRY._serialized_start=2301
  _LOGENTRY._serialized_end=2389
  _ADMINRESPONSE._serialized_start=2391
  _ADMINRESPONSE._serialized_end=2489
  _AUTOMATORINFO._serialized_start=2492
  _AUTOMATORINFO._serialized_end=2841
  _ADMINCREATEAUTOMATORREQUEST._serialized_start=2843
  _ADMINCREATEAUTOMATORREQUEST._serialized_end=2944
  _ADMINDELETEAUTOMATORREQUEST._serialized_start=2946
  _ADMINDELETEAUTOMATORREQUEST._serialized_end=2996
  _ADMINGETAUTOMATORSONNODEREQUEST._serialized_start=2998
  _ADMINGETAUTOMATORSONNODEREQUEST._serialized_end=3047
  _ADMINGETAUTOMATORSFORENTERPRISEREQUEST._serialized_start=3049
  _ADMINGETAUTOMATORSFORENTERPRISEREQUEST._serialized_end=3111
  _ADMINGETAUTOMATORREQUEST._serialized_start=3113
  _ADMINGETAUTOMATORREQUEST._serialized_end=3160
  _ADMINENABLEAUTOMATORREQUEST._serialized_start=3162
  _ADMINENABLEAUTOMATORREQUEST._serialized_end=3229
  _ADMINEDITAUTOMATORREQUEST._serialized_start=3232
  _ADMINEDITAUTOMATORREQUEST._serialized_end=3432
  _ADMINSETUPAUTOMATORREQUEST._serialized_start=3435
  _ADMINSETUPAUTOMATORREQUEST._serialized_end=3618
  _ADMINSETUPAUTOMATORRESPONSE._serialized_start=3621
  _ADMINSETUPAUTOMATORRESPONSE._serialized_end=3786
  _ADMINAUTOMATORSKILLSREQUEST._serialized_start=3788
  _ADMINAUTOMATORSKILLSREQUEST._serialized_end=3838
  _AUTOMATORSKILL._serialized_start=3840
  _AUTOMATORSKILL._serialized_end=3935
  _ADMINAUTOMATORSKILLSRESPONSE._serialized_start=3937
  _ADMINAUTOMATORSKILLSRESPONSE._serialized_end=4053
  _ADMINRESETAUTOMATORREQUEST._serialized_start=4055
  _ADMINRESETAUTOMATORREQUEST._serialized_end=4104
  _ADMININITIALIZEAUTOMATORREQUEST._serialized_start=4106
  _ADMININITIALIZEAUTOMATORREQUEST._serialized_end=4160
  _ADMINAUTOMATORLOGREQUEST._serialized_start=4162
  _ADMINAUTOMATORLOGREQUEST._serialized_end=4209
  _ADMINAUTOMATORLOGCLEARREQUEST._serialized_start=4211
  _ADMINAUTOMATORLOGCLEARREQUEST._serialized_end=4263
# @@protoc_insertion_point(module_scope)
