import json

import rclpy
from rclpy.node import Node

from interfaces_pkg.srv import TaskList

class client_node(Node):
    def __init__(self):
        super().__init__("client_node")
        self.client = self.create_client(TaskList, "/task_get_state")
        while not self.client.wait_for_service(timeout_sec=1.0):
            self.get_logger().info("/task_get_state service not available, waiting again...")
        self.taskList_dict = {}
    def send_request(self):  # 发送请求
        request = TaskList.Request()
        request.receive_task_list = True
        self.client.call_async(request).add_done_callback(self.taskGetState_callback)

    def taskGetState_callback(self, future):  # 服务完成回调函数
        response = future.result()
        taskList_json = response.task_list
        self.taskList_dict = json.loads(taskList_json)

        self.get_logger().info("taskList_dict: " + str(self.taskList_dict))


def main(args=None):
    rclpy.init()
    node = client_node()
    node.send_request()
    try:
        rclpy.spin(node)
    except KeyboardInterrupt:
        node.get_logger().info("Keyboard Interrupt")
    rclpy.shutdown()