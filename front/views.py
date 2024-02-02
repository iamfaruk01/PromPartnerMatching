from django.shortcuts import render
from django.http import HttpResponse
from .models import Partner

def index(request):
    return render(request, 'index.html')

from .models import Partner

def match_partners(request):
    if request.method == 'POST':
        name = request.POST.get('name').lower()
        email = request.POST.get('email').lower()
        preferred_partner_names_str = request.POST.get('preferred_partner')

        # Split the string into a list based on commas and convert to lowercase
        preferred_partner_names = [name.strip().lower() for name in preferred_partner_names_str.split(',')]

        # Save the user input to the database
        partner = Partner.objects.create(
            name=name,
            email=email,
            preferred_partners=', '.join(preferred_partner_names)  # Join the list into a comma-separated string
        )

        # Find matches in the database based on the names in preferred_partner_names
        matching_partners = Partner.objects.filter(name__in=preferred_partner_names)

        # filter partners if in the database's preferred_partners colummns the 'name' is present
        matching_partners = matching_partners.filter(preferred_partners__contains=name)


        # Optionally, you can perform additional logic or redirect the user
        return render(request, "resultMatch.html", {"name": name, "matching_partners": matching_partners})
    else:
        return render(request, 'index.html')

