# 本项目用于 ROS2 基础学习
- ROS2 官方文档：https://docs.ros.org/en/humble/index.html
- 参考鱼香 ROS2 教程：https://fishros.com

本项目的为在公司中开发使用 ROS2 时，所遇到的一些问题及测试方法所用的项目，并非完全从 0 开始学习 ROS2，用于个人记录与复习

## interfaces_pkg
- 自定义消息类型
1. 创建 .msg 与 .srv 文件，用于存放话题与服务相关消息，注意：**.msg 与 .srv 文件名必须以大写名称开头，文件内容的变量名只能是蛇形命名**
2. 在 package.xml 文件中添加依赖项
```package.xml
<build_depend>rosidl_default_generators</build_depend>

<exec_depend>rosidl_default_runtime</exec_depend>

<member_of_group>rosidl_interface_packages</member_of_group>
```
3. 在 CMakeLists.txt 文件中添加依赖项
```CMakeLists.txt
find_package(rosidl_default_generators REQUIRED)

rosidl_generate_interfaces(${PROJECT_NAME}
  "msg/<msg_name>.msg"
  "srv/<srv_name>.srv"
)
```

## service_pkg:
1. 在字符串内使用双引号，要么需要加转义字符 \，要么外层使用双引号，内部使用但引号，格式如下：
```python
"{\"navigation\":[\"toilet\", \"waiting\"], \"stand_down\":[\" \", \"waiting\"]}"
# 或者
'{"navigation":["toilet", "waiting"], "stand_down":[" ", "waiting"]}'
```
2. 服务端的回调函数，需返回 response，否则会出现报错
3. JSON 格式内只可以使用双引号，不可使用单引号
4. future.result() 返回的是 response 对象
