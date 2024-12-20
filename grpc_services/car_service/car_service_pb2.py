# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: car_service.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x11\x63\x61r_service.proto\x12\x0b\x63\x61r_service\"\x99\x01\n\rAddCarRequest\x12\x0f\n\x07gos_num\x18\x01 \x01(\t\x12\r\n\x05\x62rand\x18\x02 \x01(\t\x12\r\n\x05model\x18\x03 \x01(\t\x12\x16\n\x0eprice_per_hour\x18\x04 \x01(\x02\x12\x10\n\x08location\x18\x05 \x01(\t\x12\x0e\n\x06status\x18\x06 \x01(\t\x12\x1f\n\x17\x64river_license_category\x18\x07 \x01(\t\"B\n\x0e\x41\x64\x64\x43\x61rResponse\x12\x0f\n\x07success\x18\x01 \x01(\x08\x12\x0f\n\x07message\x18\x02 \x01(\t\x12\x0e\n\x06\x63\x61r_id\x18\x03 \x01(\x05\"\x11\n\x0fListCarsRequest\"2\n\x10ListCarsResponse\x12\x1e\n\x04\x63\x61rs\x18\x01 \x03(\x0b\x32\x10.car_service.Car\"8\n\x16UpdateCarStatusRequest\x12\x0e\n\x06\x63\x61r_id\x18\x01 \x01(\x05\x12\x0e\n\x06status\x18\x02 \x01(\t\";\n\x17UpdateCarStatusResponse\x12\x0f\n\x07success\x18\x01 \x01(\x08\x12\x0f\n\x07message\x18\x02 \x01(\t\"&\n\x14GetCarDetailsRequest\x12\x0e\n\x06\x63\x61r_id\x18\x01 \x01(\x05\"\xb1\x01\n\x15GetCarDetailsResponse\x12\x0e\n\x06\x63\x61r_id\x18\x01 \x01(\x05\x12\r\n\x05\x62rand\x18\x02 \x01(\t\x12\x0f\n\x07gos_num\x18\x03 \x01(\t\x12\r\n\x05model\x18\x04 \x01(\t\x12\x16\n\x0eprice_per_hour\x18\x05 \x01(\x02\x12\x10\n\x08location\x18\x06 \x01(\t\x12\x0e\n\x06status\x18\x07 \x01(\t\x12\x1f\n\x17\x64river_license_category\x18\x08 \x01(\t\"\"\n\x10\x44\x65leteCarRequest\x12\x0e\n\x06\x63\x61r_id\x18\x01 \x01(\x05\"5\n\x11\x44\x65leteCarResponse\x12\x0f\n\x07success\x18\x01 \x01(\x08\x12\x0f\n\x07message\x18\x02 \x01(\t\"F\n\x0f\x46indCarsRequest\x12!\n\x19\x64river_license_categories\x18\x01 \x03(\t\x12\x10\n\x08location\x18\x02 \x01(\t\"7\n\x10\x46indCarsResponse\x12#\n\x04\x63\x61rs\x18\x01 \x03(\x0b\x32\x15.car_service.Car_rent\"\x9f\x01\n\x03\x43\x61r\x12\x0e\n\x06\x63\x61r_id\x18\x01 \x01(\x05\x12\x0f\n\x07gos_num\x18\x02 \x01(\t\x12\r\n\x05\x62rand\x18\x03 \x01(\t\x12\r\n\x05model\x18\x04 \x01(\t\x12\x16\n\x0eprice_per_hour\x18\x05 \x01(\x02\x12\x10\n\x08location\x18\x06 \x01(\t\x12\x0e\n\x06status\x18\x07 \x01(\t\x12\x1f\n\x17\x64river_license_category\x18\x08 \x01(\t\"a\n\x08\x43\x61r_rent\x12\x0e\n\x06\x63\x61r_id\x18\x01 \x01(\x05\x12\x0f\n\x07gos_num\x18\x02 \x01(\t\x12\r\n\x05\x62rand\x18\x03 \x01(\t\x12\r\n\x05model\x18\x04 \x01(\t\x12\x16\n\x0eprice_per_hour\x18\x05 \x01(\x02\x32\xf8\x03\n\nCarService\x12\x41\n\x06\x41\x64\x64\x43\x61r\x12\x1a.car_service.AddCarRequest\x1a\x1b.car_service.AddCarResponse\x12G\n\x08ListCars\x12\x1c.car_service.ListCarsRequest\x1a\x1d.car_service.ListCarsResponse\x12\\\n\x0fUpdateCarStatus\x12#.car_service.UpdateCarStatusRequest\x1a$.car_service.UpdateCarStatusResponse\x12V\n\rGetCarDetails\x12!.car_service.GetCarDetailsRequest\x1a\".car_service.GetCarDetailsResponse\x12J\n\tDeleteCar\x12\x1d.car_service.DeleteCarRequest\x1a\x1e.car_service.DeleteCarResponse\x12\\\n\x1d\x46indCarsByLocationAndCategory\x12\x1c.car_service.FindCarsRequest\x1a\x1d.car_service.FindCarsResponseb\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'car_service_pb2', _globals)
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  _globals['_ADDCARREQUEST']._serialized_start=35
  _globals['_ADDCARREQUEST']._serialized_end=188
  _globals['_ADDCARRESPONSE']._serialized_start=190
  _globals['_ADDCARRESPONSE']._serialized_end=256
  _globals['_LISTCARSREQUEST']._serialized_start=258
  _globals['_LISTCARSREQUEST']._serialized_end=275
  _globals['_LISTCARSRESPONSE']._serialized_start=277
  _globals['_LISTCARSRESPONSE']._serialized_end=327
  _globals['_UPDATECARSTATUSREQUEST']._serialized_start=329
  _globals['_UPDATECARSTATUSREQUEST']._serialized_end=385
  _globals['_UPDATECARSTATUSRESPONSE']._serialized_start=387
  _globals['_UPDATECARSTATUSRESPONSE']._serialized_end=446
  _globals['_GETCARDETAILSREQUEST']._serialized_start=448
  _globals['_GETCARDETAILSREQUEST']._serialized_end=486
  _globals['_GETCARDETAILSRESPONSE']._serialized_start=489
  _globals['_GETCARDETAILSRESPONSE']._serialized_end=666
  _globals['_DELETECARREQUEST']._serialized_start=668
  _globals['_DELETECARREQUEST']._serialized_end=702
  _globals['_DELETECARRESPONSE']._serialized_start=704
  _globals['_DELETECARRESPONSE']._serialized_end=757
  _globals['_FINDCARSREQUEST']._serialized_start=759
  _globals['_FINDCARSREQUEST']._serialized_end=829
  _globals['_FINDCARSRESPONSE']._serialized_start=831
  _globals['_FINDCARSRESPONSE']._serialized_end=886
  _globals['_CAR']._serialized_start=889
  _globals['_CAR']._serialized_end=1048
  _globals['_CAR_RENT']._serialized_start=1050
  _globals['_CAR_RENT']._serialized_end=1147
  _globals['_CARSERVICE']._serialized_start=1150
  _globals['_CARSERVICE']._serialized_end=1654
# @@protoc_insertion_point(module_scope)
