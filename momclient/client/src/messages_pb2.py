# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: messages.proto
"""Generated protocol buffer code."""
from google.protobuf.internal import builder as _builder
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x0emessages.proto\x12\x08messages\"<\n\x11\x43onnectionRequest\x12\x13\n\x0bqueue_label\x18\x01 \x01(\t\x12\x12\n\nchannel_id\x18\x02 \x01(\t\"5\n\x07Message\x12\n\n\x02id\x18\x01 \x01(\t\x12\x0f\n\x07\x63ontent\x18\x02 \x01(\x0c\x12\r\n\x05topic\x18\x03 \x01(\t2W\n\rMessageStream\x12\x46\n\x10\x43onnectToChannel\x12\x1b.messages.ConnectionRequest\x1a\x11.messages.Message\"\x00\x30\x01\x42\x06\xa2\x02\x03MSGb\x06proto3')

_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, globals())
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'messages_pb2', globals())
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  DESCRIPTOR._serialized_options = b'\242\002\003MSG'
  _CONNECTIONREQUEST._serialized_start=28
  _CONNECTIONREQUEST._serialized_end=88
  _MESSAGE._serialized_start=90
  _MESSAGE._serialized_end=143
  _MESSAGESTREAM._serialized_start=145
  _MESSAGESTREAM._serialized_end=232
# @@protoc_insertion_point(module_scope)