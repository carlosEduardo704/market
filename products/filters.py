import django_filters

from products.models import Product, Department


class ProductFilter(django_filters.FilterSet):
    class Meta:
        model = Product
        fields = {
            "department": ["exact"],
            "price": ["lt", "gt"] 
        }
    
    department = django_filters.ModelChoiceFilter(
        queryset = Department.objects.all(),
        label = "Departamento:"
    )

    ordenacao = django_filters.OrderingFilter(
        # Define as opções disponíveis no dropdown:
        fields=(
            ('price'), # Primeiro valor: campo do modelo; Segundo valor: nome no GET (opcional)
        ),
        choices=(
            ('price', 'Preço: Do menor para o maior'),    # Ordena pelo preço (ascendente)
            ('-price', 'Preço: Do maior para o menor'),   # Ordena por preço (descendente, por causa do '-' )
        ),
        label='Classificar por:',
        
    )