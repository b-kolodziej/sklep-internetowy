from django.shortcuts import render, Http404

# Create your views here.
from .models import Product, ProductImage

def search(request):
	try:
		search = request.GET.get('search')
	except:
		search = None
	if search:
		products = Product.objects.filter(title__icontains=search)
		context = {'query': search, 'products': products}
		template = 'products/results.html'
	else:
		template = 'products/home.html'
		context = {}
	return render(request, template, context)



def home(request):
	products = Product.objects.all()
	template = 'products/home.html'
	context = {"products" : products}
	return render(request, template, context)


def all(request):

	products = Product.objects.all()
	context = {"products" : products}
	template = 'products/all.html'
	return render(request, template, context)



def single(request, slug):
	try:
		product = Product.objects.get(slug=slug)
		#images = product.productimage_set.all()
		images = ProductImage.objects.filter(product=product)
		context = {'product' : product, 'images': images}
		template = 'products/single.html'
		return render(request, template, context)
	except:
		raise Http404
