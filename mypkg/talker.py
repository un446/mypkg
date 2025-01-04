#!/usr/bin/python3
# SPDX-FileCopyrightText: 2024 Yuna Isomura
# SPDX-License-Identifier: BSD-3-Clause

import rclpy
from rclpy.node import Node
from std_msgs.msg import String
import subprocess
import re

class Temperature(Node):
    def __init__(self):
        super().__init__('temperature')
        self.publisher = self.create_publisher(String, '/temperature', 10)
        self.timer = self.create_timer(1.0, self.publish_temperature)
        
    def main():
        result = subprocess.run(['sensors'], stdout=subprocess.PIPE)
        output = result.stdout.decode('utf-8')

        match = re.search(r'Core 0:\s+\+(\d+)\.\d+℃ ', output)
        if match:
            return f"{match.group(1)}℃ "
        else:
            return "温度を読み込めません"

    def publish_temperature(self):
        temperature = self.get_temperature()

        if temperature != "温度を読み込めません":
            msg = String()
            msg.data = temperature
            self.pub
