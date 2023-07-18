from django.shortcuts import render

# Create your views here.

def index(request):
    return render(request, 'index.html')
def insert(request):
    if request.method == "POST":
        name = request.POST.get('name')
        age = request.POST.get('age')
        gender = request.POST.get('gender')

        # print(name,school,email)

    data = Student(name=name, age=age, gender=gender)
    data.save()

    return render(request, 'index.html')