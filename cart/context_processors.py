from cart.models import Cart


def get_total_from_cart(request):
    if request.user.is_authenticated:
        total_itens = Cart.objects.get(usuario=request.user).get_total_itens

        return {
            'cart_total_itens': total_itens
        }

    else:
        total_itens = 0
    
        return {
            'cart_total_itens': total_itens
        }
