


###Module imports###
try:
  import pandas as pd
  import numpy as np
  import datetime as dt
  import matplotlib.pyplot as plt
  import os
  import sys
  import glob
  import time
  import tkinter as tk
  from tkinter.ttk import * #Frowned upon, but It appears that tkinter.ttk has to be called this way.
except:
  print('You are missing one of the required modules')
  raise

#############User Input

#Dictionary of states, stations, and station names-- Skip to line 80
stations={'Alabama':{'Albertville_Muni_Arp':'K8A0','Alexander City':'KALX','Analusia':'K79J','Anniston':'KANB','Auburn AWOS':'KAUO','Birmingham':'KBHM','Brookley Aprt':'KBFM','Calera':'KEET','Decatur-Pryor Field':'KDCU','Dothan':'KDHN','Evergreen':'KGZH','Florala':'K0J4','Folsom Field Airport':'K3A1','Ft. Rucker':'KOZR','Gadsden':'KGAD','Haleyviille':'K1M4','Huntsville ASOS':'KHSV','Isbell Field Airport':'K4A9','Jack Edwards Airpot':'KJKA','Lowe AHP':'KLOR','Mac_Crenshaw_mem airport':'KPRN','Madison County Exec AP':'KMDQ','Maxwell AFB':'KMXF','Mobile':'KMOB','Montgomery ASOS':'KMGM','Muscle Shoals':'KMSL','Redstone Arsenal':'KHUA','Talladega Municipal Airport':'KASN','Troy':'KTOI','Tuscaloosa':'KTCL','Visco Knoll 768 Oil':'KVOA','Walker Co. Bevill field':'KJFX','Weedon Field Airport':'KEUF'},
         'Alaska':{'Adak Island':'PADK','Ambler':'PAFM','Anaktuvuk':'PAKP','Anchorage':'PANC','Angoon':'PAGN','Aniak':'PANI','Annette Island':'PANT','Annik Airport':'PANV','Arctic Village':'PARC','ATKA':'PAAK','Atqasuk':'PATQ','Barrow':'PABR','Barter Island':'PABA','Bethel':'PABE','Bettles':'PABT','Big Delta':'PABI','Birchwood':'PABV','Buckland':'PABL','Cape Lisburne AFS':'PALU','Cape Newenham AWOS':'PAEH','Cape Romanzof AWOS':'PACZ','Chevak Airport':'PAVA','Chignik':'PAJC','Cold Bay':'PACD','Cordova':'PACV','Deadhorse':'PASC','Deadhorse/Alpine air':'PALP','Deering':'PADE','Dillingham':'PADL','Dutch Harbor':'PADU','Eagle':'PAEG','Egegik':'PAII','Eielson AFB':'PAEI','Elmendorf AFB':'PAED','Emmonak':'PAEM','Eureka':'PAZK','Fairbanks':'PAFA','False Pass Airport':'PAKF','Ft. Yukon':'PFYU','Galena':'PAGA','Gambell':'PAGM','Golovin':'PAGL','Gulkana':'PAGK','Gustavas':'PAGS','Haines':'PAHN','Holy Cross':'PAHC','Homer':'PAHO','Hoonah AP':'PAOH','Hooper Bay':'PAHP','Huslia':'PAHL','Hydaburg Seaplane':'PAHY','Igiugig':'PAIG','Iliamna':'PAIL','Indian Mtn.':'PAIM','Juneau':'PAJN','Kake':'PAFE','Kalskag':'PALG','Kaltag':'PAKV','Kenai':'PAEN','Ketchikan':'KECA2','Ketchikan ASOS':'PAKT','Kiana':'PAIK','King Cove':'PAVC','King Salmon':'PAKN','Kipnuk Airport':'PAKI','Kivalina':'PAVL','Klawock':'PAKW','Kodiak':'PADQ','Kodiak Island':'KDAA2','Koliganek':'PAJZ','Kotzebue':'PAOT','Koyuk':'PAKK','Kuparuk Airport':'PAKU','Lake Hood Seaplane':'PALH','Manokotak Airport':'PAMB','Marshall':'PADM','Mcgrath':'PAMC','Mckinley Park':'PAIN','Mekoryuk':'PAMY','Merrill Field Airpt':'PAMR','Metlakatla':'PAMM','Middleton':'PAMD','Minchumina':'PAMH','Mountain Village':'PAMO','Nelson Lagoon':'PAOU','Nenana':'PANN','New Stuyahok':'PANW','Nikolai':'PAFS','Noatak':'PAWN','Nokolski':'OLSA2','Nome':'PAOM','Noorvik':'PFNO','Northway':'PAOR','Nuiqsut Airport':'PAQT','Palmer':'PAAQ','Petersburg':'PAPG','Pilot Point':'PAPN','Point Hope':'PAPO','Point Lay':'PPIZ','Port Alsworth':'PALJ','Port Heiden':'PAPH','Portage Glacier':'PATO','Ruby Airport':'PARY','Russian Mission':'PARS','St. Paul Island':'PASN','St. Mary\'s':'PASM','Sand Point':'PASD','Savoonga airport':'PASA','Scammon Bay':'PACM','Selanik':'PASK','Seldovia':'PASO','Seward':'PAWD','Shemya AFB':'PASY','Shishmaref':'PASH','Shungnak Arpt':'PAGH','Sitka':'PASI','Skagway':'PAGY','Sleetmute':'PASL','Soldotna':'PASX','Sparrevohn':'PASV','St. George Island':'PAPB','St. Michael':'PAMK','Talkeetna Arpt':'PATK','Tanana':'PATA','Tatalina AFS':'PATL','Teller':'PATE','Tin CIty AFS':'PATC','Togiak Village':'PATG','Toksook Bay':'PAOO','Unalakleet':'PAUN','Valdez SAWRS':'PAVD','Wainwright':'PAWI','Wainwright AAF':'PAFB','Wales':'PAIW','Wasilla':'PAWS','Wrangell':'PAWG','Yakutat':'PAYA'},
          'Arkansas':{'Arkadelphia':'KADF','Batesville':'KBVX','Baxter Cty. Regional Arpt':'KBPK','Bentonville':'KVBT','Blytheville Municipal':'KHKA','Camden':'KCDH','Clinton Municipal Airport':'KCCA','Corning Municipal Airport':'K4M9','De Queen':'KDEQ','El DOrado':'KELD','Fayetteville':'KFYV0','FLippin':'KFLP','Fort Smith':'KFSM','Harrison':'KHRO','Hot Springs':'KHOT','Jonesboro':'KJBR','Little Rock':'KLIT','Little Rock AFB':'KLRF','Mena Intermountain':'KMEZ','Monticello':'KLLQ','Mt. Ida':'KMWT','Newport Municipal Airport':'KM19','Northwest Arkansas':'KXNA','Pine Bluff':'KPBF','Rogers':'KROG','Russellville':'KRUE','Searcy Municipal Airport':'KSRC','Siloam springs':'KSLG','Springdale Municipal Airpt':'KASG','Stuttgart':'KSGT','Texarkana':'KTXK','Walknut RIdge':'KARG','West Memphis Municipal Airport':'KAWM'},
          'Arizona':{'Buckeye Municipal Airpt':'KBXK','Bullhead City':'KIFP','Casa Grande':'KCGZ','Chandler':'KCHD','Chandler/Williams AF':'KIWA','Davis-Monthan AFB':'KDMA','Deer Valley':'KDVT','Douglas':'KDUG','FLagstaff':'KFLG','Ft. Huachuca':'KFHU','Gila Bend':'KGBN','Glendale Municipal Airpt':'KGEU','Goodyear':'KGYR','Grand Canyon':'KGCN','Kingman':'KIGM','Luke AFB':'KLUF','Nogales International':'KOLS','Page':'KPGA','Payson Airpt':'KPAN','Phoenix':'KPHX','Pioneer Airfield':'KALK','Prescott':'KPRC','Safford':'KSAD','Scottsdale':'KSDL','Sedona Airpt':'KSEZ','Show Low':'KSOW','St. Johns Air Park':'KSJN','Tucson':'KTUS','Williams Clark':'KCMR','Window Rock':'KRQE','Winslow':'KINW','Yuma International Airport':'KNYL'},
          'California':{'29 Palms':'KNXP','9414763 Oakland':'LNDC1','Alturas':'KAAT','Arcata':'KACV','Auburn Municipal Airport':'KAUN','Avalon':'KAVX','Bakersfield':'KBFL','Beale AFB':'KBAB','Bishop ASOS':'KBIH','Blue Canyon ASOS':'KBLU','Blythe':'KBLH','Burbank':'KBUR','Camarillo AWOS':'KCMA','Camp Pendleton':'KNFG','Campo':'KCZZ','Carlsbad':'KCRQ','Castle AFB':'KMER','Chico':'KCIC','China Lake NAS':'KNID','Chino':'KCNO','Columbia Airport':'KO22','Concord':'KCCR','Corona Municipal Airport':'KAJO','Crescent City':'KCEC','Daggett':'KDAG','Desert Resorts':'KTRM','Edwards AFB':'KEDW','Edwards AFB AUX':'K9L2','El Centro NAF':'KNJK','Fresno':'KFAT','Fullerton':'KFUL','Gnoss Field Airport':'KDVO','Half Moon Bay Airport':'KHAF','Hanford':'KHJO','Hawthorne':'KHHR','Hayward':'KHWD','Hollister Municipal Airport':'KCVH','Imperial':'KIPL','Imperial Beach NAS':'KNRS','Lancaster':'KWJF','Lemoore NAS':'KNLC','Lincoln Regional Airport':'KLHM','Livermore':'KLVK','Lompoc':'KLPC','Long Beach':'KLGB','Los Alamitos':'KSLI','Los Angeles':'KLAX','Madera':'KMAE','Mammothh Lakes':'KMMH','March AFB':'KRIV','Marysville':'KMYV','Mather AFB':'KMHR','Mcclellan AFB':'KMCC','Merced':'KMCE','Miramar NAS':'KNKX','Modesto':'KMOD','Mojave':'KMHV','Montague':'KSIY','Monterey':'KMRY','Mountain View NAS':'KNUQ','Mt. Shasta':'KMHS','Mt. Wilson':'KMWS','Napa':'KAPC','Needles':'KEED','North Island NAS':'KNZY','Oakland':'KOAK','Oceanside':'KNXF','Ontario':'KONT','Oroville':'KOVE','Oxnard':'KOXR','Palm Springs':'KPSP','Palmdale':'KPMD','Palo Alto':'KPAO','Paso Robles':'KPRB','Petaluma':'KO69','Point Mugu NAS':'KNTD','Porterville':'KPTV','Ramona':'KRNM','Red Bluff':'KRBL','Redding':'KRDD','Riverside':'KRAL','Sacramento':'KSAC','Sacramento Met. Airport':'KSMF','Salinas':'KSNS','San Carlos':'KSQL','San Diego':'KMYF','San Diego/Brown':'KSDM','San Francisco':'KSFO','San Jose':'KRHV','San Luis Obispo':'KSBP','San Nicolas I. NAS':'KNSI','Sandburg':'KSDB','Santa Ana':'KSNA','Santa Barbara':'KSBA','Santa Maria':'KSMX','Santa Monica':'KSMO','Santa Rosa':'KSTS',' Santa Ynez':'KIZA','South Lake Taho':'KTVL','Stockton':'KSCK','Tehachapi Municipal Airport':'KTSP','Torrance':'KTOA','Travis AFB':'KSUU','Truckee':'KTRK','Ukiah':'KUKI','University Airport':'KEDU','USC Campus':'KCQT','Vacaville':'KVCB','Van Nuys':'KVNY','Vanderberg AFB':'KVBG','Victorville':'KVCV','Visalia':'KVIS','Watsonville':'KWVI','Weaverville Airport':'KO54'},
          'Colorado':{'Akron':'KAKO','Alamosa':'KALS','Aspen':'KASE','Boulder Municipal Airport':'KBDU','Broomfield':'KBJC','Buckley Angb Airport':'KBKF','Burlington':'KITR','Colorado Springs':'KCOS','Copper Mountain':'KCCU','Cortez':'KCEZ','Cottonwood Pass':'K7BM','Craig':'KCAG','Denver International Airport':'KDEN','Durango':'KDRO','Eagle':'KEGE','Elbert Mountain':'KMNH','Englewood':'KAPA','Erie Municipal Airport':'KEIK','Fort Carson':'KFCS','Front Range Airport':'KFTG','Ft. Collins':'KFNL','Grand Junction':'KGJT','Greeley':'KGXY','Gunnison':'KGUC','Harriet Alexander':'KANK','Hayden':'KHDN','Holyoke':'KHEQ','Kremmling':'K20V','La Junta':'KLHX','La Veta Mountain':'KVTP','Lamar':'KLAA','Leadville':'KLXV','Limon':'KLIC','Meeker':'KEEO','Montrose':'KMTJ','Mount Wener':'K3MW','Pagosa Springs':'KPSO','Pagosa Springs':'KCPW','Pueblo':'KPUB','Rifle Regional Airport':'KRIL','Saguache Municipal Airport':'K04V','Salida Mountain':'KMYP','Springfield':'KSPD','Steamboat Springs':'KSBS','Sterling Municipal Airport':'KSTK','Telluride Regiona':'KTEX','Trinidad':'KTAD','USAF Academy':'KAFF','Vance Brand Airport':'KLMO','Walden Jackson Airport':'K33V','Wilerson Pass':'K4BM','Wray Municipal Airport':'K2V5'},
          'Connecticut':{'Bridgeport':'KBDR','Chester Airport':'KSNC','Danbury':'KDXR','Groton':'KGON','Hartford':'KBDL','Hartford-Brainard':'KHFD','Meriden Markham Municipal':'KMMK','New Haven':'KHVN','Oxford':'KOXC','Willimantic':'KIJD'},
          'District of Columbia':{'Washington':'KDCA'},
          'Delaware':{'Dover AFB':'KDOV','Georgetown':'KGED','Wilmington':'KILG'},
          'Florida':{},
          'Georgia':{},
          'Hawaii':{},
          'Idaho':{},
          'Indiana':{},
          'Iowa':{},
          'Kansas':{},
          'Kentucky':{},
          'Louisiana':{},
          'Maine':{},
          'Maryland':{'Aberdeen':'KAPG','Andrews AFB':'KADW','Baltimore':'KBWI','Baltimore ASOS':'KDMH','Bay Bridge Airport':'KW29','Cambridge-Dorchester':'KCGE','Camp David':'KRSP','Caroll County Airport':'KDMW','College Park Airport':'KCGS','Easton':'KESN','Fort Meade':'KFME','Frederick Municipal Airport':'KFDK','Garrett County Airport':'K2G4','Glenn Martin Airport':'KMTN','Greater Cumberland':'KCBE','Hagerstown':'KHGR','Montgomery County Airport':'KGAI','Ocean City':'KOXB','Patapsco':'44043','Patomic':'44042','Patuxent River NAS':'KNHK','Salisbury':'KSBY','St. Inigoes':'KNUI','St. Mary\'s County Regional Airport':'K2W6','U.S. Naval Academy':'KNAK'},
          'Massachusetts':{},
          'Michigan':{},
          'Minnesota':{},
          'Mississippi':{'Jackson':'KHKS'},
          'Missouri':{},
          'Nebraska':{},
          'Nevada':{},
          'New Hampshire':{},
          'New Jersey':{},
          'New Mexico':{},
          'New York':{},
          'North Carolina':{},
          'North Dakota':{},
          'Ohio':{},
          'Oklahoma':{},
          'Oregon':{},
          'Pennsylvania':{},
          'Rhode Island':{},
          'South Carolina':{},
          'South Dakota':{},
          'Tennessee':{},
          'Texas':{},
          'Utah':{},
          'Vermont':{},
          'Virginia':{},
          'Washington':{},
          'West Virginia':{},
          'Wisconsin':{},
          'Wyoming':{}}

monthDict={'january':str(1).zfill(2),'february':str(2).zfill(2),'march':str(3).zfill(2),'april':str(4).zfill(2),'may':str(5).zfill(2),'june':str(6).zfill(2),'july':str(7).zfill(2),'august':str(8).zfill(2),'september':str(9).zfill(2),'october':10,'november':11,'december':12} 
#Have to use zfill for 8 and 9 due to python treating them as 'octals'





###Program Start

runTime=''
modelKey=''
modelName=''
saveCSV=''
delPNG=''
###########Tkinter UI

app=tk.Tk()
app.title('MOS Animator')
app.geometry('500x400')

#Model selection
tk.Label(app,text='Choose a Model').pack()
model=tk.StringVar(app)
model.set('NAM')
opt=Combobox(app,textvariable=model)
opt['values']=['NAM','GFS']
opt.config(width=50, font=('Arial',12))
opt.pack()

#State selection
tk.Label(app,text='Choose a state').pack()
state=tk.StringVar(app)
state.set('Arizona') #Maryland
opt=Combobox(app,textvariable=state)
opt['values']=list(stations.keys())
opt.config(width=50, font=('Arial',12))
opt.pack()



#Stations for each state--- needs to change based on state selection-----Look at how to update this on change for state
tk.Label(app,text='Choose a Station').pack()
station=tk.StringVar(app)
station.set('Tucson')
StatOpt=Combobox(app,textvariable=station)
StatOpt['values']=list(stations[state.get()].keys())
StatOpt.config(width=20, font=('Arial',12))
StatOpt.pack()




##Runtime selection
tk.Label(app,text='Choose a Runtime').pack()
#Option to select today (selected by default)
current=tk.IntVar()
current.set(1)
check=tk.Checkbutton(app,text='Use Today\'s date',variable=current)
check.pack()

#Year,Month,Day-- Switch to grid to make these on the same line
#add a check that converts month name to numerical value
#Month
tk.Label(app,text='Enter your own runtime').pack()
tk.Label(app,text='Month (MM)').pack()
month=tk.Entry(app)
month.pack()
#day
tk.Label(app,text='Day (DD)').pack()
day=tk.Entry(app)
day.pack()
#Year
tk.Label(app,text='Year (YYYY)').pack()
year=tk.Entry(app)
year.pack()


##Extra options
tk.Label(app,text='Extra Options').pack()
#Option to save CSV
saveCSV=tk.IntVar()
check=tk.Checkbutton(app,text='Save a CSV',variable=saveCSV)
check.pack()

#Option to delete PNGS
delPNG=tk.IntVar()
delPNG.set(1)
check=tk.Checkbutton(app,text='Delete the plotted PNGS',variable=delPNG)
check.pack()

###Functions

#FUnction that updates station list when a state is selected
def changeDropDown(*args):
  StatOpt['values']=list(stations[state.get()].keys())
  station.set(next(iter(stations[state.get()].keys())))

    
#Trace that changes stations based on state
state.trace('w',changeDropDown)

#Callback function for submission
def callback():
  global month, stationKey, runTime, modelName, delPNG, saveCSV #Bad practice, but reduces the need to change class objects
  #Get model
  modelName=model.get()
  print('The model is: ' +modelName)
  #Get station
  stateOut=state.get()
  stationOut=station.get()
  stationKey=stations[stateOut][stationOut]
  print('The station is: {0}, {1}: {2}'.format(stationOut,stateOut,stationKey))
  #Get runtime
  if current.get()==1:
    runTime=dt.datetime.today().strftime('%Y-%m-%d')
  else:
  #####Doesn't quite work as expected, entering a month name rather than a month code won't throw an error at this point but it will throw an error at file readin
    try: #Assume the user entered two digit month code
      runTime=str(year.get())+'-'+str(month.get())+'-'+str(day.get())
    except:
      #Assume the user entered month name
      try:
        month=month.str.lower().map(monthDict)
        runTime=str(year.get())+'-'+str(month.get())+'-'+str(day.get())
      except:
        #Throw an error
        print('Couldn\'t read the entered date. Please try again')
        raise
  print('The runtime is: '+runTime)
  #Return variables and close the tkinter UI
  delPNG=delPNG.get()
  saveCSV=saveCSV.get()
  app.destroy()

#Submit button
submitbutton=tk.Button(app,text='Run',width=50,command=callback)
submitbutton.pack()
app.mainloop()
print('Running the plotting script now\n')



######Plotting Script

###File Input###
startTime=time.time()
try:
  print('Reading the files in')
  #URL='https://mesonet.agron.iastate.edu/mos/csv.php?station=KAMW&runtime=2020-03-18&model=NAM'
  URL='https://mesonet.agron.iastate.edu/mos/csv.php?station={0}&model={1}&runtime={2}'.format(stationKey,modelName,runTime)
  dataIn=pd.read_csv(URL, skiprows=1, delimiter=',', header=None).values
except:
  print('An error occurred during file input')
  raise

###Data Prep###
#Extract the variables
try:
  print('Extracting Variables')
  time=pd.to_datetime(dataIn[:,3]) 
  temp=dataIn[:,5]
  dpt=dataIn[:,6]
  #Use a dictionary for cloud cover? cloud=dataIn[:,7]
  wdr=np.array(dataIn[:,8],dtype=np.float64)
  wsp=dataIn[:,9]
  cig=dataIn[:,17] #Use dictionary for height
  #Cloudheights are translated to the midpoint of their respective categories in ft
  cloudDic={1:100,2:300,3:750,4:1450,5:2500,6:4800,7:9300,8:12000,9:0}
  cloudHeight=[]
  for i in cig:
    cloudHeight=np.append(cloudHeight,cloudDic[i])
except:
  print('Something went wrong while reading in the variables')
  raise

###Create Directory for files
try:
  print('Creating a directory')
  curDir=os.getcwd()
  dirName='MOS_'+stationKey+'_'+str(time[0].month_name())+'_'+str(time[0].day)
  os.mkdir(dirName)
  os.chdir(dirName)
except:
  print('Something went wrong while making a directory')
  raise

###Plotting###
try:
  print('Creating Plots')
  r=np.arange(0,3*len(time),3) #Forecast times in steps of three hours
  i=0
  while i<len(time):
  #Create the figure and subplots
    fig=plt.figure(figsize=(10,10))
    ax1=plt.subplot2grid((5,2),(0,0),rowspan=2,colspan=2)
    ax1.set_xlim(min(time),max(time))
    ax2=plt.subplot2grid((5,2),(3,0),rowspan=2)
    ax3=plt.subplot2grid((5,2),(3,1),rowspan=2,polar=True)

  #plot calls
      #Temperature-colors based off skew-T
    ax1.plot(time[:i+1], temp[:i+1],color='red')
    ax1.plot(time[i], temp[i], marker='o',color='red',label='Temperature')
      #Dewpoint
    ax1.plot(time[:i+1], dpt[:i+1],color='green')
    ax1.plot(time[i], dpt[i], marker='o',color='green',label='Dewpoint')
    ax1.set_xlim(min(time),max(time))
    ax1.set_ylim(min(dpt)-2,max(temp)+2)
    ax1.legend(loc=0)
      #wind
    if i==0:
      ax3.plot(np.radians([0,wdr[0]]),[0,1],color='red')
      ax3.scatter(np.radians(wdr[0]), r[0], c='red')
  #Plot line to current
    else:
      ax3.plot(np.radians(wdr[:i+1]),r[:i+1],color='blue')
      ax3.plot(np.radians([0,wdr[i]]),[0,r[i]],color='red')
      ax3.scatter(np.radians(wdr[i]), r[i], c='red')
      #Cloud ceiling 
    ax2.plot(time[:i+1], cloudHeight[:i+1],color='grey')
    ax2.plot(time[i], cloudHeight[i], marker='o',color='grey')
    ax2.set_xlim(min(time),max(time))
    ax2.set_ylim(0,max(cloudHeight)+1000)
    plt.setp(ax2.xaxis.get_majorticklabels(),rotation=45)
  ####### #Plot labels and title
    ax1.set_title('Model Output Statistics for {0} {1} at {2}'.format(str(time[i])[:-6],'UTC',stationKey))
    ax2.set_title('Ceiling Height')
    ax3.set_title('Wind Direction \n')
    ax1.set_ylabel('Temperature \n \u00b0 F')
    ax2.set_ylabel('Altitude (ft)')
    #savefig line
    plt.savefig('MOS_'+stationKey+'_'+str(time[0].month_name())+'_'+str(time[0].day)+str('_{0:03}'.format(i)))
    #Close plot to save space
    plt.close()
    #Iterator
    i+=1
    print('{0} of {1}'.format(i,len(time)))
except:
  print('Something went wrong while plotting.')
  raise

###CSV Output###
#Save the file out as a CSV- saves as strings to avoid errors
if saveCSV==1:
  try:
    print('Saving CSV')
    csvName='MOS_'+stationKey+'_'+str(time[0].month_name())+'_'+str(time[0].day)+'.csv' 
    np.savetxt(csvName,dataIn,fmt='%s',delimiter=',',comments='#')
  except:
    print('An error occurred while saving the CSV')
    raise

###GIF Output###
#combine images into gif
try:
  print('Creating GIF')
  gifName='MOS_'+stationKey+'_'+str(time[0].month_name())+'_'+str(time[0].day)+'.gif' 
  os.system('convert -delay 30 *.png '+gifName)
  if delPNG==1:
    try:
      filelist = glob.glob(os.path.join(os.path.abspath(os.getcwd()), "*.png"))
      for f in filelist:
        os.remove(f)
    except:
      print('Could not delete the png files')
except:
  print('Something went wrong while making the gif')
  raise

###Final steps###
try:
  print('Wrapping up')
  os.chdir(curDir)
  if saveCSV==1:
     
    print('The csv is located at {0}'.format(os.path.join(curDir,dirName,dirName,csvName)))
  print('The gif is located at {0}'.format(os.path.join(curDir,dirName,gifName)))
  #endTime=time.time()
  #print('Total time to run: '+str(endTime-startTime))
except:
  print('Something went wrong in the final steps')
  raise