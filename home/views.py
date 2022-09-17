from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import BookListSerializer ,MemberListSerializer
from .models import BookList
from django.contrib.auth.models import User
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.permissions import IsAuthenticated ,IsAdminUser

# Create your views here.
class Books(APIView):
    authentication_classes=[JWTAuthentication]
    permission_classes=[IsAuthenticated,IsAdminUser]
    def get(self, request):
        # print(request.user.is_staff)
        data = BookList.objects.all()
        serializerr= BookListSerializer(data,many=True)

        return Response(serializerr.data)

    def post(self , request):
        data = request.data 
        serializerr = BookListSerializer(data=data)
        if serializerr.is_valid():
            serializerr.save()
            return Response({
                "status":200,
                "massage":"Book Added"
            })
        else:
            return Response({"status":"error"})
    def patch(self,request):
        data = request.data
        node = BookList.objects.get(BookId=data["BookId"])
        serializerr=BookListSerializer(node,data=data,partial=True)
        if serializerr.is_valid():
            serializerr.save()
            return Response({
                "status":200,
                "massage":"Book Update"
            })
        else:
            return Response({"massage":"error"})
    
    def delete(self,request):
        data = request.data
        node = BookList.objects.get(BookId=data["BookId"])
        node.delete()
        return Response({"massage":"Book deleted"})


class Memberlist(APIView):
    authentication_classes=[JWTAuthentication]
    permission_classes=[IsAuthenticated,IsAdminUser]

    def get(self,request):
        data = User.objects.all()
        serializerr = MemberListSerializer(data,many=True)
        return Response(serializerr.data)
    def post(self,request):
        data = request.data 
        serializerr = MemberListSerializer(data=data)
        if serializerr.is_valid():
            serializerr.save()
            return Response({
                "status":200,
                "massage":"Member Created"
            })
        else:
            return Response({"status":"error"})
    def delete(self,request):
        data = request.data
        node = User.objects.get(username=data["username"])
        node.delete()
        return Response({"massage":"Member Deleted"})
    
    def patch(self,request):
        data = request.data
        node = User.objects.get(id=data["id"])
        serializerr=MemberListSerializer(node,data=data,partial=True)
        if serializerr.is_valid():
            serializerr.save()
            return Response({
                "status":200,
                "massage":"Member Update"
            })
        else:
            return Response({"massage":"error"})



class MemberPanel(APIView):

    authentication_classes=[JWTAuthentication]
    permission_classes=[IsAuthenticated]
    def get(self, request):
        data = BookList.objects.all()
        serializerr= BookListSerializer(data,many=True)

        return Response(serializerr.data)
    
    def post(self,request):
        data=request.data
        
        status=BookList.objects.get(BookId=data["BookId"])
        serializerr= BookListSerializer(status,many=True)

        status.BookStatus ="Borrow"
        status.save()
        return Response({"You have Borrow ":data["BookId"]})

    def patch(self,request):
        data=request.data
        
        status=BookList.objects.get(BookId=data["BookId"])
        serializerr= BookListSerializer(status,many=True)
        

        status.BookStatus ="AVAILABLE"
        status.save()
        return Response({"You have Return ":data["BookId"]})

    def delete(self,request):
        if request.user.is_staff == False :
            node = User.objects.get(username=request.user.username)
            node.delete()
            return Response({"massage":"Your Account Have Deleted"})
        else:
            return Response({"massage":"Something wrong"})



     