from django.shortcuts import render, get_object_or_404, redirect,reverse
from django.views.generic import ListView, DetailView
from django.http import HttpResponse
from django.http import JsonResponse
from django.contrib import messages
from django.db.models import Avg
from django.http import Http404
# store/views.py or wherever you're importing
from .models import Feature, Category, Product, ProductColor, ProductStorage, ProductImage, Review, RelatedProduct



# store/views.py







def product_list(request):

    
    store_title ="TechVerse"
    features = Feature.objects.all()
    return render(request, 'ecommerce/home.html', {'store_title':store_title,'features':features})


   


# Sample Data in Python




def details(request, product_id):
    try:
        product = Product.objects.get(id=product_id)  # Fetch single product
        top_reviews = product.reviews.filter(rating__gte=4)[:5]  # Assuming 'reviews' is related_name
    except Product.DoesNotExist:
        # Handle product not found error
        return render(request, 'ecommerce/product_not_found.html')  

    # Make sure context is defined outside try-except
    context = {
        'product': product,
        'top_reviews': top_reviews,
    }

    return render(request, 'ecommerce/details.html', context)

        
      
        
    #Show 404 if product not found
    #top_reviews = product.reviews.filter(rating__gte=4)[:5]
    #context = {
    #    "product": product,
    #    "top_reviews": top_reviews,
    #    "review_stats": review_stats,
    #    "related_products": related_products,
    #}

    #return render(request, 'store/details.html', context)


def add_review(request, slug):
    product = get_object_or_404(Product, slug=slug)

    if request.method == "POST":
        name = request.POST.get("name")
        email = request.POST.get("email")
        rating = int(request.POST.get("rating"))
        comment = request.POST.get("comment")

        # Save the review to database
        product.reviews.create(
            name=name,
            email=email,
            rating=rating,
            comment=comment
        )

        messages.success(request, "Your review has been submitted!")
        return redirect("store:product_details", slug=slug)

    return redirect("store:product_details", slug=slug)    
    

def account(request):
    return render(request, 'ecommerce/account.html')


#def dev(request):
#    return render(request, 'store/dev.html')

def old_url_redirect(request):

    return redirect(reverse('ecommerce:home'))

def new_url_views(request):  
    return HttpResponse("this new page")     




# Create your views here.




