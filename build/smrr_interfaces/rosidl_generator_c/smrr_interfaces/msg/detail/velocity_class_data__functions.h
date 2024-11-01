// generated from rosidl_generator_c/resource/idl__functions.h.em
// with input from smrr_interfaces:msg/VelocityClassData.idl
// generated code does not contain a copyright notice

#ifndef SMRR_INTERFACES__MSG__DETAIL__VELOCITY_CLASS_DATA__FUNCTIONS_H_
#define SMRR_INTERFACES__MSG__DETAIL__VELOCITY_CLASS_DATA__FUNCTIONS_H_

#ifdef __cplusplus
extern "C"
{
#endif

#include <stdbool.h>
#include <stdlib.h>

#include "rosidl_runtime_c/visibility_control.h"
#include "smrr_interfaces/msg/rosidl_generator_c__visibility_control.h"

#include "smrr_interfaces/msg/detail/velocity_class_data__struct.h"

/// Initialize msg/VelocityClassData message.
/**
 * If the init function is called twice for the same message without
 * calling fini inbetween previously allocated memory will be leaked.
 * \param[in,out] msg The previously allocated message pointer.
 * Fields without a default value will not be initialized by this function.
 * You might want to call memset(msg, 0, sizeof(
 * smrr_interfaces__msg__VelocityClassData
 * )) before or use
 * smrr_interfaces__msg__VelocityClassData__create()
 * to allocate and initialize the message.
 * \return true if initialization was successful, otherwise false
 */
ROSIDL_GENERATOR_C_PUBLIC_smrr_interfaces
bool
smrr_interfaces__msg__VelocityClassData__init(smrr_interfaces__msg__VelocityClassData * msg);

/// Finalize msg/VelocityClassData message.
/**
 * \param[in,out] msg The allocated message pointer.
 */
ROSIDL_GENERATOR_C_PUBLIC_smrr_interfaces
void
smrr_interfaces__msg__VelocityClassData__fini(smrr_interfaces__msg__VelocityClassData * msg);

/// Create msg/VelocityClassData message.
/**
 * It allocates the memory for the message, sets the memory to zero, and
 * calls
 * smrr_interfaces__msg__VelocityClassData__init().
 * \return The pointer to the initialized message if successful,
 * otherwise NULL
 */
ROSIDL_GENERATOR_C_PUBLIC_smrr_interfaces
smrr_interfaces__msg__VelocityClassData *
smrr_interfaces__msg__VelocityClassData__create();

/// Destroy msg/VelocityClassData message.
/**
 * It calls
 * smrr_interfaces__msg__VelocityClassData__fini()
 * and frees the memory of the message.
 * \param[in,out] msg The allocated message pointer.
 */
ROSIDL_GENERATOR_C_PUBLIC_smrr_interfaces
void
smrr_interfaces__msg__VelocityClassData__destroy(smrr_interfaces__msg__VelocityClassData * msg);

/// Check for msg/VelocityClassData message equality.
/**
 * \param[in] lhs The message on the left hand size of the equality operator.
 * \param[in] rhs The message on the right hand size of the equality operator.
 * \return true if messages are equal, otherwise false.
 */
ROSIDL_GENERATOR_C_PUBLIC_smrr_interfaces
bool
smrr_interfaces__msg__VelocityClassData__are_equal(const smrr_interfaces__msg__VelocityClassData * lhs, const smrr_interfaces__msg__VelocityClassData * rhs);

/// Copy a msg/VelocityClassData message.
/**
 * This functions performs a deep copy, as opposed to the shallow copy that
 * plain assignment yields.
 *
 * \param[in] input The source message pointer.
 * \param[out] output The target message pointer, which must
 *   have been initialized before calling this function.
 * \return true if successful, or false if either pointer is null
 *   or memory allocation fails.
 */
ROSIDL_GENERATOR_C_PUBLIC_smrr_interfaces
bool
smrr_interfaces__msg__VelocityClassData__copy(
  const smrr_interfaces__msg__VelocityClassData * input,
  smrr_interfaces__msg__VelocityClassData * output);

/// Initialize array of msg/VelocityClassData messages.
/**
 * It allocates the memory for the number of elements and calls
 * smrr_interfaces__msg__VelocityClassData__init()
 * for each element of the array.
 * \param[in,out] array The allocated array pointer.
 * \param[in] size The size / capacity of the array.
 * \return true if initialization was successful, otherwise false
 * If the array pointer is valid and the size is zero it is guaranteed
 # to return true.
 */
ROSIDL_GENERATOR_C_PUBLIC_smrr_interfaces
bool
smrr_interfaces__msg__VelocityClassData__Sequence__init(smrr_interfaces__msg__VelocityClassData__Sequence * array, size_t size);

/// Finalize array of msg/VelocityClassData messages.
/**
 * It calls
 * smrr_interfaces__msg__VelocityClassData__fini()
 * for each element of the array and frees the memory for the number of
 * elements.
 * \param[in,out] array The initialized array pointer.
 */
ROSIDL_GENERATOR_C_PUBLIC_smrr_interfaces
void
smrr_interfaces__msg__VelocityClassData__Sequence__fini(smrr_interfaces__msg__VelocityClassData__Sequence * array);

/// Create array of msg/VelocityClassData messages.
/**
 * It allocates the memory for the array and calls
 * smrr_interfaces__msg__VelocityClassData__Sequence__init().
 * \param[in] size The size / capacity of the array.
 * \return The pointer to the initialized array if successful, otherwise NULL
 */
ROSIDL_GENERATOR_C_PUBLIC_smrr_interfaces
smrr_interfaces__msg__VelocityClassData__Sequence *
smrr_interfaces__msg__VelocityClassData__Sequence__create(size_t size);

/// Destroy array of msg/VelocityClassData messages.
/**
 * It calls
 * smrr_interfaces__msg__VelocityClassData__Sequence__fini()
 * on the array,
 * and frees the memory of the array.
 * \param[in,out] array The initialized array pointer.
 */
ROSIDL_GENERATOR_C_PUBLIC_smrr_interfaces
void
smrr_interfaces__msg__VelocityClassData__Sequence__destroy(smrr_interfaces__msg__VelocityClassData__Sequence * array);

/// Check for msg/VelocityClassData message array equality.
/**
 * \param[in] lhs The message array on the left hand size of the equality operator.
 * \param[in] rhs The message array on the right hand size of the equality operator.
 * \return true if message arrays are equal in size and content, otherwise false.
 */
ROSIDL_GENERATOR_C_PUBLIC_smrr_interfaces
bool
smrr_interfaces__msg__VelocityClassData__Sequence__are_equal(const smrr_interfaces__msg__VelocityClassData__Sequence * lhs, const smrr_interfaces__msg__VelocityClassData__Sequence * rhs);

/// Copy an array of msg/VelocityClassData messages.
/**
 * This functions performs a deep copy, as opposed to the shallow copy that
 * plain assignment yields.
 *
 * \param[in] input The source array pointer.
 * \param[out] output The target array pointer, which must
 *   have been initialized before calling this function.
 * \return true if successful, or false if either pointer
 *   is null or memory allocation fails.
 */
ROSIDL_GENERATOR_C_PUBLIC_smrr_interfaces
bool
smrr_interfaces__msg__VelocityClassData__Sequence__copy(
  const smrr_interfaces__msg__VelocityClassData__Sequence * input,
  smrr_interfaces__msg__VelocityClassData__Sequence * output);

#ifdef __cplusplus
}
#endif

#endif  // SMRR_INTERFACES__MSG__DETAIL__VELOCITY_CLASS_DATA__FUNCTIONS_H_
