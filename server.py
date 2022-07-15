# -*-coding = utf-8 -*-
# @Time : 2022/7/14 16:09
# @Author :skq
# @File : server.py
# @Software: PyCharm
import grpc
from python.pet.v1 import pet_pb2
from python.pet.v1 import pet_pb2_grpc
from concurrent import futures
import logging

pet_data = []#宠物数据库
max_id = 1#记录宠物id（每个宠物唯一）


class PetStoreService(pet_pb2_grpc.PetStoreServiceServicer):
    def GetPet(self, request, context):
        global pet_data
        print("用户使用getpet")
        for i in pet_data:
            if i.pet_id == request.pet_id:
                return pet_pb2.GetPetResponse(pet=i)
        return pet_pb2.GetPetResponse()

    def PutPet(self, request, context):
        global pet_data, max_id
        print("用户使用putpet")
        pet = pet_pb2.Pet(pet_type=request.pet_type, pet_id=str(max_id), name=request.name)
        max_id += 1
        pet_data.append(pet)
        return pet_pb2.PutPetResponse(pet=pet)

    def DeletePet(self, request, context):
        global pet_data, max_id
        print("用户使用deletepet")
        for i in pet_data[:]:
            if i.pet_id == request.pet_id:
                pet_data.remove(i)
        return pet_pb2.DeletePetResponse()


if __name__ == '__main__':
    #实例化server
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=5))
    pet_pb2_grpc.add_PetStoreServiceServicer_to_server(PetStoreService(), server)
    #启动server
    server.add_insecure_port('[::]:50051')
    server.start()
    server.wait_for_termination()
