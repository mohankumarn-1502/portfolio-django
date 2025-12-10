from django.shortcuts import render

# Create your views here.
def IndexPageResponse(request):
    return render(request,'./index.html')

def ToolsPageResponse(request):
    return render(request,'./tools.html')

def AboutPageResponse(request):
    return render(request,'./about.html')

def ResumePageResponse(request):
    return render(request,'./resume.html')

def ProjectPageResponse(request):
    return render(request,'./projects.html')

def AmaPageResponse(request):
    return render(request,'./ama.html')