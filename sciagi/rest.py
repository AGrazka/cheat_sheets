pip install djangorestframework  # trzeba dodać też w settingsach


class MovieListView(APIView):
    def get(self, request):
        movies = Movie.objects.all().order_by("title")
        serializer = MovieSerializer(movies, many=True, context={"request": request})
        return Response(serializer.data)

class MovieListAPIView(ListAPIView):
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer
