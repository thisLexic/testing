from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import CreateView
from . import forms
from django.urls import reverse_lazy
from django.contrib.auth.decorators import login_required
from .forms import CreateEntryForm, CreateDailyCashForm, ProductNumberFormSet
from .models import Product, Branch, Entry
from django.contrib import messages
# from django.contrib.auth.mixins import LoginRequiredMixin


# class EntryCreateView(LoginRequiredMixin, CreateView):
#     # form_class = forms.EntryForm
#     fields = ('product_number','branch', 'product', 'date')
#     model = Entry
#     template_name = "form.html"
#     success_url = reverse_lazy("form:create")
#     redirect_field_name = '/form/'
#     login_url = '/'

@login_required
def create_sold(request):
    isEmpty = False
    isRepeat = False
    if request.method == "POST":
        request_post = request.POST
        date = request_post.__getitem__("date")
        branch = get_object_or_404(Branch, pk=request_post.__getitem__("branch"))
        # print(request_post)
        dailyCash = request_post.__getitem__("actual_income")
        # print(dailyCash)
        form = CreateEntryForm(request_post)
        formM = CreateDailyCashForm(request_post)
        formP = ProductNumberFormSet
        print(formM.is_valid())

        if form.is_valid() and formM.is_valid(): 
            num = Product.objects.all().count()
            # this for loop is to check for empty values of
            for n, product in zip(range(num), Product.objects.all()):
                if "" == request_post.__getitem__("form-" + str(n) + "-product_number"):
                    isEmpty = True
            # is there a better way of looping through the items in a formset?
            if (not isEmpty):
                formM = CreateDailyCashForm(request_post)
                cash = formM.save(commit=False)
                cash.theoretical_income = float(0)

                for n, p in zip(range(num), Product.objects.all()):
                    # for saving to Entry table
                    form = CreateEntryForm(request_post)
                    pn = request_post.__getitem__("form-" + str(n) + "-product_number")
                    entry = form.save(commit=False)
                    entry.product = p
                    entry.product_number = pn
                    try:
                        entry.save()
                    except:
                        isRepeat = True
                        break
                    cash.theoretical_income += float(pn)*float(p.price)
                # for saving to DailyCash table
                cash.branch = branch
                cash.date = date
                cash.difference_value = abs(cash.theoretical_income - float(cash.actual_income))
                try:
                    cash.difference_percent = cash.difference_value/cash.theoretical_income
                except:
                    cash.difference_percent = 0
                cash.save()
                form = CreateEntryForm()
                formM = CreateDailyCashForm()
                formP = ProductNumberFormSet
            # messages.success(request, 'Successfully submitted the form for ' + date)
    else:
        form = CreateEntryForm
        formM = CreateDailyCashForm
        formP = ProductNumberFormSet
        date = ""
        branch = ""
    return render(request, 'form.html', {'form': form,
        # 'form_products':zip(Product.objects.all(), form.product_number_set),
        "isempty":isEmpty,
        "formM":formM,
        "formP":zip(Product.objects.all(), formP),
        "isrepeat":isRepeat,
        "invaliddate":date,
        "invalidbranch":branch,
    	})


def create_inventory(request):
    # to be done
    if request.method == "POST":
        pass
    else:
        form = CreateEntryForm
        formM = CreateDailyCashForm
        formP = ProductNumberFormSet
    return render(request, 'form.html', {'form': form,
        # 'form_products':zip(Product.objects.all(), form.product_number_set),
        "isempty":isEmpty,
        "formM":formM,
        "formP":zip(Product.objects.all(), formP),
        })