from cart.models import Cart


def get_total_from_cart(request):
    if request.user.is_authenticated:
        cart, created = Cart.objects.get_or_create(usuario=request.user)
        total_itens = cart.get_total_itens

        return {
            'cart_total_itens': total_itens
        }

    else:
        total_itens = 0
    
        return {
            'cart_total_itens': total_itens
        }
