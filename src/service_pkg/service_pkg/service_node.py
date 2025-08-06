import json

import rclpy
from rclpy.node import Node

from interfaces_pkg.srv import TaskList

class service_node(Node):
    def __init__(self):
        super().__init__("service_node")
        self.get_logger().info("service node")
        
        self.service = self.create_service(TaskList, "/task_get_state", self.taskGetState_callback)
        self.get_logger().info("service created")   

    def taskGetState_callback(self, request:TaskList.Request, response:TaskList.Response):
        if request.receive_task_list == True:
            # 获得 JSON 格式的任务列表
            taskList_dict = {"navigation":["toilet", "waiting"], 
                                                  "stand_down":[" ", "waiting"]}
            response.task_list = json.dumps(taskList_dict)

        return response
            

def main(args=None):
    rclpy.init(args=args)
    node = service_node()
    try:
        rclpy.spin(node)
    except KeyboardInterrupt:
        node.get_logger().info("keyboard interrupt")
    rclpy.shutdown()


if __name__ == "__main__":
    main()
