// generated from rosidl_typesupport_fastrtps_c/resource/idl__type_support_c.cpp.em
// with input from smrr_interfaces:msg/PrefVelocity.idl
// generated code does not contain a copyright notice
#include "smrr_interfaces/msg/detail/pref_velocity__rosidl_typesupport_fastrtps_c.h"


#include <cassert>
#include <limits>
#include <string>
#include "rosidl_typesupport_fastrtps_c/identifier.h"
#include "rosidl_typesupport_fastrtps_c/wstring_conversion.hpp"
#include "rosidl_typesupport_fastrtps_cpp/message_type_support.h"
#include "smrr_interfaces/msg/rosidl_typesupport_fastrtps_c__visibility_control.h"
#include "smrr_interfaces/msg/detail/pref_velocity__struct.h"
#include "smrr_interfaces/msg/detail/pref_velocity__functions.h"
#include "fastcdr/Cdr.h"

#ifndef _WIN32
# pragma GCC diagnostic push
# pragma GCC diagnostic ignored "-Wunused-parameter"
# ifdef __clang__
#  pragma clang diagnostic ignored "-Wdeprecated-register"
#  pragma clang diagnostic ignored "-Wreturn-type-c-linkage"
# endif
#endif
#ifndef _WIN32
# pragma GCC diagnostic pop
#endif

// includes and forward declarations of message dependencies and their conversion functions

#if defined(__cplusplus)
extern "C"
{
#endif

#include "rosidl_runtime_c/primitives_sequence.h"  // agent_ids, preferred_velocities
#include "rosidl_runtime_c/primitives_sequence_functions.h"  // agent_ids, preferred_velocities
#include "smrr_interfaces/msg/detail/data_element_string__functions.h"  // class_ids

// forward declare type support functions
size_t get_serialized_size_smrr_interfaces__msg__DataElementString(
  const void * untyped_ros_message,
  size_t current_alignment);

size_t max_serialized_size_smrr_interfaces__msg__DataElementString(
  bool & full_bounded,
  bool & is_plain,
  size_t current_alignment);

const rosidl_message_type_support_t *
  ROSIDL_TYPESUPPORT_INTERFACE__MESSAGE_SYMBOL_NAME(rosidl_typesupport_fastrtps_c, smrr_interfaces, msg, DataElementString)();


using _PrefVelocity__ros_msg_type = smrr_interfaces__msg__PrefVelocity;

static bool _PrefVelocity__cdr_serialize(
  const void * untyped_ros_message,
  eprosima::fastcdr::Cdr & cdr)
{
  if (!untyped_ros_message) {
    fprintf(stderr, "ros message handle is null\n");
    return false;
  }
  const _PrefVelocity__ros_msg_type * ros_message = static_cast<const _PrefVelocity__ros_msg_type *>(untyped_ros_message);
  // Field name: agent_ids
  {
    size_t size = ros_message->agent_ids.size;
    auto array_ptr = ros_message->agent_ids.data;
    cdr << static_cast<uint32_t>(size);
    cdr.serializeArray(array_ptr, size);
  }

  // Field name: class_ids
  {
    const message_type_support_callbacks_t * callbacks =
      static_cast<const message_type_support_callbacks_t *>(
      ROSIDL_TYPESUPPORT_INTERFACE__MESSAGE_SYMBOL_NAME(
        rosidl_typesupport_fastrtps_c, smrr_interfaces, msg, DataElementString
      )()->data);
    size_t size = ros_message->class_ids.size;
    auto array_ptr = ros_message->class_ids.data;
    cdr << static_cast<uint32_t>(size);
    for (size_t i = 0; i < size; ++i) {
      if (!callbacks->cdr_serialize(
          &array_ptr[i], cdr))
      {
        return false;
      }
    }
  }

  // Field name: preferred_velocities
  {
    size_t size = ros_message->preferred_velocities.size;
    auto array_ptr = ros_message->preferred_velocities.data;
    cdr << static_cast<uint32_t>(size);
    cdr.serializeArray(array_ptr, size);
  }

  return true;
}

static bool _PrefVelocity__cdr_deserialize(
  eprosima::fastcdr::Cdr & cdr,
  void * untyped_ros_message)
{
  if (!untyped_ros_message) {
    fprintf(stderr, "ros message handle is null\n");
    return false;
  }
  _PrefVelocity__ros_msg_type * ros_message = static_cast<_PrefVelocity__ros_msg_type *>(untyped_ros_message);
  // Field name: agent_ids
  {
    uint32_t cdrSize;
    cdr >> cdrSize;
    size_t size = static_cast<size_t>(cdrSize);
    if (ros_message->agent_ids.data) {
      rosidl_runtime_c__int32__Sequence__fini(&ros_message->agent_ids);
    }
    if (!rosidl_runtime_c__int32__Sequence__init(&ros_message->agent_ids, size)) {
      fprintf(stderr, "failed to create array for field 'agent_ids'");
      return false;
    }
    auto array_ptr = ros_message->agent_ids.data;
    cdr.deserializeArray(array_ptr, size);
  }

  // Field name: class_ids
  {
    const message_type_support_callbacks_t * callbacks =
      static_cast<const message_type_support_callbacks_t *>(
      ROSIDL_TYPESUPPORT_INTERFACE__MESSAGE_SYMBOL_NAME(
        rosidl_typesupport_fastrtps_c, smrr_interfaces, msg, DataElementString
      )()->data);
    uint32_t cdrSize;
    cdr >> cdrSize;
    size_t size = static_cast<size_t>(cdrSize);
    if (ros_message->class_ids.data) {
      smrr_interfaces__msg__DataElementString__Sequence__fini(&ros_message->class_ids);
    }
    if (!smrr_interfaces__msg__DataElementString__Sequence__init(&ros_message->class_ids, size)) {
      fprintf(stderr, "failed to create array for field 'class_ids'");
      return false;
    }
    auto array_ptr = ros_message->class_ids.data;
    for (size_t i = 0; i < size; ++i) {
      if (!callbacks->cdr_deserialize(
          cdr, &array_ptr[i]))
      {
        return false;
      }
    }
  }

  // Field name: preferred_velocities
  {
    uint32_t cdrSize;
    cdr >> cdrSize;
    size_t size = static_cast<size_t>(cdrSize);
    if (ros_message->preferred_velocities.data) {
      rosidl_runtime_c__float__Sequence__fini(&ros_message->preferred_velocities);
    }
    if (!rosidl_runtime_c__float__Sequence__init(&ros_message->preferred_velocities, size)) {
      fprintf(stderr, "failed to create array for field 'preferred_velocities'");
      return false;
    }
    auto array_ptr = ros_message->preferred_velocities.data;
    cdr.deserializeArray(array_ptr, size);
  }

  return true;
}  // NOLINT(readability/fn_size)

ROSIDL_TYPESUPPORT_FASTRTPS_C_PUBLIC_smrr_interfaces
size_t get_serialized_size_smrr_interfaces__msg__PrefVelocity(
  const void * untyped_ros_message,
  size_t current_alignment)
{
  const _PrefVelocity__ros_msg_type * ros_message = static_cast<const _PrefVelocity__ros_msg_type *>(untyped_ros_message);
  (void)ros_message;
  size_t initial_alignment = current_alignment;

  const size_t padding = 4;
  const size_t wchar_size = 4;
  (void)padding;
  (void)wchar_size;

  // field.name agent_ids
  {
    size_t array_size = ros_message->agent_ids.size;
    auto array_ptr = ros_message->agent_ids.data;
    current_alignment += padding +
      eprosima::fastcdr::Cdr::alignment(current_alignment, padding);
    (void)array_ptr;
    size_t item_size = sizeof(array_ptr[0]);
    current_alignment += array_size * item_size +
      eprosima::fastcdr::Cdr::alignment(current_alignment, item_size);
  }
  // field.name class_ids
  {
    size_t array_size = ros_message->class_ids.size;
    auto array_ptr = ros_message->class_ids.data;
    current_alignment += padding +
      eprosima::fastcdr::Cdr::alignment(current_alignment, padding);

    for (size_t index = 0; index < array_size; ++index) {
      current_alignment += get_serialized_size_smrr_interfaces__msg__DataElementString(
        &array_ptr[index], current_alignment);
    }
  }
  // field.name preferred_velocities
  {
    size_t array_size = ros_message->preferred_velocities.size;
    auto array_ptr = ros_message->preferred_velocities.data;
    current_alignment += padding +
      eprosima::fastcdr::Cdr::alignment(current_alignment, padding);
    (void)array_ptr;
    size_t item_size = sizeof(array_ptr[0]);
    current_alignment += array_size * item_size +
      eprosima::fastcdr::Cdr::alignment(current_alignment, item_size);
  }

  return current_alignment - initial_alignment;
}

static uint32_t _PrefVelocity__get_serialized_size(const void * untyped_ros_message)
{
  return static_cast<uint32_t>(
    get_serialized_size_smrr_interfaces__msg__PrefVelocity(
      untyped_ros_message, 0));
}

ROSIDL_TYPESUPPORT_FASTRTPS_C_PUBLIC_smrr_interfaces
size_t max_serialized_size_smrr_interfaces__msg__PrefVelocity(
  bool & full_bounded,
  bool & is_plain,
  size_t current_alignment)
{
  size_t initial_alignment = current_alignment;

  const size_t padding = 4;
  const size_t wchar_size = 4;
  size_t last_member_size = 0;
  (void)last_member_size;
  (void)padding;
  (void)wchar_size;

  full_bounded = true;
  is_plain = true;

  // member: agent_ids
  {
    size_t array_size = 0;
    full_bounded = false;
    is_plain = false;
    current_alignment += padding +
      eprosima::fastcdr::Cdr::alignment(current_alignment, padding);

    last_member_size = array_size * sizeof(uint32_t);
    current_alignment += array_size * sizeof(uint32_t) +
      eprosima::fastcdr::Cdr::alignment(current_alignment, sizeof(uint32_t));
  }
  // member: class_ids
  {
    size_t array_size = 0;
    full_bounded = false;
    is_plain = false;
    current_alignment += padding +
      eprosima::fastcdr::Cdr::alignment(current_alignment, padding);


    last_member_size = 0;
    for (size_t index = 0; index < array_size; ++index) {
      bool inner_full_bounded;
      bool inner_is_plain;
      size_t inner_size;
      inner_size =
        max_serialized_size_smrr_interfaces__msg__DataElementString(
        inner_full_bounded, inner_is_plain, current_alignment);
      last_member_size += inner_size;
      current_alignment += inner_size;
      full_bounded &= inner_full_bounded;
      is_plain &= inner_is_plain;
    }
  }
  // member: preferred_velocities
  {
    size_t array_size = 0;
    full_bounded = false;
    is_plain = false;
    current_alignment += padding +
      eprosima::fastcdr::Cdr::alignment(current_alignment, padding);

    last_member_size = array_size * sizeof(uint32_t);
    current_alignment += array_size * sizeof(uint32_t) +
      eprosima::fastcdr::Cdr::alignment(current_alignment, sizeof(uint32_t));
  }

  size_t ret_val = current_alignment - initial_alignment;
  if (is_plain) {
    // All members are plain, and type is not empty.
    // We still need to check that the in-memory alignment
    // is the same as the CDR mandated alignment.
    using DataType = smrr_interfaces__msg__PrefVelocity;
    is_plain =
      (
      offsetof(DataType, preferred_velocities) +
      last_member_size
      ) == ret_val;
  }

  return ret_val;
}

static size_t _PrefVelocity__max_serialized_size(char & bounds_info)
{
  bool full_bounded;
  bool is_plain;
  size_t ret_val;

  ret_val = max_serialized_size_smrr_interfaces__msg__PrefVelocity(
    full_bounded, is_plain, 0);

  bounds_info =
    is_plain ? ROSIDL_TYPESUPPORT_FASTRTPS_PLAIN_TYPE :
    full_bounded ? ROSIDL_TYPESUPPORT_FASTRTPS_BOUNDED_TYPE : ROSIDL_TYPESUPPORT_FASTRTPS_UNBOUNDED_TYPE;
  return ret_val;
}


static message_type_support_callbacks_t __callbacks_PrefVelocity = {
  "smrr_interfaces::msg",
  "PrefVelocity",
  _PrefVelocity__cdr_serialize,
  _PrefVelocity__cdr_deserialize,
  _PrefVelocity__get_serialized_size,
  _PrefVelocity__max_serialized_size
};

static rosidl_message_type_support_t _PrefVelocity__type_support = {
  rosidl_typesupport_fastrtps_c__identifier,
  &__callbacks_PrefVelocity,
  get_message_typesupport_handle_function,
};

const rosidl_message_type_support_t *
ROSIDL_TYPESUPPORT_INTERFACE__MESSAGE_SYMBOL_NAME(rosidl_typesupport_fastrtps_c, smrr_interfaces, msg, PrefVelocity)() {
  return &_PrefVelocity__type_support;
}

#if defined(__cplusplus)
}
#endif
