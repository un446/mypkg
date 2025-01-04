#!/usr/bin/python3
# SPDX-FileCopyrightText: 2024 Yuna Isomura
# SPDX-License-Identifier: BSD-3-Clause

import rclpy
from rclpy.node import Node
<<<<<<< HEAD
from person_msgs.srv import Query

rclpy.init()
node = Node("talker")
=======
from std_msgs.msg import String
import subprocess
import re
>>>>>>> lesson10

class Temperature(Node):
    def __init__(self):
        super().__init__('temperature')
        self.publisher = self.create_publisher(String, '/temperature', 10)
        self.timer = self.create_timer(1.0, self.publish_temperature)
        
    def main():
        result = subprocess.run(['sensors'], stdout=subprocess.PIPE)
        output = result.stdout.decode('utf-8')

<<<<<<< HEAD
def cb(request, response):
    if request.name == "磯村結奈":
        response.age = 20

    else:
        response.age = 255

    return response
=======
        match = re.search(r'Core 0:\s+\+(\d+)\.\d+℃ ', output)
        if match:
            return f"{match.group(1)}℃ "
        else:
            return "温度を読み込めません"
>>>>>>> lesson10

    def publish_temperature(self):
        temperature = self.get_temperature()

<<<<<<< HEAD
def main():
    srv = node.create_service(Query, "query", cb)
    rclpy.spin(node)
=======
        if temperature != "温度を読み込めません":
            msg = String()
            msg.data = temperature
            self.pub
>>>>>>> lesson10
