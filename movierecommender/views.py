from . import views
from .models import Movie
from django.shortcuts import render


def generate_movies_context():
    context = {}
    # Show only movies in recommendation list
    # Sorted by vote_average in desc
    # Get recommended movie counts
    recommended_count = Movie.objects.filter(
        recommended=True
    ).count()
    # If there are no recommended movies
    if recommended_count == 0:
        # Just return the top voted and unwatched movies as popular ones
        movies = Movie.objects.filter(
            watched=False
        ).order_by('-vote_count')[:20]
    else:
        # Get the top voted, unwatched, and recommended movies
        movies = Movie.objects.filter(
            watched=False
        ).filter(
            recommended=True
        ).order_by('-vote_count')[:20]
    context['movie_list'] = movies
    return context

# HINT: Create a view to provide movie recommendations list for the HTML template
def movie_recommendation_view(request):
    if request.method == "GET":
      context = generate_movies_context()
      return render(request, 'movierecommender/movie_list.html', context)


# def movie_recommendation_view(request):
#     if request.method == "GET":
#         context = {}

#         rec_count = Movie.objects.filter(
#             recommended=True
#         ).count()

#         if rec_count == 0:
#             movies = Movie.objects.filter(
#                 watched=False
#             ).order_by('-vote_count')[:20]

#         else:
#             movies =  Movie.objects.filter(
#                 watched=False
#             ).filter(
#                 recommended=True
#             ).order_by('-vote_count')[:20]
#         context['movie_list'] = movies
#         return render(request, 'movierecommender/movie_list.html', context)

