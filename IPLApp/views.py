from django.shortcuts import render,HttpResponseRedirect
import MySQLdb
import datetime
from django.http import HttpResponse
from django.core.files.storage import FileSystemStorage
import json
from datetime import date
from datetime import datetime
import datetime
import webbrowser

db = MySQLdb.connect('localhost','root','','ipl')
c = db.cursor()

# Create your views here.

def sendsms(ph,msg):
    sendToPhoneNumber= "+91"+ph
    userid = "2000022557"
    passwd = "54321@lcc"
    url = "http://enterprise.smsgupshup.com/GatewayAPI/rest?method=sendMessage&send_to=" + sendToPhoneNumber + "&msg=" + msg + "&userid=" + userid + "&password=" + passwd + "&v=1.1&msg_type=TEXT&auth_scheme=PLAIN"
    # contents = urllib.request.urlopen(url)
    webbrowser.open(url)
    
def CommonHome(request):
    return render(request,'CommonHome.html')

def SignIn(request):  
    request.session['username']=""
    request.session['NAME']=""
    request.session['uid']=""
    request.session['cid']=""
    request.session['sid']=""
    msg=""
    if request.POST:
        email = request.POST.get("email")
        password = request.POST.get("password")
        c.execute("select * from login where uname='"+ email +"' and pass='"+ password +"'")
        ds = c.fetchone()
        request.session['username']=email
        if ds is not None:
            if ds[2] == 'Admin':
                return HttpResponseRedirect('/AdminHome/')
            elif ds[2] == 'Customer':
                c.execute("select * from cust_reg where email='"+email+"' and password='"+password+"'")
                ds = c.fetchone()
                request.session['cid'] = ds[0]
                request.session['NAME'] = ds[1]
                return HttpResponseRedirect('/CustomerHome/')
            elif ds[2] == 'Club':
                c.execute("select * from club where email='"+email+"' and password='"+password+"'")
                ds = c.fetchone()
                request.session['clid'] = ds[0]
                return HttpResponseRedirect('/ClubHome/')
        else:
            msg = "Incorrect username or password"
    return render(request,'Login.html',{"msg":msg}) 

def ClubRegistration(request):
    msg = ""
    if request.POST:
        name = request.POST.get("clname")
        adrs = request.POST.get("owner")
        district = request.POST.get("venue")
        location = request.POST.get("coach")
        phone = request.POST.get("email")
        email = request.POST.get("Password")
        qry = "insert into club(club,owner,venue,coach,email,password,status) values('"+ name +"','"+ adrs +"','"+ district +"','"+ location +"','"+ phone +"','"+ email +"','Registered')"
        qry1= "insert into login values('"+phone+"','"+email+"','Club')"
        c.execute(qry)
        c.execute(qry1)
        print(qry)
        db.commit()
        msg = "club Details Added Successfully."
        return HttpResponseRedirect('/SignIn/')
    return render(request,'ClubRegistration.html',{"msg":msg})

def CustomerRegistration(request):
    if request.POST:
        cname = request.POST.get("cname")
        address = request.POST.get("address")
        gender = request.POST.get("gender")
        email = request.POST.get("Email")
        mobile = request.POST.get("mobile")
        password = request.POST.get("Password")
        type= "Customer"
        qry="insert into cust_reg(cname,address,gender,email,mobile,password) values('"+ cname +"','"+ address +"','"+ gender +"','"+ email +"','"+ mobile +"','"+ password +"')"
        qr ="insert into login values('"+ email +"','"+ password +"','"+ type +"')"
        c.execute(qry)
        c.execute(qr)
        db.commit()
        return HttpResponseRedirect('/SignIn/')
    return render(request,'CustomerRegistration.html')

def AdminHome(request):
    return render(request,'AdminHome.html') 

def ClubHome(request):
    return render(request,'ClubHome.html')

def CustomerHome(request):
    return render(request,'CustomerHome.html')

def AdminViewCustomers(request):
    data = ""
    c.execute("select * from cust_reg")
    data=c.fetchall() 
    return render (request,"AdminViewCustomers.html",{"data":data})

def AdminViewClub(request):
    c.execute("SELECT * from club where status = 'Registered'")
    data = c.fetchall()
    if request.GET:
        cl = request.GET.get('id')
        st = request.GET.get('st')
        c.execute("update club set status = '"+st+"' where clid = '"+cl+"'")
        db.commit()
        return HttpResponseRedirect("/AdminViewClub/")
    return render(request,"AdminViewClub.html",{"data":data})

def AdminAddFixtures(request):
    msg=""
    c.execute("select * from club")
    data = c.fetchall()
    if request.POST:
        teamone = request.POST.get('team1')
        teamtwo = request.POST.get('team2')
        venue = request.POST.get('venue')
        mdate = request.POST.get('date')
        mtime = request.POST.get('time')
        c.execute("insert into fixtures(teamone,teamtwo,venue,mdate,mtime) values('"+teamone+"','"+teamtwo+"','"+venue+"','"+mdate+"','"+mtime+"')")
        db.commit()
        msg = "Match Added Successfully."
    return render(request,'AdminAddFixtures.html',{"msg":msg,"data":data})

def ClubAddPlayer(request):
    msg=""
    clid = request.session['clid']
    if request.POST:
        name = request.POST.get('clname')
        type = request.POST.get('type')
        category = request.POST.get('category')
        match = request.POST.get('match')
        runs = request.POST.get('runs')
        wickets = request.POST.get('wickets')
        if request.POST and request.FILES:
            img=request.FILES.get("file")
            fs=FileSystemStorage()
            filename=fs.save(img.name,img)
            path=fs.url(filename)
            c.execute("insert into player(player,team,type,category,matches,totalruns,totalwickets,image) values('"+name+"','" +str(clid) +"','"+type+"','"+category+"','"+match+"','"+runs+"','"+wickets+"','"+path+"')")
            db.commit()
            msg = "Player Added Successfully."
    return render(request,'ClubAddPlayer.html',{"msg":msg})

def ClubAddNewsUpdates(request):
    msg=""
    clid = request.session['clid']
    if request.POST:
        name = request.POST.get('clname')
        match = request.POST.get('match')
        if request.POST and request.FILES:
            img=request.FILES.get("file")
            fs=FileSystemStorage()
            filename=fs.save(img.name,img)
            path=fs.url(filename)
            c.execute("insert into news(clid,news,details,image) values('" +str(clid) +"','"+name+"','"+match+"','"+path+"')")
            db.commit()
            msg = "News Added Successfully."
    return render(request,'ClubAddNewsUpdates.html',{"msg":msg})

def ClubViewFixtures(request):
    data = ""
    c.execute("select * from fixtures")
    data=c.fetchall() 
    return render (request,"ClubViewFixtures.html",{"data":data})

def ClubViewFeedback(request):
    data = ""
    clid = request.session["clid"]
    c.execute("SELECT feedback.*, cust_reg.* FROM feedback INNER JOIN cust_reg on cust_reg.cid = feedback.cid where feedback.clid = '"+str(clid)+"'")
    data = c.fetchall()
    if request.GET:
        a = request.GET.get('id')
        c.execute("delete from feedback where fid = '"+a+"'")
        db.commit()
        return HttpResponseRedirect("/ClubViewFeedback/")
    return render (request,"ClubViewFeedback.html",{"data":data})

def ClubViewcomplaints(request):
    data = ""
    clid = request.session["clid"]
    c.execute("SELECT complaints.*, cust_reg.* FROM complaints INNER JOIN cust_reg on cust_reg.cid = complaints.cid where complaints.clid = '"+str(clid)+"'")
    data = c.fetchall()
    if request.GET:
        a = request.GET.get('id')
        c.execute("delete from complaints where fid = '"+a+"'")
        db.commit()
        return HttpResponseRedirect("/ClubViewcomplaints/")
    return render (request,"ClubViewcomplaints.html",{"data":data})

def CustomerViewClubDetails(request):
    data = ""
    c.execute("select * from club")
    data=c.fetchall() 
    return render (request,"CustomerViewClubDetails.html",{"data":data})

def CustomerViewFixtures(request):
    data = ""
    c.execute("select * from fixtures")
    data=c.fetchall() 
    return render (request,"CustomerViewFixtures.html",{"data":data})

def CustomerViewNewsUpdates(request):
    data = ""
    c.execute("select * from news")
    data=c.fetchall() 
    if request.GET:
        a = request.GET.get('id')
        request.session["nid"] = a
        return HttpResponseRedirect('/CustomerViewMoreNewsUpdates/')
    return render (request,"CustomerViewNewsUpdates.html",{"data":data})

def CustomerViewMoreNewsUpdates(request):
    data = ""
    nid = request.session["nid"]
    c.execute("select * from news where nid = '"+nid+"'")
    data=c.fetchall() 
    return render (request,"CustomerViewMoreNewsUpdates.html",{"data":data})

def CustomerAddFeedback(request):
    msg=""
    c.execute("select * from club")
    data=c.fetchall() 
    cid = request.session['cid']  
    if request.POST:
        a=request.POST.get("room")
        b = date.today()
        d=request.POST.get("dist")
        c.execute("insert into feedback(cid,clid,feedback,fdate) values('"+str(cid)+"','"+str(d)+"','"+a+"','"+str(b)+"')")
        db.commit()
        msg = "Feedback Added Successfully."
    return render(request,"CustomerAddFeedback.html",{"msg":msg,"data":data})

def CustomerAddComplaints(request):
    msg=""
    c.execute("select * from club")
    data=c.fetchall() 
    cid = request.session['cid']  
    if request.POST:
        a=request.POST.get("room")
        b = date.today()
        d=request.POST.get("dist")
        c.execute("insert into complaints(cid,clid,complaints,cdate) values('"+str(cid)+"','"+str(d)+"','"+a+"','"+str(b)+"')")
        db.commit()
        msg = "Complaints Added Successfully."
    return render(request,"CustomerAddComplaints.html",{"msg":msg,"data":data})

def CustomerViewTeamSquad(request):
    data = ""
    c.execute("select * from club")
    data=c.fetchall() 
    if request.POST:
        a=request.POST.get("dist")
        request.session["team"] = a
        return HttpResponseRedirect('/CustomerViewPlayers/')
    return render (request,"CustomerViewTeamSquad.html",{"data":data})

def CustomerViewPlayers(request):
    data = ""
    a= request.session["team"]
    c.execute("select * from player where team ='"+a+"' ")
    data=c.fetchall() 
    if request.GET:
        a=request.GET.get("id")
        request.session["pid"] = a
        return HttpResponseRedirect('/CustomerViewPlayerDetails/')
    return render (request,"CustomerViewPlayers.html",{"data":data})

def CustomerViewPlayerDetails(request):
    data = ""
    a= request.session["pid"]
    c.execute("select * from player where pid ='"+a+"' ")
    data=c.fetchall() 
    return render (request,"CustomerViewPlayerDetails.html",{"data":data})


from prediction import predict
def predict_result(request):
    data=""
    if request.method == 'POST':
        home_team = request.POST.get('homeTeam')
        away_team = request.POST.get('awayTeam')
        city = request.POST.get('city')
        toss_winner = request.POST.get('tossWinner')
        toss_decision = request.POST.get('selector1')
        print(home_team, away_team, city, toss_winner, toss_decision)
        winner_team = predict(home_team, away_team, city, toss_winner, toss_decision).__str__()
        print("Winning Team is -> " + winner_team)
        # home_team_name = convert_back_to_team_names(home_team).__str__()
        # away_team_name = convert_back_to_team_names(away_team).__str__()
        data=winner_team
        print(data)
        
        return render(request,"predictionresult.html",{"data":data})
        

    return render(request,"predict.html",{"data":data})

def score(request):
    data=""
    if request.method == 'POST':
        runs=request.POST.get("run")
        wicket=request.POST.get("wicket")
        over=request.POST.get("over")
        s1=request.POST.get("s1")
        s2=request.POST.get("s2")
        
        #random forest algm
        import pandas as pd
        dataset = pd.read_csv('data/ipl.csv')
        X = dataset.iloc[:,[7,8,9,12,13]].values
        y = dataset.iloc[:, 14].values

        # Splitting the dataset into the Training set and Test set
        from sklearn.model_selection import train_test_split
        X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.25, random_state = 0)

        # Feature Scaling
        from sklearn.preprocessing import StandardScaler
        sc = StandardScaler()
        X_train = sc.fit_transform(X_train)
        X_test = sc.transform(X_test)

        # Training the dataset
        from sklearn.ensemble import RandomForestRegressor
        reg = RandomForestRegressor(n_estimators=100,max_features=None)
        reg.fit(X_train,y_train)

        # Testing the dataset on trained model
        y_pred = reg.predict(X_test)
        score = reg.score(X_test,y_test)*100
        # print("R square value:" , score)
        # print("Custom accuracy:" , custom_accuracy(y_test,y_pred,20))

        # Testing with a custom input
        import numpy as np
        new_prediction = reg.predict(sc.transform(np.array([[runs,wicket,over,s1,s2]]))) #run,wickets,overs,striker run,s2 run
        print("Prediction score:" , new_prediction)
        data=np.round(new_prediction)
        return render(request,"predictionresult1.html",{"data":data})

    return render(request,"score.html",{"data":data})
