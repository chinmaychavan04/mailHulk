
from django.http.response import HttpResponse
from django.shortcuts import redirect, render
from .forms import Mailform
from .models import Mail
import pandas as pd
from .send_email import sendMail

# Create your views here.
def login(request):
    form = Mailform(request.POST or None, request.FILES or None)
    if form.is_valid():
        form.save()
        obj = Mail.objects.get(activated=False)
        excel_data = pd.read_excel(obj.email.path)
        df = pd.DataFrame(excel_data)
        mail_list = list(df['email'])
        #print(mail_list)
        obj.activated = True
        obj.save()
        sendMail(request, mail_list)
        return render(request, 'ac/upload1.html')
    content = {'form': form}
    return render(request, 'ac/upload.html', content)

