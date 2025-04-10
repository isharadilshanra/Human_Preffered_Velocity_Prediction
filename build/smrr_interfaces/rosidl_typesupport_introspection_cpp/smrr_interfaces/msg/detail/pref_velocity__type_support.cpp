// generated from rosidl_typesupport_introspection_cpp/resource/idl__type_support.cpp.em
// with input from smrr_interfaces:msg/PrefVelocity.idl
// generated code does not contain a copyright notice

#include "array"
#include "cstddef"
#include "string"
#include "vector"
#include "rosidl_runtime_c/message_type_support_struct.h"
#include "rosidl_typesupport_cpp/message_type_support.hpp"
#include "rosidl_typesupport_interface/macros.h"
#include "smrr_interfaces/msg/detail/pref_velocity__struct.hpp"
#include "rosidl_typesupport_introspection_cpp/field_types.hpp"
#include "rosidl_typesupport_introspection_cpp/identifier.hpp"
#include "rosidl_typesupport_introspection_cpp/message_introspection.hpp"
#include "rosidl_typesupport_introspection_cpp/message_type_support_decl.hpp"
#include "rosidl_typesupport_introspection_cpp/visibility_control.h"

namespace smrr_interfaces
{

namespace msg
{

namespace rosidl_typesupport_introspection_cpp
{

void PrefVelocity_init_function(
  void * message_memory, rosidl_runtime_cpp::MessageInitialization _init)
{
  new (message_memory) smrr_interfaces::msg::PrefVelocity(_init);
}

void PrefVelocity_fini_function(void * message_memory)
{
  auto typed_message = static_cast<smrr_interfaces::msg::PrefVelocity *>(message_memory);
  typed_message->~PrefVelocity();
}

size_t size_function__PrefVelocity__agent_ids(const void * untyped_member)
{
  const auto * member = reinterpret_cast<const std::vector<int32_t> *>(untyped_member);
  return member->size();
}

const void * get_const_function__PrefVelocity__agent_ids(const void * untyped_member, size_t index)
{
  const auto & member =
    *reinterpret_cast<const std::vector<int32_t> *>(untyped_member);
  return &member[index];
}

void * get_function__PrefVelocity__agent_ids(void * untyped_member, size_t index)
{
  auto & member =
    *reinterpret_cast<std::vector<int32_t> *>(untyped_member);
  return &member[index];
}

void fetch_function__PrefVelocity__agent_ids(
  const void * untyped_member, size_t index, void * untyped_value)
{
  const auto & item = *reinterpret_cast<const int32_t *>(
    get_const_function__PrefVelocity__agent_ids(untyped_member, index));
  auto & value = *reinterpret_cast<int32_t *>(untyped_value);
  value = item;
}

void assign_function__PrefVelocity__agent_ids(
  void * untyped_member, size_t index, const void * untyped_value)
{
  auto & item = *reinterpret_cast<int32_t *>(
    get_function__PrefVelocity__agent_ids(untyped_member, index));
  const auto & value = *reinterpret_cast<const int32_t *>(untyped_value);
  item = value;
}

void resize_function__PrefVelocity__agent_ids(void * untyped_member, size_t size)
{
  auto * member =
    reinterpret_cast<std::vector<int32_t> *>(untyped_member);
  member->resize(size);
}

size_t size_function__PrefVelocity__class_ids(const void * untyped_member)
{
  const auto * member = reinterpret_cast<const std::vector<std::string> *>(untyped_member);
  return member->size();
}

const void * get_const_function__PrefVelocity__class_ids(const void * untyped_member, size_t index)
{
  const auto & member =
    *reinterpret_cast<const std::vector<std::string> *>(untyped_member);
  return &member[index];
}

void * get_function__PrefVelocity__class_ids(void * untyped_member, size_t index)
{
  auto & member =
    *reinterpret_cast<std::vector<std::string> *>(untyped_member);
  return &member[index];
}

void fetch_function__PrefVelocity__class_ids(
  const void * untyped_member, size_t index, void * untyped_value)
{
  const auto & item = *reinterpret_cast<const std::string *>(
    get_const_function__PrefVelocity__class_ids(untyped_member, index));
  auto & value = *reinterpret_cast<std::string *>(untyped_value);
  value = item;
}

void assign_function__PrefVelocity__class_ids(
  void * untyped_member, size_t index, const void * untyped_value)
{
  auto & item = *reinterpret_cast<std::string *>(
    get_function__PrefVelocity__class_ids(untyped_member, index));
  const auto & value = *reinterpret_cast<const std::string *>(untyped_value);
  item = value;
}

void resize_function__PrefVelocity__class_ids(void * untyped_member, size_t size)
{
  auto * member =
    reinterpret_cast<std::vector<std::string> *>(untyped_member);
  member->resize(size);
}

size_t size_function__PrefVelocity__preferred_velocities(const void * untyped_member)
{
  const auto * member = reinterpret_cast<const std::vector<float> *>(untyped_member);
  return member->size();
}

const void * get_const_function__PrefVelocity__preferred_velocities(const void * untyped_member, size_t index)
{
  const auto & member =
    *reinterpret_cast<const std::vector<float> *>(untyped_member);
  return &member[index];
}

void * get_function__PrefVelocity__preferred_velocities(void * untyped_member, size_t index)
{
  auto & member =
    *reinterpret_cast<std::vector<float> *>(untyped_member);
  return &member[index];
}

void fetch_function__PrefVelocity__preferred_velocities(
  const void * untyped_member, size_t index, void * untyped_value)
{
  const auto & item = *reinterpret_cast<const float *>(
    get_const_function__PrefVelocity__preferred_velocities(untyped_member, index));
  auto & value = *reinterpret_cast<float *>(untyped_value);
  value = item;
}

void assign_function__PrefVelocity__preferred_velocities(
  void * untyped_member, size_t index, const void * untyped_value)
{
  auto & item = *reinterpret_cast<float *>(
    get_function__PrefVelocity__preferred_velocities(untyped_member, index));
  const auto & value = *reinterpret_cast<const float *>(untyped_value);
  item = value;
}

void resize_function__PrefVelocity__preferred_velocities(void * untyped_member, size_t size)
{
  auto * member =
    reinterpret_cast<std::vector<float> *>(untyped_member);
  member->resize(size);
}

static const ::rosidl_typesupport_introspection_cpp::MessageMember PrefVelocity_message_member_array[3] = {
  {
    "agent_ids",  // name
    ::rosidl_typesupport_introspection_cpp::ROS_TYPE_INT32,  // type
    0,  // upper bound of string
    nullptr,  // members of sub message
    true,  // is array
    0,  // array size
    false,  // is upper bound
    offsetof(smrr_interfaces::msg::PrefVelocity, agent_ids),  // bytes offset in struct
    nullptr,  // default value
    size_function__PrefVelocity__agent_ids,  // size() function pointer
    get_const_function__PrefVelocity__agent_ids,  // get_const(index) function pointer
    get_function__PrefVelocity__agent_ids,  // get(index) function pointer
    fetch_function__PrefVelocity__agent_ids,  // fetch(index, &value) function pointer
    assign_function__PrefVelocity__agent_ids,  // assign(index, value) function pointer
    resize_function__PrefVelocity__agent_ids  // resize(index) function pointer
  },
  {
    "class_ids",  // name
    ::rosidl_typesupport_introspection_cpp::ROS_TYPE_STRING,  // type
    0,  // upper bound of string
    nullptr,  // members of sub message
    true,  // is array
    0,  // array size
    false,  // is upper bound
    offsetof(smrr_interfaces::msg::PrefVelocity, class_ids),  // bytes offset in struct
    nullptr,  // default value
    size_function__PrefVelocity__class_ids,  // size() function pointer
    get_const_function__PrefVelocity__class_ids,  // get_const(index) function pointer
    get_function__PrefVelocity__class_ids,  // get(index) function pointer
    fetch_function__PrefVelocity__class_ids,  // fetch(index, &value) function pointer
    assign_function__PrefVelocity__class_ids,  // assign(index, value) function pointer
    resize_function__PrefVelocity__class_ids  // resize(index) function pointer
  },
  {
    "preferred_velocities",  // name
    ::rosidl_typesupport_introspection_cpp::ROS_TYPE_FLOAT,  // type
    0,  // upper bound of string
    nullptr,  // members of sub message
    true,  // is array
    0,  // array size
    false,  // is upper bound
    offsetof(smrr_interfaces::msg::PrefVelocity, preferred_velocities),  // bytes offset in struct
    nullptr,  // default value
    size_function__PrefVelocity__preferred_velocities,  // size() function pointer
    get_const_function__PrefVelocity__preferred_velocities,  // get_const(index) function pointer
    get_function__PrefVelocity__preferred_velocities,  // get(index) function pointer
    fetch_function__PrefVelocity__preferred_velocities,  // fetch(index, &value) function pointer
    assign_function__PrefVelocity__preferred_velocities,  // assign(index, value) function pointer
    resize_function__PrefVelocity__preferred_velocities  // resize(index) function pointer
  }
};

static const ::rosidl_typesupport_introspection_cpp::MessageMembers PrefVelocity_message_members = {
  "smrr_interfaces::msg",  // message namespace
  "PrefVelocity",  // message name
  3,  // number of fields
  sizeof(smrr_interfaces::msg::PrefVelocity),
  PrefVelocity_message_member_array,  // message members
  PrefVelocity_init_function,  // function to initialize message memory (memory has to be allocated)
  PrefVelocity_fini_function  // function to terminate message instance (will not free memory)
};

static const rosidl_message_type_support_t PrefVelocity_message_type_support_handle = {
  ::rosidl_typesupport_introspection_cpp::typesupport_identifier,
  &PrefVelocity_message_members,
  get_message_typesupport_handle_function,
};

}  // namespace rosidl_typesupport_introspection_cpp

}  // namespace msg

}  // namespace smrr_interfaces


namespace rosidl_typesupport_introspection_cpp
{

template<>
ROSIDL_TYPESUPPORT_INTROSPECTION_CPP_PUBLIC
const rosidl_message_type_support_t *
get_message_type_support_handle<smrr_interfaces::msg::PrefVelocity>()
{
  return &::smrr_interfaces::msg::rosidl_typesupport_introspection_cpp::PrefVelocity_message_type_support_handle;
}

}  // namespace rosidl_typesupport_introspection_cpp

#ifdef __cplusplus
extern "C"
{
#endif

ROSIDL_TYPESUPPORT_INTROSPECTION_CPP_PUBLIC
const rosidl_message_type_support_t *
ROSIDL_TYPESUPPORT_INTERFACE__MESSAGE_SYMBOL_NAME(rosidl_typesupport_introspection_cpp, smrr_interfaces, msg, PrefVelocity)() {
  return &::smrr_interfaces::msg::rosidl_typesupport_introspection_cpp::PrefVelocity_message_type_support_handle;
}

#ifdef __cplusplus
}
#endif
