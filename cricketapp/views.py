from django.shortcuts import render,redirect,HttpResponseRedirect,HttpResponse
from .models import *
from django.contrib.auth import authenticate
from django.contrib import messages

# Create your views here.
def index(request):
    return render(request,'index.html')

def login(request):
    if request.POST:
        Username=request.POST['email']
        Password=request.POST['password']
        print(Username,'##',Password)
        user=authenticate(username=Username,password=Password)
        print(user)
        if user is not None:
            # login(request,user)
            if user.usertype=='admin':
                id=user.id
                request.session['uid']=id
                request.session['type']='admin'
                msg="login successfully"
                messages.info(request,msg)
                print("msg",msg)
                return redirect('/adminhome')
            
            elif user.usertype=='customer':
                id=user.id
                request.session['uid']=id
                request.session['type']='customer'
                msg="login successfully"
                messages.info(request,msg)
                print("msg",msg)
                return redirect('/customerhome')
            
            elif user.usertype=='club':
                id=user.id
                request.session['uid']=id
                request.session['type']='club'
                msg="login successfully"
                messages.info(request,msg)
                print("msg",msg)
                return redirect('/clubhome')
            
            else:
                msg="username or password invalid"
                messages.info(request,msg)
                print("msg",msg)
                return redirect('/login')
    return render(request,'login.html')

def register(request):
    if request.POST:
        name=request.POST['name']
        Address=request.POST['Address']
        email=request.POST['email']
        password=request.POST['password']
        phone=request.POST['phone']
        if Register.objects.filter(email=email,phone=phone).exists():
            print("already exists")
            messages.info(request," User Already exists")
        else:
            q=Login.objects.create_user(username=email,usertype='customer',password=password,viewpassword=password)
            q.save()
            reg=Register.objects.create(name=name,Address=Address,email=email,phone=phone,user=q)
            reg.save()
            messages.info(request," User Register successfully")
            return redirect('/login')

    return render(request,'register.html')

def clubregister(request):
    if request.POST:
        name=request.POST['name']
        owner=request.POST['owner']
        email=request.POST['email']
        password=request.POST['password']
        contact_number=request.POST['phone']
        logo=request.FILES['logo']

        if Club.objects.filter(email=email,contact_number=contact_number).exists():
            print("already exists")
            messages.info(request," User Already exists")
        else:
            q=Login.objects.create_user(username=email,usertype='club',password=password,viewpassword=password,is_active=0)
            q.save()
            reg=Club.objects.create(name=name,owner=owner,email=email,contact_number=contact_number,logo=logo,user=q)
            reg.save()
            messages.info(request," Club Register Successfully")
            return redirect('/login')

    return render(request,'clubregister.html')


################ ADMIN #################
def adminhome(request):
    return render(request,'admin/adminhome.html')

def club(request):
    qy=Club.objects.all()
    return render(request,'admin/club.html',{'qy':qy})

def approve(request):
    status=request.GET['status']
    id=request.GET['id']
    club=Login.objects.get(id=id)
    club.is_active=int(status)
    club.save()
    if status == '1':
        messages.info(request," Approved successfully")
    else:
        messages.info(request,"Rejected successfully")
    return redirect('/club')

def deleteclub(request):
    id=request.GET.get('id')
    qry=Login.objects.filter(id=id).delete()
    messages.info(request,"Deleted Successfully")
    return redirect('/club')

def customers(request):
    qy=Register.objects.all()
    return render(request,'admin/customer.html',{'qy':qy})

def delete(request):
    id=request.GET.get('id')
    qry=Login.objects.filter(id=id).delete()
    messages.info(request," Deleted Successfully")
    return redirect('/customers')

def addfixtures(request):
    clubs=Club.objects.all()
    if request.POST:
        date=request.POST['date']
        venue=request.POST['venue']
        team1_id=request.POST['team1']
        team1=Club.objects.get(id=team1_id)
        team2_id=request.POST['team2']
        team2=Club.objects.get(id=team2_id)  
        fix=Fixture.objects.create(date=date,venue=venue,team1=team1,team2=team2)
        fix.save()
        messages.info(request," Add Fixture successfully")
        return redirect('/fixture')
    fix=Fixture.objects.all()
    return render(request,'admin/fixtures.html',{'clubs':clubs,'fix':fix})

def addresult(request):
    id=request.GET.get('id')
    if request.POST:
        result=request.POST['result']
        add=Fixture.objects.filter(id=id).update(result=result,status="finish")
        messages.info(request,"Result added Successfully")
        return redirect('/fixtures')
    return render(request,'admin/addresult.html')



######################  CLUB  ####################
def clubhome(request):
    return render(request,'club/clubhome.html')

def addplayers(request):
    uid=request.session['uid']
    if request.POST:
        name=request.POST['name']
        image=request.FILES['image']
        age=request.POST['age']
        role=request.POST['role']
        club=Club.objects.get(user=uid)
        batting_avg=request.POST['bat']
        bowling_avg=request.POST['bowl']
        play=Player.objects.create(name=name,image=image,age=age,role=role,club=club,batting_average=batting_avg,bowling_average=bowling_avg)
        play.save()
        messages.info(request,"Add players Successfully")
        return redirect('/clubhome')
    return render(request,'club/addplayer.html')

def viewplayers(request):
    uid=request.session['uid']
    club=Club.objects.get(user=uid)
    player=Player.objects.filter(club=club).all().order_by('role')
    return render(request,'club/viewplayers.html',{'player':player})

def addnews(request):
    uid=request.session['uid']
    if request.POST:
        club=Club.objects.get(user=uid)
        title=request.POST['title']
        image=request.FILES['image']
        content=request.POST['content']
        news=News.objects.create(club=club,title=title,image=image,content=content)
        news.save()
        messages.info(request,"Add news Successfully")
        return redirect('/clubhome')
    return render(request,'club/addnews.html')

def viewfixtures(request):
    qy=Fixture.objects.all()
    return render(request,'club/viewfixtures.html',{'qy':qy})


def viewfeedback(request):
    uid=request.session['uid']
    club=Club.objects.get(user=uid)
    feedbacks=Feedback.objects.filter(club=club).all()
    return render(request,'club/viewfeedback.html',{'feedbacks':feedbacks})

def viewcomplaint(request):
    uid=request.session['uid']
    club=Club.objects.get(user=uid)
    complaint=Complaint.objects.filter(club=club).all()
    return render(request,'club/viewcomplaint.html',{'complaint':complaint})
    



###################  CUSTOMER  #####################
def customerhome(request):
    return render(request,'customer/customerhome.html')

def viewclub(request):
    qy=Club.objects.all()
    return render(request,'customer/viewclub.html',{'qy':qy})

def feedback(request):
    uid=request.session['uid']
    clubs=Club.objects.all()
    if request.POST:
        feedback=request.POST['feedback']
        club_id=request.POST['club']
        club=Club.objects.get(id=club_id)
        user=Register.objects.get(user=uid)          
        fb=Feedback.objects.create(feedback=feedback,club=club,user=user)
        fb.save()
        messages.info(request," Add Feedback successfully")
        return redirect('/customerhome')
    return render(request,'customer/feedback.html',{'clubs':clubs})

def viewfixtures_cust(request):
    qy=Fixture.objects.all()
    return render(request,'customer/viewfixtures_cust.html',{'qy':qy})

def complaint(request):
    uid=request.session['uid']
    clubs=Club.objects.all()
    if request.POST:
        complaint=request.POST['complaint']
        club_id=request.POST['club']
        club=Club.objects.get(id=club_id)
        user=Register.objects.get(user=uid)      
        cpt=Complaint.objects.create(complaint=complaint,club=club,user=user)
        cpt.save()
        messages.info(request," Add Complaint successfully")
        return redirect('/customerhome')
    return render(request,'customer/complaint.html',{'clubs':clubs})

def viewnews(request):
    news=News.objects.all().order_by('-date_posted')
    return render(request,'customer/viewnews.html',{'news':news})


def viewnewsdetail(request):
    id=request.GET.get('id')
    news=News.objects.filter(id=id).all()
    return render(request,'customer/newsdetail.html',{'news':news})

def viewclub_based_players(request):
    player=Player.objects.all().order_by('club')
    return render(request,'customer/club_based_players.html',{'player':player})

def viewplayer_cus(request):
    id=request.GET.get('id')
    player=Player.objects.filter(club=id).all().order_by('role')
    return render(request,'customer/viewplayers_customer.html',{'player':player})


#################### PREDICTION #######################



from django.shortcuts import render
from sklearn.preprocessing import LabelEncoder
import joblib
import pandas as pd
from django.http import JsonResponse

def predict_toss_winner(new_data, label_encoder, model):
   
    new_data_encoded = new_data.copy()
    
    new_data_encoded['Venue'] = label_encoder.fit_transform(new_data['Venue'])
    print("#######################",new_data_encoded['Team1'])
    new_data_encoded['Team1'] = label_encoder.fit_transform(new_data['Team1'])
    new_data_encoded['Team2'] = label_encoder.fit_transform(new_data['Team2'])
    new_data_encoded['TossWinner'] = label_encoder.fit_transform(new_data['TossWinner'])
    predicted_toss_winner = model.predict(new_data_encoded)
    return label_encoder.inverse_transform(predicted_toss_winner)


def toss_prediction(request):
   if request.method == 'POST':
        venue = request.POST['venue']
        team1 = request.POST['t1']
        team2 = request.POST['t2']
        toss_winner = request.POST['toss_winner']

        # Load the trained model
        model_filename = "toss_based_winner_prediction_model.joblib"
        model = joblib.load(model_filename)

        # Load the LabelEncoder
        label_encoder = LabelEncoder()
        # label_encoder.classes_ = model.classes_

        # Make the prediction using the trained model
        new_data = pd.DataFrame({'Venue': [venue], 'Team1': [team1], 'Team2': [team2], 'TossWinner': [toss_winner]})
        print(new_data)
        predicted_toss_winner = predict_toss_winner(new_data, label_encoder, model)

        return render(request, 'club/toss_prediction.html', {'predicted_toss_winner': predicted_toss_winner[0]})

   return render(request, 'club/toss_prediction.html')


model_filename = "linear_regression_model.joblib"
model = joblib.load(model_filename)

# Function to predict the score based on user inputs
def predict_score(user_input):
    new_data = pd.DataFrame(user_input, index=[0])
    predicted_score = model.predict(new_data)
    return predicted_score[0]

def score_prediction(request):
    if request.method == 'POST':
        user_input = {
            'runs': [int(request.POST['runs'])],
            'wickets': [int(request.POST['wickets'])],
            'overs': [float(request.POST['overs'])],
            'runs_last_5': [int(request.POST['runs_last_5'])],
            'wickets_last_5': [int(request.POST['wickets_last_5'])],
            'striker': [int(request.POST['striker'])],
            'non-striker': [int(request.POST['non_striker'])]
        }

        predicted_score = predict_score(user_input)
        # return JsonResponse({'predicted_score': predicted_score})
        return render(request, 'club/runbased prediction.html',{'predicted_score': predicted_score})
    return render(request, 'club/runbased prediction.html')

def score_prediction_cust(request):
    if request.method == 'POST':
        user_input = {
            'runs': [int(request.POST['runs'])],
            'wickets': [int(request.POST['wickets'])],
            'overs': [float(request.POST['overs'])],
            'runs_last_5': [int(request.POST['runs_last_5'])],
            'wickets_last_5': [int(request.POST['wickets_last_5'])],
            'striker': [int(request.POST['striker'])],
            'non-striker': [int(request.POST['non_striker'])]
        }

        predicted_score = predict_score(user_input)
        return render(request, 'customer/score_prediction.html',{'predicted_score': predicted_score})
    return render(request, 'customer/score_prediction.html')


def toss_prediction_cust(request):
   if request.method == 'POST':
        venue = request.POST['venue']
        team1 = request.POST['t1']
        team2 = request.POST['t2']
        toss_winner = request.POST['toss_winner']

        # Load the trained model
        model_filename = "toss_based_winner_prediction_model.joblib"
        model = joblib.load(model_filename)

        # Load the LabelEncoder
        label_encoder = LabelEncoder()
        # label_encoder.classes_ = model.classes_

        # Make the prediction using the trained model
        new_data = pd.DataFrame({'Venue': [venue], 'Team1': [team1], 'Team2': [team2], 'TossWinner': [toss_winner]})
        print(new_data)
        predicted_toss_winner = predict_toss_winner(new_data, label_encoder, model)
        return render(request,  'customer/toss_prediction_cust.html',  {'predicted_toss_winner': predicted_toss_winner[0]})
   
   return render(request,  'customer/toss_prediction_cust.html')
