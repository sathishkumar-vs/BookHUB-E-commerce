from django.shortcuts import render,get_object_or_404,redirect
from .models import *
from django.contrib.auth.decorators import login_required


@login_required(login_url='/')
def homepage(request):

    categories = Category.objects.all()

    about_text = "Welcome to our Book Sales Wepsite! We offers a wide range of books in Programming, Networking, and AI. Explore our categories and find the perfect book for you."

    return render(request,"main/homepage.html",{"categories":categories,"about_text":about_text})

@login_required(login_url='/')
def books_by_category(request,category_name):

    category = get_object_or_404(Category,name = category_name)

    books = Book.objects.filter(category=category)

    return render(request,'main/books_view.html',{'category':category,'books':books})

@login_required(login_url='/')
def add_to_cart(request, book_id):

    book = get_object_or_404(Book, id=book_id)

    cart_item, created = CartItem.objects.get_or_create(user=request.user, book=book)

    if not created:

        cart_item.quantity += 1

    cart_item.save()

    return redirect('view_cart')

@login_required(login_url='/')
def view_cart(request):

    cart_items = CartItem.objects.filter(user=request.user)

    total = sum(item.total_price() for item in cart_items) 

    return render(request, 'main/cart.html', {'cart_items': cart_items, 'total': total})

@login_required(login_url='/')
def increase_quantity(request, cart_id):

    cart_item = get_object_or_404(CartItem, id=cart_id, user=request.user)

    cart_item.quantity += 1

    cart_item.save()

    return redirect('view_cart')

@login_required(login_url='/')
def decrease_quantity(request, cart_id):

    cart_item = get_object_or_404(CartItem, id=cart_id, user=request.user)

    if cart_item.quantity > 1:

        cart_item.quantity -= 1

        cart_item.save()

        return redirect('view_cart')
    
    else:

        cart_item.delete()

        return redirect('view_cart') 

@login_required(login_url='/')
def place_order(request):
    if request.method == 'POST':
        cart_items = CartItem.objects.filter(user=request.user)
        if cart_items.exists():
            order = Order.objects.create(user=request.user)
            for item in cart_items:
                OrderItem.objects.create(
                    order=order,
                    book=item.book,
                    quantity=item.quantity,
                    price=item.book.price
                )
            cart_items.delete()
        return redirect('my_orders')
    

@login_required(login_url='/')
def my_orders(request):

    orders = Order.objects.filter(user=request.user).order_by('-created_at')

    return render(request, 'main/my_orders.html', {'orders': orders})