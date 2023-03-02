from movies.models import Filmwork
from django.db.models.query import QuerySet
from django.contrib.postgres.aggregates import ArrayAgg
from django.db.models import Q
from django.http import JsonResponse
from django.views.generic.detail import BaseDetailView
from django.views.generic.list import BaseListView, MultipleObjectMixin


class MoviesApiMixin:
    model = Filmwork
    http_method_names = ['get']

    def get_queryset(self)-> QuerySet[Filmwork]:
        queryset = Filmwork.objects.all() \
            .order_by('title') \
            .prefetch_related('Genre','Person') \
            .values() \
            .annotate(genres=ArrayAgg('genrefilmwork__genre__name', 
                                    filter=Q(genrefilmwork__genre__name__isnull=False),
                                    distinct=True)
            ).annotate(
                actors=ArrayAgg('persons__full_name',
                                filter=Q(persons__fw_person__role='actor'),
                                distinct=True),
                directors=ArrayAgg('persons__full_name',
                                filter=Q(persons__fw_person__role='director'),
                                distinct=True),
                writers=ArrayAgg('persons__full_name',
                                filter=Q(persons__fw_person__role='writer'),
                                distinct=True)
            )
        return queryset
    
    def render_to_response(self, context, **response_kwargs):
        return JsonResponse(context)
    
class MoviesDetailApi(MoviesApiMixin,BaseDetailView):

    def get_context_data(self, object_list=None, **kwargs):
        filmwork_uuid = self.kwargs['pk']
        queryset = self.get_queryset().get(id=filmwork_uuid)
        return queryset


class MoviesListApi(BaseListView,MoviesApiMixin, MultipleObjectMixin):
    model = Filmwork
    
    paginate_by = 50
    http_method_names = ['get']

    def check_next(self, page):
        if page.has_next():
            return page.next_page_number()
        else:
            return None

    def check_previous(self,page):
        if page.has_previous():
            return page.previous_page_number()
        else:
            return None

    def get_context_data(self, object_list=None, **kwargs):
        queryset = self.get_queryset()
        paginator, page, queryset, is_paginated = \
            self.paginate_queryset(queryset, self.paginate_by)
        
        # testing page number provided from url
        if self.request.GET:
            page_parameter = self.request.GET['page']
            if page_parameter == 'last': current_page = paginator.num_pages
            else: current_page=page_parameter
        else:
            current_page = 1

        page_items = [i for i in paginator.get_page(current_page).object_list.values()]
        
        context = {
            "results": page_items,
            "count": paginator.count,
            "total_pages": paginator.num_pages,
            "prev": self.check_previous(page),
            "next": self.check_next(page),
        }
        return context