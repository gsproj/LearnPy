"""
	演示一个简单的UDP聊天器
"""

import socket

# 3> 实现发送消息的方法
def send_msg(udp_socket):
	msg = input("请输入要发送的信息: ")
	dest_ip = input("请输入对方的IP: ")
	
	''' 端口号需要转换为int类型 '''
	dest_port = int(input("请输入对方的端口号: "))
	
	''' 发送的消息格式'''
	udp_socket.sendto(msg.encode("utf-8"),(dest_ip, dest_port))

# 4> 实现接受消息的方法
def recv_message(udp_socket):
	recv_msg = udp_socket.recvfrom(1024)
	recv_ip = recv_msg[1]
	recv_msg = recv_msg[0].decode("utf-8")
	print(">>>%s: %s" % (str(recv_ip), recv_msg))


def main():
	# 1> 创建UDP套接字
	udp_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
	# 2> 绑定端口
	udp_socket.bind(("", 7890))
	
	# 5> 调用方法,实现发送和接收
	while True:
		print("="*30)
		print("1:发送消息")
		print("2:接收消息")
		print("="*30)
		op_num = input("请输入要操作的序列号:")

		if op_num == "1":
			send_msg(udp_socket)
		elif op_num == "2":
			recv_message(udp_socket)
		else:
			print("无法识别,请重新输入!")

if __name__ == "__main__":
	main()
