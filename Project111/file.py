import pandas as pd
import plotly.express as px
import plotly.figure_factory as ff
import statistics
import plotly.graph_objects as go
import random

pf=pd.read_csv("medium_data.csv")
data=pf["reading_time"].tolist()
mean=statistics.mean(data)
stdev=statistics.stdev(data)

#print("Population mean: {}".format(mean))
#print("Population stdev: {}".format(stdev))

def meanGen(count):
    newData=[]
    for i in range(0,count):
        num=random.randint(0,len(data)-1)
        newData.append(data[num])
    mean1=statistics.mean(newData)
    return mean1

def showFig(meanList):
    fig=ff.create_distplot([meanList],['result'],show_hist=False)
    fig.show()

meanList=[]
for i in range(0,100):
    num=meanGen(30)
    meanList.append(num)

mean2=statistics.mean(meanList)
stdev2=statistics.stdev(meanList)

print(" ")
#print("Sample mean: {}".format(mean2))
#print("Sample stdev: {}".format(stdev2))

stdevstart1=mean2-stdev2
stdevend1=mean2+stdev2
devation2=mean2-2*stdev2
stdevstart2=mean2-2*stdev2
stdevend2=mean2+2*stdev2
stdevstart3=mean2-3*stdev2
stdevend3=mean2+3*stdev2

fig=ff.create_distplot([meanList],['result'],show_hist=False)
fig.add_trace(go.Scatter(x=[mean,mean],y=[0,0.6],mode='lines',name="mean"))
fig.add_trace(go.Scatter(x=[stdevstart1,stdevstart1],y=[0,0.5],mode='lines',name="stdev1"))
fig.add_trace(go.Scatter(x=[stdevend1,stdevend1],y=[0,0.5],mode='lines',name="stdev1"))
fig.add_trace(go.Scatter(x=[stdevstart2,stdevstart2],y=[0,0.5],mode='lines',name="stdev2"))
fig.add_trace(go.Scatter(x=[stdevend2,stdevend2],y=[0,0.5],mode='lines',name="stdev2"))
fig.add_trace(go.Scatter(x=[stdevstart3,stdevstart3],y=[0,0.5],mode='lines',name="stdev3"))
fig.add_trace(go.Scatter(x=[stdevend3,stdevend3],y=[0,0.5],mode='lines',name="stdev3"))
fig.add_trace(go.Scatter(x=[mean2,mean2],y=[0,0.7],mode='lines',name="new mean"))
fig.show()