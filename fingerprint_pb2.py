# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: fingerprint.proto
"""Generated protocol buffer code."""
from google.protobuf.internal import builder as _builder
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x11\x66ingerprint.proto\x12\x0b\x66ingerprint\"\x1d\n\x0cPrintRequest\x12\r\n\x05token\x18\x01 \x01(\t\"!\n\x0b\x46ingerprint\x12\x12\n\nimage_data\x18\x01 \x01(\x0c\x32S\n\rFingerprinter\x12\x42\n\x0bGenerateOne\x12\x19.fingerprint.PrintRequest\x1a\x18.fingerprint.Fingerprintb\x06proto3')

_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, globals())
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'fingerprint_pb2', globals())
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  _PRINTREQUEST._serialized_start=34
  _PRINTREQUEST._serialized_end=63
  _FINGERPRINT._serialized_start=65
  _FINGERPRINT._serialized_end=98
  _FINGERPRINTER._serialized_start=100
  _FINGERPRINTER._serialized_end=183
# @@protoc_insertion_point(module_scope)
