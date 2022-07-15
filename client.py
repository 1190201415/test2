# -*-coding = utf-8 -*-
# @Time : 2022/7/14 15:52
# @Author :skq
# @File : client.py
# @Software: PyCharm
import grpc
from python.pet.v1 import pet_pb2
from python.pet.v1 import pet_pb2_grpc


def window():
    print("输入序号来选择操作")
    print("1、输入宠物信息")
    print("2、查询宠物信息")
    print("3、删除宠物信息")
    print("4、退出")


def petwindow():
    print("输入序号来选择操作")
    print("0、PET_TYPE_UNSPECIFIED")
    print("1、PET_TYPE_CAT")
    print("2、PET_TYPE_DOG")
    print("3、PET_TYPE_SNAKE")
    print("4、PET_TYPE_HAMSTER")


if __name__ == '__main__':
    with grpc.insecure_channel("localhost:50051") as channel:
        stub = pet_pb2_grpc.PetStoreServiceStub(channel)
        while 1:
            window()
            a = int(input())
            if a==1:#输入宠物信息
                petwindow()
                pettype = int(input())
                name = str(input("输入宠物名称"))
                rsp: pet_pb2.PutPetResponse = stub.PutPet(pet_pb2.PutPetRequest(pet_type=pettype, name=name))
                print(rsp.pet)
                input("输入任意数字返回主菜单")
            elif a==2:#查询宠物信息
                petid = str(input("输入宠物id"))
                rsp: pet_pb2.GetPetResponse = stub.GetPet(pet_pb2.GetPetRequest(pet_id=petid))
                print(rsp)
                input("输入任意数字返回主菜单")
            elif a==3:#删除宠物信息
                petid = str(input("输入宠物id"))
                rsp: pet_pb2.DeletePetResponse = stub.DeletePet(pet_pb2.DeletePetRequest(pet_id=petid))
                print(rsp)
                input("输入任意数字返回主菜单")
            elif a==4:#退出
                break
            else:
                print("无效输入")