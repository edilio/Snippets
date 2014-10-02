


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