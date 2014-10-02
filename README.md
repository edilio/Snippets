Snippets
========

some snippets 

class BooleanFilterBackend(filters.BaseFilterBackend):
    """
    Filter all the boolean fields with 1 or 0 instead of Boolean True or False.
    """
    def filter_queryset(self, request, queryset, view):
        boolean_filter_fields = getattr(view, 'boolean_filter_fields', [])
        qs = queryset
        for field in boolean_filter_fields:
            value = request.GET.get(field)
            if value == '1':
                qs = qs.filter(**{field: True})
            elif value == '0':
                qs = qs.filter(**{field: False})
        return qs
        
        
this class can be used to add boolean filters in django rest framework but using '0' and '1' instead of True and False.

Please, in the view you need to add fields to boolean_filter_fields and BooleanFilterBackend to filter_backends.

ex:

class XViewSet(SBModelViewSet):
    model = mymodel
    serializer_class = myserializer
    filter_backends = (filters.DjangoFilterBackend, BooleanFilterBackend)
    filter_fields = ('field1', 'field2', 'field3')
    boolean_filter_fields = ('bool_field', )

    ...

