from rest_framework import generics, status
from rest_framework import viewsets
from rest_framework.response import Response

from apps.base.api import GeneralListApiView
from apps.products.api.serializers.product_serializer import ProductSerializer

class ProductViewSet(viewsets.ModelViewSet):
    serializer_class = ProductSerializer

    def get_queryset(self, pk=None):
        if pk is None:
            return self.get_serializer().Meta.model.objects.filter(state=True)
        return self.get_serializer().Meta.model.objects.filter(id=pk, state=True).first()

    def list(self, request):
        product_serializer = self.get_serializer(self.get_queryset(), many=True)
        return Response(product_serializer.data, status=status.HTTP_200_OK)

    def create(self, request):
        # Send information to serializer
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'message': 'Producto creado correctamente!'}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def update(self, request, pk=None):
        if self.get_queryset(pk):
            # Send information to serializer referencing the instance
            product_serializer = self.serializer_class(self.get_queryset(pk), data=request.data)
            if product_serializer.is_valid():
                product_serializer.save()
                return Response(product_serializer.data, status=status.HTTP_200_OK)
            return Response(product_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def destroy(self, request, pk=None):
        product = self.get_queryset().filter(id=pk).first()
        if product:
            product.state = False
            product.save()
            return Response({'message': 'Producto eliminado correctamente!'}, status=status.HTTP_200_OK)
        return Response({'error': 'No existe un producto con estos datos!'}, status=status.HTTP_400_BAD_REQUEST)

# class ProductListAPIView(GeneralListApiView):
#     serializer_class = ProductSerializer

# class ProductListCreateAPIView(generics.ListCreateAPIView):
#     serializer_class = ProductSerializer
#     queryset = ProductSerializer.Meta.model.objects.filter(state=True)
#
#     # def get_queryset(self):
#     #     assert
#     #     return self.queryset
#
#     def post(self, request):
#         # Send information to serializer
#         serializer = self.serializer_class(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response({'message': 'Producto creado correctamente!'}, status=status.HTTP_201_CREATED)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

#
# class ProductRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
#     serializer_class = ProductSerializer
#
#     def get_queryset(self, pk=None):
#         if pk is None:
#             return self.get_serializer().Meta.model.objects.filter(state=True)
#         else:
#             return self.get_serializer().Meta.model.objects.filter(id=pk, state=True).first()
#
#     def patch(self, request, pk=None):
#         # product = self.get_queryset().filter(id=pk).first()
#         # if product:
#         if self.get_queryset(pk):
#             # product_serializer = self.serializer_class(product)
#             product_serializer = self.serializer_class(self.get_queryset(pk))
#             return Response(product_serializer.data, status=status.HTTP_200_OK)
#         return Response({'error': 'No existe un producto con estos datos!'}, status=status.HTTP_400_BAD_REQUEST)
#
#     def put(self, request, pk=None):
#         if self.get_queryset(pk):
#             # Send information to serializer referencing the instance
#             product_serializer = self.serializer_class(self.get_queryset(pk), data=request.data)
#             if product_serializer.is_valid():
#                 product_serializer.save()
#                 return Response(product_serializer.data, status=status.HTTP_200_OK)
#             return Response(product_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
#
#     def delete(self, request, pk=None):
#         product = self.get_queryset().filter(id=pk).first()
#         if product:
#             product.state = False
#             product.save()
#             return Response({'message': 'Producto eliminado correctamente!'}, status=status.HTTP_200_OK)
#         return Response({'error': 'No existe un producto con estos datos!'}, status=status.HTTP_400_BAD_REQUEST)


    # def get(self, request, pk=None):
    #     pass

# class ProductDestroyAPIView(generics.DestroyAPIView):
#     serializer_class = ProductSerializer
#
#     def get_queryset(self):
#         return self.get_serializer().Meta.model.objects.filter(state=True)
#
#     def delete(self, request, pk=None):
#         product = self.get_queryset().filter(id=pk).first()
#         if product:
#             product.state = False
#             product.save()
#             return Response({'message': 'Producto eliminado correctamente!'}, status=status.HTTP_200_OK)
#         return Response({'error': 'No existe un producto con estos datos!'}, status=status.HTTP_400_BAD_REQUEST)

# class ProductUpdateAPIView(generics.UpdateAPIView):
#     serializer_class = ProductSerializer
#
#     def get_queryset(self, pk):
#         # return self.get_serializer().Meta.model.objects.filter(state=True)
#         return self.get_serializer().Meta.model.objects.filter(state=True).filter(id=pk).first()
#
#     def patch(self, request, pk=None):
#         # product = self.get_queryset().filter(id=pk).first()
#         # if product:
#         if self.get_queryset(pk):
#             # product_serializer = self.serializer_class(product)
#             product_serializer = self.serializer_class(self.get_queryset(pk))
#             return Response(product_serializer.data, status=status.HTTP_200_OK)
#         return Response({'error': 'No existe un producto con estos datos!'}, status=status.HTTP_400_BAD_REQUEST)
#
#     def put(self, request, pk=None):
#         if self.get_queryset(pk):
#             product_serializer = self.serializer_class(self.get_queryset(pk), data=request.data)
#             if product_serializer.is_valid():
#                 product_serializer.save()
#                 return Response(product_serializer.data, status=status.HTTP_200_OK)
#             return Response(product_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
