// generated from rosidl_generator_cpp/resource/idl__builder.hpp.em
// with input from smrr_interfaces:msg/Buffer.idl
// generated code does not contain a copyright notice

#ifndef SMRR_INTERFACES__MSG__DETAIL__BUFFER__BUILDER_HPP_
#define SMRR_INTERFACES__MSG__DETAIL__BUFFER__BUILDER_HPP_

#include <algorithm>
#include <utility>

#include "smrr_interfaces/msg/detail/buffer__struct.hpp"
#include "rosidl_runtime_cpp/message_initialization.hpp"


namespace smrr_interfaces
{

namespace msg
{

namespace builder
{

class Init_Buffer_majority_class_id
{
public:
  explicit Init_Buffer_majority_class_id(::smrr_interfaces::msg::Buffer & msg)
  : msg_(msg)
  {}
  ::smrr_interfaces::msg::Buffer majority_class_id(::smrr_interfaces::msg::Buffer::_majority_class_id_type arg)
  {
    msg_.majority_class_id = std::move(arg);
    return std::move(msg_);
  }

private:
  ::smrr_interfaces::msg::Buffer msg_;
};

class Init_Buffer_y_variance
{
public:
  explicit Init_Buffer_y_variance(::smrr_interfaces::msg::Buffer & msg)
  : msg_(msg)
  {}
  Init_Buffer_majority_class_id y_variance(::smrr_interfaces::msg::Buffer::_y_variance_type arg)
  {
    msg_.y_variance = std::move(arg);
    return Init_Buffer_majority_class_id(msg_);
  }

private:
  ::smrr_interfaces::msg::Buffer msg_;
};

class Init_Buffer_x_variance
{
public:
  explicit Init_Buffer_x_variance(::smrr_interfaces::msg::Buffer & msg)
  : msg_(msg)
  {}
  Init_Buffer_y_variance x_variance(::smrr_interfaces::msg::Buffer::_x_variance_type arg)
  {
    msg_.x_variance = std::move(arg);
    return Init_Buffer_y_variance(msg_);
  }

private:
  ::smrr_interfaces::msg::Buffer msg_;
};

class Init_Buffer_y_std_dev
{
public:
  explicit Init_Buffer_y_std_dev(::smrr_interfaces::msg::Buffer & msg)
  : msg_(msg)
  {}
  Init_Buffer_x_variance y_std_dev(::smrr_interfaces::msg::Buffer::_y_std_dev_type arg)
  {
    msg_.y_std_dev = std::move(arg);
    return Init_Buffer_x_variance(msg_);
  }

private:
  ::smrr_interfaces::msg::Buffer msg_;
};

class Init_Buffer_x_std_dev
{
public:
  explicit Init_Buffer_x_std_dev(::smrr_interfaces::msg::Buffer & msg)
  : msg_(msg)
  {}
  Init_Buffer_y_std_dev x_std_dev(::smrr_interfaces::msg::Buffer::_x_std_dev_type arg)
  {
    msg_.x_std_dev = std::move(arg);
    return Init_Buffer_y_std_dev(msg_);
  }

private:
  ::smrr_interfaces::msg::Buffer msg_;
};

class Init_Buffer_y_mean
{
public:
  explicit Init_Buffer_y_mean(::smrr_interfaces::msg::Buffer & msg)
  : msg_(msg)
  {}
  Init_Buffer_x_std_dev y_mean(::smrr_interfaces::msg::Buffer::_y_mean_type arg)
  {
    msg_.y_mean = std::move(arg);
    return Init_Buffer_x_std_dev(msg_);
  }

private:
  ::smrr_interfaces::msg::Buffer msg_;
};

class Init_Buffer_x_mean
{
public:
  explicit Init_Buffer_x_mean(::smrr_interfaces::msg::Buffer & msg)
  : msg_(msg)
  {}
  Init_Buffer_y_mean x_mean(::smrr_interfaces::msg::Buffer::_x_mean_type arg)
  {
    msg_.x_mean = std::move(arg);
    return Init_Buffer_y_mean(msg_);
  }

private:
  ::smrr_interfaces::msg::Buffer msg_;
};

class Init_Buffer_agent_count
{
public:
  explicit Init_Buffer_agent_count(::smrr_interfaces::msg::Buffer & msg)
  : msg_(msg)
  {}
  Init_Buffer_x_mean agent_count(::smrr_interfaces::msg::Buffer::_agent_count_type arg)
  {
    msg_.agent_count = std::move(arg);
    return Init_Buffer_x_mean(msg_);
  }

private:
  ::smrr_interfaces::msg::Buffer msg_;
};

class Init_Buffer_agent_ids
{
public:
  Init_Buffer_agent_ids()
  : msg_(::rosidl_runtime_cpp::MessageInitialization::SKIP)
  {}
  Init_Buffer_agent_count agent_ids(::smrr_interfaces::msg::Buffer::_agent_ids_type arg)
  {
    msg_.agent_ids = std::move(arg);
    return Init_Buffer_agent_count(msg_);
  }

private:
  ::smrr_interfaces::msg::Buffer msg_;
};

}  // namespace builder

}  // namespace msg

template<typename MessageType>
auto build();

template<>
inline
auto build<::smrr_interfaces::msg::Buffer>()
{
  return smrr_interfaces::msg::builder::Init_Buffer_agent_ids();
}

}  // namespace smrr_interfaces

#endif  // SMRR_INTERFACES__MSG__DETAIL__BUFFER__BUILDER_HPP_
