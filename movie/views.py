from django.shortcuts import render, redirect
from django.http import HttpResponse

from .forms import CreateContactForm, CreateCustomerForm
from .models import Movie, Customer, Ticket
# Create your views here.
def home(request):
    movies = Movie.objects.all()
    context = {
        'movies' : movies
    }
    return render(request, 'movie/home.html', context)


def register(request):
    if request.method == 'POST':
        form = CreateCustomerForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = CreateCustomerForm()
        context = {
            'form' : form
        }
    return render(request, 'movie/register.html', context)


def bookings(request):
    if request.method == 'POST':

        form = CreateContactForm(request.POST)
        if form.is_valid():
            contact_no = form.cleaned_data['contact_no']

        customer = Customer.objects.get(contact_no=contact_no)
        return redirect('customer_booking', customer.id)

    else:
        form = CreateContactForm()

    return render(request, 'movie/bookings.html', {'form': form})


def book(request, movie_id):
    movie = Movie.objects.get(pk=movie_id)
    if movie.tickets_available == 0:
        print('Housefull')
        return redirect('home')

    if request.method == 'POST':

        form = CreateContactForm(request.POST)
        if form.is_valid():
            contact_no = form.cleaned_data['contact_no']

        customer = Customer.objects.get(contact_no=contact_no)
        movie.tickets_available -= 1
        movie.save()
        # insert in ticket table
        ticket = Ticket(movie_id=movie, customer_id=customer, movie_name=movie.name)
        ticket.save()
        return redirect('customer_booking', customer.id)

    else:
        form = CreateContactForm()

    return render(request, 'movie/book.html', {'form': form})


def view_details(request, movie_id):
    movie = Movie.objects.get(pk=movie_id)
    context = {
        'movie' : movie
    }
    return render(request, 'movie/view_details.html', context)


def customer_booking(request, customer_id):
    customer = Customer.objects.get(pk=customer_id)
    tickets = Ticket.objects.filter(customer_id_id=customer.id)
    context = {
        'tickets': tickets,
        'customers': customer
    }
    return render(request, 'movie/customer_booking.html', context)

def cancel(request, ticket_id):
    ticket = Ticket.objects.get(pk=ticket_id)
    customer = Customer.objects.get(pk=ticket.customer_id_id)
    movie = Movie.objects.get(name=ticket.movie_name)
    movie.tickets_available += 1
    movie.save()
    Ticket.objects.get(pk=ticket.id).delete()
    return redirect('customer_booking', customer.id)
