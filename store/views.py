from django.shortcuts import render,get_object_or_404,redirect
from .models import Product,RevieRating,ProductGallery
from category.models import Category
from cart.views import _cart_id
from cart.models import Cart,Cartitem
from django.core.paginator import Paginator,EmptyPage,PageNotAnInteger
from django.db.models import Q 
from .forms import ReviewForm
from django.contrib import messages
from orders.models import OrderProduct,Order
# Create your views here.
def store(request, category_slug=None):
    categories = None
    products = None

    if category_slug != None:
        categories = get_object_or_404(Category, slug=category_slug)
        products = Product.objects.filter(category=categories, is_available = True)
        paginator = Paginator(products, 4)
        page= request.GET.get('page')
        page_product = paginator.get_page(page)
        product_count = products.count()

    else:    
        products = Product.objects.all().filter(is_available = True).order_by('id')
        paginator = Paginator(products, 4)
        page= request.GET.get('page')
        page_product = paginator.get_page(page)
        product_count = products.count()
    context = {
        'products' : page_product,
        'product_count' : product_count
    }
    return render(request,'store.html', context)

def product_details(request, category_slug, product_slug):
    try:
        single_product=Product.objects.get(category__slug=category_slug, slug=product_slug)
        in_cart = Cartitem.objects.filter(cart__cart_id=_cart_id(request), product=single_product).exists()
    except Exception as e:
        raise e    
    
    if request.user.is_authenticated:
        try:
            orderproduct = OrderProduct.objects.filter(user=request.user, product_id=single_product.id).exists()
        except OrderProduct.DoesNotExist:    
            orderproduct = None
    else:
        orderproduct = None                

    #get the reviews
    reviews = RevieRating.objects.filter(product_id=single_product.id, status = True)
#get the product gallery
    product_gallery = ProductGallery.objects.filter(product_id=single_product.id)
    context={
        'single_product':single_product,
        'in_cart':in_cart,
        'orderproduct': orderproduct,
        'reviews': reviews,
        'product_gallery':product_gallery
    }
    return render(request, 'product_detail.html', context)

def search(request):
    if 'keyword' in request.GET:
        keyword = request.GET['keyword']
        if keyword:
            products = Product.objects.filter(Q(pro_name__icontains=keyword) |Q( desc__icontains=keyword)).order_by('-created_date')
            product_count = products.count()
    context = {
        'products':products,
        'product_count':product_count,
    }
    return render(request, 'store.html',context)

def submit_review(request, product_id):
    url = request.META.get('HTTP_REFERER')
    if request.method == "POST":
        try:
            reviews = RevieRating.objects.get(user__id=request.user.id, product__id=product_id)
            form = ReviewForm(request.POST,instance=reviews)
            form.save()
            messages.success(request,'Thank you your review has been update')
            return redirect(url)
        except RevieRating.DoesNotExist:
            form = ReviewForm(request.POST)
            if form.is_valid():
                data = RevieRating()
                data.subject = form.cleaned_data['subject']
                data.rating = form.cleaned_data['rating']
                data.review = form.cleaned_data['review']
                data.ip = request.META.get('REMOTE_ADDR')
                data.product_id = product_id
                data.user_id = request.user.id
                data.save()
                messages.success(request,'Thank you for your review')
                return redirect(url)