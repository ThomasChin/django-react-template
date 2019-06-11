from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view


# Sample View
@api_view(["GET"])
def book(request):
    books = ["The Art of War", "Deep Work", "The War of Art", "Atomic Habits"]
    return Response(status=status.HTTP_200_OK, data={"data": books})
