Snippets
========

BooleanFilterBackend for django rest framework
       
This class can be used to add boolean filters in django rest framework but using '0' and '1' instead of True and False.

Please, in the view you need to add fields to boolean_filter_fields and BooleanFilterBackend to filter_backends.

ex:

class XViewSet(SBModelViewSet):
    model = mymodel
    serializer_class = myserializer
    filter_backends = (filters.DjangoFilterBackend, BooleanFilterBackend)
    filter_fields = ('field1', 'field2', 'field3')
    boolean_filter_fields = ('bool_field', )

    ...

